# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0217\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.")
        buf.write("\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\7\65\u015b\n\65\f\65\16\65\u015e\13\65\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u0164\n\66\3\67\3\67\3\67\7\67")
        buf.write("\u0169\n\67\f\67\16\67\u016c\13\67\5\67\u016e\n\67\38")
        buf.write("\38\38\38\58\u0174\n8\38\68\u0177\n8\r8\168\u0178\39\3")
        buf.write("9\39\39\59\u017f\n9\39\69\u0182\n9\r9\169\u0183\3:\3:")
        buf.write("\3:\3:\5:\u018a\n:\3:\6:\u018d\n:\r:\16:\u018e\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3?\7?\u019c\n?\f?\16?\u019f\13")
        buf.write("?\5?\u01a1\n?\3?\6?\u01a4\n?\r?\16?\u01a5\3?\3?\7?\u01aa")
        buf.write("\n?\f?\16?\u01ad\13?\3?\5?\u01b0\n?\5?\u01b2\n?\3@\3@")
        buf.write("\6@\u01b6\n@\r@\16@\u01b7\3@\3@\6@\u01bc\n@\r@\16@\u01bd")
        buf.write("\5@\u01c0\n@\3A\3A\3B\3B\7B\u01c6\nB\fB\16B\u01c9\13B")
        buf.write("\3B\3B\3C\3C\5C\u01cf\nC\3D\3D\3D\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\7F\u01db\nF\fF\16F\u01de\13F\3F\3F\3G\3G\3G\3G\3G\7")
        buf.write("G\u01e7\nG\fG\16G\u01ea\13G\3G\3G\3G\3G\3G\3H\6H\u01f2")
        buf.write("\nH\rH\16H\u01f3\3H\3H\3I\5I\u01f9\nI\3I\3I\3J\3J\3J\3")
        buf.write("K\3K\7K\u0202\nK\fK\16K\u0205\13K\3K\3K\3K\5K\u020a\n")
        buf.write("K\3K\3K\3L\3L\7L\u0210\nL\fL\16L\u0213\13L\3L\3L\3L\3")
        buf.write("\u01e8\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m\2o\2q\2s\2u\2w\2y\2{\2}8\177\2\u0081\2\u00839\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b:\u008d;\u008f<\u0091=\u0093>")
        buf.write("\u0095?\u0097@\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\3\2\62\63\3\2\629\5\2\62;CHch\4\2GGgg\4\2--")
        buf.write("//\6\2\f\f$$))^^\7\2$$^^ppttvv\4\2\f\f\16\17\5\2\13\13")
        buf.write("\16\17\"\"\3\3\f\f\2\u0228\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\u0083\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3")
        buf.write("\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2")
        buf.write("\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009c")
        buf.write("\3\2\2\2\7\u00a1\3\2\2\2\t\u00a5\3\2\2\2\13\u00ac\3\2")
        buf.write("\2\2\r\u00b1\3\2\2\2\17\u00b6\3\2\2\2\21\u00bd\3\2\2\2")
        buf.write("\23\u00c7\3\2\2\2\25\u00ce\3\2\2\2\27\u00d2\3\2\2\2\31")
        buf.write("\u00d8\3\2\2\2\33\u00e0\3\2\2\2\35\u00e6\3\2\2\2\37\u00ea")
        buf.write("\3\2\2\2!\u00f3\3\2\2\2#\u00f9\3\2\2\2%\u00ff\3\2\2\2")
        buf.write("\'\u0103\3\2\2\2)\u0108\3\2\2\2+\u010e\3\2\2\2-\u0110")
        buf.write("\3\2\2\2/\u0112\3\2\2\2\61\u0114\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011b\3\2\2\29\u011e\3\2\2\2")
        buf.write(";\u0121\3\2\2\2=\u0123\3\2\2\2?\u0126\3\2\2\2A\u0128\3")
        buf.write("\2\2\2C\u012b\3\2\2\2E\u012e\3\2\2\2G\u0131\3\2\2\2I\u0133")
        buf.write("\3\2\2\2K\u0135\3\2\2\2M\u0138\3\2\2\2O\u013b\3\2\2\2")
        buf.write("Q\u013e\3\2\2\2S\u0141\3\2\2\2U\u0144\3\2\2\2W\u0146\3")
        buf.write("\2\2\2Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014c\3\2\2\2_\u014e")
        buf.write("\3\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e\u0154\3\2\2\2")
        buf.write("g\u0156\3\2\2\2i\u0158\3\2\2\2k\u0163\3\2\2\2m\u016d\3")
        buf.write("\2\2\2o\u0173\3\2\2\2q\u017e\3\2\2\2s\u0189\3\2\2\2u\u0190")
        buf.write("\3\2\2\2w\u0192\3\2\2\2y\u0194\3\2\2\2{\u0196\3\2\2\2")
        buf.write("}\u01b1\3\2\2\2\177\u01b3\3\2\2\2\u0081\u01c1\3\2\2\2")
        buf.write("\u0083\u01c3\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d0\3")
        buf.write("\2\2\2\u0089\u01d3\3\2\2\2\u008b\u01d6\3\2\2\2\u008d\u01e1")
        buf.write("\3\2\2\2\u008f\u01f1\3\2\2\2\u0091\u01f8\3\2\2\2\u0093")
        buf.write("\u01fc\3\2\2\2\u0095\u01ff\3\2\2\2\u0097\u020d\3\2\2\2")
        buf.write("\u0099\u009a\7k\2\2\u009a\u009b\7h\2\2\u009b\4\3\2\2\2")
        buf.write("\u009c\u009d\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f\7u")
        buf.write("\2\2\u009f\u00a0\7g\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7")
        buf.write("h\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7t\2\2\u00a4\b\3")
        buf.write("\2\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7e\2\2\u00b0\f")
        buf.write("\3\2\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7{\2\2\u00b3\u00b4")
        buf.write("\7r\2\2\u00b4\u00b5\7g\2\2\u00b5\16\3\2\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7w\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7v\2\2\u00bc\20")
        buf.write("\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\24\3\2\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\26")
        buf.write("\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7v\2\2\u00d7\30")
        buf.write("\3\2\2\2\u00d8\u00d9\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7p\2\2\u00df\32\3\2\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7v\2\2\u00e5\34\3\2\2\2\u00e6\u00e7")
        buf.write("\7x\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9\36")
        buf.write("\3\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2 \3")
        buf.write("\2\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7m\2\2\u00f8\"")
        buf.write("\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7i\2\2\u00fd\u00fe\7g\2\2\u00fe$\3")
        buf.write("\2\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7n\2\2\u0102&\3\2\2\2\u0103\u0104\7v\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7w\2\2\u0106\u0107\7g\2\2\u0107(\3")
        buf.write("\2\2\2\u0108\u0109\7h\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d*\3")
        buf.write("\2\2\2\u010e\u010f\7-\2\2\u010f,\3\2\2\2\u0110\u0111\7")
        buf.write("/\2\2\u0111.\3\2\2\2\u0112\u0113\7,\2\2\u0113\60\3\2\2")
        buf.write("\2\u0114\u0115\7\61\2\2\u0115\62\3\2\2\2\u0116\u0117\7")
        buf.write("\'\2\2\u0117\64\3\2\2\2\u0118\u0119\7<\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\66\3\2\2\2\u011b\u011c\7?\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d8\3\2\2\2\u011e\u011f\7#\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120:\3\2\2\2\u0121\u0122\7>\2\2\u0122<\3\2\2")
        buf.write("\2\u0123\u0124\7>\2\2\u0124\u0125\7?\2\2\u0125>\3\2\2")
        buf.write("\2\u0126\u0127\7@\2\2\u0127@\3\2\2\2\u0128\u0129\7@\2")
        buf.write("\2\u0129\u012a\7?\2\2\u012aB\3\2\2\2\u012b\u012c\7(\2")
        buf.write("\2\u012c\u012d\7(\2\2\u012dD\3\2\2\2\u012e\u012f\7~\2")
        buf.write("\2\u012f\u0130\7~\2\2\u0130F\3\2\2\2\u0131\u0132\7#\2")
        buf.write("\2\u0132H\3\2\2\2\u0133\u0134\7?\2\2\u0134J\3\2\2\2\u0135")
        buf.write("\u0136\7-\2\2\u0136\u0137\7?\2\2\u0137L\3\2\2\2\u0138")
        buf.write("\u0139\7/\2\2\u0139\u013a\7?\2\2\u013aN\3\2\2\2\u013b")
        buf.write("\u013c\7,\2\2\u013c\u013d\7?\2\2\u013dP\3\2\2\2\u013e")
        buf.write("\u013f\7\61\2\2\u013f\u0140\7?\2\2\u0140R\3\2\2\2\u0141")
        buf.write("\u0142\7\'\2\2\u0142\u0143\7?\2\2\u0143T\3\2\2\2\u0144")
        buf.write("\u0145\7\60\2\2\u0145V\3\2\2\2\u0146\u0147\7*\2\2\u0147")
        buf.write("X\3\2\2\2\u0148\u0149\7+\2\2\u0149Z\3\2\2\2\u014a\u014b")
        buf.write("\7}\2\2\u014b\\\3\2\2\2\u014c\u014d\7\177\2\2\u014d^\3")
        buf.write("\2\2\2\u014e\u014f\7]\2\2\u014f`\3\2\2\2\u0150\u0151\7")
        buf.write("_\2\2\u0151b\3\2\2\2\u0152\u0153\7.\2\2\u0153d\3\2\2\2")
        buf.write("\u0154\u0155\7=\2\2\u0155f\3\2\2\2\u0156\u0157\7<\2\2")
        buf.write("\u0157h\3\2\2\2\u0158\u015c\t\2\2\2\u0159\u015b\t\3\2")
        buf.write("\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015dj\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015f\u0164\5m\67\2\u0160\u0164\5o8\2\u0161\u0164")
        buf.write("\5q9\2\u0162\u0164\5s:\2\u0163\u015f\3\2\2\2\u0163\u0160")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("l\3\2\2\2\u0165\u016e\5u;\2\u0166\u016a\t\4\2\2\u0167")
        buf.write("\u0169\5u;\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016e\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016d\u0165\3\2\2\2\u016d\u0166\3")
        buf.write("\2\2\2\u016en\3\2\2\2\u016f\u0170\7\62\2\2\u0170\u0174")
        buf.write("\7d\2\2\u0171\u0172\7\62\2\2\u0172\u0174\7D\2\2\u0173")
        buf.write("\u016f\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176\3\2\2\2")
        buf.write("\u0175\u0177\5w<\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2")
        buf.write("\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179p\3")
        buf.write("\2\2\2\u017a\u017b\7\62\2\2\u017b\u017f\7q\2\2\u017c\u017d")
        buf.write("\7\62\2\2\u017d\u017f\7Q\2\2\u017e\u017a\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u0182\5y=\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184r\3\2\2\2\u0185\u0186\7\62\2")
        buf.write("\2\u0186\u018a\7z\2\2\u0187\u0188\7\62\2\2\u0188\u018a")
        buf.write("\7Z\2\2\u0189\u0185\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018c\3\2\2\2\u018b\u018d\5{>\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018ft\3\2\2\2\u0190\u0191\t\5\2\2\u0191v\3\2\2\2\u0192")
        buf.write("\u0193\t\6\2\2\u0193x\3\2\2\2\u0194\u0195\t\7\2\2\u0195")
        buf.write("z\3\2\2\2\u0196\u0197\t\b\2\2\u0197|\3\2\2\2\u0198\u01a1")
        buf.write("\5u;\2\u0199\u019d\t\4\2\2\u019a\u019c\5u;\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u01a0\u0198\3\2\2\2\u01a0\u0199\3\2\2\2\u01a1\u01b2\3")
        buf.write("\2\2\2\u01a2\u01a4\5u;\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01ab\5\u0081A\2\u01a8\u01aa\5u;")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ae\u01b0\5\177@\2\u01af\u01ae\3\2\2")
        buf.write("\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01a0")
        buf.write("\3\2\2\2\u01b1\u01a3\3\2\2\2\u01b2~\3\2\2\2\u01b3\u01bf")
        buf.write("\t\t\2\2\u01b4\u01b6\5u;\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01c0\3\2\2\2\u01b9\u01bb\t\n\2\2\u01ba\u01bc\5u;\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01b5\3")
        buf.write("\2\2\2\u01bf\u01b9\3\2\2\2\u01c0\u0080\3\2\2\2\u01c1\u01c2")
        buf.write("\7\60\2\2\u01c2\u0082\3\2\2\2\u01c3\u01c7\7$\2\2\u01c4")
        buf.write("\u01c6\5\u0085C\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2")
        buf.write("\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\7$\2\2\u01cb")
        buf.write("\u0084\3\2\2\2\u01cc\u01cf\n\13\2\2\u01cd\u01cf\5\u0087")
        buf.write("D\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u0086")
        buf.write("\3\2\2\2\u01d0\u01d1\7^\2\2\u01d1\u01d2\t\f\2\2\u01d2")
        buf.write("\u0088\3\2\2\2\u01d3\u01d4\7^\2\2\u01d4\u01d5\n\f\2\2")
        buf.write("\u01d5\u008a\3\2\2\2\u01d6\u01d7\7\61\2\2\u01d7\u01d8")
        buf.write("\7\61\2\2\u01d8\u01dc\3\2\2\2\u01d9\u01db\n\r\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01dc\3")
        buf.write("\2\2\2\u01df\u01e0\bF\2\2\u01e0\u008c\3\2\2\2\u01e1\u01e2")
        buf.write("\7\61\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e8\3\2\2\2\u01e4")
        buf.write("\u01e7\5\u008dG\2\u01e5\u01e7\13\2\2\2\u01e6\u01e4\3\2")
        buf.write("\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea")
        buf.write("\u01e8\3\2\2\2\u01eb\u01ec\7,\2\2\u01ec\u01ed\7\61\2\2")
        buf.write("\u01ed\u01ee\3\2\2\2\u01ee\u01ef\bG\2\2\u01ef\u008e\3")
        buf.write("\2\2\2\u01f0\u01f2\t\16\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2")
        buf.write("\u01f4\u01f5\3\2\2\2\u01f5\u01f6\bH\2\2\u01f6\u0090\3")
        buf.write("\2\2\2\u01f7\u01f9\7\17\2\2\u01f8\u01f7\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\7\f\2\2")
        buf.write("\u01fb\u0092\3\2\2\2\u01fc\u01fd\13\2\2\2\u01fd\u01fe")
        buf.write("\bJ\3\2\u01fe\u0094\3\2\2\2\u01ff\u0203\7$\2\2\u0200\u0202")
        buf.write("\5\u0085C\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0209\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0206\u0207\7\17\2\2\u0207\u020a")
        buf.write("\7\f\2\2\u0208\u020a\t\17\2\2\u0209\u0206\3\2\2\2\u0209")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\bK\4\2")
        buf.write("\u020c\u0096\3\2\2\2\u020d\u0211\7$\2\2\u020e\u0210\5")
        buf.write("\u0085C\2\u020f\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u0215\5\u0089E\2\u0215\u0216")
        buf.write("\bL\5\2\u0216\u0098\3\2\2\2 \2\u015c\u0163\u016a\u016d")
        buf.write("\u0173\u0178\u017e\u0183\u0189\u018e\u019d\u01a0\u01a5")
        buf.write("\u01ab\u01af\u01b1\u01b7\u01bd\u01bf\u01c7\u01ce\u01dc")
        buf.write("\u01e6\u01e8\u01f3\u01f8\u0203\u0209\u0211\6\b\2\2\3J")
        buf.write("\2\3K\3\3L\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOL = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    NEWASS = 26
    EQ = 27
    NEQ = 28
    LT = 29
    LTE = 30
    GT = 31
    GTE = 32
    AND = 33
    OR = 34
    NEGATION = 35
    ASSIGN = 36
    ADDVAL = 37
    SUBVAL = 38
    MULVAL = 39
    DIVVAL = 40
    MODVAL = 41
    POINT = 42
    R_OPEN = 43
    R_CLOSE = 44
    CUR_OPEN = 45
    CUR_CLOSE = 46
    SQ_OPEN = 47
    SQ_CLOSE = 48
    COMMA = 49
    SEMI_COLON = 50
    COLON = 51
    ID = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    STRING_LIT = 55
    CMTLINE = 56
    CMTBLOCK = 57
    WS = 58
    NEWLINE = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "':='", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOL", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NEWASS", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", 
            "AND", "OR", "NEGATION", "ASSIGN", "ADDVAL", "SUBVAL", "MULVAL", 
            "DIVVAL", "MODVAL", "POINT", "R_OPEN", "R_CLOSE", "CUR_OPEN", 
            "CUR_CLOSE", "SQ_OPEN", "SQ_CLOSE", "COMMA", "SEMI_COLON", "COLON", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "CMTLINE", "CMTBLOCK", 
            "WS", "NEWLINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOL", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NEWASS", "EQ", "NEQ", 
                  "LT", "LTE", "GT", "GTE", "AND", "OR", "NEGATION", "ASSIGN", 
                  "ADDVAL", "SUBVAL", "MULVAL", "DIVVAL", "MODVAL", "POINT", 
                  "R_OPEN", "R_CLOSE", "CUR_OPEN", "CUR_CLOSE", "SQ_OPEN", 
                  "SQ_CLOSE", "COMMA", "SEMI_COLON", "COLON", "ID", "INT_LIT", 
                  "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "DEC", "BIN", 
                  "OCT", "HEX", "FLOAT_LIT", "EXPO", "FP", "STRING_LIT", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "CMTLINE", "CMTBLOCK", 
                  "WS", "NEWLINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preTokenType = None

    def emit(self):
        tk = self.type
        prevTk = self.preTokenType  # Store the previous token type
        self.preTokenType = tk  # Update preTokenType for next token

        # Handling newline conversion logic
        if tk == self.NEWLINE:
            # Convert \n to ; if preceded by specific tokens
            if prevTk in {self.ID, self.INT_LIT, self.FLOAT_LIT, self.TRUE, 
    					  self.FALSE, self.NIL, self.STRING_LIT, 
    					  self.STRING, self.INT, self.FLOAT, self.BOOL,
                          self.RETURN, self.CONTINUE, self.BREAK, 
                          self.R_CLOSE, self.SQ_CLOSE, self.CUR_CLOSE}:
                self.text = ";"  # Convert newline to semicolon
                self.type = self.SEMI_COLON  # Change token type
                return super().emit()
            else:
                self.skip()  # Ignore newline
                return self.nextToken()

        # Handling errors
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
            if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text == '\r'): 
            	raise UncloseString(self.text[:-2]) 
            elif (self.text[-1] == '\n'):
            	raise UncloseString(self.text[:-1]) 
            else: 
            	raise UncloseString(self.text) 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
            temp = self.text 
            raise IllegalEscape(temp) 

     


