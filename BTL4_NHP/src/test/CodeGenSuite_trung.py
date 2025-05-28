import unittest
from TestUtils import TestCodeGen
from AST import *
import inspect

class CheckCodeGenSuite(unittest.TestCase):

    # Testing var_decl
    def test_var_decl_0(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = """20"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_1(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_2(self):
        input = """const a = 5; func main() { putInt(a); };"""
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_3(self):
        input = """func main() { const a = 7; putInt(a); };"""
        expect = """7"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_4(self):
        input = """const a = 5; var b int; func main() { putInt(a); putInt(b); };"""
        expect = """50"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_5(self):
        input = """const a = 9 / 3 + 3 * 10 ;
            func main() {
                b := a / 11 ;
                putInt(b) ;
            } ;"""
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_6(self):
        input = """const a = 9 / 3 + 3 * 10 ;
            func main() {
                b := a / 11 ;
                putInt(b) ;
            } ;

            var b = 8.2;"""
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_7(self):
        input = """const a = 9 / 3 + 3 * 10 ;
            var x = 3 + 5 ;
            func main() {
                b := a / 11 ;
                putIntLn(b) ;
                putInt(x) ;
            } ;

            var b = 8.2;"""
        expect = """3\n8"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_var_decl_8(self):
        input = """const a = 9 / 3 + 3 * 10 ;
            func main() {
                b := a / 11 ;
                putIntLn(b) ;
                putFloat(add(4)) ;
            } ;
            
            const b = 10.8 ;
            func add(c int) float {
               return b + c ;
            } ;"""
        expect = """3\n14.8"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing expr_operator
    def test_expr_operator_0(self):
        input = """func main() {putInt(5);};"""
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_1(self):
        input = """var x = 11; func main() { var a int = -10; putInt(a); };"""
        expect = """-10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_expr_operator_2(self):
        input = """var x = 11; func main() { var a = x + 10; putInt(a); };"""
        expect = """21"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_3(self):
        input = """var x = 11; func main() { var a = x - 10; putInt(a); };"""
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_4(self):
        input = """var x int = 11; func main() { var a = x % 8; putInt(a); };"""
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_5(self):
        input = """var x int = 11; func main() { var a = (x % 8) * 3 - 4; putInt(a); };"""
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_6(self):
        input = """func main() { var a boolean = true; putBool(a); };"""
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_7(self):
        input = """func main() { var a boolean = !true; putBool(a); };"""
        expect = """false"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_8(self):
        input = """var x = 2; func main() { var a boolean = x == 2; putBool(a); };"""
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_9(self):
        input = """var x = 2; func main() { var a boolean = !(x == 1); putBool(a); };"""
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_10(self):
        input = """const a = 5; 
        var b int; 
        func main() { 
            var x = (((a - 5) > b) && b > -1) || (a <= 5 && b >=0);
            putInt(a); putIntLn(b);  
            putBool(x);
        };"""
        expect = """50
true"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_expr_operator_11(self):
        input = """var b string = " 123" ;
            var a string = "trung" + b;

            func main() {
                putString(a);
            } ;"""
        expect = """trung 123"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
        
    # -------------------------------------------------------

    def test_expr_operator_12(self):
        input = """var a string = "trung" ;
            var b string = " 123" ;
            var c string = " 2345" ;

            func main() {
                b := a + b + c;
                putString(b);
            } ;"""
        expect = """trung 123 2345"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing if_stmt
    def test_if_stmt_0(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                var z = false;
                if (z) {
                    a += 3 ;
                } else {
                    a += 7 ;
                }

                putInt(a);
            } ;"""
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_if_stmt_1(self):
        input = """var a int = 4 ;
            var b int = 6 ;

            func main() {
                var z = false;

                if (z && a < b || 2 + 3 >= 5) {
                    a += 3 ;
                    putIntLn(b) ;
                } else {
                    a += 7 ;
                }

                putInt(a);
            } ;"""
        expect = """6
7"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_if_stmt_2(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                var z = false;
                if (z) {
                    a += 3 ;
                } else {
                    a += 7 ;
                }

                putInt(a);
            } ;"""
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_if_stmt_3(self):
        input = """const a = 5; 
        var b int; 
        func main() { 
            var x = (((a - 5) > b) && b > -1) || (a <= 5 && b >=0);                
            var z = false;
            if (z && x) {
                a += 3 ;
                putIntLn(b) ;
            } else {
                if (x) {
                    a += 7;
                } else {
                    a += 10;
                }
            }

            putInt(a);
        } ;"""
        expect = """12"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing assignment_stmt
    def test_assignment_stmt_0(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                a += 3 ;
                b += 6 ;
                putInt(a + b);
            } ;"""
        expect = """18"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assignment_stmt_1(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                a += 3 ;
                b += 6 ;
                putInt(a + b);
            } ;"""
        expect = """18"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assignment_stmt_2(self):
        input = """var a int = 3 ;
            var b float = 6.1 ;

            func main() {
                c := a + b;
                putFloatLn(c);
                a += 3 ;
                b += 6 ;
                putFloat(c);
            } ;"""
        expect = """9.1\n9.1"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assignment_stmt_3(self):
        input = """var a string = "trung" ;
            var b float = 6.1 ;

            func main() {
                c := a;
                putString(c);
            } ;"""
        expect = """trung"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing for_basic_stmt
    def test_for_basic_stmt_0(self):
        input = """var a string = "trung" ;

            func main() {
                var i int = 0 ;
                for i < 5 {
                    putString(a) ;
                    i += 1;
                }
            } ;"""
        expect = """trungtrungtrungtrungtrung"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
        
    # -------------------------------------------------------

    def test_for_basic_stmt_1(self):
        input = """var a string = "trung" ;

            func main() {
                var i int = 0 ;
                for i < 5 {
                    putString(a) ;
                    if (i % 2 == 0) {
                        putIntLn(i);
                    }
                    i += 1;
                }
            } ;"""
        expect = """trung0\ntrungtrung2\ntrungtrung4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_basic_stmt_2(self):
        input = """var a string = "trung" ;

            func main() {
                var i int = 0 ;
                for i < 5 {
                    putString(a) ;
                    if (i % 2 == 0) {
                        putIntLn(i);
                    } else {
                        break;
                    }
                    i += 1;
                }
            } ;"""
        expect = """trung0\ntrung"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing for_step_stmt
    def test_for_step_stmt_0(self):
        input = """var a string = "trung" ;

            func main() {
                var i int = 0 ;
                for i:=0; i<5; i+=1 {
                    putString(a) ;
                    if (i % 2 == 0) {
                        putIntLn(i);
                    }
                }
            } ;"""
        expect = """trung0\ntrungtrung2\ntrungtrung4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_step_stmt_1(self):
        input = """var a string = "trung" ;

            func main() {
                for i:=0; i<5; i+=1 {
                    putString(a) ;
                    if (i % 2 == 0) {
                        putIntLn(i);
                    }
                }
            } ;"""
        expect = """trung0\ntrungtrung2\ntrungtrung4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_step_stmt_2(self):
        input = """var a string = "trung" ;

            func main() {
                for i:=0; i<5; i+=1 {
                    putString(a) ;
                    if (i % 2 == 0) {
                        putIntLn(i);
                    } else {
                        continue;
                    }
                }
            } ;"""
        expect = """trung0\ntrungtrung2\ntrungtrung4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_step_stmt_3(self):
        input = """var a string = "trung" ;

            func main() {
                for i:=0; i<5; i+=1 {
                    if (i % 2 == 0) {
                        putIntLn(i);
                    } else {
                        continue;
                    }
                    putString(a) ;
                }
            } ;"""
        expect = """0\ntrung2\ntrung4\ntrung"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_step_stmt_4(self):
        input = """var a string = "trung" ;
            var x = 5 ;

            func main() {
                x := 6 ;
                for i:=1; i<6; i+=1 {
                    putInt(x) ;
                    if (x % i == 0) {
                        continue ;
                    }
                    x += 1;
                    if (x % i == 0) {
                        break ;
                    }
                }
            } ;"""
        expect = """66667"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_for_step_stmt_5(self):
        input = """func main() {
            for i:=1; i<6; i+=1 {
                for j:=6; j>=1; j-= 1{
                    putInt(j) ;
                    if (j <= i) {
                        break;
                    }
                };
                putStringLn("");
            }
        } ;"""
        expect = """654321\n65432\n6543\n654\n65\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing struct_literal
    def test_struct_literal_0(self):
        input = """type A struct {
                num int;
                op string;
            };
            func (a A) Reset(b int) {
                var x int = 10;
                putIntLn(x);
            }
            func main() {
                var x A = A{num: 10} ;
                putInt(x.num)
            };"""
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_1(self):
        input = """type A struct {
                num int;
                op string;
            };
            func (a A) Reset(b int) {
                var x int = 10;
                putIntLn(x);
            }
            func main() {
                var x A = A{num: 10} ;
                putInt(x.num * 9 + 8)
            };"""
        expect = """98"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_struct_literal_2(self):
        input = """type A struct {
                num int;
                op string;
            };
            func (a A) Reset(b int) {
                var x int = 11;
                putInt(x + b);
            }
            func main() {
                var x A = A{num: 10} ;
                x.Reset(4) ;
            };"""
        expect = """15"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_3(self):
        input = """func main() {
                var x A = A{num: 10} ;
                putInt(x.num);
            };
            type A struct {
                num int;
                op string;
            };
            func (a A) Reset(b int) {
                var x int = 11;
                putInt(x + b);
            };"""
        expect = """10"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_4(self):
        input = """func main() {
                var x A = A{num: 10} ;
                x.Reset(4) ;
            };
            func (a A) Reset(b int) {
                var x int = 11;
                putInt(x + b);
            };
            type A struct {
                num int;
                op string;
            };"""
        expect = """15"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_5(self):
        input = """var y = 11;
        
            func main() {
                var x A = A{num: 10} ;
                x.num := -6 ;
                x.Reset(36) ;
            }; 

            func (a A) Reset(b int) {
                var x int = 11 + y;
                putInt(x + b / a.num);
            }
            
            type A struct {
                num int;
                op string;
            };"""
        expect = """16"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_6(self):
        input = """var y = 11;
        
            func main() {
                var x A = A{num: 4} ;
                var y = x ;
                x.num := -6 ;
                y.Reset(36) ;
            }; 

            func (a A) Reset(b int) {
                var x int = 11 + y;
                putInt(x + b / a.num);
            }
            
            type A struct {
                num int;
                op string;
            };"""
        expect = """16"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_struct_literal_7(self):
        input = """var y = 11;
        
            func main() {
                var x A = A{num: 4} ;
                z := A{num: 4} ;
                x.num := -6 ;
                z.Reset(36) ;
            }; 

            func (a A) Reset(b int) {
                var x int = 11 + y;
                putInt(x + b / a.num);
            }
            
            type A struct {
                num int;
                op string;
            };"""
        expect = """31"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing array
    def test_array_0(self):
        input = """func main() {
                var a [3][2]int = [3][2]int{{0,0},{0,0},{0,0}};
                a[0][1] := 4;
                putInt(a[0][1])
            } ;"""
        expect = """4"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_1(self):
        input = """func main() {
                var a [2][3]int = [2][3]int{{1,2,3},{4,5,6}};
                putInt(a[1][2]);
            } ;"""
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_2(self):
        input = """func main() {
                var a [2][3]int = [2][3]int{{1,2,3},{4,5,6}};
                a[1][2] := 10 ;
                putInt(a[1][2] + a[0][2])
            } ;"""
        expect = """13"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_3(self):
        input = """func main() {
                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};
                var x int = marr[0][1];
                x += 5;
                putIntLn(x);
                putIntLn(marr[0][1]);
            } ;"""
        expect = """7\n2\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_array_4(self):
        input = """func main() {
                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};
                marr[0][0] := 2;
                putInt(marr[0][0]);
            } ;"""
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_5(self):
        input = """func main() {
                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};
                marr[0][0] += 2;
                putInt(marr[0][0]);
            } ;"""
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_6(self):
        input = """            func main() {
                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};
                var arr = marr[0];

                putInt(arr[2]);
            } ;"""
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_7(self):
        input = """            func main() {
                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};
                var arr1 = marr[0];
                var arr2 = marr[1];
                
                for idx:=0; idx<3; idx+=1 {
                    putInt(arr1[idx] + arr2[idx]);
                }
            } ;"""
        expect = """579"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_8(self):
        input = """            func main() {
                var marr = [2][3][2]int{{{1,1}, {2,2}, {3,3}}, {{4,4}, {5,5}, {6,6}}};
                var arr1 = marr[0][1];
                var arr2 = marr[1][1];
                
                for idx:=0; idx<2; idx+=1 {
                    putInt(arr1[idx] + arr2[idx]);
                }
            } ;"""
        expect = """77"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_9(self):
        input = """            var x = 1 ;

            var arr = [2]int{1, 2} ;

            func main() {

                var a [2][2]int = [2][2]int{{4, x}, {x, x+1}};

                putInt(a[0][0]);

                putInt(a[0][1]);

            } ;"""
        expect = """41"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_10(self):
        input = """            var x = 1.0 ;

            func main() {

                var a [2][2]float = [2][2]float{{4 / x, x}, {x, x+1}};

                putFloatLn(a[0][0]);

                putFloatLn(a[0][1]);

            } ;"""
        expect = """4.0\n1.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_array_11(self):
        input = """func main(){
                var p1 = Person{name: "trung" };
                var p2 = Person{name: "hieu" };
                var p = [2]Person{p1, p2};
                
                for i:=0; i<2; i+=1 {
                    p[i].Add() ;
                }
            };

            func (a Person) Add() {
                putString(a.name) ;
            }

            type Person struct {
                name string;
            }
            """
        expect = """trunghieu"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing advance_float_to_int_arr
    def test_advance_float_to_int_arr_0(self):
        input = """            func main() {

                var x = [2]int {2,3} ;

                var y [2]float;

                y := x;

                for idx:=0; idx<2; idx+=1 {

                    putFloatLn(y[idx]);

                };

            } ;"""
        expect = """2.0\n3.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_float_to_int_arr_1(self):
        input = """            func main() {

                var marr = [2][3]int{{1, 2, 3}, {4, 5, 6}};

                var fmarr [2][3]float;

                fmarr := marr;

                for idx:=0; idx<2; idx+=1 {

                    var j = 0;

                    for j < 3 {

                        putFloat(fmarr[idx][j]);

                        j += 1;

                    }

                }

            }
            """
        expect = """1.02.03.04.05.06.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_advance_float_to_int_arr_2(self):
        input = """            func main() {
                var marr = [3]int{1, 2, 3};
                var fmarr = [2][3]float{{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}};

                fmarr[0] := marr;
                for idx:=0; idx<2; idx+=1 {
                    var j = 0;
                    for j < 3 {
                        putFloat(fmarr[idx][j]);
                        j += 1;
                    }
                }
            } ;"""
        expect = """1.02.03.04.45.56.6"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_float_to_int_arr_3(self):
        input = """            func main() {
                var marr = [3][3]int{{1, 2, 3}, {4, 5, 6}, {4, 5, 6}};
                var fmarr = [2][3][3]float{ { {1.1, 1.1, 2.2}, {2.2, 1.1, 2.2}, {3.3, 1.1, 2.2} }, { {4.4, 4.4, 2.2}, {5.5, 4.4, 2.2}, {4.4, 6.6, 2.2} } };

                fmarr[1] := marr;
                for i:=0; i<2; i+=1 {
                    for j:=0; j<3; j+=1 {
                        for t:=0; t<3; t+=1 {
                            putFloat(fmarr[i][j][t]);
                        }
                    }
                }
            } ;"""
        expect = """1.11.12.22.21.12.23.31.12.21.02.03.04.05.06.04.05.06.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_float_to_int_arr_4(self):
        input = """            func main() {
                var marr = [3]int{1, 2, 3};
                var fmarr [3]float = marr;

                for i:=0; i<3; i+=1 {
                    putFloat(fmarr[i]);
                }
            } ;"""
        expect = """1.02.03.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing global_init
    def test_global_init_0(self):
        input = """var a int = 3 + 5 ;
            func main() {
                putInt(a) ;
            } ;"""
        expect = """8"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_global_init_1(self):
        input = """const a = 9 / 3 + 3 * 10 ;
            func main() {
                b := a / 11 ;
                putIntLn(b) ;
                putFloat(add(4))
            } ;
            
            const b = 10.8 ;
            func add(c int) float {
               return b + c ;
            } ;"""
        expect = """3\n14.8"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_global_init_2(self):
        input = """var a [2][3]int = [2][3]int{{1,2,3}, {10,20,30}} ;
            func main() {
                putInt(a[0][0]) ; 
            }; """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_global_init_3(self):
        input = """            var x [2]float = [2]int {1,2};

            func main() {

                putFloat(x[0]);

            }
            """
        expect = """1.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_global_init_4(self):
        input = """            var x [2][3]float = [2][3]int {{1,2,2} ,{2,3,3}};

            func main() {

                putFloat(x[0][2]);

            }
            """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing assign_interface
    def test_assign_interface_0(self):
        input = """type Display interface {
                Show() ;
            }
                    
            type People struct{
                age int ;
            } 

            func (p People) Show() {
                putString("This is class People") ;
            }
            
            func main(){
                var p Display ;
                p := People{} ;
                p.Show() ;
        };"""
        expect = """This is class People"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_1(self):
        input = """type Display interface {
                Show() ;
            }
                    
            type People struct{
                age int ;
                name string ;
            } 

            func (p People) Show() {
                putString(p.name)
            }
            
            func main(){
                var p Display ;
                p := People{ name: "Hieu" } ;
                p.Show() ;
        };"""
        expect = """Hieu"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_assign_interface_2(self):
        input = """func main(){
                var p Display ;
                p := People{ name: "Hieu" } ;
                p.Show() ;
            };

            func (p People) Show() {
                putString(p.name)
            }

            type People struct{
                age int ;
                name string ;
            }

            type Display interface {
                Show() ;
            };"""
        expect = """Hieu"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_3(self):
        input = """func main(){
                var p Display ;
                p := People{ name: "Hieu" } ;
                p.Show() ;
                p := Animal{};
                p.Show()
            };

            func (p People) Show() {
                putString(p.name)
            }
            
            func (a Animal) Show() {
                putString("Animal")
            }

            type People struct{
                age int ;
                name string ;
            }
            
            type Animal struct{
                age int ;
            }

            type Display interface {
                Show() ;
            };"""
        expect = """HieuAnimal"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_4(self):
        input = """

            func main(){

                p := Animal{ age: 0};

                putString(p.Show(1, 2.0));

            };

            

            func (a Animal) Show(x int, y float) string {

                putString("Animal ");

                putIntLn(x) ;

                return "Animal" ;

            }

            

            type Animal struct{

                age int ;

            }

            type Display interface {

                Show(x int, y float) string ;

            };

            """
        expect = """Animal 1\nAnimal"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_5(self):
        input = """            func main(){

                p := People{ age: 5, name: "Trung" };

                putString(p.Show(1, 2.0));

            };

            func (p People) Show(x int, y float) string {

                putString(p.name);

                return "People ";

            }

            type People struct{

                age int ;

                name string ;

            }

            type Display interface {

                Show(x int, y float) string ;

            };"""
        expect = """TrungPeople """
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_6(self):
        input = """            
            func main(){
                p := Animal{ age: 0};
                putString(p.Show(1, 2.0));
                v := People{ age: 5, name: "Trung" };
                putString(v.Show(1, 2.0));
            };

            func (p People) Show(x int, y float) string {
                putString(p.name);
                return "People ";
            }

            type People struct{
                age int ;
                name string ;
            }

            func (a Animal) Show(x int, y float) string {

                putIntLn(x) ;

                return "Animal" ;

            }

            

            type Animal struct{

                age int ;

            }

            type Display interface {

                Show(x int, y float) string ;

            };"""
        expect = """1\nAnimalTrungPeople """
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_7(self):
        input = """            func main(){
                p := Animal{ age: 0};
                for i:=0; i<3 ; i+=1 {
                    p.Show(i) ;
                }

                p.Show(10);
            };

            func (p People) Show(i int) {
                putString(p.name);
            }
            
            func (a Animal) Show(i int) {
                putString("Animal ");
                putIntLn(i);
            }

            type People struct{
                age int ;
                name string ;
            }
            
            type Animal struct{
                age int ;
            }

            type Display interface {
                Show(x int) ;
            };"""
        expect = """Animal 0\nAnimal 1\nAnimal 2\nAnimal 10\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_8(self):
        input = """            var p Display;

            func main(){

                p := Animal{ age: 0};

                putString(p.Show(1, 2.0));

                p := People{ age: 5, name: "Trung" };

                putString(p.Show(1, 2.0));

            };

            func (p People) Show(x int, y float) string {

                putString(p.name);

                return "People ";

            }

            type People struct{

                age int ;

                name string ;

            }

            func (a Animal) Show(x int, y float) string {

                putIntLn(x) ;

                return "Animal" ;

            }

            

            type Animal struct{

                age int ;

            }

            type Display interface {

                Show(x int, y float) string ;

            };"""
        expect = """1\nAnimalTrungPeople """
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_assign_interface_9(self):
        input = """            var p Display = Animal{ name: "Trung" };

            func main(){

                p.Show();

            };

            

            func (a Animal) Show() {

                a.name += " cho" ;

                putString("Animal ");

                putStringLn(a.name)

            }

            

            type Animal struct{

                name string ;

            }

            type Display interface {

                Show() ;

            };"""
        expect = """Animal Trung cho\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing scoping
    def test_scoping_0(self):
        input = """const a = 4 ;
        func main() {
        b := 3 ;
        change() ;
        putInt(a + b) ;
        } ;
        func change() {
        a += 5 ;
        } ;
        """
        expect = """12"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_scoping_1(self):
        input = """var a = 10 ;
            func main() {
                b := (a == 10) || change() ;
                if (b == true) {
                    putStringLn("b is true")
                } else {
                    putStringLn("b is false")
                }
                putInt(a) ;
            } ;
            func change() boolean {
                a := 20 ;
                return false ;
            } ;"""
        expect = """b is true\n20"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_scoping_2(self):
        input = """
                var x = 2;
                func main(){

                if (x > 0) {
                    var x float = 10.0;
                    putFloatLn(x);
                } 

                if (x > 1) {
                    putInt(x) ;
                }
            };"""
        expect = """10.0\n2"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_scoping_3(self):
        input = """            
            var x = 2;
            func main(){

                if (x > 0) {
                    var x string = "10.0";
                    putStringLn(x);
                } 

                for i:=1; i<=5; i+=2 {
                    var x float = x+i;
                    putFloatLn(x) ;
                }
            };"""
        expect = """10.0\n3.0\n5.0\n7.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_scoping_4(self):
        input = """            var x = 0;

            func Add(i int) boolean {

                x += 1;

                return x > i;

            }

            func print() {

                putInt(x) ;

            }

            

            func main(){

                var x = 10;

                if (Add(0) && Add(1) && Add(2) && Add(3) && Add(4)) {

                    putInt(x) ;

                }

                print();

            };"""
        expect = """105"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_scoping_5(self):
        input = """var a = A{x: 10, y: 10.0 } ;
            func main() {
                b := (a.x == 10) || change() ;
                if (b == true) {
                    putStringLn("b is true")
                } else {
                    putStringLn("b is false")
                }
                putFloat(a.y) ;
            } ;
            func change() boolean {
                a.y += 20 ;
                return false ;
            } ;
            
            type A struct {
                x int ;
                y float ;
                z boolean ;
            } ;"""
        expect = """b is true\n30.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_scoping_6(self):
        input = """            var x = 0;
            func Add(i int) boolean {
                x += 1;
                return x > i;
            }

            func print() {
                putInt(x) ;
            }            

            func main(){
                var x = 10;
                if (Add(1) && Add(2) && Add(3) && Add(4)) {
                    putInt(x) ;
                } 
                print();

            };"""
        expect = """4"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

#     # Testing advance_stack_size
    def test_advance_stack_size_0(self):
        input = """func main(){
                var p Display = Animal{ age: 0 };

                p.Show();
            };
            
            func (a Animal) Show() {
                a.age += 1 ;
                putString("Animal ");
                putIntLn(a.age);
            }
            
            type Animal struct{
                age int ;
            }

            type Display interface {
                Show() ;
            };"""
        expect = """Animal 1\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_1(self):
        input = """var p Display = Animal{ name: "Trung" };
            func main(){
                p.Show();
            };
            
            func (a Animal) Show() {
                a.name += " cho" ;
                putString("Animal ");
                putStringLn(a.name)
            }
            
            type Animal struct{
                name string ;
            }

            type Display interface {
                Show() ;
            };"""
        expect = """Animal Trung cho\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_2(self):
        input = """            func main(){
                var p Display ;
                p := People{ name: "Hieu" } ;
                p.Show() ;

                p := Animal{ age: 0};
                for i:=0; i<3 ; i+=1 {
                    p.Show() ;
                }

                p.Show();
            };

            func (p People) Show() {
                putString(p.name);
            }
            
            func (a Animal) Show() {
                a.age += 1 ;
                putString("Animal ");
                putIntLn(a.age);
            }

            type People struct{
                age int ;
                name string ;
            }
            
            type Animal struct{
                age int ;
            }

            type Display interface {
                Show() ;
            };"""
        expect = """HieuAnimal 1\nAnimal 2\nAnimal 3\nAnimal 4\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_3(self):
        input = """            
             func main(){
                var p = Animal{ age: [2]int{1, 2} } ;
                p.Show() ;
                p.Add() ;
                p.Show() ;
            };

            func (a Animal) Show() {
                for i:=0; i<2; i+=1 {
                    putInt(a.age[i]);               // Max stack: 2
                }
            }

            func (a Animal) Add() {
                for i:=0; i<2; i+=1 {
                    a.age[i] += 1;                  // Max stack: 5
                }
            }

            type Animal struct{
                age [2]int ;
            }
            """
        expect = """1223"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_4(self):
        input = """            func main(){
                var p1 = Person{name: "trung" };
                var p2 = Person{name: "hieu" };
                var a = Animal{p: [2]Person{p1, p2}, age: [2]int{1,2} };
                a.Add();
            };

            func (a Animal) print(str string) {
                putStringLn(str);
            }

            func (a Animal) Add() {
                for i:=0; i<2; i+=1 {
                    a.p[i].name += " 2004";
                    a.print(a.p[i].name) ;
                }
            }

            type Person struct {
                name string;
            }
            
            type Animal struct{
                p [2]Person ;
                age [2]int ;
            }
            """
        expect = """trung 2004\nhieu 2004\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # -------------------------------------------------------

    def test_advance_stack_size_5(self):
        input = """            func main(){

                var p1 = Person{name: "trung" };

                var p2 = Person{name: "hieu" };

                var a = Animal{p: [2]Person{p1, p2}, age: [2]int{1,2} };

                a.Add();

            };

            func (a Animal) print(str string) {

                putStringLn(str);

            }

            func (a Animal) Add() {

                for i:=0; i<2; i+=1 {

                    a.print(a.p[i].name) ;

                }

            }

            type Person struct {

                name string;

            }

            

            type Animal struct{

                p [2]Person ;

                age [2]int ;

            }
            """
        expect = """trung\nhieu\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_6(self):
        input = """            func main(){

                var p1 = Person{name: "trung" };

                var a = Animal{p: p1, age: 10 };

                a.Add();

            };

            func (a Animal) Add() {

                putString(a.p.name) ;

            }

            type Person struct {

                name string;

            }

            type Animal struct{
                p Person ;
                age int ;
            }
            """
        expect = """trung"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_7(self):
        input = """func main(){
                var p1 = Person{name: "trung" };
                var p2 = Person{name: "hieu" };
                var p = [2]Person{p1, p2};
                
                for i:=0; i<2; i+=1 {
                    p[i].Add() ;
                }
            };

            func (a Person) Add() {
                putString(a.name) ;
            }

            type Person struct {
                name string;
            }
            """
        expect = """trunghieu"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_8(self):
        input = """            func main(){

                x := 5.0;

                var arr [2]float = [2]int{1,2};

                if (x > 0) {

                    arr[0] += x;

                    putFloatLn(arr[0]);

                } 

                x += 1 ;

                putFloatLn(x) ;

            };"""
        expect = """6.0\n6.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_advance_stack_size_9(self):
        input = """            var arr [2]float = [2]int{1,2};
            
            func main(){
                x := 5.0;
                if (x > 0.0) {
                    arr[0] += x;
                    putFloatLn(arr[0]);
                } 
                x += 1 ;
                putFloatLn(x) ;
            };"""
        expect = """6.0\n6.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    # Testing function_method
    def test_function_method_0(self):
        input = """            
        func Factorial(x int) int {
                if (x <= 0) {
                    return 1;
                }
                return x * Factorial(x-1);
            }

            func main() {

                x := 5;

                putInt(Factorial(x));

            }
            """
        expect = """120"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_function_method_1(self):
        input = """            func Add(x int) int {

                return Double(x) + 1;

            }

            func Double(x int) int {

                return x * 2;

            }

            func main() {

                x := 2;

                putInt(Add(x));

            }
            """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_function_method_2(self):
        input = """            func DivByTwo(x int) int {
                if (x%2 == 0) {
                    return x/2;
                } else {
                    return (x-1)/2;
                } ;
            }

            func main() {

                var x = 58;

                for (x > 1) {

                    putInt(x);

                    x := DivByTwo(x);

                }

            }
            """
        expect = """58291473"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_function_method_3(self):
        input = """            func Recursive1(x int) int {

                if (x <= 1) {

                    return x ;

                } else {

                    putInt(x) ;

                    return Recursive2(x) ;

                }

            }

            func Recursive2(x int) int {
                return Recursive1(x-2) ;
            }

            func main() {
                var x = 16 ;
                putInt(Recursive1(x)) ;

            }
            """
        expect = """1614121086420"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_function_method_4(self):
        input = """            var lock = true;

            var val = 0;

            func foo1() {

                if (val <= 2) {

                    lock := false;

                    putString("foo1");

                    val += 1;

                } else {

                    lock := true;

                }

            }

            func foo2() {

                if (lock) {

                    putString("foo2") ;

                }

            }

            func main() {
                for i:=0; i<=3; i+=1 {
                    foo1();
                    foo2();
                }

            }
            """
        expect = """foo1foo1foo1foo2"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))

    def test_166(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func sumAges(p1 Person, p2 Person) int {
            return p1.age + p2.age;
        }
        func main() {
            var p1 Person = Person{name: "Dan", age: 20};
            var p2 Person = Person{name: "Eve", age: 25};
            var total int = sumAges(p1, p2);
            putIntLn(total);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "45\n", inspect.stack()[0].function))
    
    def test_171(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) duplicate() Person {
            return Person{name: p.name, age: p.age};
        }
        func main() {
            var p1 Person = Person{name: "Jack", age: 31};
            var p2 Person = p1.duplicate();
            putStringLn(p2.name);
            putIntLn(p2.age);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Jack\n31\n", inspect.stack()[0].function))
    
    