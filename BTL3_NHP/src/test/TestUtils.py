import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
#if not './main/minigo/parser/' in sys.path:
#    sys.path.append('./main/minigo/parser/')
#if os.path.isdir('../target/main/minigo/parser') and not '../target/main/minigo/parser/' in sys.path:
#    sys.path.append('../target/main/minigo/parser/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticError import *
from StaticCheck import StaticChecker

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MiniGoParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

class TestAST:
    @staticmethod
    def checkASTGen(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = MiniGoParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
class TestChecker:
    @staticmethod
    def test(input,expect,num):
        return TestChecker.checkStatic(input,expect,num)
    @staticmethod
    def checkStatic(input,expect,num):
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = MiniGoLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = MiniGoParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            #dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e)+'\n') # NHP
            # dest.write(str(e)) # Votien
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod
    def test1(inputdir,outputdir,num):
        
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        
        try:
            lexer = MiniGoLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
            tokens = CommonTokenStream(lexer)
            parser = MiniGoParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)

            checker = StaticChecker(asttree)
            res = checker.check()
            
        except StaticError as e:
            dest.write(str(e)+'\n')
        except:
            trace = traceback.format_exc()
            print ("Test " + str(num) + " catches unexpected error:" + trace + "\n")
        finally:
            dest.close()
             