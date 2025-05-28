# Generated from e:/2_LEARNING_BKU/2_File_2/K22_HK242/CO3005_PPL/Main/Assignment/Assignment1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,14,74,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,54,8,8,11,8,12,8,55,1,9,
        1,9,1,9,1,9,1,10,4,10,63,8,10,11,10,12,10,64,1,10,1,10,1,11,1,11,
        1,12,1,12,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,1,0,2,1,0,97,122,3,0,9,9,13,13,32,
        32,75,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,
        0,3,33,1,0,0,0,5,37,1,0,0,0,7,39,1,0,0,0,9,44,1,0,0,0,11,46,1,0,
        0,0,13,48,1,0,0,0,15,50,1,0,0,0,17,53,1,0,0,0,19,57,1,0,0,0,21,62,
        1,0,0,0,23,68,1,0,0,0,25,70,1,0,0,0,27,72,1,0,0,0,29,30,5,118,0,
        0,30,31,5,97,0,0,31,32,5,114,0,0,32,2,1,0,0,0,33,34,5,105,0,0,34,
        35,5,110,0,0,35,36,5,116,0,0,36,4,1,0,0,0,37,38,5,59,0,0,38,6,1,
        0,0,0,39,40,5,102,0,0,40,41,5,117,0,0,41,42,5,110,0,0,42,43,5,99,
        0,0,43,8,1,0,0,0,44,45,5,40,0,0,45,10,1,0,0,0,46,47,5,41,0,0,47,
        12,1,0,0,0,48,49,5,123,0,0,49,14,1,0,0,0,50,51,5,125,0,0,51,16,1,
        0,0,0,52,54,7,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,
        56,1,0,0,0,56,18,1,0,0,0,57,58,5,10,0,0,58,59,1,0,0,0,59,60,6,9,
        0,0,60,20,1,0,0,0,61,63,7,1,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,
        1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,6,10,0,0,67,22,1,0,0,0,
        68,69,9,0,0,0,69,24,1,0,0,0,70,71,9,0,0,0,71,26,1,0,0,0,72,73,9,
        0,0,0,73,28,1,0,0,0,3,0,55,64,1,6,0,0
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ID = 9
    NL = 10
    WS = 11
    ERROR_CHAR = 12
    ILLEGAL_ESCAPE = 13
    UNCLOSE_STRING = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'int'", "';'", "'func'", "'('", "')'", "'{'", "'}'", 
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


