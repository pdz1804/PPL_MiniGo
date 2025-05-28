import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *

class CheckSuite(unittest.TestCase):

    # Testing redeclaration
    def test_redeclaration_0(self):
        input = """var a int; var b int; var a int; 
"""
        expect = """Redeclared Variable: a\n"""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclaration_1(self):
        input = """var a int; 
var b int; 
func main() {
   var d int;
   var a int;
}
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclaration_2(self):
        input = """const a = 3 ; var a int = 3 ; 
"""
        expect = """Redeclared Variable: a\n"""
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclaration_3(self):
        input = """var a int = 3 ; const a = 3 ; 
"""
        expect = """Redeclared Constant: a\n"""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclaration_4(self):
        input = """var a int = 3 ;
            func add(a int, b int, a float) int {
                return a + b ;
            }

"""
        expect = """Redeclared Parameter: a\n"""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclaration_5(self):
        input = """var a int = 3 ;
            func add(a int, b int) int {
                return a + b ;
            }
            type add struct {
                a int;
                b float;
            };
"""
        expect = """Redeclared Type: add\n"""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclaration_6(self):
        input = """var a int = 3 ;
            type add struct {
                a int;
                b float;
            };
            func add(a int, b int) int {
                return a + b ;
            } ;
"""
        expect = """Redeclared Function: add\n"""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclaration_7(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                    // value float;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                } ;
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
"""
        expect = """Redeclared Method: Greet\n"""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclaration_8(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) value(a int, b float, c int) string {
                    return "Hello, " + p.name;
                } ;
"""
        expect = """Redeclared Method: value\n"""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclaration_9(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                    value float;
                };
"""
        expect = """Redeclared Field: value\n"""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclaration_10(self):
        input = """type Calculator interface {
                Add(x, y int) int;
                Subtract(a, b float, c int) float;
                Reset();
                SayHello(name string)
                Subtract(a, b int) int;
            };
"""
        expect = """Redeclared Prototype: Subtract\n"""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclaration_11(self):
        input = """            func Adding(a, b int, c, d float) float {
                var x int = 5;
                var arr [3]int = [3]int{1,2,3};
                
                var idx int;
                var value int;
                for idx, value := range arr {
                    var idx = 4 ;
                }        

                return a * c * x
            };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclaration_12(self):
        input = """func Add(x int) int {
    for y := 1; y<5; y += 1 {
         var y = 10;
     }
}

"""
        expect = """Redeclared Variable: y\n"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclaration_13(self):
        input = """func Add(x int) int {
    var y = 5;
    for y := 1; y<5; y += 1 {
         var y = 10;
     }
}
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,413))

    # Testing undeclaration
    def test_undeclaration_0(self):
        input = """func Adding(a, b int, c, d float) float {
                for (i < 1) {
                    a += b; 
                    c += d;
                }        

            return a * c
        };
"""
        expect = """Undeclared Identifier: i\n"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclaration_1(self):
        input = """var a int = 10 ;
            var b float = 1.1 ;
            var z = a + c ; 
"""
        expect = """Undeclared Identifier: c\n"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclaration_2(self):
        input = """var a int = 10 ;
            func main() {
                print(a) ;
            } ;
"""
        expect = """Undeclared Function: print\n"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclaration_3(self):
        input = """var a int = 10 ;
            var b float = 1.1 ;
            func main() {
                z := add(a, b, a) ;
            } ;
"""
        expect = """Undeclared Function: add\n"""
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclaration_4(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                }; 
            func main() {
                var p Calculator ;
                p.show()
            } ;
