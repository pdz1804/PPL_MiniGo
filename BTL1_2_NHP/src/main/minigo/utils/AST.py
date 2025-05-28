from __future__ import annotations
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class BlockMember(AST):
    __metaclass__ = ABCMeta
    pass

class Stmt(BlockMember):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class PrimLit(Literal):
    __metaclass__ = ABCMeta
    pass
@dataclass
class Program(AST):
    decl : List[Decl]

    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

@dataclass
class ParamDecl(Decl):
    parName: str
    parType: Type
    def __str__(self):
        return "ParDecl(" + self.parName + "," + str(self.parType) + ")"

    def accept(self, v, param):
        return v.visitParamDecl(self, param)

@dataclass    
class VarDecl(Decl,BlockMember):
    varName : str
    varType : Type # None if there is no type
    varInit : Expr # None if there is no initialization

    def __str__(self):
        return "VarDecl(" + self.varName +  (("," + str(self.varType)) if self.varType else "") + ("" if self.varInit is None else (","+ str(self.varInit))) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

@dataclass    
class ConstDecl(Decl,BlockMember):
    conName : str
    conType : Type # None if there is no type 
    iniExpr : Expr

    def __str__(self):
        return "ConstDecl(" + self.conName  + ((","+str(self.conType)) if self.conType else "") + "," + str(self.iniExpr) + ")"

    def accept(self, v, param):
        return v.visitConstDecl(self, param)

@dataclass
class FuncDecl(Decl):
    name: str
    params: List[ParamDecl]
    retType: Type # VoidType if there is no return type
    body: Block

    def __str__(self):
        return "FuncDecl(" + self.name + ",[" +  ','.join(str(i) for i in self.params) + "]," + str(self.retType) + "," + str(self.body) + ")"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)

@dataclass
class MethodDecl(Decl):
    receiver: str
    recType: Type 
    fun: FuncDecl

    def __str__(self):
        return "MethodDecl("+ self.receiver + "," + str(self.recType) + "," + str(self.fun) +")"

    def accept(self, v, param):
        return v.visitMethodDecl(self,param)
    

@dataclass
class Prototype(AST):
    name: str
    params:List[Type]
    retType: Type # VoidType if there is no return type

    def __str__(self):
        return "Prototype(" + self.name + ",[" + ','.join(str(i) for i in self.params) + "]," + str(self.retType) + ")"

    def accept(self, v, param):
        return v.visitPrototype(self,param)

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)

class BoolType(Type):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitBoolType(self, param)

class StringType(Type):
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return v.visitStringType(self, param)

class VoidType(Type):
    def __str__(self):
        return "VoidType"

    def accept(self, v, param):
        return v.visitVoidType(self, param)

@dataclass
class ArrayType(Type):
    dimens:List[Expr]
    eleType:Type
        
    def __str__(self):
        return "ArrayType(" + str(self.eleType) + ",[" + ','.join(str(i) for i in self.dimens) + "])"

    def accept(self, v, param):
        return v.visitArrayType(self, param)

@dataclass
class StructType(Type):
    name: str
    elements:List[Tuple[str,Type]]
    methods:List[MethodDecl]
        
    def __str__(self):
        return "StructType("+ self.name + ",[" + ','.join(("(" + i + "," + str(j) + ")") for i,j in self.elements) + "],["+ ','.join(str(i) for i in self.methods) +"])"

    def accept(self, v, param):
        return v.visitStructType(self, param)

@dataclass
class InterfaceType(Type):
    name: str
    methods:List[Prototype]
        
    def __str__(self):
        return "InterfaceType(" + self.name + ",["+ ','.join(str(i) for i in self.methods) +"])"

    def accept(self, v, param):
        return v.visitInterfaceType(self, param)

@dataclass
class Block(Stmt):
    member:List[BlockMember]

    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.member)  + "])"

    def accept(self, v, param):
        return v.visitBlock(self, param)

@dataclass
class Assign(Stmt):
    lhs: LHS
    rhs: Expr # if assign operator is +=, rhs is BinaryOp(+,lhs,rhs), similar to -=,*=,/=,%=

    def __str__(self):
        return "Assign(" + str(self.lhs) + "," + str(self.rhs) + ")"

    def accept(self, v, param):
        return v.visitAssign(self, param)

