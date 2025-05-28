# update: 16/07/2018
from abc import ABC
from dataclasses import dataclass
from typing import Union
import AST

class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"
class Method(Kind):
    def __str__(self):
        return "Method"
class Parameter(Kind):
    def __str__(self):
        return "Parameter"
class Variable(Kind):
    def __str__(self):
        return "Variable"
class Constant(Kind):
    def __str__(self):
        return "Constant"
class Field(Kind):
    def __str__(self):
        return "Field"
class Identifier(Kind):
    def __str__(self):
        return "Identifier"
class Type(Kind):
    def __str__(self):
        return "Type"        
class Prototype(Kind):
    def __str__(self):
        return "Prototype"  
 
class StaticError(Exception):
    pass

@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str # name of identifier
    
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n
@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier
    
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

@dataclass
class TypeMismatch(StaticError):
    err: Union[AST.Expr, AST.Stmt]

    def __str__(self):
        return  "Type Mismatch: "+ str(self.err)
