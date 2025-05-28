# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u02bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00b2\n\3\3\4\3\4\3\4\5\4")
        buf.write("\u00b7\n\4\3\5\3\5\3\5\3\5\5\5\u00bd\n\5\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00cd\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\5\t\u00d4\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00dc\n\n\3\13\3\13\3\13\5\13\u00e1\n\13\3")
        buf.write("\f\3\f\3\f\5\f\u00e6\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00ef\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u0101\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\5\23\u0113\n\23\3\24\3\24\3")
        buf.write("\24\5\24\u0118\n\24\3\24\3\24\3\24\5\24\u011d\n\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u0126\n\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\5\27\u012f\n\27\3\30\3\30")
        buf.write("\5\30\u0133\n\30\3\31\3\31\3\31\5\31\u0138\n\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\5\34\u0148\n\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\5\36\u0154\n\36\3\36\3\36\5\36")
        buf.write("\u0158\n\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0162\n\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u016e")
        buf.write("\n!\3!\3!\3!\5!\u0173\n!\3!\3!\3!\3\"\3\"\3#\3#\3#\3$")
        buf.write("\3$\5$\u017f\n$\3$\3$\3%\3%\3%\3%\5%\u0187\n%\3&\3&\3")
        buf.write("&\5&\u018c\n&\3\'\3\'\3\'\5\'\u0191\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u0199\n(\3)\3)\3)\3)\5)\u019f\n)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\5+\u01ac\n+\3,\3,\3,\3-\3-\5-\u01b3")
        buf.write("\n-\3.\3.\3.\5.\u01b8\n.\3.\3.\3.\3.\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\5\64\u01d4\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\5\67\u01e6\n\67\38\38\38\39\39\3")
        buf.write("9\3:\3:\5:\u01f0\n:\3:\3:\3;\3;\5;\u01f6\n;\3;\5;\u01f9")
        buf.write("\n;\3;\5;\u01fc\n;\3;\3;\3;\5;\u0201\n;\3;\3;\3<\3<\3")
        buf.write("<\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3")
        buf.write("A\3A\5A\u021b\nA\3B\3B\3B\3B\3B\3B\7B\u0223\nB\fB\16B")
        buf.write("\u0226\13B\3C\3C\3C\3C\3C\3C\7C\u022e\nC\fC\16C\u0231")
        buf.write("\13C\3D\3D\3D\3D\3D\3D\3D\7D\u023a\nD\fD\16D\u023d\13")
        buf.write("D\3E\3E\3F\3F\3F\3F\3F\3F\3F\7F\u0248\nF\fF\16F\u024b")
        buf.write("\13F\3G\3G\3H\3H\3H\3H\3H\3H\3H\7H\u0256\nH\fH\16H\u0259")
        buf.write("\13H\3I\3I\3J\3J\3J\3J\5J\u0261\nJ\3K\3K\3L\3L\3L\3L\3")
        buf.write("L\7L\u026a\nL\fL\16L\u026d\13L\3M\3M\3M\3M\5M\u0273\n")
        buf.write("M\3N\3N\3N\3N\3N\3N\5N\u027b\nN\3O\3O\5O\u027f\nO\3O\3")
        buf.write("O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u0291\n")
        buf.write("P\3Q\3Q\5Q\u0295\nQ\3R\3R\3R\3R\3S\3S\3S\5S\u029e\nS\3")
        buf.write("S\5S\u02a1\nS\3T\3T\5T\u02a5\nT\3T\5T\u02a8\nT\3U\3U\3")
        buf.write("U\5U\u02ad\nU\3U\3U\3U\3U\5U\u02b3\nU\3U\3U\3U\3U\3U\3")
        buf.write("U\5U\u02bb\nU\5U\u02bd\nU\3U\2\b\u0082\u0084\u0086\u008a")
        buf.write("\u008e\u0096V\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("xz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write("\u00a4\u00a6\u00a8\2\n\4\2\24\26\679\3\2\66\67\3\2\13")
        buf.write("\16\3\2\'+\3\2\35\"\3\2\27\30\3\2\31\33\4\2\30\30%%\2")
        buf.write("\u02bf\2\u00aa\3\2\2\2\4\u00b1\3\2\2\2\6\u00b6\3\2\2\2")
        buf.write("\b\u00bc\3\2\2\2\n\u00be\3\2\2\2\f\u00c0\3\2\2\2\16\u00c5")
        buf.write("\3\2\2\2\20\u00d3\3\2\2\2\22\u00db\3\2\2\2\24\u00e0\3")
        buf.write("\2\2\2\26\u00e2\3\2\2\2\30\u00ee\3\2\2\2\32\u00f0\3\2")
        buf.write("\2\2\34\u00f4\3\2\2\2\36\u0100\3\2\2\2 \u0102\3\2\2\2")
        buf.write("\"\u0106\3\2\2\2$\u0112\3\2\2\2&\u0114\3\2\2\2(\u0125")
        buf.write("\3\2\2\2*\u0127\3\2\2\2,\u012e\3\2\2\2.\u0132\3\2\2\2")
        buf.write("\60\u0134\3\2\2\2\62\u013d\3\2\2\2\64\u0142\3\2\2\2\66")
        buf.write("\u0147\3\2\2\28\u0149\3\2\2\2:\u014f\3\2\2\2<\u0161\3")
        buf.write("\2\2\2>\u0163\3\2\2\2@\u0166\3\2\2\2B\u0177\3\2\2\2D\u0179")
        buf.write("\3\2\2\2F\u017c\3\2\2\2H\u0186\3\2\2\2J\u018b\3\2\2\2")
        buf.write("L\u0190\3\2\2\2N\u0198\3\2\2\2P\u019a\3\2\2\2R\u01a3\3")
        buf.write("\2\2\2T\u01ab\3\2\2\2V\u01ad\3\2\2\2X\u01b2\3\2\2\2Z\u01b4")
        buf.write("\3\2\2\2\\\u01bd\3\2\2\2^\u01c1\3\2\2\2`\u01c5\3\2\2\2")
        buf.write("b\u01cc\3\2\2\2d\u01ce\3\2\2\2f\u01d3\3\2\2\2h\u01d5\3")
        buf.write("\2\2\2j\u01dc\3\2\2\2l\u01e2\3\2\2\2n\u01e7\3\2\2\2p\u01ea")
        buf.write("\3\2\2\2r\u01ed\3\2\2\2t\u0200\3\2\2\2v\u0204\3\2\2\2")
        buf.write("x\u0207\3\2\2\2z\u020a\3\2\2\2|\u020e\3\2\2\2~\u0212\3")
        buf.write("\2\2\2\u0080\u021a\3\2\2\2\u0082\u021c\3\2\2\2\u0084\u0227")
        buf.write("\3\2\2\2\u0086\u0232\3\2\2\2\u0088\u023e\3\2\2\2\u008a")
        buf.write("\u0240\3\2\2\2\u008c\u024c\3\2\2\2\u008e\u024e\3\2\2\2")
        buf.write("\u0090\u025a\3\2\2\2\u0092\u0260\3\2\2\2\u0094\u0262\3")
        buf.write("\2\2\2\u0096\u0264\3\2\2\2\u0098\u0272\3\2\2\2\u009a\u027a")
        buf.write("\3\2\2\2\u009c\u027c\3\2\2\2\u009e\u0290\3\2\2\2\u00a0")
        buf.write("\u0292\3\2\2\2\u00a2\u0296\3\2\2\2\u00a4\u029a\3\2\2\2")
        buf.write("\u00a6\u02a2\3\2\2\2\u00a8\u02bc\3\2\2\2\u00aa\u00ab\5")
        buf.write("\4\3\2\u00ab\u00ac\7\2\2\3\u00ac\3\3\2\2\2\u00ad\u00ae")
        buf.write("\5\6\4\2\u00ae\u00af\5\4\3\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00b2\5\6\4\2\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2\5\3\2\2\2\u00b3\u00b7\5\b\5\2\u00b4\u00b7\5.\30")
        buf.write("\2\u00b5\u00b7\58\35\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\7\3\2\2\2\u00b8\u00bd")
        buf.write("\5:\36\2\u00b9\u00bd\5@!\2\u00ba\u00bd\5\34\17\2\u00bb")
        buf.write("\u00bd\5\"\22\2\u00bc\u00b8\3\2\2\2\u00bc\u00b9\3\2\2")
        buf.write("\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\t\3\2")
        buf.write("\2\2\u00be\u00bf\t\2\2\2\u00bf\13\3\2\2\2\u00c0\u00c1")
        buf.write("\5\16\b\2\u00c1\u00c2\7/\2\2\u00c2\u00c3\5\20\t\2\u00c3")
        buf.write("\u00c4\7\60\2\2\u00c4\r\3\2\2\2\u00c5\u00c6\7\61\2\2\u00c6")
        buf.write("\u00c7\t\3\2\2\u00c7\u00c8\7\62\2\2\u00c8\u00cc\3\2\2")
        buf.write("\2\u00c9\u00cd\5\16\b\2\u00ca\u00cd\5\64\33\2\u00cb\u00cd")
        buf.write("\7\66\2\2\u00cc\u00c9\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\17\3\2\2\2\u00ce\u00cf\5\22\n\2\u00cf")
        buf.write("\u00d0\7\63\2\2\u00d0\u00d1\5\20\t\2\u00d1\u00d4\3\2\2")
        buf.write("\2\u00d2\u00d4\5\22\n\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d4\21\3\2\2\2\u00d5\u00dc\3\2\2\2\u00d6\u00d7")
        buf.write("\7/\2\2\u00d7\u00d8\5\20\t\2\u00d8\u00d9\7\60\2\2\u00d9")
        buf.write("\u00dc\3\2\2\2\u00da\u00dc\5\24\13\2\u00db\u00d5\3\2\2")
        buf.write("\2\u00db\u00d6\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\23\3")
        buf.write("\2\2\2\u00dd\u00e1\5\n\6\2\u00de\u00e1\5\26\f\2\u00df")
        buf.write("\u00e1\7\66\2\2\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2")
        buf.write("\2\u00e0\u00df\3\2\2\2\u00e1\25\3\2\2\2\u00e2\u00e3\7")
        buf.write("\66\2\2\u00e3\u00e5\7/\2\2\u00e4\u00e6\5\30\r\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\7\60\2\2\u00e8\27\3\2\2\2\u00e9\u00ea\5\32")
        buf.write("\16\2\u00ea\u00eb\7\63\2\2\u00eb\u00ec\5\30\r\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00ef\5\32\16\2\u00ee\u00e9\3\2\2")
        buf.write("\2\u00ee\u00ed\3\2\2\2\u00ef\31\3\2\2\2\u00f0\u00f1\7")
        buf.write("\66\2\2\u00f1\u00f2\7\65\2\2\u00f2\u00f3\5\u0082B\2\u00f3")
        buf.write("\33\3\2\2\2\u00f4\u00f5\7\b\2\2\u00f5\u00f6\7\66\2\2\u00f6")
        buf.write("\u00f7\7\t\2\2\u00f7\u00f8\7/\2\2\u00f8\u00f9\5\36\20")
        buf.write("\2\u00f9\u00fa\7\60\2\2\u00fa\u00fb\7\64\2\2\u00fb\35")
        buf.write("\3\2\2\2\u00fc\u00fd\5 \21\2\u00fd\u00fe\5\36\20\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u0101\5 \21\2\u0100\u00fc\3\2\2\2")
        buf.write("\u0100\u00ff\3\2\2\2\u0101\37\3\2\2\2\u0102\u0103\7\66")
        buf.write("\2\2\u0103\u0104\5\66\34\2\u0104\u0105\7\64\2\2\u0105")
        buf.write("!\3\2\2\2\u0106\u0107\7\b\2\2\u0107\u0108\7\66\2\2\u0108")
        buf.write("\u0109\7\n\2\2\u0109\u010a\7/\2\2\u010a\u010b\5$\23\2")
        buf.write("\u010b\u010c\7\60\2\2\u010c\u010d\7\64\2\2\u010d#\3\2")
        buf.write("\2\2\u010e\u010f\5&\24\2\u010f\u0110\5$\23\2\u0110\u0113")
        buf.write("\3\2\2\2\u0111\u0113\5&\24\2\u0112\u010e\3\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113%\3\2\2\2\u0114\u0115\7\66\2\2\u0115")
        buf.write("\u0117\7-\2\2\u0116\u0118\5(\25\2\u0117\u0116\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\7")
        buf.write(".\2\2\u011a\u011c\3\2\2\2\u011b\u011d\5\66\34\2\u011c")
        buf.write("\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011f\7\64\2\2\u011f\'\3\2\2\2\u0120\u0121\5*\26")
        buf.write("\2\u0121\u0122\7\63\2\2\u0122\u0123\5(\25\2\u0123\u0126")
        buf.write("\3\2\2\2\u0124\u0126\5*\26\2\u0125\u0120\3\2\2\2\u0125")
        buf.write("\u0124\3\2\2\2\u0126)\3\2\2\2\u0127\u0128\5,\27\2\u0128")
        buf.write("\u0129\5\66\34\2\u0129+\3\2\2\2\u012a\u012b\7\66\2\2\u012b")
        buf.write("\u012c\7\63\2\2\u012c\u012f\5,\27\2\u012d\u012f\7\66\2")
        buf.write("\2\u012e\u012a\3\2\2\2\u012e\u012d\3\2\2\2\u012f-\3\2")
        buf.write("\2\2\u0130\u0133\5\62\32\2\u0131\u0133\5\60\31\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133/\3\2\2\2\u0134")
        buf.write("\u0135\7\20\2\2\u0135\u0137\7\66\2\2\u0136\u0138\5\66")
        buf.write("\34\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013a\7&\2\2\u013a\u013b\5\u0082B\2\u013b")
        buf.write("\u013c\7\64\2\2\u013c\61\3\2\2\2\u013d\u013e\7\20\2\2")
        buf.write("\u013e\u013f\7\66\2\2\u013f\u0140\5\66\34\2\u0140\u0141")
        buf.write("\7\64\2\2\u0141\63\3\2\2\2\u0142\u0143\t\4\2\2\u0143\65")
        buf.write("\3\2\2\2\u0144\u0148\5\64\33\2\u0145\u0148\5\16\b\2\u0146")
        buf.write("\u0148\7\66\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2")
        buf.write("\2\u0147\u0146\3\2\2\2\u0148\67\3\2\2\2\u0149\u014a\7")
        buf.write("\17\2\2\u014a\u014b\7\66\2\2\u014b\u014c\7&\2\2\u014c")
        buf.write("\u014d\5\u0082B\2\u014d\u014e\7\64\2\2\u014e9\3\2\2\2")
        buf.write("\u014f\u0150\7\7\2\2\u0150\u0151\7\66\2\2\u0151\u0153")
        buf.write("\7-\2\2\u0152\u0154\5<\37\2\u0153\u0152\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\7.\2\2")
        buf.write("\u0156\u0158\5\66\34\2\u0157\u0156\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\5F$\2\u015a\u015b")
        buf.write("\7\64\2\2\u015b;\3\2\2\2\u015c\u015d\5> \2\u015d\u015e")
        buf.write("\7\63\2\2\u015e\u015f\5<\37\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u0162\5> \2\u0161\u015c\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("=\3\2\2\2\u0163\u0164\5,\27\2\u0164\u0165\5\66\34\2\u0165")
        buf.write("?\3\2\2\2\u0166\u0167\7\7\2\2\u0167\u0168\7-\2\2\u0168")
        buf.write("\u0169\5B\"\2\u0169\u016a\7.\2\2\u016a\u016b\7\66\2\2")
        buf.write("\u016b\u016d\7-\2\2\u016c\u016e\5<\37\2\u016d\u016c\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170")
        buf.write("\7.\2\2\u0170\u0172\3\2\2\2\u0171\u0173\5\66\34\2\u0172")
        buf.write("\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0175\5F$\2\u0175\u0176\7\64\2\2\u0176A\3\2\2\2")
        buf.write("\u0177\u0178\5D#\2\u0178C\3\2\2\2\u0179\u017a\7\66\2\2")
        buf.write("\u017a\u017b\7\66\2\2\u017bE\3\2\2\2\u017c\u017e\7/\2")
        buf.write("\2\u017d\u017f\5H%\2\u017e\u017d\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\7\60\2\2\u0181")
        buf.write("G\3\2\2\2\u0182\u0183\5J&\2\u0183\u0184\5H%\2\u0184\u0187")
        buf.write("\3\2\2\2\u0185\u0187\5J&\2\u0186\u0182\3\2\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187I\3\2\2\2\u0188\u018c\5.\30\2\u0189\u018c")
        buf.write("\58\35\2\u018a\u018c\5L\'\2\u018b\u0188\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018cK\3\2\2\2\u018d")
        buf.write("\u0191\5N(\2\u018e\u0191\5n8\2\u018f\u0191\5p9\2\u0190")
        buf.write("\u018d\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191M\3\2\2\2\u0192\u0199\5P)\2\u0193\u0199\5d\63\2")
        buf.write("\u0194\u0199\5r:\2\u0195\u0199\5t;\2\u0196\u0199\5x=\2")
        buf.write("\u0197\u0199\5~@\2\u0198\u0192\3\2\2\2\u0198\u0193\3\2")
        buf.write("\2\2\u0198\u0194\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199O\3\2\2\2\u019a\u019e")
        buf.write("\7\5\2\2\u019b\u019f\5R*\2\u019c\u019f\5`\61\2\u019d\u019f")
        buf.write("\5b\62\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\5F$\2\u01a1")
        buf.write("\u01a2\7\64\2\2\u01a2Q\3\2\2\2\u01a3\u01a4\5T+\2\u01a4")
        buf.write("\u01a5\5V,\2\u01a5\u01a6\5X-\2\u01a6S\3\2\2\2\u01a7\u01a8")
        buf.write("\5X-\2\u01a8\u01a9\7\64\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01ac\5Z.\2\u01ab\u01a7\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac")
        buf.write("U\3\2\2\2\u01ad\u01ae\5\u0082B\2\u01ae\u01af\7\64\2\2")
        buf.write("\u01afW\3\2\2\2\u01b0\u01b3\5\\/\2\u01b1\u01b3\5^\60\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3Y\3\2\2")
        buf.write("\2\u01b4\u01b5\7\20\2\2\u01b5\u01b7\7\66\2\2\u01b6\u01b8")
        buf.write("\5\66\34\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\7&\2\2\u01ba\u01bb\5\u0082")
        buf.write("B\2\u01bb\u01bc\7\64\2\2\u01bc[\3\2\2\2\u01bd\u01be\7")
        buf.write("\66\2\2\u01be\u01bf\t\5\2\2\u01bf\u01c0\5\u0082B\2\u01c0")
        buf.write("]\3\2\2\2\u01c1\u01c2\7\66\2\2\u01c2\u01c3\7\34\2\2\u01c3")
        buf.write("\u01c4\5\u0082B\2\u01c4_\3\2\2\2\u01c5\u01c6\7\66\2\2")
        buf.write("\u01c6\u01c7\7\63\2\2\u01c7\u01c8\7\66\2\2\u01c8\u01c9")
        buf.write("\7\34\2\2\u01c9\u01ca\7\23\2\2\u01ca\u01cb\5\u0082B\2")
        buf.write("\u01cba\3\2\2\2\u01cc\u01cd\5\u0082B\2\u01cdc\3\2\2\2")
        buf.write("\u01ce\u01cf\5f\64\2\u01cf\u01d0\7\64\2\2\u01d0e\3\2\2")
        buf.write("\2\u01d1\u01d4\5h\65\2\u01d2\u01d4\5j\66\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4g\3\2\2\2\u01d5\u01d6")
        buf.write("\7\3\2\2\u01d6\u01d7\7-\2\2\u01d7\u01d8\5\u0082B\2\u01d8")
        buf.write("\u01d9\7.\2\2\u01d9\u01da\5F$\2\u01da\u01db\5l\67\2\u01db")
        buf.write("i\3\2\2\2\u01dc\u01dd\7\3\2\2\u01dd\u01de\7-\2\2\u01de")
        buf.write("\u01df\5\u0082B\2\u01df\u01e0\7.\2\2\u01e0\u01e1\5F$\2")
        buf.write("\u01e1k\3\2\2\2\u01e2\u01e5\7\4\2\2\u01e3\u01e6\5f\64")
        buf.write("\2\u01e4\u01e6\5F$\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3")
        buf.write("\2\2\2\u01e6m\3\2\2\2\u01e7\u01e8\7\22\2\2\u01e8\u01e9")
        buf.write("\7\64\2\2\u01e9o\3\2\2\2\u01ea\u01eb\7\21\2\2\u01eb\u01ec")
        buf.write("\7\64\2\2\u01ecq\3\2\2\2\u01ed\u01ef\7\6\2\2\u01ee\u01f0")
        buf.write("\5\u0082B\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01f2\7\64\2\2\u01f2s\3\2\2\2\u01f3")
        buf.write("\u01f5\7\66\2\2\u01f4\u01f6\5\u009cO\2\u01f5\u01f4\3\2")
        buf.write("\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f9")
        buf.write("\5\u00a0Q\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01fb\3\2\2\2\u01fa\u01fc\5\u00a8U\2\u01fb\u01fa\3\2")
        buf.write("\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe")
        buf.write("\7,\2\2\u01fe\u0201\5v<\2\u01ff\u0201\5v<\2\u0200\u01f3")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0203\7\64\2\2\u0203u\3\2\2\2\u0204\u0205\7\66\2\2\u0205")
        buf.write("\u0206\5\u009cO\2\u0206w\3\2\2\2\u0207\u0208\5z>\2\u0208")
        buf.write("\u0209\7\64\2\2\u0209y\3\2\2\2\u020a\u020b\5\u00a6T\2")
        buf.write("\u020b\u020c\7\34\2\2\u020c\u020d\5\u0082B\2\u020d{\3")
        buf.write("\2\2\2\u020e\u020f\5\u00a6T\2\u020f\u0210\t\5\2\2\u0210")
        buf.write("\u0211\5\u0082B\2\u0211}\3\2\2\2\u0212\u0213\5|?\2\u0213")
        buf.write("\u0214\7\64\2\2\u0214\177\3\2\2\2\u0215\u0216\5\u0082")
        buf.write("B\2\u0216\u0217\7\63\2\2\u0217\u0218\5\u0080A\2\u0218")
        buf.write("\u021b\3\2\2\2\u0219\u021b\5\u0082B\2\u021a\u0215\3\2")
        buf.write("\2\2\u021a\u0219\3\2\2\2\u021b\u0081\3\2\2\2\u021c\u021d")
        buf.write("\bB\1\2\u021d\u021e\5\u0084C\2\u021e\u0224\3\2\2\2\u021f")
        buf.write("\u0220\f\4\2\2\u0220\u0221\7$\2\2\u0221\u0223\5\u0084")
        buf.write("C\2\u0222\u021f\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222")
        buf.write("\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0083\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u0228\bC\1\2\u0228\u0229\5\u0086")
        buf.write("D\2\u0229\u022f\3\2\2\2\u022a\u022b\f\4\2\2\u022b\u022c")
        buf.write("\7#\2\2\u022c\u022e\5\u0086D\2\u022d\u022a\3\2\2\2\u022e")
        buf.write("\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write("\u0230\u0085\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0233\b")
        buf.write("D\1\2\u0233\u0234\5\u008aF\2\u0234\u023b\3\2\2\2\u0235")
        buf.write("\u0236\f\4\2\2\u0236\u0237\5\u0088E\2\u0237\u0238\5\u008a")
        buf.write("F\2\u0238\u023a\3\2\2\2\u0239\u0235\3\2\2\2\u023a\u023d")
        buf.write("\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u0087\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f\t\6\2\2")
        buf.write("\u023f\u0089\3\2\2\2\u0240\u0241\bF\1\2\u0241\u0242\5")
        buf.write("\u008eH\2\u0242\u0249\3\2\2\2\u0243\u0244\f\4\2\2\u0244")
        buf.write("\u0245\5\u008cG\2\u0245\u0246\5\u008eH\2\u0246\u0248\3")
        buf.write("\2\2\2\u0247\u0243\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u008b\3\2\2\2\u024b")
        buf.write("\u0249\3\2\2\2\u024c\u024d\t\7\2\2\u024d\u008d\3\2\2\2")
        buf.write("\u024e\u024f\bH\1\2\u024f\u0250\5\u0092J\2\u0250\u0257")
        buf.write("\3\2\2\2\u0251\u0252\f\4\2\2\u0252\u0253\5\u0090I\2\u0253")
        buf.write("\u0254\5\u0092J\2\u0254\u0256\3\2\2\2\u0255\u0251\3\2")
        buf.write("\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258")
        buf.write("\3\2\2\2\u0258\u008f\3\2\2\2\u0259\u0257\3\2\2\2\u025a")
        buf.write("\u025b\t\b\2\2\u025b\u0091\3\2\2\2\u025c\u025d\5\u0094")
        buf.write("K\2\u025d\u025e\5\u0092J\2\u025e\u0261\3\2\2\2\u025f\u0261")
        buf.write("\5\u0096L\2\u0260\u025c\3\2\2\2\u0260\u025f\3\2\2\2\u0261")
        buf.write("\u0093\3\2\2\2\u0262\u0263\t\t\2\2\u0263\u0095\3\2\2\2")
        buf.write("\u0264\u0265\bL\1\2\u0265\u0266\5\u009eP\2\u0266\u026b")
        buf.write("\3\2\2\2\u0267\u0268\f\4\2\2\u0268\u026a\5\u0098M\2\u0269")
        buf.write("\u0267\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u0269\3\2\2\2")
        buf.write("\u026b\u026c\3\2\2\2\u026c\u0097\3\2\2\2\u026d\u026b\3")
        buf.write("\2\2\2\u026e\u026f\5\u009aN\2\u026f\u0270\5\u0098M\2\u0270")
        buf.write("\u0273\3\2\2\2\u0271\u0273\5\u009aN\2\u0272\u026e\3\2")
        buf.write("\2\2\u0272\u0271\3\2\2\2\u0273\u0099\3\2\2\2\u0274\u0275")
        buf.write("\7,\2\2\u0275\u027b\7\66\2\2\u0276\u0277\7,\2\2\u0277")
        buf.write("\u0278\7\66\2\2\u0278\u027b\5\u009cO\2\u0279\u027b\5\u00a2")
        buf.write("R\2\u027a\u0274\3\2\2\2\u027a\u0276\3\2\2\2\u027a\u0279")
        buf.write("\3\2\2\2\u027b\u009b\3\2\2\2\u027c\u027e\7-\2\2\u027d")
        buf.write("\u027f\5\u0080A\2\u027e\u027d\3\2\2\2\u027e\u027f\3\2")
        buf.write("\2\2\u027f\u0280\3\2\2\2\u0280\u0281\7.\2\2\u0281\u009d")
        buf.write("\3\2\2\2\u0282\u0291\7\25\2\2\u0283\u0291\7\26\2\2\u0284")
        buf.write("\u0291\7\24\2\2\u0285\u0291\78\2\2\u0286\u0291\79\2\2")
        buf.write("\u0287\u0291\7\67\2\2\u0288\u0291\5\f\7\2\u0289\u0291")
        buf.write("\5\26\f\2\u028a\u0291\7\66\2\2\u028b\u0291\5v<\2\u028c")
        buf.write("\u028d\7-\2\2\u028d\u028e\5\u0082B\2\u028e\u028f\7.\2")
        buf.write("\2\u028f\u0291\3\2\2\2\u0290\u0282\3\2\2\2\u0290\u0283")
        buf.write("\3\2\2\2\u0290\u0284\3\2\2\2\u0290\u0285\3\2\2\2\u0290")
        buf.write("\u0286\3\2\2\2\u0290\u0287\3\2\2\2\u0290\u0288\3\2\2\2")
        buf.write("\u0290\u0289\3\2\2\2\u0290\u028a\3\2\2\2\u0290\u028b\3")
        buf.write("\2\2\2\u0290\u028c\3\2\2\2\u0291\u009f\3\2\2\2\u0292\u0294")
        buf.write("\5\u00a2R\2\u0293\u0295\5\u00a0Q\2\u0294\u0293\3\2\2\2")
        buf.write("\u0294\u0295\3\2\2\2\u0295\u00a1\3\2\2\2\u0296\u0297\7")
        buf.write("\61\2\2\u0297\u0298\5\u0082B\2\u0298\u0299\7\62\2\2\u0299")
        buf.write("\u00a3\3\2\2\2\u029a\u029b\7,\2\2\u029b\u029d\7\66\2\2")
        buf.write("\u029c\u029e\5\u00a0Q\2\u029d\u029c\3\2\2\2\u029d\u029e")
        buf.write("\3\2\2\2\u029e\u02a0\3\2\2\2\u029f\u02a1\5\u00a4S\2\u02a0")
        buf.write("\u029f\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u00a5\3\2\2\2")
        buf.write("\u02a2\u02a4\7\66\2\2\u02a3\u02a5\5\u00a0Q\2\u02a4\u02a3")
        buf.write("\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a7\3\2\2\2\u02a6")
        buf.write("\u02a8\5\u00a4S\2\u02a7\u02a6\3\2\2\2\u02a7\u02a8\3\2")
        buf.write("\2\2\u02a8\u00a7\3\2\2\2\u02a9\u02aa\7,\2\2\u02aa\u02ac")
        buf.write("\7\66\2\2\u02ab\u02ad\5\u00a8U\2\u02ac\u02ab\3\2\2\2\u02ac")
        buf.write("\u02ad\3\2\2\2\u02ad\u02bd\3\2\2\2\u02ae\u02af\7,\2\2")
        buf.write("\u02af\u02b0\7\66\2\2\u02b0\u02b2\5\u00a0Q\2\u02b1\u02b3")
        buf.write("\5\u00a8U\2\u02b2\u02b1\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3")
        buf.write("\u02bd\3\2\2\2\u02b4\u02b5\7,\2\2\u02b5\u02b6\7\66\2\2")
        buf.write("\u02b6\u02b7\5\u009cO\2\u02b7\u02b8\5\u00a0Q\2\u02b8\u02ba")
        buf.write("\3\2\2\2\u02b9\u02bb\5\u00a8U\2\u02ba\u02b9\3\2\2\2\u02ba")
        buf.write("\u02bb\3\2\2\2\u02bb\u02bd\3\2\2\2\u02bc\u02a9\3\2\2\2")
        buf.write("\u02bc\u02ae\3\2\2\2\u02bc\u02b4\3\2\2\2\u02bd\u00a9\3")
        buf.write("\2\2\2>\u00b1\u00b6\u00bc\u00cc\u00d3\u00db\u00e0\u00e5")
        buf.write("\u00ee\u0100\u0112\u0117\u011c\u0125\u012e\u0132\u0137")
        buf.write("\u0147\u0153\u0157\u0161\u016d\u0172\u017e\u0186\u018b")
        buf.write("\u0190\u0198\u019e\u01ab\u01b2\u01b7\u01d3\u01e5\u01ef")
        buf.write("\u01f5\u01f8\u01fb\u0200\u021a\u0224\u022f\u023b\u0249")
        buf.write("\u0257\u0260\u026b\u0272\u027a\u027e\u0290\u0294\u029d")
        buf.write("\u02a0\u02a4\u02a7\u02ac\u02b2\u02ba\u02bc")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "':='", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
                     "'||'", "'!'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOL", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NEWASS", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", 
                      "AND", "OR", "NEGATION", "ASSIGN", "ADDVAL", "SUBVAL", 
                      "MULVAL", "DIVVAL", "MODVAL", "POINT", "R_OPEN", "R_CLOSE", 
                      "CUR_OPEN", "CUR_CLOSE", "SQ_OPEN", "SQ_CLOSE", "COMMA", 
                      "SEMI_COLON", "COLON", "ID", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "CMTLINE", "CMTBLOCK", "WS", "NEWLINE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_program_lst = 1
    RULE_program_mem = 2
    RULE_declared = 3
    RULE_literal = 4
    RULE_array_lit = 5
    RULE_array_type = 6
    RULE_array_lit_lst = 7
    RULE_array_lit_mem = 8
    RULE_array_lit_mem_single = 9
    RULE_struct_lit = 10
    RULE_list_struct_elem_lst = 11
    RULE_list_struct_elem_mem = 12
    RULE_struct_type = 13
    RULE_struct_attribute_lst = 14
    RULE_struct_attribute_mem = 15
    RULE_interface_type = 16
    RULE_interface_method_lst = 17
    RULE_interface_method_mem = 18
    RULE_interface_method_param_lst = 19
    RULE_interface_method_param_lst_mem = 20
    RULE_id_lst = 21
    RULE_var_decl = 22
    RULE_var_decl_with_init = 23
    RULE_var_decl_non_init = 24
    RULE_prim_type = 25
    RULE_var_type = 26
    RULE_const_decl = 27
    RULE_func_decl = 28
    RULE_para_lst = 29
    RULE_para_mem = 30
    RULE_method_decl = 31
    RULE_method_receiver_lst = 32
    RULE_method_receiver_mem = 33
    RULE_block_func = 34
    RULE_block_func_lst = 35
    RULE_block_func_mem = 36
    RULE_stmt_block = 37
    RULE_stmt = 38
    RULE_for_stmt = 39
    RULE_for_stmt_01 = 40
    RULE_for_stmt_01_init = 41
    RULE_for_stmt_01_cond = 42
    RULE_for_stmt_01_upda = 43
    RULE_for_stmt_01_var_decl_init = 44
    RULE_for_stmt_01_upda_incr = 45
    RULE_for_stmt_01_assign = 46
    RULE_for_stmt_02 = 47
    RULE_for_stmt_03 = 48
    RULE_if_stmt = 49
    RULE_if_stmt_rec = 50
    RULE_if_stmt_type1 = 51
    RULE_if_stmt_type2 = 52
    RULE_else_stmt = 53
    RULE_break_stmt = 54
    RULE_cont_stmt = 55
    RULE_return_stmt = 56
    RULE_call_func = 57
    RULE_func_call = 58
    RULE_assign_stmt_semi = 59
    RULE_assign_stmt = 60
    RULE_increase_stmt = 61
    RULE_increase_stmt_semi = 62
    RULE_expr_list = 63
    RULE_expr = 64
    RULE_expr1 = 65
    RULE_expr2 = 66
    RULE_comp_op = 67
    RULE_expr3 = 68
    RULE_add_op = 69
    RULE_expr4 = 70
    RULE_mul_op = 71
    RULE_expr5 = 72
    RULE_unary_op = 73
    RULE_expr6 = 74
    RULE_expr6_postfix_lst = 75
    RULE_expr6_postfix_mem = 76
    RULE_method_args = 77
    RULE_expr7 = 78
    RULE_array_access = 79
    RULE_array_index = 80
    RULE_attribute_chain = 81
    RULE_lhs_expr = 82
    RULE_property_chain = 83

    ruleNames =  [ "program", "program_lst", "program_mem", "declared", 
                   "literal", "array_lit", "array_type", "array_lit_lst", 
                   "array_lit_mem", "array_lit_mem_single", "struct_lit", 
                   "list_struct_elem_lst", "list_struct_elem_mem", "struct_type", 
                   "struct_attribute_lst", "struct_attribute_mem", "interface_type", 
                   "interface_method_lst", "interface_method_mem", "interface_method_param_lst", 
                   "interface_method_param_lst_mem", "id_lst", "var_decl", 
                   "var_decl_with_init", "var_decl_non_init", "prim_type", 
                   "var_type", "const_decl", "func_decl", "para_lst", "para_mem", 
                   "method_decl", "method_receiver_lst", "method_receiver_mem", 
                   "block_func", "block_func_lst", "block_func_mem", "stmt_block", 
                   "stmt", "for_stmt", "for_stmt_01", "for_stmt_01_init", 
                   "for_stmt_01_cond", "for_stmt_01_upda", "for_stmt_01_var_decl_init", 
                   "for_stmt_01_upda_incr", "for_stmt_01_assign", "for_stmt_02", 
                   "for_stmt_03", "if_stmt", "if_stmt_rec", "if_stmt_type1", 
                   "if_stmt_type2", "else_stmt", "break_stmt", "cont_stmt", 
                   "return_stmt", "call_func", "func_call", "assign_stmt_semi", 
                   "assign_stmt", "increase_stmt", "increase_stmt_semi", 
                   "expr_list", "expr", "expr1", "expr2", "comp_op", "expr3", 
                   "add_op", "expr4", "mul_op", "expr5", "unary_op", "expr6", 
                   "expr6_postfix_lst", "expr6_postfix_mem", "method_args", 
                   "expr7", "array_access", "array_index", "attribute_chain", 
                   "lhs_expr", "property_chain" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOL=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    NEWASS=26
    EQ=27
    NEQ=28
    LT=29
    LTE=30
    GT=31
    GTE=32
    AND=33
    OR=34
    NEGATION=35
    ASSIGN=36
    ADDVAL=37
    SUBVAL=38
    MULVAL=39
    DIVVAL=40
    MODVAL=41
    POINT=42
    R_OPEN=43
    R_CLOSE=44
    CUR_OPEN=45
    CUR_CLOSE=46
    SQ_OPEN=47
    SQ_CLOSE=48
    COMMA=49
    SEMI_COLON=50
    COLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    CMTLINE=56
    CMTBLOCK=57
    WS=58
    NEWLINE=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Program_lstContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.program_lst()
            self.state = 169
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Program_memContext,0)


        def program_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Program_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_lst" ):
                return visitor.visitProgram_lst(self)
            else:
                return visitor.visitChildren(self)




    def program_lst(self):

        localctx = MiniGoParser.Program_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_lst)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.program_mem()
                self.state = 172
                self.program_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.program_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_mem" ):
                return visitor.visitProgram_mem(self)
            else:
                return visitor.visitChildren(self)




    def program_mem(self):

        localctx = MiniGoParser.Program_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program_mem)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.declared()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.var_decl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.const_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declared)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.method_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.struct_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.interface_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def array_lit_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_lstContext,0)


        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.array_type()
            self.state = 191
            self.match(MiniGoParser.CUR_OPEN)
            self.state = 192
            self.array_lit_lst()
            self.state = 193
            self.match(MiniGoParser.CUR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_OPEN(self):
            return self.getToken(MiniGoParser.SQ_OPEN, 0)

        def SQ_CLOSE(self):
            return self.getToken(MiniGoParser.SQ_CLOSE, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def prim_type(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.SQ_OPEN)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 197
            self.match(MiniGoParser.SQ_CLOSE)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SQ_OPEN]:
                self.state = 199
                self.array_type()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOL]:
                self.state = 200
                self.prim_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 201
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_memContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_lit_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_lst" ):
                return visitor.visitArray_lit_lst(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_lst(self):

        localctx = MiniGoParser.Array_lit_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_lit_lst)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.array_lit_mem()
                self.state = 205
                self.match(MiniGoParser.COMMA)
                self.state = 206
                self.array_lit_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.array_lit_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def array_lit_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_lstContext,0)


        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def array_lit_mem_single(self):
            return self.getTypedRuleContext(MiniGoParser.Array_lit_mem_singleContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_mem" ):
                return visitor.visitArray_lit_mem(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_mem(self):

        localctx = MiniGoParser.Array_lit_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_lit_mem)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CUR_CLOSE, MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.CUR_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MiniGoParser.CUR_OPEN)
                self.state = 213
                self.array_lit_lst()
                self.state = 214
                self.match(MiniGoParser.CUR_CLOSE)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.array_lit_mem_single()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_mem_singleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit_mem_single

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_mem_single" ):
                return visitor.visitArray_lit_mem_single(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_mem_single(self):

        localctx = MiniGoParser.Array_lit_mem_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_lit_mem_single)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.struct_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def list_struct_elem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elem_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.ID)
            self.state = 225
            self.match(MiniGoParser.CUR_OPEN)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 226
                self.list_struct_elem_lst()


            self.state = 229
            self.match(MiniGoParser.CUR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elem_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_struct_elem_mem(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elem_memContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_struct_elem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_elem_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_elem_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_elem_lst" ):
                return visitor.visitList_struct_elem_lst(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_elem_lst(self):

        localctx = MiniGoParser.List_struct_elem_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_struct_elem_lst)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.list_struct_elem_mem()
                self.state = 232
                self.match(MiniGoParser.COMMA)
                self.state = 233
                self.list_struct_elem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.list_struct_elem_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_elem_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_elem_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_elem_mem" ):
                return visitor.visitList_struct_elem_mem(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_elem_mem(self):

        localctx = MiniGoParser.List_struct_elem_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_struct_elem_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 239
            self.match(MiniGoParser.COLON)
            self.state = 240
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def struct_attribute_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attribute_lstContext,0)


        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.TYPE)
            self.state = 243
            self.match(MiniGoParser.ID)
            self.state = 244
            self.match(MiniGoParser.STRUCT)
            self.state = 245
            self.match(MiniGoParser.CUR_OPEN)
            self.state = 246
            self.struct_attribute_lst()
            self.state = 247
            self.match(MiniGoParser.CUR_CLOSE)
            self.state = 248
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_attribute_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_attribute_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attribute_memContext,0)


        def struct_attribute_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attribute_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_attribute_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_attribute_lst" ):
                return visitor.visitStruct_attribute_lst(self)
            else:
                return visitor.visitChildren(self)




    def struct_attribute_lst(self):

        localctx = MiniGoParser.Struct_attribute_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_attribute_lst)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.struct_attribute_mem()
                self.state = 251
                self.struct_attribute_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.struct_attribute_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_attribute_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_attribute_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_attribute_mem" ):
                return visitor.visitStruct_attribute_mem(self)
            else:
                return visitor.visitChildren(self)




    def struct_attribute_mem(self):

        localctx = MiniGoParser.Struct_attribute_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_attribute_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.ID)
            self.state = 257
            self.var_type()
            self.state = 258
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def interface_method_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_lstContext,0)


        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.TYPE)
            self.state = 261
            self.match(MiniGoParser.ID)
            self.state = 262
            self.match(MiniGoParser.INTERFACE)
            self.state = 263
            self.match(MiniGoParser.CUR_OPEN)
            self.state = 264
            self.interface_method_lst()
            self.state = 265
            self.match(MiniGoParser.CUR_CLOSE)
            self.state = 266
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_memContext,0)


        def interface_method_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_lst" ):
                return visitor.visitInterface_method_lst(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_lst(self):

        localctx = MiniGoParser.Interface_method_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interface_method_lst)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.interface_method_mem()
                self.state = 269
                self.interface_method_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.interface_method_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def interface_method_param_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_mem" ):
                return visitor.visitInterface_method_mem(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_mem(self):

        localctx = MiniGoParser.Interface_method_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_interface_method_mem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.ID)

            self.state = 275
            self.match(MiniGoParser.R_OPEN)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 276
                self.interface_method_param_lst()


            self.state = 279
            self.match(MiniGoParser.R_CLOSE)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 281
                self.var_type()


            self.state = 284
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method_param_lst_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_lst_memContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def interface_method_param_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_method_param_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param_lst" ):
                return visitor.visitInterface_method_param_lst(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param_lst(self):

        localctx = MiniGoParser.Interface_method_param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_interface_method_param_lst)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.interface_method_param_lst_mem()
                self.state = 287
                self.match(MiniGoParser.COMMA)
                self.state = 288
                self.interface_method_param_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.interface_method_param_lst_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_method_param_lst_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_lstContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method_param_lst_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method_param_lst_mem" ):
                return visitor.visitInterface_method_param_lst_mem(self)
            else:
                return visitor.visitChildren(self)




    def interface_method_param_lst_mem(self):

        localctx = MiniGoParser.Interface_method_param_lst_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_interface_method_param_lst_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.id_lst()
            self.state = 294
            self.var_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_lst" ):
                return visitor.visitId_lst(self)
            else:
                return visitor.visitChildren(self)




    def id_lst(self):

        localctx = MiniGoParser.Id_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_id_lst)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(MiniGoParser.ID)
                self.state = 297
                self.match(MiniGoParser.COMMA)
                self.state = 298
                self.id_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_non_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_non_initContext,0)


        def var_decl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_with_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_decl)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.var_decl_non_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.var_decl_with_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_with_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_with_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_with_init" ):
                return visitor.visitVar_decl_with_init(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_with_init(self):

        localctx = MiniGoParser.Var_decl_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_var_decl_with_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.VAR)
            self.state = 307
            self.match(MiniGoParser.ID)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 308
                self.var_type()


            self.state = 311
            self.match(MiniGoParser.ASSIGN)

            self.state = 312
            self.expr(0)
            self.state = 313
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_non_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_non_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_non_init" ):
                return visitor.visitVar_decl_non_init(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_non_init(self):

        localctx = MiniGoParser.Var_decl_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_decl_non_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MiniGoParser.VAR)
            self.state = 316
            self.match(MiniGoParser.ID)

            self.state = 317
            self.var_type()
            self.state = 318
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOL(self):
            return self.getToken(MiniGoParser.BOOL, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prim_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrim_type" ):
                return visitor.visitPrim_type(self)
            else:
                return visitor.visitChildren(self)




    def prim_type(self):

        localctx = MiniGoParser.Prim_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_prim_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(MiniGoParser.Prim_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = MiniGoParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_var_type)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.prim_type()
                pass
            elif token in [MiniGoParser.SQ_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.array_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MiniGoParser.CONST)
            self.state = 328
            self.match(MiniGoParser.ID)

            self.state = 329
            self.match(MiniGoParser.ASSIGN)

            self.state = 330
            self.expr(0)
            self.state = 331
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def para_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Para_lstContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.FUNC)
            self.state = 334
            self.match(MiniGoParser.ID)
            self.state = 335
            self.match(MiniGoParser.R_OPEN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 336
                self.para_lst()


            self.state = 339
            self.match(MiniGoParser.R_CLOSE)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 340
                self.var_type()


            self.state = 343
            self.block_func()
            self.state = 344
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Para_memContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def para_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Para_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_lst" ):
                return visitor.visitPara_lst(self)
            else:
                return visitor.visitChildren(self)




    def para_lst(self):

        localctx = MiniGoParser.Para_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_para_lst)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.para_mem()
                self.state = 347
                self.match(MiniGoParser.COMMA)
                self.state = 348
                self.para_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.para_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_lstContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_mem" ):
                return visitor.visitPara_mem(self)
            else:
                return visitor.visitChildren(self)




    def para_mem(self):

        localctx = MiniGoParser.Para_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_para_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.id_lst()
            self.state = 354
            self.var_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def R_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.R_OPEN)
            else:
                return self.getToken(MiniGoParser.R_OPEN, i)

        def R_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.R_CLOSE)
            else:
                return self.getToken(MiniGoParser.R_CLOSE, i)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def method_receiver_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Method_receiver_lstContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def para_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Para_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(MiniGoParser.FUNC)
            self.state = 357
            self.match(MiniGoParser.R_OPEN)

            self.state = 358
            self.method_receiver_lst()
            self.state = 359
            self.match(MiniGoParser.R_CLOSE)
            self.state = 360
            self.match(MiniGoParser.ID)

            self.state = 361
            self.match(MiniGoParser.R_OPEN)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 362
                self.para_lst()


            self.state = 365
            self.match(MiniGoParser.R_CLOSE)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 367
                self.var_type()


            self.state = 370
            self.block_func()
            self.state = 371
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_receiver_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_receiver_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Method_receiver_memContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_receiver_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_receiver_lst" ):
                return visitor.visitMethod_receiver_lst(self)
            else:
                return visitor.visitChildren(self)




    def method_receiver_lst(self):

        localctx = MiniGoParser.Method_receiver_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_method_receiver_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.method_receiver_mem()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_receiver_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_receiver_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_receiver_mem" ):
                return visitor.visitMethod_receiver_mem(self)
            else:
                return visitor.visitChildren(self)




    def method_receiver_mem(self):

        localctx = MiniGoParser.Method_receiver_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_receiver_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MiniGoParser.ID)
            self.state = 376
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUR_OPEN(self):
            return self.getToken(MiniGoParser.CUR_OPEN, 0)

        def CUR_CLOSE(self):
            return self.getToken(MiniGoParser.CUR_CLOSE, 0)

        def block_func_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Block_func_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_func" ):
                return visitor.visitBlock_func(self)
            else:
                return visitor.visitChildren(self)




    def block_func(self):

        localctx = MiniGoParser.Block_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.CUR_OPEN)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 379
                self.block_func_lst()


            self.state = 382
            self.match(MiniGoParser.CUR_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_func_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_func_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Block_func_memContext,0)


        def block_func_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Block_func_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_func_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_func_lst" ):
                return visitor.visitBlock_func_lst(self)
            else:
                return visitor.visitChildren(self)




    def block_func_lst(self):

        localctx = MiniGoParser.Block_func_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block_func_lst)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.block_func_mem()
                self.state = 385
                self.block_func_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.block_func_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_func_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_func_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_func_mem" ):
                return visitor.visitBlock_func_mem(self)
            else:
                return visitor.visitChildren(self)




    def block_func_mem(self):

        localctx = MiniGoParser.Block_func_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_block_func_mem)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.var_decl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.const_decl()
                pass
            elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.stmt_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Cont_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = MiniGoParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_block)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt()
                pass
            elif token in [MiniGoParser.BREAK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.break_stmt()
                pass
            elif token in [MiniGoParser.CONTINUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.cont_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def call_func(self):
            return self.getTypedRuleContext(MiniGoParser.Call_funcContext,0)


        def assign_stmt_semi(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmt_semiContext,0)


        def increase_stmt_semi(self):
            return self.getTypedRuleContext(MiniGoParser.Increase_stmt_semiContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.for_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.return_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.call_func()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.assign_stmt_semi()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 405
                self.increase_stmt_semi()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def for_stmt_01(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01Context,0)


        def for_stmt_02(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_02Context,0)


        def for_stmt_03(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_03Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.FOR)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 409
                self.for_stmt_01()
                pass

            elif la_ == 2:
                self.state = 410
                self.for_stmt_02()
                pass

            elif la_ == 3:
                self.state = 411
                self.for_stmt_03()
                pass


            self.state = 414
            self.block_func()
            self.state = 415
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_stmt_01_init(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_initContext,0)


        def for_stmt_01_cond(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_condContext,0)


        def for_stmt_01_upda(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_updaContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01" ):
                return visitor.visitFor_stmt_01(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01(self):

        localctx = MiniGoParser.For_stmt_01Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_stmt_01)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.for_stmt_01_init()
            self.state = 418
            self.for_stmt_01_cond()
            self.state = 419
            self.for_stmt_01_upda()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_stmt_01_upda(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_updaContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def for_stmt_01_var_decl_init(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_var_decl_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_init" ):
                return visitor.visitFor_stmt_01_init(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_init(self):

        localctx = MiniGoParser.For_stmt_01_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_for_stmt_01_init)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.for_stmt_01_upda()
                self.state = 422
                self.match(MiniGoParser.SEMI_COLON)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.for_stmt_01_var_decl_init()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_cond" ):
                return visitor.visitFor_stmt_01_cond(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_cond(self):

        localctx = MiniGoParser.For_stmt_01_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_for_stmt_01_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.expr(0)
            self.state = 428
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_updaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_stmt_01_upda_incr(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_upda_incrContext,0)


        def for_stmt_01_assign(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmt_01_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_upda

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_upda" ):
                return visitor.visitFor_stmt_01_upda(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_upda(self):

        localctx = MiniGoParser.For_stmt_01_updaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_for_stmt_01_upda)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.for_stmt_01_upda_incr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.for_stmt_01_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_var_decl_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_var_decl_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_var_decl_init" ):
                return visitor.visitFor_stmt_01_var_decl_init(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_var_decl_init(self):

        localctx = MiniGoParser.For_stmt_01_var_decl_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_for_stmt_01_var_decl_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.VAR)
            self.state = 435
            self.match(MiniGoParser.ID)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 436
                self.var_type()


            self.state = 439
            self.match(MiniGoParser.ASSIGN)

            self.state = 440
            self.expr(0)
            self.state = 441
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_upda_incrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ADDVAL(self):
            return self.getToken(MiniGoParser.ADDVAL, 0)

        def SUBVAL(self):
            return self.getToken(MiniGoParser.SUBVAL, 0)

        def MULVAL(self):
            return self.getToken(MiniGoParser.MULVAL, 0)

        def DIVVAL(self):
            return self.getToken(MiniGoParser.DIVVAL, 0)

        def MODVAL(self):
            return self.getToken(MiniGoParser.MODVAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_upda_incr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_upda_incr" ):
                return visitor.visitFor_stmt_01_upda_incr(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_upda_incr(self):

        localctx = MiniGoParser.For_stmt_01_upda_incrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_for_stmt_01_upda_incr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(MiniGoParser.ID)
            self.state = 444
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADDVAL) | (1 << MiniGoParser.SUBVAL) | (1 << MiniGoParser.MULVAL) | (1 << MiniGoParser.DIVVAL) | (1 << MiniGoParser.MODVAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 445
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_01_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def NEWASS(self):
            return self.getToken(MiniGoParser.NEWASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_01_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_01_assign" ):
                return visitor.visitFor_stmt_01_assign(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_01_assign(self):

        localctx = MiniGoParser.For_stmt_01_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_stmt_01_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(MiniGoParser.ID)

            self.state = 448
            self.match(MiniGoParser.NEWASS)
            self.state = 449
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_02Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def NEWASS(self):
            return self.getToken(MiniGoParser.NEWASS, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_02

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_02" ):
                return visitor.visitFor_stmt_02(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_02(self):

        localctx = MiniGoParser.For_stmt_02Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_for_stmt_02)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.ID)
            self.state = 452
            self.match(MiniGoParser.COMMA)
            self.state = 453
            self.match(MiniGoParser.ID)
            self.state = 454
            self.match(MiniGoParser.NEWASS)
            self.state = 455
            self.match(MiniGoParser.RANGE)

            self.state = 456
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_03Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt_03

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_03" ):
                return visitor.visitFor_stmt_03(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_03(self):

        localctx = MiniGoParser.For_stmt_03Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_stmt_03)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt_rec(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_recContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.if_stmt_rec()
            self.state = 461
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_recContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt_type1(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_type1Context,0)


        def if_stmt_type2(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_type2Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_rec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_rec" ):
                return visitor.visitIf_stmt_rec(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_rec(self):

        localctx = MiniGoParser.If_stmt_recContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_if_stmt_rec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 463
                self.if_stmt_type1()
                pass

            elif la_ == 2:
                self.state = 464
                self.if_stmt_type2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_type1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_type1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_type1" ):
                return visitor.visitIf_stmt_type1(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_type1(self):

        localctx = MiniGoParser.If_stmt_type1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_if_stmt_type1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.IF)
            self.state = 468
            self.match(MiniGoParser.R_OPEN)

            self.state = 469
            self.expr(0)
            self.state = 470
            self.match(MiniGoParser.R_CLOSE)
            self.state = 471
            self.block_func()
            self.state = 472
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_type2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_type2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_type2" ):
                return visitor.visitIf_stmt_type2(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_type2(self):

        localctx = MiniGoParser.If_stmt_type2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_if_stmt_type2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.IF)
            self.state = 475
            self.match(MiniGoParser.R_OPEN)

            self.state = 476
            self.expr(0)
            self.state = 477
            self.match(MiniGoParser.R_CLOSE)
            self.state = 478
            self.block_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_stmt_rec(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_recContext,0)


        def block_func(self):
            return self.getTypedRuleContext(MiniGoParser.Block_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniGoParser.ELSE)
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF]:
                self.state = 481
                self.if_stmt_rec()
                pass
            elif token in [MiniGoParser.CUR_OPEN]:
                self.state = 482
                self.block_func()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.BREAK)
            self.state = 486
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = MiniGoParser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.CONTINUE)
            self.state = 489
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.RETURN)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NEGATION) | (1 << MiniGoParser.R_OPEN) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 492
                self.expr(0)


            self.state = 495
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def POINT(self):
            return self.getToken(MiniGoParser.POINT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_args(self):
            return self.getTypedRuleContext(MiniGoParser.Method_argsContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def property_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Property_chainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = MiniGoParser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_call_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 497
                self.match(MiniGoParser.ID)
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.R_OPEN:
                    self.state = 498
                    self.method_args()


                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SQ_OPEN:
                    self.state = 501
                    self.array_access()


                self.state = 505
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 504
                    self.property_chain()


                self.state = 507
                self.match(MiniGoParser.POINT)
                self.state = 508
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 509
                self.func_call()
                pass


            self.state = 512
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def method_args(self):
            return self.getTypedRuleContext(MiniGoParser.Method_argsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.ID)
            self.state = 515
            self.method_args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmt_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt_semi" ):
                return visitor.visitAssign_stmt_semi(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt_semi(self):

        localctx = MiniGoParser.Assign_stmt_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_assign_stmt_semi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.assign_stmt()
            self.state = 518
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def NEWASS(self):
            return self.getToken(MiniGoParser.NEWASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.lhs_expr()

            self.state = 521
            self.match(MiniGoParser.NEWASS)
            self.state = 522
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Increase_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ADDVAL(self):
            return self.getToken(MiniGoParser.ADDVAL, 0)

        def SUBVAL(self):
            return self.getToken(MiniGoParser.SUBVAL, 0)

        def MULVAL(self):
            return self.getToken(MiniGoParser.MULVAL, 0)

        def DIVVAL(self):
            return self.getToken(MiniGoParser.DIVVAL, 0)

        def MODVAL(self):
            return self.getToken(MiniGoParser.MODVAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_increase_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrease_stmt" ):
                return visitor.visitIncrease_stmt(self)
            else:
                return visitor.visitChildren(self)




    def increase_stmt(self):

        localctx = MiniGoParser.Increase_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_increase_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.lhs_expr()
            self.state = 525
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADDVAL) | (1 << MiniGoParser.SUBVAL) | (1 << MiniGoParser.MULVAL) | (1 << MiniGoParser.DIVVAL) | (1 << MiniGoParser.MODVAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 526
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Increase_stmt_semiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def increase_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Increase_stmtContext,0)


        def SEMI_COLON(self):
            return self.getToken(MiniGoParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_increase_stmt_semi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrease_stmt_semi" ):
                return visitor.visitIncrease_stmt_semi(self)
            else:
                return visitor.visitChildren(self)




    def increase_stmt_semi(self):

        localctx = MiniGoParser.Increase_stmt_semiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_increase_stmt_semi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.increase_stmt()
            self.state = 529
            self.match(MiniGoParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_expr_list)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.expr(0)
                self.state = 532
                self.match(MiniGoParser.COMMA)
                self.state = 533
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 541
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 542
                    self.match(MiniGoParser.OR)
                    self.state = 543
                    self.expr1(0) 
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 557
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 552
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 553
                    self.match(MiniGoParser.AND)
                    self.state = 554
                    self.expr2(0) 
                self.state = 559
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def comp_op(self):
            return self.getTypedRuleContext(MiniGoParser.Comp_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 569
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 563
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 564
                    self.comp_op()
                    self.state = 565
                    self.expr3(0) 
                self.state = 571
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comp_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_comp_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_op" ):
                return visitor.visitComp_op(self)
            else:
                return visitor.visitChildren(self)




    def comp_op(self):

        localctx = MiniGoParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def add_op(self):
            return self.getTypedRuleContext(MiniGoParser.Add_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 577
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 578
                    self.add_op()
                    self.state = 579
                    self.expr4(0) 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = MiniGoParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def mul_op(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 597
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 591
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 592
                    self.mul_op()
                    self.state = 593
                    self.expr5() 
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = MiniGoParser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_op(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_opContext,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_expr5)
        try:
            self.state = 606
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NEGATION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.unary_op()
                self.state = 603
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.R_OPEN, MiniGoParser.SQ_OPEN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATION(self):
            return self.getToken(MiniGoParser.NEGATION, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = MiniGoParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NEGATION):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def expr6_postfix_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6_postfix_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 617
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 613
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 614
                    self.expr6_postfix_lst() 
                self.state = 619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6_postfix_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6_postfix_mem(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6_postfix_memContext,0)


        def expr6_postfix_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6_postfix_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6_postfix_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6_postfix_lst" ):
                return visitor.visitExpr6_postfix_lst(self)
            else:
                return visitor.visitChildren(self)




    def expr6_postfix_lst(self):

        localctx = MiniGoParser.Expr6_postfix_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_expr6_postfix_lst)
        try:
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.expr6_postfix_mem()
                self.state = 621
                self.expr6_postfix_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 623
                self.expr6_postfix_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6_postfix_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINT(self):
            return self.getToken(MiniGoParser.POINT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def method_args(self):
            return self.getTypedRuleContext(MiniGoParser.Method_argsContext,0)


        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6_postfix_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6_postfix_mem" ):
                return visitor.visitExpr6_postfix_mem(self)
            else:
                return visitor.visitChildren(self)




    def expr6_postfix_mem(self):

        localctx = MiniGoParser.Expr6_postfix_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_expr6_postfix_mem)
        try:
            self.state = 632
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.match(MiniGoParser.POINT)
                self.state = 627
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(MiniGoParser.POINT)
                self.state = 629
                self.match(MiniGoParser.ID)
                self.state = 630
                self.method_args()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 631
                self.array_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_args" ):
                return visitor.visitMethod_args(self)
            else:
                return visitor.visitChildren(self)




    def method_args(self):

        localctx = MiniGoParser.Method_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_method_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.match(MiniGoParser.R_OPEN)
            self.state = 636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NEGATION) | (1 << MiniGoParser.R_OPEN) | (1 << MiniGoParser.SQ_OPEN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 635
                self.expr_list()


            self.state = 638
            self.match(MiniGoParser.R_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def R_OPEN(self):
            return self.getToken(MiniGoParser.R_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def R_CLOSE(self):
            return self.getToken(MiniGoParser.R_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_expr7)
        try:
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 642
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 643
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 644
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 645
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 646
                self.array_lit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 647
                self.struct_lit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 648
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 649
                self.func_call()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 650
                self.match(MiniGoParser.R_OPEN)
                self.state = 651
                self.expr(0)
                self.state = 652
                self.match(MiniGoParser.R_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_array_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.array_index()
            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SQ_OPEN:
                self.state = 657
                self.array_access()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_OPEN(self):
            return self.getToken(MiniGoParser.SQ_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SQ_CLOSE(self):
            return self.getToken(MiniGoParser.SQ_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(MiniGoParser.SQ_OPEN)
            self.state = 661
            self.expr(0)
            self.state = 662
            self.match(MiniGoParser.SQ_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_chainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINT(self):
            return self.getToken(MiniGoParser.POINT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def attribute_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Attribute_chainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_attribute_chain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_chain" ):
                return visitor.visitAttribute_chain(self)
            else:
                return visitor.visitChildren(self)




    def attribute_chain(self):

        localctx = MiniGoParser.Attribute_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_attribute_chain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(MiniGoParser.POINT)
            self.state = 665
            self.match(MiniGoParser.ID)
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SQ_OPEN:
                self.state = 666
                self.array_access()


            self.state = 670
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.POINT:
                self.state = 669
                self.attribute_chain()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def attribute_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Attribute_chainContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_expr" ):
                return visitor.visitLhs_expr(self)
            else:
                return visitor.visitChildren(self)




    def lhs_expr(self):

        localctx = MiniGoParser.Lhs_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_lhs_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(MiniGoParser.ID)
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SQ_OPEN:
                self.state = 673
                self.array_access()


            self.state = 677
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.POINT:
                self.state = 676
                self.attribute_chain()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Property_chainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINT(self):
            return self.getToken(MiniGoParser.POINT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def property_chain(self):
            return self.getTypedRuleContext(MiniGoParser.Property_chainContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def method_args(self):
            return self.getTypedRuleContext(MiniGoParser.Method_argsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_property_chain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProperty_chain" ):
                return visitor.visitProperty_chain(self)
            else:
                return visitor.visitChildren(self)




    def property_chain(self):

        localctx = MiniGoParser.Property_chainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_property_chain)
        try:
            self.state = 698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                self.match(MiniGoParser.POINT)
                self.state = 680
                self.match(MiniGoParser.ID)
                self.state = 682
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 681
                    self.property_chain()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 684
                self.match(MiniGoParser.POINT)
                self.state = 685
                self.match(MiniGoParser.ID)
                self.state = 686
                self.array_access()
                self.state = 688
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 687
                    self.property_chain()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 690
                self.match(MiniGoParser.POINT)
                self.state = 691
                self.match(MiniGoParser.ID)

                self.state = 692
                self.method_args()
                self.state = 693
                self.array_access()
                self.state = 696
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 695
                    self.property_chain()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[64] = self.expr_sempred
        self._predicates[65] = self.expr1_sempred
        self._predicates[66] = self.expr2_sempred
        self._predicates[68] = self.expr3_sempred
        self._predicates[70] = self.expr4_sempred
        self._predicates[74] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




