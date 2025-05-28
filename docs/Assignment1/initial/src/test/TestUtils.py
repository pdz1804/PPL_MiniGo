import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/minigo/parser/' in sys.path:
    sys.path.append('./main/minigo/parser/')
if os.path.isdir('../target/main/minigo/parser') and not '../target/main/minigo/parser/' in sys.path:
    sys.path.append('../target/main/minigo/parser/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
import difflib

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
    def test(inputdir,outputdir,num):
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
        try:
            TestLexer.printLexeme(dest,lexer,"\n")
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message+"\n")
        except Exception as err:
            dest.write(str(err)+"\n")
        finally:
            dest.close() 
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer,",")
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        except Exception as err:
            dest.write(str(err)+"\n")
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer,char):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+char)
            TestLexer.printLexeme(dest,lexer,char)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column + 1)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def test(inputdir,outputdir,num):
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MiniGoParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful\n")
        except SyntaxException as f:
            dest.write(f.message + "\n")
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
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


        
