from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])

    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitFuncdecl(self,ctx:MiniGoParser.FuncdeclContext):
        return FuncDecl(ctx.ID().getText(),[],VoidType(),Block([]))
    	
    def visitVardecl(self,ctx:MiniGoParser.VardeclContext):
        return VarDecl(ctx.ID().getText(),IntType(),None)

    

