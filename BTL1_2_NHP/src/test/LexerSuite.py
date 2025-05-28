# ------------------------------------------------
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# ------------------------------------------------     

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    # def test_keyword_var(self):
    #     """test keyword var"""
    #     self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    # def test_keyword_func(self):
    #     """test keyword func"""
    #     self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 101))

    def test_002(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else", "else,<EOF>", 102))

    def test_003(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("return", "return,<EOF>", 103))

    def test_004(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("func type struct", "func,type,struct,<EOF>", 104))

    def test_005(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("boolean string int float", "boolean,string,int,float,<EOF>", 105))

    # ------------------- Operators -------------------
    
    def test_006(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 106))

    def test_007(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("== != > < <= >=", "==,!=,>,<,<=,>=,<EOF>", 107))

    def test_008(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 108))

    def test_009(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("= += -= *= /= %=", "=,+=,-=,*=,/=,%=,<EOF>", 109))

    def test_010(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme(":=", ":=,<EOF>", 110))

    # ------------------- Separators -------------------

    def test_011(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("() {}", "(,),{,},<EOF>", 111))

    def test_012(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[],", "[,],,,<EOF>", 112))

    def test_013(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 113))

    def test_014(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme(":", ":,<EOF>", 114))

    # ------------------- Identifiers -------------------

    def test_015(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_validID _Another123", "_validID,_Another123,<EOF>", 115))

    def test_016(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("VarName varName123", "VarName,varName123,<EOF>", 116))

    # ------------------- Integer Literals -------------------

    def test_017(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("123 0 99999999", "123,0,99999999,<EOF>", 117))

    def test_018(self):
        """Literals INT - Binary"""
        self.assertTrue(TestLexer.checkLexeme("0b1010", "0b1010,<EOF>", 118))

    def test_019(self):
        """Literals INT - Octal"""
        self.assertTrue(TestLexer.checkLexeme("0o77", "0o77,<EOF>", 119))

    def test_020(self):
        """Literals INT - Hexadecimal"""
        self.assertTrue(TestLexer.checkLexeme("0x1A", "0x1A,<EOF>", 120))

    # ------------------- Float Literals -------------------

    def test_021(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.34", "12.34,<EOF>", 121))

    def test_022(self):
        """Literals FLOAT with exponent"""
        self.assertTrue(TestLexer.checkLexeme("001.2e-3", "001.2e-3,<EOF>", 122))

    def test_023(self):
        """Literals FLOAT without integer before dot"""
        self.assertTrue(TestLexer.checkLexeme(".456", ".,456,<EOF>", 123))

    def test_024(self):
        """Literals FLOAT with exponent but missing digits"""
        self.assertTrue(TestLexer.checkLexeme(".e+2", ".,e,+,2,<EOF>", 124))

    # ------------------- String Literals -------------------

    def test_025(self):
        """Literals STRING"""
        self.assertTrue(TestLexer.checkLexeme('"Hello World"', '"Hello World",<EOF>', 125))

    def test_026(self):
        """Literals STRING with escape sequences"""
        self.assertTrue(TestLexer.checkLexeme('"Line\\nBreak"', '"Line\\nBreak",<EOF>', 126))

    def test_027(self):
        """Literals STRING with illegal escape"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal\\qEscape"', "Illegal escape in string: \"Illegal\\q", 127))

    def test_028(self):
        """Literals STRING - Unclosed"""
        self.assertTrue(TestLexer.checkLexeme('"Unclosed String', 'Unclosed string: "Unclosed String', 128))

    # ------------------- Comments -------------------

    def test_029(self):
        """Single-line comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment", "<EOF>", 129))

    def test_030(self):
        """Multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme("""
            /* test
            / a / */
        """, "<EOF>", 130))

    def test_031(self):
        """Nested comments"""
        self.assertTrue(TestLexer.checkLexeme("/* Outer /* Inner */ Outer again */", "<EOF>", 131))

    # ------------------- Error Handling -------------------

    def test_032(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^", "ErrorToken ^", 132))

    def test_033(self):
        """Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme('"Unfinished', 'Unclosed string: "Unfinished', 133))

    def test_034(self):
        """Illegal Escape"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal\\xEscape"', "Illegal escape in string: \"Illegal\\x", 134))

    # ------------------- Complex Cases -------------------

    def test_035(self):
        """Complex Mixed Tokens"""
        self.assertTrue(TestLexer.checkLexeme("""  func main() { 
                                                return 42; 
                                            }
                                            """, "func,main,(,),{,return,42,;,},;,<EOF>", 135))

    def test_036(self):
        """Complex Expression"""
        self.assertTrue(TestLexer.checkLexeme("a := 1 + 2.3 * (b - c);", "a,:=,1,+,2.3,*,(,b,-,c,),;,<EOF>", 136))

    def test_037(self):
        """Complex Multi-line Program"""
        self.assertTrue(TestLexer.checkLexeme("""
        func add(a int, b int) int {
            return a + b;
        }
        """, """func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},;,<EOF>""", 137))

    # ------------------- Additional Complex Cases -------------------

    def test_038(self):
        """Complex Nested Expressions"""
        self.assertTrue(TestLexer.checkLexeme("x = (y + 10) * (z - 5);", "x,=,(,y,+,10,),*,(,z,-,5,),;,<EOF>", 138))

    def test_039(self):
        """Function Definition"""
        self.assertTrue(TestLexer.checkLexeme("""  
                                    func foo(x int, y float) { 
                                        return x * y; 
                                    }
                                    """, "func,foo,(,x,int,,,y,float,),{,return,x,*,y,;,},;,<EOF>", 139))

    def test_040(self):
        """Variable Declaration"""
        self.assertTrue(TestLexer.checkLexeme("var a int = 42;", "var,a,int,=,42,;,<EOF>", 140))

    def test_041(self):
        """Boolean Literals"""
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 141))

    def test_042(self):
        """Nil Value"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 142))

    def test_043(self):
        """Assignment Operator"""
        self.assertTrue(TestLexer.checkLexeme("x := 100;", "x,:=,100,;,<EOF>", 143))

    def test_044(self):
        """Augmented Assignment Operators"""
        self.assertTrue(TestLexer.checkLexeme("a += 1; b -= 2; c *= 3; d /= 4;", "a,+=,1,;,b,-=,2,;,c,*=,3,;,d,/=,4,;,<EOF>", 144))

    def test_045(self):
        """For Loop"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        for i := 0; i < 10; i += 1 { 
                                            print(i); 
                                        }
                                        """, "for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},;,<EOF>", 145))
        # for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,},;,<EOF>

    def test_046(self):
        """While-like Loop using For"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        for x > 0 { 
                                            x -= 1; 
                                        }
                                        """, "for,x,>,0,{,x,-=,1,;,},;,<EOF>", 146))

    def test_047(self):
        """If-Else Statement"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        if (x > 10) { 
                                            y = 20; 
                                        } else { 
                                            y = 30; 
                                        }
                                        """, "if,(,x,>,10,),{,y,=,20,;,},else,{,y,=,30,;,},;,<EOF>", 147))
    
    def test_048(self):
        """If-Else Statement"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        if (x > 10) { 
                                            y = 20; 
                                        } 
                                        
                                        """, "if,(,x,>,10,),{,y,=,20,;,},;,<EOF>", 148))

    def test_049(self):
        """Nested If-Else"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        if (a > b) { 
                                            if (c < d) { 
                                                return a; 
                                            } 
                                        }
                                        """, "if,(,a,>,b,),{,if,(,c,<,d,),{,return,a,;,},;,},;,<EOF>", 149))

    def test_050(self):
        """Struct Definition"""
        self.assertTrue(TestLexer.checkLexeme("struct Point { x int; y int; };", "struct,Point,{,x,int,;,y,int,;,},;,<EOF>", 150))

    def test_051(self):
        """Struct Initialization"""
        self.assertTrue(TestLexer.checkLexeme("p := Point{10, 20};", "p,:=,Point,{,10,,,20,},;,<EOF>", 151))

    def test_052(self):
        """Var Declaration without initialization"""
        self.assertTrue(TestLexer.checkLexeme("var arr [5]int;", "var,arr,[,5,],int,;,<EOF>", 152))

    def test_053(self):
        """Array Access"""
        self.assertTrue(TestLexer.checkLexeme("x = arr[2];", "x,=,arr,[,2,],;,<EOF>", 153))

    def test_054(self):
        """Function Call"""
        self.assertTrue(TestLexer.checkLexeme("foo(42, 3.14);", "foo,(,42,,,3.14,),;,<EOF>", 154))

    def test_055(self):
        """Chained Function Calls"""
        self.assertTrue(TestLexer.checkLexeme("foo().bar().baz();", "foo,(,),.,bar,(,),.,baz,(,),;,<EOF>", 155))

    def test_056(self):
        """Continue Statement"""
        self.assertTrue(TestLexer.checkLexeme("continue;", "continue,;,<EOF>", 156))

    def test_057(self):
        """Break Statement"""
        self.assertTrue(TestLexer.checkLexeme("break;", "break,;,<EOF>", 157))

    def test_058(self):
        """Range Expression"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        for i in range(1, 10) { 
                                            print(i); 
                                        }
                                        """, "for,i,in,range,(,1,,,10,),{,print,(,i,),;,},;,<EOF>", 158))

    def test_059(self):
        """Multi-line String"""
        self.assertTrue(TestLexer.checkLexeme('"Line 1\\nLine 2\\n"', '"Line 1\\nLine 2\\n",<EOF>', 159))

    def test_060(self):
        """String with Escaped Double Quotes"""
        self.assertTrue(TestLexer.checkLexeme('"He said, \\"Hello!\\""', '"He said, \\"Hello!\\"",<EOF>', 160))

    def test_061(self):
        """Illegal Character"""
        self.assertTrue(TestLexer.checkLexeme("$", "ErrorToken $", 161))

    # ------------------- Additional testcases for above Cases -------------------

    def test_062(self):
        """Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme('"This is an unclosed string', 'Unclosed string: "This is an unclosed string', 162))

    def test_063(self):
        """String with Tab and Newline Escape"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\tWorld\\nEnd"', '"Hello\\tWorld\\nEnd",<EOF>', 163))

    def test_064(self):
        """String with Double Quotes Escaped"""
        self.assertTrue(TestLexer.checkLexeme('"This is a \\"quoted\\" string"', '"This is a \\"quoted\\" string",<EOF>', 164))

    def test_065(self):
        """Hexadecimal Literal with Lowercase Letters"""
        self.assertTrue(TestLexer.checkLexeme("0xabcdef", "0xabcdef,<EOF>", 165))

    def test_066(self):
        """Hexadecimal Literal with Uppercase Letters"""
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF", "0xABCDEF,<EOF>", 166))

    def test_067(self):
        """Floating Point Number Without Leading Integer would not be consider floating point"""
        self.assertTrue(TestLexer.checkLexeme(".123", ".,123,<EOF>", 167))

    def test_068(self):
        """Floating Point Number Without Trailing Integer"""
        self.assertTrue(TestLexer.checkLexeme("123.", "123.,<EOF>", 168))

    def test_069(self):
        """Floating Point Number with Exponent"""
        self.assertTrue(TestLexer.checkLexeme("5.67e8", "5.67e8,<EOF>", 169))

    def test_070(self):
        """Floating Point Number with Negative Exponent"""
        self.assertTrue(TestLexer.checkLexeme("1.2e-3", "1.2e-3,<EOF>", 170))

    def test_071(self):
        """Struct Definition"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        struct Person { 
                                            name string; 
                                            age int; 
                                        }
                                        """, "struct,Person,{,name,string,;,age,int,;,},;,<EOF>", 171))

    def test_072(self):
        """Struct with Nested Struct"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        struct Point { 
                                            x int; 
                                            y int; 
                                        } 
                                        struct Rectangle { 
                                            p1 Point; 
                                            p2 Point; 
                                        }
                                        """, "struct,Point,{,x,int,;,y,int,;,},;,struct,Rectangle,{,p1,Point,;,p2,Point,;,},;,<EOF>", 172))

    def test_073(self):
        """Array Declaration"""
        self.assertTrue(TestLexer.checkLexeme("var arr [1][2][3][10]float;", "var,arr,[,1,],[,2,],[,3,],[,10,],float,;,<EOF>", 173))

    def test_074(self):
        """Array Indexing"""
        self.assertTrue(TestLexer.checkLexeme("x = arr[5][4][3][2][1];", "x,=,arr,[,5,],[,4,],[,3,],[,2,],[,1,],;,<EOF>", 174))

    def test_075(self):
        """Accessing Struct Properties"""
        self.assertTrue(TestLexer.checkLexeme("person.name = 'John';", "person,.,name,=,ErrorToken '", 175))

    def test_076(self):
        """Logical Operators"""
        self.assertTrue(TestLexer.checkLexeme("a && b || !c", "a,&&,b,||,!,c,<EOF>", 176))

    def test_077(self):
        """Comparison Operators"""
        self.assertTrue(TestLexer.checkLexeme("x == y && y != z", "x,==,y,&&,y,!=,z,<EOF>", 177))

    def test_078(self):
        """Mathematical Operators"""
        self.assertTrue(TestLexer.checkLexeme("x = (a + b) * c - d / e % f;", "x,=,(,a,+,b,),*,c,-,d,/,e,%,f,;,<EOF>", 178))

    # ------------------- Control Flow -------------------

    def test_079(self):
        """For Loop"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        for i := 0; i < 10; i += 1 { 
                                            print(i)
                                            print(i+2)
                                            print(i+3)
                                            print(i+4)
                                            print(i+5)
                                        }
                                        """, "for,i,:=,0,;,i,<,10,;,i,+=,1,{,print,(,i,),;,print,(,i,+,2,),;,print,(,i,+,3,),;,print,(,i,+,4,),;,print,(,i,+,5,),;,},;,<EOF>", 179))

    def test_080(self):
        """While Loop Simulation with For"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        for x > 0 { 
                                            x -= 1 
                                        }
                                        """, "for,x,>,0,{,x,-=,1,;,},;,<EOF>", 180))

    def test_081(self):
        """If-Else Statement"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        if (a > b) { 
                                            return x 
                                        } else { 
                                            return y 
                                        }
                                        """, "if,(,a,>,b,),{,return,x,;,},else,{,return,y,;,},;,<EOF>", 181))

    def test_082(self):
        """Function Definition"""
        self.assertTrue(TestLexer.checkLexeme("""
                                        func sum(a int, b int) int { 
                                            return a + b; 
                                        }
                                        """, "func,sum,(,a,int,,,b,int,),int,{,return,a,+,b,;,},;,<EOF>", 182))

    def test_083(self):
        """Function Call"""
        self.assertTrue(TestLexer.checkLexeme("result = sum(10, 20);", "result,=,sum,(,10,,,20,),;,<EOF>", 183))

    def test_084(self):
        """Function Call with Nested Calls"""
        self.assertTrue(TestLexer.checkLexeme("print(sum(3, multiply(2, 5)));", "print,(,sum,(,3,,,multiply,(,2,,,5,),),),;,<EOF>", 184))

    def test_085(self):
        """Illegal Character"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 185))

    def test_086(self):
        """Illegal Escape Sequence"""
        self.assertTrue(TestLexer.checkLexeme('"Invalid\\q"', "Illegal escape in string: \"Invalid\\q", 186))

    def test_087(self):
        """Unclosed Block Comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is an unclosed comment", "/,*,This,is,an,unclosed,comment,<EOF>", 187))

    def test_088(self):
        """Empty Input"""
        self.assertTrue(TestLexer.checkLexeme("", "<EOF>", 188))

    def test_089(self):
        """Extremely Long Identifier"""
        self.assertTrue(TestLexer.checkLexeme("thisIsAnExtremelyLongIdentifierThatShouldStillBeValid1234567890", "thisIsAnExtremelyLongIdentifierThatShouldStillBeValid1234567890,<EOF>", 189))

    def test_090(self):
        """Extremely Large Integer"""
        self.assertTrue(TestLexer.checkLexeme("999999999999999999999999999999", "999999999999999999999999999999,<EOF>", 190))

    def test_091(self):
        """Mix of Valid and Invalid Tokens"""
        self.assertTrue(TestLexer.checkLexeme("123 abc #$%", "123,abc,ErrorToken #", 191))

    def test_092(self):
        """Deeply Nested Expressions with Function Calls"""
        self.assertTrue(TestLexer.checkLexeme(
            "result = foo(bar(baz(1, 2), 3), qux(4, 5));",
            "result,=,foo,(,bar,(,baz,(,1,,,2,),,,3,),,,qux,(,4,,,5,),),;,<EOF>",
            192
        ))

    def test_093(self):
        """Complex Nested Struct Definition"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            struct Outer { 
                func sum(a int, b int) int { 
                    return a + b 
                }
                attr string
            }
            """,
            "struct,Outer,{,func,sum,(,a,int,,,b,int,),int,{,return,a,+,b,;,},;,attr,string,;,},;,<EOF>",
            193
        ))

    def test_094(self):
        """Recursive Function Definition"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func factorial(n int) int { 
                if (n == 0) { 
                    return 1; 
                } 
                return n * factorial(n - 1); 
            }
            """,
            "func,factorial,(,n,int,),int,{,if,(,n,==,0,),{,return,1,;,},;,return,n,*,factorial,(,n,-,1,),;,},;,<EOF>",
            194
        ))

    def test_095(self):
        """Extreme Nesting with Loops and Conditions"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            for i := 0; i < 10; i += 1 { 
                if (i % 2 == 0) { 
                    while (j < 5) { 
                        j += 1 
                    } 
                } else { 
                    print(i) 
                } 
            }
            """,
            "for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,%,2,==,0,),{,while,(,j,<,5,),{,j,+=,1,;,},;,},else,{,print,(,i,),;,},;,},;,<EOF>",
            195
        ))

    def test_096(self):
        """Ambiguous Token Sequences"""
        self.assertTrue(TestLexer.checkLexeme(
            "x===y; a!!!b; c&&&&d;",
            "x,==,=,y,;,a,!,!,!,b,;,c,&&,&&,d,;,<EOF>",
            196
        ))

    def test_097(self):
        """Deeply Nested Arithmetic Expressions"""
        self.assertTrue(TestLexer.checkLexeme(
            "result = ((((a + b) * (c - d)) / e) % f) ** g;",
            "result,=,(,(,(,(,a,+,b,),*,(,c,-,d,),),/,e,),%,f,),*,*,g,;,<EOF>",
            197
        ))

    def test_098(self):
        """Lambda-like Function Assignment"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            func double(x int) int { 
                return x * 2 
            } 
            y = double(5);
            """,
            "func,double,(,x,int,),int,{,return,x,*,2,;,},;,y,=,double,(,5,),;,<EOF>",
            198
        ))

    def test_099(self):
        """Deeply Nested Function Calls"""
        self.assertTrue(TestLexer.checkLexeme(
            "compute(max(min(3, 5), avg(10, 20)), sqrt(16));",
            "compute,(,max,(,min,(,3,,,5,),,,avg,(,10,,,20,),),,,sqrt,(,16,),),;,<EOF>",
            199
        ))

    def test_100(self):
        """Final Complex Test Case with Mixed Syntax"""
        self.assertTrue(TestLexer.checkLexeme(
            """
            struct Matrix { 
                data [10][10]float; 
            }
            func multiply(m1 Matrix, m2 Matrix) Matrix {
                var result Matrix;
                for i := 0; i < 10; i += 1 {
                    for j := 0; j < 10; j += 1 {
                        result.data[i][j] = 0;
                        for k := 0; k < 10; k += 1 {
                            result.data[i][j] += m1.data[i][k] * m2.data[k][j]
                        }
                    }
                }
                return result;
            }
            """,
            """struct,Matrix,{,data,[,10,],[,10,],float,;,},;,func,multiply,(,m1,Matrix,,,m2,Matrix,),Matrix,{,var,result,Matrix,;,for,i,:=,0,;,i,<,10,;,i,+=,1,{,for,j,:=,0,;,j,<,10,;,j,+=,1,{,result,.,data,[,i,],[,j,],=,0,;,for,k,:=,0,;,k,<,10,;,k,+=,1,{,result,.,data,[,i,],[,j,],+=,m1,.,data,[,i,],[,k,],*,m2,.,data,[,k,],[,j,],;,},;,},;,},;,return,result,;,},;,<EOF>""", 200))
    
    # def test_khoa_tc_41(self):
    #     input = """1.02.03.04.05"""
    #     expect = """1.02,.,0,3.04,.,0,5,<EOF>"""
    #     # 1.02,.,03.04,.,0,5,<EOF>
    #     self.assertTrue(TestLexer.checkLexeme(input, expect, 201))
# ------------------------------------------------
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# ------------------------------------------------      