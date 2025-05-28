import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # Testing simple_program
    def test_simple_program_0(self):
        input = """func main() {
            return ;
        };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_program_1(self):
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program_2(self):
        input = """var x float ;"""
        expect = str(Program([VarDecl("x",FloatType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_program_3(self):
        input = """func main () {
            return ;
        }; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Return(None)])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_program_4(self):
        input = """func main() {
    break;
    continue;
        };"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Break(), Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_simple_program_5(self):
        input = """func main() { x += 1; }
        """
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Assign(Id("x"),BinaryOp("+", Id("x"), IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_simple_program_6(self):
        input = """func main() {x.a := 1;}
        """
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([Assign(FieldAccess(Id("x"), "a"),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program_7(self):
        input = """func main() {x.a();} ; """
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([MethCall(Id("x"), "a", [])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_simple_program_8(self):
        input = """type Calculator struct {
            val1 int;
            val2 int;
            val3 float
            val4 string
        };"""
        expect = str(Program([StructType("Calculator",
                                [("val1",IntType()),("val2",IntType()),("val3",FloatType()),("val4",StringType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_simple_program_9(self):
        input = """type Calculator struct {
            value int;
        };"""
        expect = str(Program([StructType("Calculator",[("value",IntType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_simple_program_10(self):
        input = """type Calculator interface {
            Add(x, y int) int;
        }; """
        expect = str(Program([
            InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType())])
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_simple_program_11(self):
        input = """type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }; """
        expect = str(Program([
            InterfaceType("Calculator",[
                Prototype("Add",[IntType(),IntType()],IntType()),
                Prototype("Subtract",[FloatType(),FloatType(),IntType()],FloatType()),
                Prototype("Reset",[],VoidType()),
                Prototype("SayHello",[StringType()],VoidType())
                ])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_simple_program_12(self):
        input = """func DoThing() {
            return ;
        } ;"""
        expect = str(Program([FuncDecl("DoThing",[],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_simple_program_13(self):
        input = """func DoThing(a int) int {
            return ;
        } ;"""
        expect = str(Program([FuncDecl("DoThing",[ParamDecl("a", IntType())],IntType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_simple_program_14(self):
        input = """func DoThing(a int, b string, c boolean) boolean {
            return ;
        } ;"""
        expect = str(Program([FuncDecl("DoThing", [ParamDecl("a", IntType()), ParamDecl("b", StringType()), ParamDecl("c", BoolType())],
                        BoolType(), Block([
                            Return(None)
                        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_simple_program_15(self):
        input = """
        func (p Person) Greet() string {
            return "Hello, " + p.name;
        }
        """
        expect = str(Program([MethodDecl("p",Id("Person"),
                        FuncDecl("Greet",
                                 [],
                                 StringType(),
                                 Block([Return(BinaryOp("+",StringLiteral("\"Hello, \""),FieldAccess(Id("p"),"name")))])))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_simple_program_16(self):
        input = """func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
        }
        """
        expect = str(Program([MethodDecl("c",Id("Calculator"),
                        FuncDecl("Add",[ParamDecl("x", IntType())],IntType(),Block([
                            Assign(lhs=FieldAccess(Id("c"), "value"), rhs=BinaryOp("+",FieldAccess(Id("c"), "value"),Id("x"))),
                            Return(FieldAccess(Id("c"), "value"))
                        ])))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_simple_program_17(self):
        input = """var x int = 10;
            var y string = "hieu1";
            var z float = 10.5;
            var t boolean = true;"""
        expect = str(Program([
            VarDecl("x", IntType(), IntLiteral(10)),
            VarDecl("y", StringType(), StringLiteral("\"hieu1\"")),
            VarDecl("z", FloatType(), FloatLiteral(10.5)),
            VarDecl("t", BoolType(), BooleanLiteral(True))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_simple_program_18(self):
        input = """
            var x int;
            var y = "hieu1";"""
        expect = str(Program([
            VarDecl("x", IntType(), None),
            VarDecl("y", None, StringLiteral("\"hieu1\"")),
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_simple_program_19(self):
        input = """
            var s string = "123"
            func DoThing() int {
                var b float = 3.0;
                const a = 3 ;
        } ;"""
        expect = str(Program([
            VarDecl("s", StringType(), StringLiteral("\"123\"")),
            FuncDecl("DoThing",
                     [],
                     IntType(),
                     Block([
                        VarDecl("b", FloatType(), FloatLiteral(3.0)),
                        ConstDecl("a", None, IntLiteral(3))
                     ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    # Testing expression
    def test_expression_0(self):
        input = """var b int = 5 + 3 / 2 - 7 && 8 ;
        ;"""
        expect = str(Program([VarDecl("b", IntType(), 
                                      BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(5), 
                                                                            BinaryOp("/", IntLiteral(3), IntLiteral(2))),
                                                             IntLiteral(7)),
                                                IntLiteral(8)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    # Testing variable_declaration
    def test_variable_declaration_0(self):
        input = """var a int ;"""
        expect = str(Program([VarDecl("a",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_variable_declaration_1(self):
        input = """var s string ;"""
        expect = str(Program([VarDecl("s",StringType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_variable_declaration_2(self):
        input = """var f float ;"""
        expect = str(Program([VarDecl("f",FloatType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_variable_declaration_3(self):
        input = """var b boolean ;"""
        expect = str(Program([VarDecl("b",BoolType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_variable_declaration_4(self):
        input = """var _a12 int = 10 ;
