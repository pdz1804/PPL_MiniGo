# Generated from /Users/nhphung/LocalDocuments/fromMacBookAir1/Monhoc/KS-NNLT/Materials/Assignments/MiniGo/Assignment4/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#vardecl.
    def enterVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#vardecl.
    def exitVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcdecl.
    def enterFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcdecl.
    def exitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#exp.
    def enterExp(self, ctx:MiniGoParser.ExpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#exp.
    def exitExp(self, ctx:MiniGoParser.ExpContext):
        pass



del MiniGoParser