@dataclass
class If(Stmt):
    expr:Expr
    thenStmt:Stmt
    elseStmt:Stmt # None if there is no else

    def __str__(self):
        return "If(" + str(self.expr) + "," + str(self.thenStmt) + ("" if (self.elseStmt is None) else "," + str(self.elseStmt)) + ")"

    def accept(self, v, param):
        return v.visitIf(self, param)

@dataclass
class ForBasic(Stmt):
    cond:Expr
    loop:Block

    def __str__(self):
        return "For(" + str(self.cond) + "," + str(self.loop) + ")"

    def accept(self, v, param):
        return v.visitForBasic(self, param)

@dataclass
class ForStep(Stmt):
    init:Stmt
    cond:Expr
    upda:Assign
    loop:Block

    def __str__(self):
        return "For(" + str(self.init) + "," + str(self.cond) + "," + str(self.upda) + "," + str(self.loop) + ")"

    def accept(self, v, param):
        return v.visitForStep(self, param)

@dataclass
class ForEach(Stmt):
    idx: Id
    value: Id
    arr: Expr
    loop:Block

    def __str__(self):
        return "ForEach(" + str(self.idx) + "," + str(self.value) + "," + str(self.arr) + "," + str(self.loop) + ")"

    def accept(self, v, param):
        return v.visitForEach(self, param)

class Break(Stmt):
    def __str__(self):
        return "Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)
    
class Continue(Stmt):
    def __str__(self):
        return "Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)

@dataclass
class Return(Stmt):
    expr:Expr # None if there is no expr

    def __str__(self):
        return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)



@dataclass
class Id(Type,LHS):
    name : str

    def __str__(self):
        return  "Id(" + self.name + ")" 

    def accept(self, v, param):
        return v.visitId(self, param)

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:List[Expr]

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + ",[" + ','.join(str(i) for i in self.idx) + "])"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)

@dataclass
class FieldAccess(LHS):
    receiver:Expr
    field:str

    def __str__(self):
        return "FieldAccess(" + str(self.receiver) + "," + self.field + ")"

    def accept(self, v, param):
        return v.visitFieldAccess(self, param)

@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr

    def __str__(self):
        return "BinaryOp(" + str(self.left) + "," + self.op + "," +  str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)

@dataclass
class FuncCall(Expr,Stmt):
    funName:str
    args:List[Expr] # [] if there is no arg 

    def __str__(self):
        return "FuncCall(" + str(self.funName) + ",[" +  ','.join(str(i) for i in self.args) + "])"

    def accept(self, v, param):
        return v.visitFuncCall(self, param)

@dataclass
class MethCall(Expr,Stmt):
    receiver: Expr
    metName: str
    args:List[Expr]

    def __str__(self):
        return "MethodCall(" + str(self.receiver) + "," + self.metName + ",[" +  ','.join(str(i) for i in self.args) + "])"

    def accept(self, v, param):
        return v.visitMethCall(self, param)


@dataclass
class IntLiteral(PrimLit):
    value:int

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

@dataclass
class FloatLiteral(PrimLit):
    value:float

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)

@dataclass
class StringLiteral(PrimLit):
    value:str

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):

        return v.visitStringLiteral(self, param)
@dataclass
class BooleanLiteral(PrimLit):
    value:bool

    def __str__(self):
        return "BooleanLiteral(" + str(self.value).lower() + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)

NestedList = PrimLit | list['NestedList']
def nested2Str(dat: NestedList):
    if isinstance(dat,list):
        return '[' + ','.join(nested2Str(i) for i in dat) + ']'
    else:
        return str(dat)

@dataclass
class ArrayLiteral(Literal):
    dimens:List[Expr]
    eleType: Type
    value: NestedList

    def __str__(self):
        return "ArrayLiteral([" + ','.join(str(i) for i in self.dimens) + "]," + str(self.eleType) + "," + nested2Str(self.value) + ")"

    def accept(self, v, param):
        return v.visitArrayLiteral(self, param)

@dataclass
class StructLiteral(Literal):
    name:str
    elements: List[Tuple[str,Expr]] # [] if there is no elements
    
    def __str__(self):
        return "StructLiteral(" + self.name + ',[' + ','.join(("("+str(i)+","+str(j)+")") for i,j in self.elements) + "])"

    def accept(self, v, param):
        return v.visitStructLiteral(self, param)

class NilLiteral(Literal):
    def __str__(self):
        return "Nil"

    def accept(self, v, param):
        return v.visitNilLiteral(self, param)