var x int = 0x20 ;
var hieu23 = 0B101 ;
var hieu23 = 0o24 ;"""
        expect = str(Program([
            VarDecl("_a12",IntType(),IntLiteral(10)),
            VarDecl("x",IntType(),IntLiteral(0x20)),
            VarDecl("hieu23",None,IntLiteral(0b101)),
            VarDecl("hieu23",None,IntLiteral(0o24))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_variable_declaration_5(self):
        input = """var s string = "hieu is handsome"
"""
        expect = str(Program([VarDecl("s",StringType(),StringLiteral("\"hieu is handsome\""))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_variable_declaration_6(self):
        input = """var f float = 0.0375 ;"""
        expect = str(Program([VarDecl("f",FloatType(),FloatLiteral(0.0375))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_variable_declaration_7(self):
        input = """var b boolean = true;
var b2 boolean = false;"""
        expect = str(Program([VarDecl("b",BoolType(),BooleanLiteral(True)),
                              VarDecl("b2",BoolType(),BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_variable_declaration_8(self):
        input = """const a = 10 ;"""
        expect = str(Program([ConstDecl("a",None,IntLiteral(10))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_variable_declaration_9(self):
        input = """var a = 10.e+2;"""
        expect = str(Program([VarDecl("a",None,FloatLiteral(10.e+2))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_variable_declaration_10(self):
        input = """var a = true;"""
        expect = str(Program([VarDecl("a",None,BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_variable_declaration_11(self):
        input = """func main(){
var x int = 10 ; 
var y float = 10.5 ;
var z string = "Hieu" ; 
var b boolean = true ;
}
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            VarDecl("x", IntType(), IntLiteral(10)),
            VarDecl("y", FloatType(), FloatLiteral(10.5)),
            VarDecl("z", StringType(), StringLiteral("\"Hieu\"")),
            VarDecl("b", BoolType(), BooleanLiteral(True)),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_variable_declaration_12(self):
        input = """func main() {
var x = 10; 
var y = 10.5; 
var z = "Hieu"; 
var b = true;
}
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            VarDecl("x", None, IntLiteral(10)),
            VarDecl("y", None, FloatLiteral(10.5)),
            VarDecl("z", None, StringLiteral("\"Hieu\"")),
            VarDecl("b", None, BooleanLiteral(True)),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_variable_declaration_13(self):
        input = """func main() {
const Pi = 3.14; 
const Greeting = "Hello, MiniGo!"; 
const MaxSize = 100 + 50;
}
"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            ConstDecl("Pi", None, FloatLiteral(3.14)),
            ConstDecl("Greeting", None, StringLiteral("\"Hello, MiniGo!\"")),
            ConstDecl("MaxSize", None, BinaryOp("+", IntLiteral(100), IntLiteral(50))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_variable_declaration_14(self):
        input = """var x int = p.age;"""
        expect = str(Program([VarDecl("x", IntType(), FieldAccess(Id("p"), "age"))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_variable_declaration_15(self):
        input = """var x int = sum(a, 10);"""
        expect = str(Program([VarDecl("x", IntType(), FuncCall("sum", [Id("a"), IntLiteral(10)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_variable_declaration_16(self):
        input = """var x float = p.sum(a, 19.2);
var z string = s.show();
var y int = rand.arr[10];"""
        expect = str(Program([
            VarDecl("x", FloatType(), MethCall(Id("p"), "sum", [Id("a"), FloatLiteral(19.2)])),
            VarDecl("z", StringType(), MethCall(Id("s"), "show", [])),
            VarDecl("y", IntType(), ArrayCell(FieldAccess(Id("rand"), "arr"), [IntLiteral(10)])),
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_variable_declaration_17(self):
        input = """var x float = [2]float{1.0,2.2};
var arr float = [2][2]float{{1.0,2.2},{3.3,4.0}};"""
        expect = str(Program([
            VarDecl("x", FloatType(), ArrayLiteral([IntLiteral(2)], FloatType(), [FloatLiteral(1.0), FloatLiteral(2.2)])),
            VarDecl("arr", FloatType(), ArrayLiteral([IntLiteral(2),IntLiteral(2)], FloatType(), 
                    [[FloatLiteral(1.0), FloatLiteral(2.2)], [FloatLiteral(3.3), FloatLiteral(4.0)]])),
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_variable_declaration_18(self):
        input = """var x float = y + (10 * z.arr[10]);"""
        expect = str(Program([
            VarDecl("x", FloatType(), 
                BinaryOp("+", Id("y"), BinaryOp("*", IntLiteral(10), ArrayCell(FieldAccess(Id("z"), "arr"), [IntLiteral(10)])))
                )]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    # Testing struct_declaration
    def test_struct_declaration_0(self):
        input = """type Calculator struct {
 value int;
 };"""
        expect = str(Program([StructType("Calculator",[("value",IntType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_struct_declaration_1(self):
        input = """type Calculator struct {
 val1 int;
 val2 int;
 val3 float
 val4 string
 };"""
        expect = str(Program([StructType("Calculator",
[("val1",IntType()),("val2",IntType()),("val3",FloatType()),("val4",StringType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_struct_declaration_2(self):
        input = """type Computer struct {
            s Screen;
            k Keyboard;
            v Value;
        };"""
        expect = str(Program([StructType("Computer",[
            ("s",Id("Screen")),
            ("k",Id("Keyboard")),
            ("v",Id("Value"))
            ],[])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    # Testing interface_declaration
    def test_interface_declaration_0(self):
        input = """type Calculator interface {
 Add(x, y int) int;
 };"""
        expect = str(Program([InterfaceType("Calculator",[Prototype("Add", [IntType(), IntType()], IntType())])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_interface_declaration_1(self):
        input = """type Calculator interface {
 Add(x, y int) int;
 Subtract(a, b float, c int) float;
 Reset()
 SayHello(name string)
 };"""
        expect = str(Program([InterfaceType("Calculator",[
            Prototype("Add", [IntType(), IntType()], IntType()),
            Prototype("Subtract", [FloatType(), FloatType(), IntType()], FloatType()),
            Prototype("Reset", [], VoidType()),
            Prototype("SayHello", [StringType()], VoidType())
            ])]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    # Testing assignment_stmt
    def test_assignment_stmt_0(self):
        input = """func main() {
a := 10+1;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("a"), BinaryOp("+", IntLiteral(10), IntLiteral(1)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_assignment_stmt_1(self):
        input = """func main() {
s += "trung";
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("s"), BinaryOp("+", Id("s"), StringLiteral("\"trung\"")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_assignment_stmt_2(self):
        input = """func main() {
a -= 10\n
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(10)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_assignment_stmt_3(self):
        input = """func main() {
person.name := \"John\";
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(FieldAccess(Id("person"),"name"), StringLiteral("\"John\""))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_assignment_stmt_4(self):
        input = """func main() {
person.age := 30 * 2 + 6;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(FieldAccess(Id("person"), "age"), BinaryOp("+", BinaryOp("*", IntLiteral(30), IntLiteral(2)), IntLiteral(6)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_assignment_stmt_5(self):
        input = """func main() {
a[2][3] := b[2] + 1;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]), 
                   BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(2)]), IntLiteral(1))),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_assignment_stmt_6(self):
        input = """func main() {
arr := [3]int{10, 20, 30};
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("arr"),ArrayLiteral(
                       [IntLiteral(3)],
                      IntType(),
                     [IntLiteral(10),IntLiteral(20),IntLiteral(30)]
)),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_assignment_stmt_7(self):
        input = """func main() {
marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}\n
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("marr"), ArrayLiteral([IntLiteral(2), IntLiteral(3)], IntType(), [
                                                                [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                                                                [IntLiteral(4), IntLiteral(5), IntLiteral(6)]]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_assignment_stmt_8(self):
        input = """func main() {
p := Person{name: "Alice", age: 30};
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("p"), StructLiteral("Person", [("name", StringLiteral("\"Alice\"")), ("age", IntLiteral(30))]))
        ]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_assignment_stmt_9(self):
        input = """func main() {
q := Person{};
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("q"), StructLiteral("Person", []))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_expression_1(self):
        input = """var a = true || false;"""
        expect = str(Program([VarDecl("a", None, BinaryOp("||", BooleanLiteral(True), BooleanLiteral(False)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_expression_2(self):
        input = """var a = arr[1][0] ;"""
        expect = str(Program([VarDecl("a", None, ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(0)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_expression_3(self):
        input = """var a = 10+2;"""
        expect = str(Program([VarDecl("a", None, BinaryOp("+", IntLiteral(10), IntLiteral(2)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_expression_4(self):
        input = """func main() {
person.name := \"Trung\";
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(FieldAccess(Id("person"),"name"), StringLiteral("\"Trung\""))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_expression_5(self):
        input = """func main() {
arr[10][10.1] := 0;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(ArrayCell(Id("arr"),[IntLiteral(10),FloatLiteral(10.1)]), IntLiteral(0))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_expression_6(self):
        input = """func main() {
arr[10][\"10\"] := 1;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(ArrayCell(Id("arr"),[IntLiteral(10),StringLiteral("\"10\"")]), IntLiteral(1))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_expression_7(self):
        input = """func main() {
x := a % 5;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("x"), BinaryOp("%", Id("a"), IntLiteral(5)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_expression_8(self):
        input = """func main() {
y := x && z;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("y"), BinaryOp("&&", Id("x"), Id("z")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_expression_9(self):
        input = """func main() {
is_loading := ! x;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("is_loading"), UnaryOp("!", Id("x")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_expression_10(self):
        input = """func main() {
x /= x >= y;
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            Assign(Id("x"), BinaryOp("/", Id("x"), BinaryOp(">=", Id("x"), Id("y"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_expression_11(self):
        input = """var x = a[1][2][3].methodcall(a[1], b[2]) && c;"""
        expect = str(Program([
            VarDecl("x", None, BinaryOp("&&", MethCall(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                       "methodcall", [ArrayCell(Id("a"), [IntLiteral(1)]), ArrayCell(Id("b"), [IntLiteral(2)])]
                                                       ), Id("c")))            
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_expression_12(self):
        input = """const x = a[1][2][3].methodcall(a[1], funccall(x, 10)) && c;"""
        expect = str(Program([
            ConstDecl("x", None, BinaryOp("&&", MethCall(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                                                       "methodcall", [ArrayCell(Id("a"), [IntLiteral(1)]), FuncCall("funccall", [Id("x"), IntLiteral(10)])]
                                                       ), Id("c")))            
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_expression_13(self):
        input = """var x int = a[1].methodcall()[10+2];"""
        expect = str(Program([
            VarDecl("x", IntType(), ArrayCell(
                MethCall(ArrayCell(Id("a"), [IntLiteral(1)]), "methodcall", []),
                [BinaryOp("+", IntLiteral(10), IntLiteral(2))]    
            ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_expression_14(self):
        input = """var x int = a[1].methodcall()[10+2][2][a % 5];"""
        expect = str(Program([
            VarDecl("x", IntType(), ArrayCell(
                MethCall(ArrayCell(Id("a"), [IntLiteral(1)]), "methodcall", []),
                [BinaryOp("+", IntLiteral(10), IntLiteral(2)), IntLiteral(2), BinaryOp("%", Id("a"), IntLiteral(5))]    
            ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_expression_15(self):
        input = """var x int = a[1].methodcall()[10+2][2][a % 5][a && !b];"""
        expect = str(Program([
            VarDecl("x", IntType(), ArrayCell(
                MethCall(ArrayCell(Id("a"), [IntLiteral(1)]), "methodcall", []),
                [BinaryOp("+", IntLiteral(10), IntLiteral(2)), IntLiteral(2), 
                 BinaryOp("%", Id("a"), IntLiteral(5)), BinaryOp("&&", Id("a"), UnaryOp("!", Id("b")))]    
            ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_expression_16(self):
        input = """func main() {
        x += funccall("trung"+"hieu", [2][3]int{{1, 2, 3}, 4, 5})
};"""
        expect = str(Program([
            FuncDecl("main", [], VoidType(), Block([
                    Assign(Id("x"), BinaryOp("+", Id("x"), FuncCall("funccall", [
                    BinaryOp("+", StringLiteral("\"trung\""), StringLiteral("\"hieu\"")), 
                    ArrayLiteral([IntLiteral(2), IntLiteral(3)], IntType(), [
                        [IntLiteral(1), IntLiteral(2), IntLiteral(3)], 
                        IntLiteral(4), IntLiteral(5)
                    ])
            ])))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    # Testing for_statement
    def test_for_statement_0(self):
        input = """func Adding(a, b int, c, d float) int {
    for i < 1 {
        a += b; 
        c += d;
    }        

    return a * c
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType()), ParamDecl("c", FloatType()), ParamDecl("d", FloatType())], IntType(), Block([
            ForBasic(BinaryOp("<", Id("i"), IntLiteral(1)), Block([
                Assign(Id("a"), BinaryOp("+", Id("a"), Id("b"))),
                Assign(Id("c"), BinaryOp("+", Id("c"), Id("d")))
            ])), 
            Return(BinaryOp("*", Id("a"), Id("c")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_for_statement_1(self):
        input = """func Adding(a, b int, c, d float) int {
    var x int = 5;
    
    for x <= 10 {
        a += b; 
        c += d;
        x += 1;
    }        

    return a * c * x
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType()), ParamDecl("c", FloatType()), ParamDecl("d", FloatType())], IntType(), Block([
            VarDecl("x", IntType(), IntLiteral(5)),
            ForBasic(BinaryOp("<=", Id("x"), IntLiteral(10)), Block([
                Assign(Id("a"), BinaryOp("+", Id("a"), Id("b"))),
                Assign(Id("c"), BinaryOp("+", Id("c"), Id("d"))),
                Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))
            ])), 
            Return(BinaryOp("*", BinaryOp("*", Id("a"), Id("c")), Id("x")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_for_statement_2(self):
        input = """func Adding(a, b int) {
    for var x int = 0; x <= 5; x += 1 {
        print(x+a);
        a += b;
    }        

    return;
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(VarDecl("x", IntType(), IntLiteral(0)),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                    Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                        FuncCall("print", [BinaryOp("+", Id("x"), Id("a"))]),
                        Assign(Id("a"), BinaryOp("+", Id("a"), Id("b")))
                    ]) ), 
            Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_for_statement_3(self):
        input = """func Adding(a, b int) {
    for x := 20 && a; x <= 5; x += 1 {
        print(x+a);
        a += b;
    }

    return;
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(Assign(Id("x"), BinaryOp("&&", IntLiteral(20), Id("a"))),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                    Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                        FuncCall("print", [BinaryOp("+", Id("x"), Id("a"))]),
                        Assign(Id("a"), BinaryOp("+", Id("a"), Id("b")))
                    ]) ), 
            Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_for_statement_4(self):
        input = """func Adding(a, b int) {
    for x := 20 && a; x <= 5; x += 1 {
        for var x int = 0; x <= 5; x += 1 {
            print(x+a);
            break;
        }
    }
    return;
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(Assign(Id("x"), BinaryOp("&&", IntLiteral(20), Id("a"))),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                    Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                        ForStep(VarDecl("x", IntType(), IntLiteral(0)),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                            Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                                FuncCall("print", [BinaryOp("+", Id("x"), Id("a"))]),
                                Break(),
                            ]) ),
                    ]) ), 
            Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_for_statement_5(self):
        input = """func Adding(a, b int) {
    for x := 20 && a; x <= 5; x += 1 {
        for idx,_ := range [2][3]float{{2.3,1.e+3,2.0}} {
            break ;
        }
    }
    return;
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(Assign(Id("x"), BinaryOp("&&", IntLiteral(20), Id("a"))),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                    Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                        ForEach(Id("idx"), Id("_"), ArrayLiteral([IntLiteral(2), IntLiteral(3)], FloatType(), 
                                                                 [[FloatLiteral(2.3), FloatLiteral(1.e+3), FloatLiteral(2.0)]]), Block([
                            Break()                   
                ]))]) ), 
            Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_for_statement_6(self):
        input = """func Adding(a, b int) {
    for x := 20 && a; x <= 5; x += 1 {
        for idx,_ := range [2][3]float{{2.3,1.e+3,2.0}} {
            if (x > 10) {
                break;
            } else {
                x += 10 ;
            }
            print(x)
        }
    }
    return;
};"""
        expect = str(Program([FuncDecl("Adding", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(Assign(Id("x"), BinaryOp("&&", IntLiteral(20), Id("a"))),  BinaryOp("<=",Id("x"),IntLiteral(5)),  
                    Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))), Block([
                        ForEach(Id("idx"), Id("_"), ArrayLiteral([IntLiteral(2), IntLiteral(3)], FloatType(), 
                                                                 [[FloatLiteral(2.3), FloatLiteral(1.e+3), FloatLiteral(2.0)]]), Block([
                            If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([Break()]), 
                               Block([Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(10)))])), 
                            FuncCall("print", [Id("x")])                   
                ]))]) ), 
            Return(None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    # Testing if_statement
    def test_if_statement_0(self):
        input = """func main() {
if (x > 10) {
println("x is greater than 10") ;
count -= 1
}
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), Block([
            If(BinaryOp(">", Id("x"), IntLiteral(10)), Block([
                FuncCall("println", [StringLiteral("\"x is greater than 10\"")]),
                Assign(Id("count"), BinaryOp("-", Id("count"), IntLiteral(1)))
            ]), None)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_if_statement_1(self):
        input = """func main() {
if (x > 10) {
            println("x is greater than 10");
        } else {
            println("x is less than 10");
            count -= 1 ;
        }
};"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                If(BinaryOp(">", Id("x"), IntLiteral(10)), 
                    Block([
                        FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
                    ]),
                    Block([
                        FuncCall("println", [StringLiteral("\"x is less than 10\"")]),
                        Assign(Id("count"), BinaryOp("-", Id("count"), IntLiteral(1)))
                    ])
            )
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_assignment_stmt_10(self):
        input = """func main() {
arr[0] := 10 ;
arr[0][1] += 9 ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(ArrayCell(Id("arr"),[IntLiteral(0)]), IntLiteral(10)),
                Assign(ArrayCell(Id("arr"),[IntLiteral(0),IntLiteral(1)]),
                       BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(0),IntLiteral(1)]),IntLiteral(9)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_assignment_stmt_11(self):
        input = """func main() {
person.name := "Hieu" ;
person.is_student := true ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(FieldAccess(Id("person"), "name"), StringLiteral("\"Hieu\"")),
                Assign(FieldAccess(Id("person"), "is_student"), BooleanLiteral(True)),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_assignment_stmt_12(self):
        input = """func main() {
arr[0].name := "Hieu" ;
arr3[0][1].is_student := true ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(FieldAccess(ArrayCell(Id("arr"), [IntLiteral(0)]), "name"), StringLiteral("\"Hieu\"")),
                Assign(FieldAccess(ArrayCell(Id("arr3"), [IntLiteral(0),IntLiteral(1)]), "is_student"), 
                       BooleanLiteral(True)),
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_assignment_stmt_13(self):
        input = """func main() {
a /= 10 + 23.2 ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a"), BinaryOp("/",Id("a"),BinaryOp("+",IntLiteral(10),FloatLiteral(23.2))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_assignment_stmt_14(self):
        input = """func main() {
ax %= person.age ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("ax"), BinaryOp("%",Id("ax"),FieldAccess(Id("person"),"age")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_assignment_stmt_15(self):
        input = """func main() {
a9 %= [2]int{1,2} ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a9"), BinaryOp("%",Id("a9"),ArrayLiteral([IntLiteral(2)],
                                                        IntType(),[IntLiteral(1),IntLiteral(2)])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_assignment_stmt_16(self):
        input = """func main() {
a9 %= calculator.Add(1,2) ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a9"), BinaryOp("%",Id("a9"),MethCall(Id("calculator"), "Add", 
                                                            [IntLiteral(1),IntLiteral(2)])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_assignment_stmt_17(self):
        input = """func main() {
a9 %= calculator.Add(1,2) + 10 - 12 / 4 ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a9"), BinaryOp("%",Id("a9"), 
                    BinaryOp("-", BinaryOp("+", MethCall(Id("calculator"), "Add", [IntLiteral(1),IntLiteral(2)]), IntLiteral(10)),
                         BinaryOp("/", IntLiteral(12), IntLiteral(4)))))
        ]))]))
        
        # print("test 387")
        # print(expect)
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_assignment_stmt_18(self):
        input = """func main() {
a9 %= sum(1,2) + 10 - 12 / 4 * 2 ;
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                Assign(Id("a9"), BinaryOp("%",Id("a9"), 
                    BinaryOp("-", BinaryOp("+", FuncCall("sum",[IntLiteral(1),IntLiteral(2)]), IntLiteral(10)),
                         BinaryOp("*", BinaryOp("/", IntLiteral(12), IntLiteral(4)), IntLiteral(2)))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    # Testing func_call
    def test_func_call_0(self):
        input = """func main() {
foo(2 + x, 4 / y);
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                FuncCall("foo", [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("/", IntLiteral(4), Id("y"))])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_func_call_1(self):
        input = """func main() {
m.goo();
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                MethCall(Id("m"), "goo", [])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_func_call_2(self):
        input = """func main() {
m[3].goo();
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                MethCall(ArrayCell(Id("m"), [IntLiteral(3)]), "goo", [])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_func_call_3(self):
        input = """func main() {
m[3].add(1,2,3,10,9.8)
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                MethCall(ArrayCell(Id("m"), [IntLiteral(3)]), "add", 
                         [IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(10),FloatLiteral(9.8)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_func_call_4(self):
        input = """func main() {
println("x is greater than 10");
}
"""
        expect = str(Program([FuncDecl("main", [], VoidType(), 
            Block([
                FuncCall("println", [StringLiteral("\"x is greater than 10\"")])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    # Testing complex
    def test_complex_0(self):
        input = """func main() {
        rand.Seed(time.Now().UnixNano()) // Seed the random number generator

        fmt.Println("Random numbers:")
        for i := 0; i < 10; i+=1 {
                num := rand.Intn(100) + 1 // Generate a number between 1 and 100
                fmt.Println(num)
        }
}
"""
        expect = "Program([FuncDecl(main,[],VoidType,Block([MethodCall(Id(rand),Seed,[MethodCall(MethodCall(Id(time),Now,[]),UnixNano,[])]),MethodCall(Id(fmt),Println,[StringLiteral(\"Random numbers:\")]),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Assign(Id(num),BinaryOp(MethodCall(Id(rand),Intn,[IntLiteral(100)]),+,IntLiteral(1))),MethodCall(Id(fmt),Println,[Id(num)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_complex_1(self):
        input = """func randomChoice() {
        choices := [5]string{"Go", "Python", "Java", "C++", "JavaScript"}
        rand.Seed(time.Now().UnixNano())
        x := rand.Intn(len(choices))
        fmt.Println("Random choice:", choices[x])
}
"""
        expect = "Program([FuncDecl(randomChoice,[],VoidType,Block([Assign(Id(choices),ArrayLiteral([IntLiteral(5)],StringType,[StringLiteral(\"Go\"),StringLiteral(\"Python\"),StringLiteral(\"Java\"),StringLiteral(\"C++\"),StringLiteral(\"JavaScript\")])),MethodCall(Id(rand),Seed,[MethodCall(MethodCall(Id(time),Now,[]),UnixNano,[])]),Assign(Id(x),MethodCall(Id(rand),Intn,[FuncCall(len,[Id(choices)])])),MethodCall(Id(fmt),Println,[StringLiteral(\"Random choice:\"),ArrayCell(Id(choices),[Id(x)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

#     def test_complex_2(self):
#         input = """const Pi = 3.14;
# const Zero = a;  //  Semantic Error: Constant must have an initialization value
# const Invalid = 10 + true; //  Type mismatch (int + boolean)

# // Global variable declarations (valid and invalid)
# var globalInt int = 10;
# var globalFloat float = 5.5;
# var globalBool boolean = true;
# var globalString string = "MiniGo";
# var globalArray [3]int;
# // globalArray := [3]int{1, 2, 3};
# var emptyArray [0]int; //  Edge case: Empty array

# var invalidArray [3]int;
# // invalidArray := [3]float{1.0, 2.0, 3.0};  //  Type mismatch (int array with float values)

# // Struct declaration (valid and invalid)
# type Person struct {
#     name string;
#     age int;
# }

# // Interface declaration (valid and invalid)
# type Greeter interface {
#     Greet() string;
#     InvalidMethod(a, b float) int;
# }

# // Function declaration (valid and invalid)
# func add(x int, y int) int {
#     return x + y;
# }

# func noReturn(x int, y int) int {
#     return x + y  //  Semantic Error: Function must return an int but does not have a return statement
# }

# func multiReturn() int { 
#     return 10  
# }

# // Method declaration (valid and invalid)
# func (p Person) Greet() string {
#     return "Hello, " + p.name;
# }

# func (p Person) InvalidMethod() int {
#     return p.undefinedField;  //  Semantic Error: `undefinedField` does not exist in struct
# }

# // Main function (valid and invalid operations)
# func main() {
#     // Local variable declarations
#     var localInt int = 20;
#     var localFloat float = 10.5;
#     var localBool boolean = false;
#     var localString string = "Test";
#     var localArray [2]int
#     localArray := [2]int{5, 6};

#     // Assignment statements
#     localInt := localInt + 5;
#     localFloat += 2.5;
#     localBool := !localBool;
#     localString := localString + " Case";

#     localString := localInt;  //  Semantic Error: Type mismatch (string = int)

#     // Struct instantiation
#     var p Person = Person{name: "Alice", age: 25};
#     var invalidPerson Person = Person{a:42, b:"Bob"};  //  Semantic Error: Incorrect order/types

#     // Array element assignment (valid and invalid)
#     localArray[0] := 99;
#     globalArray[2] := 42;
#     localArray[2] := 5;  //  Runtime Error: Index out of bounds

#     // Print values
#     putInt(localInt);
#     putFloat(localFloat);
#     putBool(localBool);
#     putString(localString);
#     putLn();

#     // If-else statement (valid and invalid)
#     if (localInt > 10) {
#         putStringLn("localInt is greater than 10");
#     } else if (localInt == 10) {
#         putStringLn("localInt is exactly 10");
#     } else {
#         putStringLn("localInt is less than 10");
#     }

#     if (localInt) {  //  Semantic Error: Condition must be boolean, but int is given
#         putStringLn("This should not compile.");
#     }

#     // For loop (valid and invalid)
#     var i int = 0;
#     for i < 5 {
#         putInt(i);
#         putLn();
#         i += 1;
#     }

#     for i := 0; i < 3; i += 1 {
#         putInt(globalArray[i]);
#         putLn();
#     }

#     for index, value := range localArray {
#         putInt(index);
#         putString(": ");
#         putInt(value);
#         putLn();
#     }

#     for index, value := range localInt {  //  Semantic Error: Cannot iterate over int
#         putInt(index);
#     }

#     // Function calls (valid and invalid)
#     var sum int = add(7, 8);
#     putInt(sum);
#     putLn();

#     add(1, "string");  //  Semantic Error: Type mismatch (int, string)

#     // Method calls (valid and invalid)
#     putStringLn(p.Greet());

#     var g Greeter;
#     g.Greet();  //  Semantic Error: Interface variable is not initialized

#     // Break and continue in loops (valid and invalid)
#     for i := 0; i < 10; i += 1 {
#         if (i == 5) {
#             break;
#         }
#         if (i % 2 == 0) {
#             continue;
#         }
#         putInt(i);
#         putLn();
#     }

#     break;  //  Syntax Error: `break` cannot be used outside of a loop

#     // Type mismatches
#     var mixType int = "wrong";  //  Semantic Error: Type mismatch (int = string)

#     // Function with invalid return usage
#     var returned int = noReturn(5, 6);  //  Semantic Error: Function does not return a value
# };
# """
#         expect = "Program([ConstDecl(Pi,FloatLiteral(3.14)),ConstDecl(Zero,Id(a)),ConstDecl(Invalid,BinaryOp(IntLiteral(10),+,BooleanLiteral(true))),VarDecl(globalInt,IntType,IntLiteral(10)),VarDecl(globalFloat,FloatType,FloatLiteral(5.5)),VarDecl(globalBool,BoolType,BooleanLiteral(true)),VarDecl(globalString,StringType,StringLiteral(\"MiniGo\")),VarDecl(globalArray,ArrayType(IntType,[IntLiteral(3)])),VarDecl(emptyArray,ArrayType(IntType,[IntLiteral(0)])),VarDecl(invalidArray,ArrayType(IntType,[IntLiteral(3)])),StructType(Person,[(name,StringType),(age,IntType)],[]),InterfaceType(Greeter,[Prototype(Greet,[],StringType),Prototype(InvalidMethod,[FloatType,FloatType],IntType)]),FuncDecl(add,[ParDecl(x,IntType),ParDecl(y,IntType)],IntType,Block([Return(BinaryOp(Id(x),+,Id(y)))])),FuncDecl(noReturn,[ParDecl(x,IntType),ParDecl(y,IntType)],IntType,Block([Return(BinaryOp(Id(x),+,Id(y)))])),FuncDecl(multiReturn,[],IntType,Block([Return(IntLiteral(10))])),MethodDecl(p,Id(Person),FuncDecl(Greet,[],StringType,Block([Return(BinaryOp(StringLiteral(\"Hello, \"),+,FieldAccess(Id(p),name)))]))),MethodDecl(p,Id(Person),FuncDecl(InvalidMethod,[],IntType,Block([Return(FieldAccess(Id(p),undefinedField))]))),FuncDecl(main,[],VoidType,Block([VarDecl(localInt,IntType,IntLiteral(20)),VarDecl(localFloat,FloatType,FloatLiteral(10.5)),VarDecl(localBool,BoolType,BooleanLiteral(false)),VarDecl(localString,StringType,StringLiteral(\"Test\")),VarDecl(localArray,ArrayType(IntType,[IntLiteral(2)])),Assign(Id(localArray),ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(5),IntLiteral(6)])),Assign(Id(localInt),BinaryOp(Id(localInt),+,IntLiteral(5))),Assign(Id(localFloat),BinaryOp(Id(localFloat),+,FloatLiteral(2.5))),Assign(Id(localBool),UnaryOp(!,Id(localBool))),Assign(Id(localString),BinaryOp(Id(localString),+,StringLiteral(\" Case\"))),Assign(Id(localString),Id(localInt)),VarDecl(p,Id(Person),StructLiteral(Person,[(name,StringLiteral(\"Alice\")),(age,IntLiteral(25))])),VarDecl(invalidPerson,Id(Person),StructLiteral(Person,[(a,IntLiteral(42)),(b,StringLiteral(\"Bob\"))])),Assign(ArrayCell(Id(localArray),[IntLiteral(0)]),IntLiteral(99)),Assign(ArrayCell(Id(globalArray),[IntLiteral(2)]),IntLiteral(42)),Assign(ArrayCell(Id(localArray),[IntLiteral(2)]),IntLiteral(5)),FuncCall(putInt,[Id(localInt)]),FuncCall(putFloat,[Id(localFloat)]),FuncCall(putBool,[Id(localBool)]),FuncCall(putString,[Id(localString)]),FuncCall(putLn,[]),If(BinaryOp(Id(localInt),>,IntLiteral(10)),Block([FuncCall(putStringLn,[StringLiteral(\"localInt is greater than 10\")])]),Block([FuncCall(putStringLn,[StringLiteral(\"localInt is less than 10\")])])),If(Id(localInt),Block([FuncCall(putStringLn,[StringLiteral(\"This should not compile.\")])])),VarDecl(i,IntType,IntLiteral(0)),For(BinaryOp(Id(i),<,IntLiteral(5)),Block([FuncCall(putInt,[Id(i)]),FuncCall(putLn,[]),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1)))])),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(3)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([FuncCall(putInt,[ArrayCell(Id(globalArray),[Id(i)])]),FuncCall(putLn,[])])),ForEach(Id(index),Id(value),Id(localArray),Block([FuncCall(putInt,[Id(index)]),FuncCall(putString,[StringLiteral(\": \")]),FuncCall(putInt,[Id(value)]),FuncCall(putLn,[])])),ForEach(Id(index),Id(value),Id(localInt),Block([FuncCall(putInt,[Id(index)])])),VarDecl(sum,IntType,FuncCall(add,[IntLiteral(7),IntLiteral(8)])),FuncCall(putInt,[Id(sum)]),FuncCall(putLn,[]),FuncCall(add,[IntLiteral(1),StringLiteral(\"string\")]),FuncCall(putStringLn,[MethodCall(Id(p),Greet,[])]),VarDecl(g,Id(Greeter)),MethodCall(Id(g),Greet,[]),For(Assign(Id(i),IntLiteral(0)),BinaryOp(Id(i),<,IntLiteral(10)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([If(BinaryOp(Id(i),==,IntLiteral(5)),Block([Break()])),If(BinaryOp(BinaryOp(Id(i),%,IntLiteral(2)),==,IntLiteral(0)),Block([Continue()])),FuncCall(putInt,[Id(i)]),FuncCall(putLn,[])])),Break(),VarDecl(mixType,IntType,StringLiteral(\"wrong\")),VarDecl(returned,IntType,FuncCall(noReturn,[IntLiteral(5),IntLiteral(6)]))]))])"
#         self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_complex_3(self):
        input = """func Add() {
        a[2+3&&2] += foo().b[2];       
    };"""
        expect = "Program([FuncDecl(Add,[],VoidType,Block([Assign(ArrayCell(Id(a),[BinaryOp(BinaryOp(IntLiteral(2),+,IntLiteral(3)),&&,IntLiteral(2))]),BinaryOp(ArrayCell(Id(a),[BinaryOp(BinaryOp(IntLiteral(2),+,IntLiteral(3)),&&,IntLiteral(2))]),+,ArrayCell(FieldAccess(FuncCall(foo,[]),b),[IntLiteral(2)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_complex_4(self):
        input = """func Add() {
        return (2 + 3)[b]
        return b.c[c]
    };"""
        expect = "Program([FuncDecl(Add,[],VoidType,Block([Return(ArrayCell(BinaryOp(IntLiteral(2),+,IntLiteral(3)),[Id(b)])),Return(ArrayCell(FieldAccess(Id(b),c),[Id(c)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

#     def test_complex_5(self):
#         input = """type Calculator interface {
#     Add(x, y int) int;
#     Subtract(a, b float, c int) float;
#     Reset()
#     SayHello(name string)
# }

# func Adding(a, b int) {
#     arr := [a][b]int{{}};
#     var x int;

#     for x := 20 && a; x <= 5; x += 1 {
#         for idx,_ := range [2][3]float{{2.3,1.e+3,2.0}} {
#             if (x > 10) {
#                 break ;
#             } else {
#                 x += 10 ;
#             }
#             x += idx % 20 + 5 ;
#             arr[idx][0] := x ;
#             print(x);
#         }
#     }

#     return x;
# };
                
# func main() {
#     var x int = Adding(10, 20);
#     print(x+3);

#     return 0;
# };"""
#         expect = "Program([InterfaceType(Calculator,[Prototype(Add,[IntType,IntType],IntType),Prototype(Subtract,[FloatType,FloatType,IntType],FloatType),Prototype(Reset,[],VoidType),Prototype(SayHello,[StringType],VoidType)]),FuncDecl(Adding,[ParDecl(a,IntType),ParDecl(b,IntType)],VoidType,Block([Assign(Id(arr),ArrayLiteral([Id(a),Id(b)],IntType,[[]])),VarDecl(x,IntType,IntLiteral(0)),For(Assign(Id(x),BinaryOp(IntLiteral(20),&&,Id(a))),BinaryOp(Id(x),<=,IntLiteral(5)),Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(1))),Block([ForEach(Id(idx),Id(_),ArrayLiteral([IntLiteral(2),IntLiteral(3)],FloatType,[[FloatLiteral(2.3),FloatLiteral(1000.0),FloatLiteral(2.0)]]),Block([If(BinaryOp(Id(x),>,IntLiteral(10)),Block([Break()]),Block([Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(10)))])),Assign(Id(x),BinaryOp(Id(x),+,BinaryOp(BinaryOp(Id(idx),%,IntLiteral(20)),+,IntLiteral(5)))),Assign(ArrayCell(Id(arr),[Id(idx),IntLiteral(0)]),Id(x)),FuncCall(print,[Id(x)])]))])),Return(Id(x))])),FuncDecl(main,[],VoidType,Block([VarDecl(x,IntType,FuncCall(Adding,[IntLiteral(10),IntLiteral(20)])),FuncCall(print,[BinaryOp(Id(x),+,IntLiteral(3))]),Return(IntLiteral(0))]))])"
#         self.assertTrue(TestAST.checkASTGen(input, expect, 399))