"""
        expect = """Undeclared Method: show\n"""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclaration_5(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                
                var x = Calculator{}
                func main() {
                    x.age := 21
                } ;
"""
        expect = """Undeclared Field: age\n"""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclaration_6(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                func main() {
                    c := Calculator{value: 20, name: "Hieu", university: "BKU"}
                } ;
"""
        expect = """Undeclared Field: university\n"""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclaration_7(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                func main() {
                    var s Calculator = Calculator{value: 20, name: "Hieu"} ;
                    var s3 string ;
                    s3 := "name " + s.Name ;
                } ;
"""
        expect = """Undeclared Field: Name\n"""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclaration_8(self):
        input = """func foo(a int) {
            foo(1);
            var foo = 1;
            foo(2); // error
        } ; 
"""
        expect = """Undeclared Function: foo\n"""
        self.assertTrue(TestChecker.test(input,expect,422))

    # Testing declaration_stmt
    def test_declaration_stmt_0(self):
        input = """var a int = 1.2;
"""
        expect = """Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_declaration_stmt_1(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                
                var x = Calculator{value: "Trung", name: "Hieu"} ;
"""
        expect = """Type Mismatch: StructLiteral(Calculator,[(value,StringLiteral("Trung")),(name,StringLiteral("Hieu"))])\n"""
        self.assertTrue(TestChecker.test(input,expect,424))

    # Testing assignment_stmt
    def test_assignment_stmt_0(self):
        input = """var a boolean ;
            func main() {
            a := 10;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(a),IntLiteral(10))\n"""
        self.assertTrue(TestChecker.test(input,expect,425))

    # Testing checking_expr
    def test_checking_expr_0(self):
        input = """var a int = 3 ;
            var b float = a + 3.2 ;
            var c = b / 1 ;
            var d boolean = c == b ;
            var e = d && false ;
            var f = a % 100 ;
            var z string = "Hieu " + "Trung " + " anh Khoa" ; 
            func main () {
                e := d || d ;
                d := !d ; d := b > c ; d := b >= c ; d := c < b ; d := c == b ; d := c <= b ;
            } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_checking_expr_1(self):
        input = """var a int = 3 ;
            var b float = a + 3.2 ;
            var c = b / 1 ;
            var d boolean = a == c ;
            var z string = "Hieu " + "Trung " + " anh Khoa" ; 
"""
        expect = """Type Mismatch: BinaryOp(Id(a),==,Id(c))\n"""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_checking_expr_2(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                func main() {
                    c := Calculator{value: 20, name: 13}
                } ;
"""
        expect = """Type Mismatch: StructLiteral(Calculator,[(value,IntLiteral(20)),(name,IntLiteral(13))])\n"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_checking_expr_3(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func (p Calculator) Greet(a int, b float, c int) string {
                    return "Hello, " + p.name;
                }
                func main() {
                    c := Calculator{value: 20, name: "Hieu"}
                } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_checking_expr_4(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func main() {
                    var s Calculator = Calculator{value: 20, name: "Hieu"} ;
                    var s3 string ;
                    s3 := "name " + s.name ;
                    var s5 = "age = " + s.value ;
                } ;
"""
        expect = """Type Mismatch: BinaryOp(StringLiteral(\"age = \"),+,FieldAccess(Id(s),value))\n"""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_checking_expr_5(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };
                func main() {
                    var s Calculator = Calculator{value: 20, name: "Hieu"} ;
                    var s3 string ;
                    s3 := "name " + s.name ;
                    var s5 = s3.value + s.value ;
                } ;
"""
        expect = """Type Mismatch: FieldAccess(Id(s3),value)\n"""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_checking_expr_6(self):
        input = """const size = 3 ;
                var arr [size] float ;
                func main() {
                    arr := [size] float{1.0, 2.0, 3.0}
                    arr := [3] int {3,5,10}
                }
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_checking_expr_7(self):
        input = """const size = 3.0 ;
                var arr [size] int ;
        """
        expect = """Type Mismatch: ArrayType(IntType,[Id(size)])\n"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_checking_expr_8(self):
        input = """const size = 3 ;
                var arr [size] string ;
                func main() {
                    arr := [size] boolean {"hieu", "trung"}
                } ;
        """
        expect = """Type Mismatch: Assign(Id(arr),ArrayLiteral([Id(size)],BoolType,[StringLiteral(\"hieu\"),StringLiteral(\"trung\")]))\n""" # khac cai nay t bao loi arr lit
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_checking_expr_9(self):
        input = """type Calculator struct {
                    value int;
                    name string;
                };

            func main() {
                var c = Calculator{value: 10, name: "hieu"} ;
                var a = "toi di hoc"
                c.value += 10 ;
                a.name += "hieu" ;
            } ;
"""
        expect = """Type Mismatch: FieldAccess(Id(a),name)\n"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_checking_expr_10(self):
        input = """const size = 3 ;
            func main() {
                var a [size]int = [3]int{1,2,3}
                var b = "toi di hoc"
                b[0] := "toi"
            } ;
"""
        expect = """Type Mismatch: ArrayCell(Id(b),[IntLiteral(0)])\n"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_checking_expr_11(self):
        input = """const size = 3 ;
            var x int ;
            func main() {
                var a [size]int = [3]int{1,2,3}
                var b = "toi di hoc"
                a[x] := 10
            } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_checking_expr_12(self):
        input = """const size = 3 ;
            var x = true ;
            var y = 10 ;
            func main() {
                var a [size]int = [3]int{1,2,3}
                var b = "toi di hoc"
                a[y][x] := 10
            } ;
"""
        expect = """Type Mismatch: ArrayCell(Id(a),[Id(y),Id(x)])\n"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_checking_expr_13(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                var a = "toi di hoc" ;
                var s string = a + " hom nay" ;
            } ;
            
            var c float = a + b ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_checking_expr_14(self):
        input = """var a int = 3 ;
            var b int = 6 ;

            func main() {
                var a = "toi di hoc" ;
                if (true) {
                    a += 3 ;
                }
            } ;
            
            var c float = a + b ;
"""
        expect = """Type Mismatch: BinaryOp(Id(a),+,IntLiteral(3))\n"""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_assignment_stmt_1(self):
        input = """var a boolean ;
            func main() {
            a := 10;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(a),IntLiteral(10))\n"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_assignment_stmt_2(self):
        input = """var a float ;
            func main() {
            a := 10;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_assignment_stmt_3(self):
        input = """var a int ;
            func main() {
            a := 10.0;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(a),FloatLiteral(10.0))\n"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_assignment_stmt_4(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                var arr [3]int = [3]int{1,2,3};
                
                for idx, value := range arr {
                    value := 1.2 ;
                }        

                return a * c * x
            };
"""
        expect = """Undeclared Identifier: idx\n"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_assignment_stmt_5(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for i := 10; i > 0; i -= 1.1 {
                    x += 1 ;
                }

                return a * c * x
            };
"""
        expect = """Type Mismatch: Assign(Id(i),BinaryOp(Id(i),-,FloatLiteral(1.1)))\n"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_assignment_stmt_6(self):
        input = """var arr [3]int ;
            func main() {
                arr := [4]int{1,3,9,10}
                return ;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(arr),ArrayLiteral([IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(3),IntLiteral(9),IntLiteral(10)]))\n"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_assignment_stmt_7(self):
        input = """var arr [3]int ;
            func main() {
                arr := [3][2]int{{1,3},{2,3},{4,4}}
                return ;
            } ;
"""
        expect = """Type Mismatch: Assign(Id(arr),ArrayLiteral([IntLiteral(3),IntLiteral(2)],IntType,[[IntLiteral(1),IntLiteral(3)],[IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(4)]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_assignment_stmt_8(self):
        input = """const size = 3 ;
                var arr [size] string ;
                func main() {
                    arr := [size] boolean {"hieu", "trung"}
                } ;
"""
        expect = """Type Mismatch: Assign(Id(arr),ArrayLiteral([Id(size)],BoolType,[StringLiteral(\"hieu\"),StringLiteral(\"trung\")]))\n"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_assignment_stmt_9(self):
        input = """type Hieu struct {
                    prize int ;
                }
                func (h Hieu) Greet() string {
                    return "hieu xin chao" ;
                }
                func (h Hieu) CanDoMath() boolean {
                    return true ;
                }
                func (h Hieu) Plus(i, j int) int {
                    return i + j ;
                }

                type Person interface {
                    Greet() string ;
                    CanDoMath() boolean ;
                    Plus(a int, b int) int ;
                }

                func main() {
                    var p Person ;
                    p := Hieu {prize: 3} ;
                } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_assignment_stmt_10(self):
        input = """type Hieu struct {
                    prize int ;
                }
                func (h Hieu) Greet() string {
                    return "hieu xin chao" ;
                }
                func (h Hieu) CanDoMath() boolean {
                    return true ;
                }
                func (h Hieu) Plus(i, j int) int {
                    return i + j ;
                }

                type Person interface {
                    Greet() string ;
                    CanDoMath() boolean ;
                }

                func main() {
                    var p Person ;
                    p := Hieu {prize: 3} ;
                } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_assignment_stmt_11(self):
        input = """type Hieu struct {
                    prize int ;
                }
                func (h Hieu) Greet() string {
                    return "hieu xin chao" ;
                }
                func (h Hieu) CanDoMath() boolean {
                    return true ;
                }
                func (h Hieu) Plus(i, j int) int {
                    return i + j ;
                }

                type Person interface {
                    Greet() string ;
                    CanDoMath() boolean ;
                    Plus(i int, j int) float ;  // wrong type here
                }

                func main() {
                    var p Person ;
                    p := Hieu {prize: 3} ;
                } ;
"""
        expect = """Type Mismatch: Assign(Id(p),StructLiteral(Hieu,[(prize,IntLiteral(3))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_assignment_stmt_12(self):
        input = """type Hieu struct {
                    prize int ;
                }
                func (h Hieu) Greet() string {
                    return "hieu xin chao" ;
                }
                func (h Hieu) CanDoMath() boolean {
                    return true ;
                }

                type Person interface {
                    Greet() string ;
                    CanDoMath() boolean ;
                    Plus(i int, j int) float ;
                }

                func main() {
                    var p Person ;
                    p := Hieu {prize: 3} ;
                } ;
"""
        expect = """Type Mismatch: Assign(Id(p),StructLiteral(Hieu,[(prize,IntLiteral(3))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_assignment_stmt_13(self):
        input = """type Hieu struct {
                    full_name string ;
                    age int ;
                }
                var s string = " di hoc"
                func main(s boolean) {
                    var h Hieu ;
                    z := h.full_name + s
                } ;
"""
        expect = """Type Mismatch: BinaryOp(FieldAccess(Id(h),full_name),+,Id(s))\n"""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_assignment_stmt_14(self):
        input = """type Hieu struct {
                    full_name string ;
                    age int ;
                }
                var t boolean = false ;
                func main(t float) {
                    var h Hieu ;
                    z := h.age + t
                } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,454))

    # Testing return_stmt
    def test_return_stmt_0(self):
        input = """var a float = 1.1 ;
            func main() {
                var a int = 10;
                return a ;
            } ;
"""
        expect = """Type Mismatch: Return(Id(a))\n"""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_return_stmt_1(self):
        input = """        var a = "trung" ;

        func Add(x int, y int) int {
            x += 2;
            var x float = 2.0;

            return y;
        }
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_return_stmt_2(self):
        input = """        const a  = "trung" ;
        const b = "hieu" + a;
        func Add(x int, y int) string {
            x += 2;
            var x float = 2.0;
            var a int = 10;
            var b float = 15;

            return a + b;
        }
"""
        expect = """Type Mismatch: Return(BinaryOp(Id(a),+,Id(b)))\n"""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_return_stmt_3(self):
        input = """const a  = "trung" ;
        const b = "hieu" + a;
        func Add(x int, y string, z int) {
            x += 2;
            var x float = 2.0;
            var y int = 10;
            var b float = 15;

            for x < 10.0 {
                x += 1.0 ;
                y -= 5;
                if (y < 0) {
                    return y;
                }
            }
        }
"""
        expect = """Type Mismatch: Return(Id(y))\n"""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_return_stmt_4(self):
        input = """const a  = "trung" ;
        const b = "hieu" + a;
        func Add(x int, y string, z int) boolean {
            x += 2;
            var x float = 2.0;
            var y int = 10;
            var b float = 15;

            for x < 10.0 {
                x += 1.0 ;
                y -= 5;
                return;
            }
        }
"""
        expect = """Type Mismatch: Return()\n"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_return_stmt_5(self):
        input = """func Add(x int, y string, z int) boolean {
            x += 2;
            var x float = 2.0;
            var y int = 10;
            var b float = 15;

            for x < 10.0 {
                x += 1.0 ;
                y -= 5;
                if (y < 0) {
                    if (10 > 3) {
                        var idx int;
                        var val float;
                        for idx, val := range [3]int{10, 20, 30} {
                            if (val > 5) {
                                return val <= 10;
                            }
                        }
                    }
                }
            }
        } ;
"""
        expect = """Type Mismatch: ForEach(Id(idx),Id(val),ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(10),IntLiteral(20),IntLiteral(30)]),Block([If(BinaryOp(Id(val),>,IntLiteral(5)),Block([Return(BinaryOp(Id(val),<=,IntLiteral(10)))]))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,460))

    # Testing type_compatible
    def test_type_compatible_0(self):
        input = """var a string = "trung" ;
        var b int = 10 ;
        var c float = 20.25 ;
        var d boolean = false ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_compatible_1(self):
        input = """var a float ;
            func main() {
            a := 10;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_type_compatible_2(self):
        input = """var arr [3]int ;
            const c = 1 + 2 / 1 ;
            func main() {
                arr := [c]int{1,3,9}
                return ;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_compatible_3(self):
        input = """var arr [3]int ;
            func main() {
                arr := [4]int{1,3,9,10}
                return ;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(arr),ArrayLiteral([IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(3),IntLiteral(9),IntLiteral(10)]))\n"""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_compatible_4(self):
        input = """var arr [3]int ;
            const c = (true && false) || true ;
            func main() {
                arr := [c]int{1,3,9}
                return ;
        } ;
"""
        expect = """Type Mismatch: ArrayLiteral([Id(c)],IntType,[IntLiteral(1),IntLiteral(3),IntLiteral(9)])\n"""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_type_compatible_5(self):
        input = """        const b  = 10 ;
        var c float = 20 ;
        var d boolean = false ;
        var x int = false;
"""
        expect = """Type Mismatch: VarDecl(x,IntType,BooleanLiteral(false))\n"""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_compatible_6(self):
        input = """
        const b  = 10 ;
        var c float = 20 ;
        var d boolean = false ;

        func Add(x int) int {
            x := true;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),BooleanLiteral(true))\n"""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_compatible_7(self):
        input = """const b  = 10 ;
        var c float = 20 ;
        var d boolean = false ;
        var y Person;

        func Add(x Person) Person {
            y := Person{name: "trung", age: 18};
            x := y;

            return x;
        }

        type Person struct {
            name string ;
            age int ;
        }

        type person struct {
            name string ;
            age int ;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_compatible_8(self):
        input = """
        const b  = 10 ;
        var c float = 20 ;
        var d boolean = false ;
        var y Person;

        func Add(x person) Person {
            x := Person{name: "trung", age: 20};

            return x;
        }

        type Person struct {
            name string ;
            age int ;
        }

        type person struct {
            name string ;
            age int ;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),StructLiteral(Person,[(name,StringLiteral("trung")),(age,IntLiteral(20))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_type_compatible_9(self):
        input = """
        const b  = 10 ;
        var c float = 20 ;
        var d boolean = false ;
        var y Person;

        func Add(x person) Person {
            y := Person{name: "trung", age: 18};
            x := y;

            return y;
        }

        type Person struct {
            name string ;
            age int ;
        }

        type person struct {
            name string ;
            age int ;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),Id(y))\n"""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_type_compatible_10(self):
        input = """var y Person;

        func Add(x Doctor) Doctor {
            y := Person{name: "trung", age: 18};
            x := Doctor{p: y, degree: "Master"};

            return y;
        }

        type Person struct {
            name string ;
            age int ;
        }

        type Doctor struct {
            p Person;
            degree string;
        } ;
"""
        expect = """Type Mismatch: Return(Id(y))\n"""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_type_compatible_11(self):
        input = """var y = 15;

        func Add(x int) [2][5]int {
            var multi_arr [2][3]int;
            multi_arr := [2][3]int{{1, 2, 3}, {4, 5, 6}}

            return multi_arr;
        } ;
"""
        expect = """Type Mismatch: Return(Id(multi_arr))\n"""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_type_compatible_12(self):
        input = """
        var y = 15;
        var x [2][3]float ;

        func Add(x int) [2][5]int {
            var multi_arr [2][3]int;
            multi := [2][3]int{{1, 2, 3}, {4, 5, 6}};
            x := multi;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),Id(multi))\n"""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_type_compatible_13(self):
        input = """
        var y = 15;
        var x [2][3][7][8][10]float ;

        func Add(z [2][3][7][8][11]float) [2][3]int {
            var multi_arr [2][3]int;
            multi := [2][3]int{{1, 2, 3}, {4, 5, 6}};
            x := z ;

            return multi;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),Id(z))\n"""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_type_compatible_14(self):
        input = """
        var y = 15;
        var x [2][3][7][8][10]float ;

        func Add(z [2][3][7][8][10]int) [2][3]int {
            var multi_arr [2][3]int;
            multi := [2][3]int{{1, 2, 3}, {4, 5, 6}};
            x := z ;

            return multi;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_type_compatible_15(self):
        input = """
        var x Calculator = A{num: 10, op: "+"};

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) Add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x, y float, c int) float {
            return x
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_type_compatible_16(self):
        input = """
        var x Calculator = A{num: 10, op: "+"};

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) Add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x, y float, c int) int {
            return c;
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        } ;
"""
        expect = """Type Mismatch: VarDecl(x,Id(Calculator),StructLiteral(A,[(num,IntLiteral(10)),(op,StringLiteral("+"))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_type_compatible_17(self):
        input = """
        var x Calculator = A{num: 10, op: "+"};

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
        }

        func (x A) Add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x, y float, c int) float {
            return c;
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        }

"""
        expect = """Type Mismatch: Return(Id(c))\n"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_type_compatible_18(self):
        input = """
        var x Calculator = A{num: 10, op: "+"};

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x,y float, c int) int {
            return c;
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        } ;
"""
        expect = """Type Mismatch: VarDecl(x,Id(Calculator),StructLiteral(A,[(num,IntLiteral(10)),(op,StringLiteral("+"))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_type_compatible_19(self):
        input = """
        var y A = A{num: 20, op: "-"};
        var x Calculator = A{num: 10, op: "+"};

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x,y float, c int) int {
            return c;
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello() {
            return;
        }

        type A struct {
            num int;
            op string;
        } ;
"""
        expect = """Type Mismatch: VarDecl(x,Id(Calculator),StructLiteral(A,[(num,IntLiteral(10)),(op,StringLiteral("+"))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_type_compatible_20(self):
        input = """func doSomething(p Hieu, age int, score float) {
                    s := "Full name is " + p.getName() ;
                    return ;
                }
                func (p Hieu) getName() string {
                    return p.full_name ;
                }
                type Hieu struct {
                    full_name string ;
                    age int ;
                }
                func main() {
                    var h Hieu = Hieu{} ;
                    doSomething(h, 10, 11.2)
                    return ;
                } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_type_compatible_21(self):
        input = """func add3(a, b float, c int) float {
                    return a + b + c ;
                }
                func main() {
                    var a = 3 ;
                    var b = 1.0 ; 
                    var c float = 2 ;
                    z := add3(a, b, c) ;
                    z += 4.0 ;
                } ;
"""
        expect = """Type Mismatch: FuncCall(add3,[Id(a),Id(b),Id(c)])\n"""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_type_compatible_22(self):
        input = """func add3(a, b float, c int) float {
                    return a + b + c ;
                }
                func main() {
                    var a float = 3 ;
                    var b = 1.0 ; 
                    var c int ;
                    d := 3 / a ;
                    z := add3(a, b, c, d) ;
                }
"""
        expect = """Type Mismatch: FuncCall(add3,[Id(a),Id(b),Id(c),Id(d)])\n"""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_compatible_23(self):
        input = """
        func main() {
            y := A{num: 20, op: "-"};
            var x Calculator;
            x := y;
        }

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x,y float, c int) int {
            return c;
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello() {
            return;
        }

        type A struct {
            num int;
            op string;
        } ;
"""
        expect = """Type Mismatch: Assign(Id(x),Id(y))\n"""
        self.assertTrue(TestChecker.test(input,expect,484))

    # Testing if_for_stmt
    def test_if_for_stmt_0(self):
        input = """var a = 1 ;
            var b string = "toi di hoc" ;
            func main() {
                if (a + 2) {
                    b := "@123"
                } else {
                    b := "random ... " ;
                }
            } ;
"""
        expect = """Type Mismatch: If(BinaryOp(Id(a),+,IntLiteral(2)),Block([Assign(Id(b),StringLiteral(\"@123\"))]),Block([Assign(Id(b),StringLiteral(\"random ... \"))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_if_for_stmt_1(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for x + 3 {
                    a += b; 
                    c += d;
                    x += 1;
                }        

                return a * c * x
            };
"""
        expect = """Type Mismatch: For(BinaryOp(Id(x),+,IntLiteral(3)),Block([Assign(Id(a),BinaryOp(Id(a),+,Id(b))),Assign(Id(c),BinaryOp(Id(c),+,Id(d))),Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(1)))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_if_for_stmt_2(self):
        input = """type Hieu struct {
                full_name string ;
                age int ;
            }
            func main() {
                var h Hieu ;
                if (h.canDoMath()) {
                    b := "@123"
                } else {
                    b := "random ... " ;
                }
            }
            func (h Hieu) canDoMath() boolean {
                return true ;
            } ;
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_if_for_stmt_3(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for idx, value := range x {
                    a += b; 
                    c += d;
                    x += 1;
                }

                return a * c * x
            };
"""
        expect = """Type Mismatch: ForEach(Id(idx),Id(value),Id(x),Block([Assign(Id(a),BinaryOp(Id(a),+,Id(b))),Assign(Id(c),BinaryOp(Id(c),+,Id(d))),Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(1)))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_if_for_stmt_4(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for i := 10; i + 8; i -= 1 {
                    x += 1 ;
                }

                return a * c * x
            };
"""
        expect = """Type Mismatch: For(Assign(Id(i),IntLiteral(10)),BinaryOp(Id(i),+,IntLiteral(8)),Assign(Id(i),BinaryOp(Id(i),-,IntLiteral(1))),Block([Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(1)))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_if_for_stmt_5(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for i := 10; i > 0; i -= 1 {
                    x += 1 ;
                }

                return a * c * x
            };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_if_for_stmt_6(self):
        input = """func Adding(a, b int, c, d float) float {
                var x int = 5;
                
                for i := 10; i == true; i -= 1.1 {
                    x += 1 ;
                }

                return a * c * x
            };
"""
        expect = """Type Mismatch: BinaryOp(Id(i),==,BooleanLiteral(true))\n"""
        self.assertTrue(TestChecker.test(input,expect,491))

    # Testing compile_inherit_value
    def test_compile_inherit_value_0(self):
        input = """
        const a = 10;
        const b = 5;

        var arr [a][b]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
"""
        expect = """Type Mismatch: VarDecl(arr,ArrayType(IntType,[Id(a),Id(b)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType,[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_compile_inherit_value_1(self):
        input = """
        const a = 2;
        const b = 3;

        var arr [a][b][1]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
"""
        expect = """Type Mismatch: VarDecl(arr,ArrayType(IntType,[Id(a),Id(b),IntLiteral(1)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType,[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]]))\n"""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_compile_inherit_value_2(self):
        input = """
        const a = 2;
        const b = 3;

        var arr [a][b]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_compile_inherit_value_3(self):
        input = """
        const a = (2 + 5) * 10 + 5;
        const b = 3 + a;

        var arr [a][b]float;

        func foo(x [75][78]float) {
            var y = 10.0;
            foo(arr);
        };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_compile_inherit_value_4(self):
        input = """
        const a = 4*7 + 4 - 2;   
        const b = 3 + a;
        const c = 15*2;
        const d = (5+1)*6-3;

        var arr [a][b]float;

        func foo(x [c][d]float) {
            var y = 10.0;
            foo(arr);
        };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_compile_inherit_value_5(self):
        input = """
        const a = 2*7 + 4 - 2;   
        const b = 3 + a;
        const c = 15*2;
        const d = (5+1)*6-3;

        var arr [a][b]float;

        func foo(x [c][d]float) {
            var y = 10.0;
            foo(arr);
        };
"""
        expect = """Type Mismatch: FuncCall(foo,[Id(arr)])\n"""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_compile_inherit_value_6(self):
        input = """
        const a = 7 + 4 - 2;            // a = 9   
        const b = 3 + a;                // b = 12
        const c = 2;
        const d = a + b - c - 7;            // d = 12
        const z = c * c * c + 1;

        var arr [a][b]float;

        func foo(x [z][d]float) {
            var y = 10.0;
            foo(arr);
        };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_compile_inherit_value_7(self):
        input = """
        const a = 7 + 4 - 2;            // a = 9   
        const b = 3 + a;                // b = 12
        const c = 2;
        const d = a + b - c - 7;            // d = 12
        const z = c * c * c + 1;

        var arr [a][b]float;

        func foo(x [z][d]float) {
            var y = 10.0;
            var a int = 5;
            z := 10;
            d := 12;
            foo(arr);
        };
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_compile_inherit_value_8(self):
        input = """
        const a = 7 + 4 - 2;            // a = 9   
        const b = 3 + a;                // b = 12
        const c = 2;
        const d = a + b - c - 7;            // d = 12
        const z = c * c * c + 1;

        var arr [a][b]float;

        func foo(x [z][d]int) {
            var y = 10.0;
            var a int = 5;
            foo(arr);
        };
"""
        expect = """Type Mismatch: FuncCall(foo,[Id(arr)])\n"""
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_compile_inherit_value_9(self):
        input = """
        const a = 7 + 4 - 2;            // a = 9   
        const b = 3 + a;                // b = 12
        const c = 2;
        const d = a + b - c - 7;            // d = 12
        const z = c * c * c + 1;

        var arr [a][b]float;

        func foo(x [z][d]int) {
            arr := x;
        };
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_compile_inherit_value_10(self):
        input = """
        const a = 7 + 4 - 2;            // a = 9   
        const b = 3 + a;                // b = 12
        const c = 2;
        const d = a + b - c - 7;            // d = 12
        const z = c * c * c + 1;

        var arr [a][b]Calculator;

        func foo(x [z][d]A) {
            arr := x;
        }

        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) Add(x, y int) int {
            return x+y;
        }

        func (a A) Subtract(x, y float, c int) float {
            return x
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        };
"""
        expect = """Type Mismatch: Assign(Id(arr),Id(x))\n"""
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_shadow_variable_0(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset();
            SayHello(name string);
        }

        func (x A) Add(x, y int) int {
            x.num := y;
            return y;
        }

        func (a A) Subtract(x, y float, c int) float {
            return x
        }

        func (a A) Reset() {
            var x int = 10;
            putIntLn(x);
        }

        func (a A) SayHello(name string) {
            return;
        }

        type A struct {
            num int;
            op string;
        };
"""
        expect = """Type Mismatch: FieldAccess(Id(x),num)\n"""
        self.assertTrue(TestChecker.test(input,expect,503))
        
    def test_array_dimen_0(self):
        input = """
        const e  = 3 ;
        var d [e]int ;
        var b [e]int ;

        func Adding(x [3]int) {
            var e int = 5;
            x := d;
            return;
        }

        func Minus (x [5] int) {
            var e int = 5;
            x := b;
            return
        }
        

                """
        expect = "Type Mismatch: Assign(Id(x),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_array_dimen_1(self):
        input = """
        const e  = 3 ;
        var d [e]int ;

        func Adding(x [e]int) {
            var e int = 5;
            Adding(x);
        }

        func Minus (y [5]int) {
            var e int = 5;
            Adding(y);
        }
        

                """
        expect = "Type Mismatch: FuncCall(Adding,[Id(y)])\n"
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_array_dimen_2(self):
        input = """
        const e  = 3 ;
        const z = 3;
        var d [e]int ;

        func Adding(x [e]int) {
            var e int = 5;
            var arr[z]int;
            if (e > 4) {
                var z int = 5;
                Adding(arr);
            }
        }

        func Minus (y [5]int) {
            var e int = 3;
            z += 2;
            var arr[z]int;
            if (e > 4) {
                var z boolean = true;
                if (z) {
                    var e int = 5;
                    Minus(arr);
                }
            }
        }
        """
        expect = "Type Mismatch: FuncCall(Minus,[Id(arr)])\n"
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_array_dimen_3(self):
        input = """
        const e  = 3 ;
        const z = 3;
        var arr1 [e]int ;

        func Adding(x [e]int) {
            var e int = 5;

            var arr2[e]int ;
            if (e > 4) {
                var e int = 3;
                var z int = 5;
                
                var arr3[e] int;
                if (z > 2) {
                    var z int = 5;
                    var arr4 [z]int;

                    for _, e := range arr4 {
                        var z int = 6;

                        // Start raising Error
                        arr3 := arr1;
                        arr2 := arr4;
                        arr1 := arr2;           // Raise error
                        arr4 := arr3;
                    }
                }
            }
        }       

                """
        expect = "Type Mismatch: Assign(Id(arr1),Id(arr2))\n"
        self.assertTrue(TestChecker.test(input,expect,507))
    
    def test_array_dimen_4(self):
        input = """
        const x = 10;
        const y = 7;

        func (c mstruct) add(arr[x][y]int) {
            var arr1[10][7]int ;
            arr1 := arr ;
            c.add(arr1) ;
        }
        
        type mstruct struct {
            a int
        };
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,508))
        
    def test_array_dimen_5(self):
        input = """
        const x = 10;
        const y = 7;

        func (c mstruct) add(arr[x][y]int) {
            var arr1[10][7]int ;
            const x = 5;
            const y = 2;
            arr1 := arr ;
            c.add(arr1) ;
        }

        const d = 5;
        const e = 2;

        func (c mstruct) minus(arr[d][e]int) {
            const d = 10;
            const e = 7;
            var arr1[5][2]int;
            c.minus(arr1);
            c.add(arr1);            // must raise error here
        }
        
        type mstruct struct {
            a int
        }
        """
        expect = "Type Mismatch: MethodCall(Id(c),add,[Id(arr1)])\n"
        self.assertTrue(TestChecker.test(input,expect,509))
