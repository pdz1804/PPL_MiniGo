import unittest
from TestUtils import TestAST
from AST import *

# class ASTGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """func main() {};"""
#         expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,300))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """var x int ;"""
#         expect = str(Program([VarDecl("x",IntType(),None)]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
#     def test_call_without_parameter(self):
#         """More complex program"""
#         input = """func main () {}; var x int ;"""
#         expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,302))


class ASTGenSuite(unittest.TestCase):

    def test_100(self):
        input = """
            func quangphu() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU PDZ";
            };
"""
        expect = Program([FuncDecl("quangphu",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral('"2"')],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral('"THANKS YOU PDZ"'))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 200))

    
    
    def test_101(self):
        input = """ 
                    const x = 10
                    const y = foo( a(),b.a(2, 3) )
                """
        expect = Program([
            ConstDecl("x",None,IntLiteral(10)),
			ConstDecl("y",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 201))

    def test_102(self):
        input = "const y = 3.14;"
        expect = Program([
            ConstDecl("y",None,FloatLiteral(3.14))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 202))

    def test_103(self):
        input = "const a = a[1].b.c()[2].d.e();"
        expect = Program([
            ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 203))

    def test_104(self):
        input = "const name = \"John Doe\";"
        expect = Program([
            ConstDecl("name",None,StringLiteral('"John Doe"'))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 204))

    def test_105(self):
        input = "var age int = 25;"
        expect = Program([
            VarDecl("age",IntType(),IntLiteral(25))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 205))

    def test_106(self):
        input = "var counter int;"
        expect = Program([
            VarDecl("counter",IntType(), None)
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 206))

    def test_107(self):
        input = "const result = 5 + 3;"
        expect = Program([
            ConstDecl("result",None,BinaryOp("+", IntLiteral(5), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 207))

    def test_108(self):
        input = "const result = 6 * 7;"
        expect = Program([
            ConstDecl("result",None,BinaryOp("*", IntLiteral(6), IntLiteral(7)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 208))

    def test_109(self):
        input = "const check = true && false;"
        expect = Program([
            ConstDecl("check",None,BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 209))

    def test_110(self):
        input = "const isEqual = 5 == 5;"
        expect = Program([
            ConstDecl("isEqual",None,BinaryOp("==", IntLiteral(5), IntLiteral(5)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 210))

    def test_111(self):
        input = """
                type Person struct {
                    name string
                    age int
                }
                """
        expect = Program([
            StructType("Person",[("name",StringType()),("age",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 211))

    def test_112(self):
        input = """
                type Person struct { 
                    name string; 
                    age int; 
                    dob string
                }
                """
        expect = Program([
            StructType("Person",
                [
                    ("name",StringType()),
                    ("age",IntType()),
                    ("dob",StringType())
                ],
                []
            )
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 212))

    def test_113(self):
        input = """
                func greet(name string) { 
                    return "Hello " + name
                }
                
                func main() {
                    var name = "Quang Phu Dep Trai"
                    greet(name)
                }
                """
        expect = Program([
            FuncDecl("greet",[ParamDecl("name",StringType())],VoidType(),Block([
                Return(BinaryOp("+", StringLiteral('"Hello "'), Id("name")))
            ])),
			FuncDecl("main",[],VoidType(),Block([
                VarDecl("name", None,StringLiteral('"Quang Phu Dep Trai"')),
                FuncCall("greet",[Id("name")])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 213))

    def test_114(self):
        input = """
                func add(a int, b int) int { 
                    return a + b; 
                };
                """
        expect = Program([
            FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 214))

    def test_115(self):
        input = """
                func check(x int) { 
                    if (x > 0) { 
                        return "Greater than zero"
                    } 
                }
                
                func main() {
                    var num1 int;
                    num1 := 100
                    check(num1)
                }
                """
        expect = Program([
            FuncDecl("check",[ParamDecl("x",IntType())],VoidType(),Block([
                If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([
                    Return(StringLiteral('"Greater than zero"'))
                ]), None)
            ])),
			FuncDecl("main",[],VoidType(),Block([
                VarDecl("num1",IntType(), None),
                Assign(Id("num1"),IntLiteral(100)),
                FuncCall("check",[Id("num1")])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 215))

    def test_116(self):
        input = """
                func check(x int) { 
                    if (x > 0) { 
                        return; 
                    } else { 
                        return; 
                    } 
                }
                
                """
        expect = Program([
            FuncDecl("check",[ParamDecl("x",IntType())],VoidType(),Block([
                If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([
                    Return(None)
                ]), 
                Block([
                    Return(None)
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 216))

    def test_117(self):
        input = """
                func loop() { 
                    foo(1, 2);
                    a[2].foo(1,3);
                    for x < 10 { 
                        x += 1; 
                    } 
                }
                """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),
                MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)]),
                ForBasic(BinaryOp("<", Id("x"), IntLiteral(10)),Block([
                    Assign(Id("x"),BinaryOp("+", Id("x"), IntLiteral(1)))
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 217))

    def test_118(self):
        input = """
                func loop() { 
                    for i := 0; i < 10; i += 1 { 
                        print(i) 
                    } 
                }
                """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    FuncCall("print",[Id("i")])
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 218))

    def test_119(self):
        input = """
                func getValueDouble(num int) int { 
                    return num*2; 
                }
                """
        expect = Program([
            FuncDecl("getValueDouble",[ParamDecl("num",IntType())],IntType(),Block([
                Return(BinaryOp("*", Id("num"), IntLiteral(2)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 219))

    def test_120(self):
        input = """
                func main() { 
                    greet(); 
                }
                """
        expect = Program([
            FuncDecl("main",[],VoidType(),Block([
                FuncCall("greet",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 220))

    def test_121(self):
        input = """
                const value = (a + b) * (c - d) / e
                """
        expect = Program([
            ConstDecl("value",None,BinaryOp("/", BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))), Id("e")))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 221))

    def test_122(self):
        input = """const p = Person{ name: \"Alice\", age: 30 };"""
        expect = Program([
            ConstDecl("p",None,StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(30))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 222))

    def test_123(self):
        input = """
                func check(x int) { 
                    if (x > 0) { 
                        if (x < 10) { 
                            return; 
                        } 
                    } 
                }
                """
        expect = Program([
            FuncDecl("check",[ParamDecl("x",IntType())],VoidType(),Block([
                If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([
                    If(BinaryOp("<", Id("x"), IntLiteral(10)), Block([
                        Return(None)
                    ]), None)
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 223))

    def test_124(self):
        input = """
                func loop() { 
                    for i := 0; i < 10; i += 1 { 
                        if (i % 2 == 0) { 
                            continue; 
                        } 
                    } 
                    for i := 0; i < 10; i += 1 { 
                        if (i == 7) { 
                            break; 
                        } 
                    } 
                }
                """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), Block([
                        Continue()
                    ]), None)
                ])),
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    If(BinaryOp("==", Id("i"), IntLiteral(7)), Block([
                        Break()
                    ]), None)
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 224))

    def test_125(self):
        input = """
                type Car struct { 
                    haha string
                    hihi int
                    hoho C
                    
                }
                """
        expect = Program([
            StructType("Car",[
                ("haha",StringType()),
                ("hihi",IntType()),
                ("hoho",Id("C"))
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 225))

    def test_126(self):
        input = """
                func createCar() Car { 
                    return Car{}; 
                }
                """
        expect = Program([
            FuncDecl("createCar",[],Id("Car"),Block([
                Return(StructLiteral("Car",[]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 226))

    def test_127(self):
        input = "var matrix [3][3]int;"
        expect = Program([
            VarDecl("matrix",ArrayType([IntLiteral(3),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 227))

    def test_128(self):
        input = "var numbers [5]int = [5]int{1, 2, 3, 4, 5};"
        expect = Program([
            VarDecl("numbers",ArrayType([IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 228))

    def test_129(self):
        input = "const age = p.age;"
        expect = Program([
            ConstDecl("age",None,FieldAccess(Id("p"),"age"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 229))

    def test_130(self):
        input = """
                func main() { 
                    add(minus(add(5, 10))); 
                }
                """
        expect = Program([
            FuncDecl("main",[],VoidType(),Block([
                FuncCall("add",[FuncCall("minus",[FuncCall("add",[IntLiteral(5),IntLiteral(10)])])])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 230))

    def test_131(self):
        input = "const result = (a > b) && (c < d) || (e == f);"
        expect = Program([
            ConstDecl("result",None,BinaryOp("||", BinaryOp("&&", BinaryOp(">", Id("a"), Id("b")), BinaryOp("<", Id("c"), Id("d"))), BinaryOp("==", Id("e"), Id("f"))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 231))

    def test_132(self):
        input = """
                func nested() { 
                    for i := 0; i < 10; i += 1 { 
                        for j := 0; j < 5; j += 1 { 
                            print(i, j); 
                        } 
                    } 
                }
                """
        expect = Program([
            FuncDecl("nested",[],VoidType(),Block([
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<", Id("j"), IntLiteral(5)),Assign(Id("j"),BinaryOp("+", Id("j"), IntLiteral(1))),Block([
                        FuncCall("print",[Id("i"),Id("j")])
                    ]))
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 232))

    def test_133(self):
        input = """
                type House struct { rooms int; } 
                type City struct { houses [100]House; } 
                
                func build() { 
                    print("Phu Dep Trai")
                }
                """
        expect = Program([
            StructType("House",[("rooms",IntType())],[]),
			StructType("City",[("houses",ArrayType([IntLiteral(100)],Id("House")))],[]),
			FuncDecl("build",[],VoidType(),Block([
                FuncCall("print",[StringLiteral('"Phu Dep Trai"')])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 233))

    def test_134(self):
        input = """
                type Person struct { 
                    address Address
                    name string
                    dob string
                    familyMember [10]Person
                }
                """
        expect = Program([
            StructType("Person",[
                ("address",Id("Address")),
                ("name",StringType()),
                ("dob",StringType()),
                ("familyMember",ArrayType([IntLiteral(10)],Id("Person")))
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 234))

    def test_135(self):
        input = """
                type Car struct { 
                    model string; 
                    wheels int
                    yaer int
                }
                """
        expect = Program([
            StructType("Car",[
                ("model",StringType()),
                ("wheels",IntType()),
                ("yaer",IntType())
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 235))

    def test_136(self):
        input = """func add(a int, b int) { 
                        return a + b; 
                    };"""
        expect = Program([
            FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 236))

    def test_137(self):
        input = """func add(a int, b int) { 
                        return a - b; 
                        return;
                        return;
                    }
                    """
        expect = Program([
            FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([
                Return(BinaryOp("-", Id("a"), Id("b"))),
                Return(None),
                Return(None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 237))

    def test_138(self):
        input = """
                type Shape interface {
                    Area() float;
                    Perimeter() float;
                }
                """
        expect = Program([
            InterfaceType("Shape",[
                Prototype("Area",[],FloatType()),
                Prototype("Perimeter",[],FloatType())
            ])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 238))

    def test_139(self):
        input = """
                type Circle struct {
                    radius float;
                    
                }
                """
        expect = Program([
            StructType("Circle",[("radius",FloatType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 239))

    def test_140(self):
        input = """
            func test() {
                for i := 0; i < 5; i += 1 {
                    for j := 0; j < 3; j += 1 {
                        for k := 0; k < 2; k += 1 {
                            print(i, j, k);
                        }
                    }
                }
            }
        """
        expect = Program([
            FuncDecl("test",[],VoidType(),Block([
                ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(5)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<", Id("j"), IntLiteral(3)),Assign(Id("j"),BinaryOp("+", Id("j"), IntLiteral(1))),Block([
                        ForStep(Assign(Id("k"),IntLiteral(0)),BinaryOp("<", Id("k"), IntLiteral(2)),Assign(Id("k"),BinaryOp("+", Id("k"), IntLiteral(1))),Block([
                            FuncCall("print",[Id("i"),Id("j"),Id("k")])
                        ]))
                    ]))
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 240))

    def test_141(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2)
                a.foo();
                a[2].c.foo(foo(), 2)
            } 
                                     
            func main() {
                result := foo().bar().baz(5, 10).qux();
            }
        """
        expect = Program([
            FuncDecl("foo",[],VoidType(),Block([
                FuncCall("foo",[]),
                FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),
                MethCall(Id("a"),"foo",[]),
                MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])
            ])),
			FuncDecl("main",[],VoidType(),Block([
                Assign(Id("result"),MethCall(MethCall(MethCall(FuncCall("foo",[]),"bar",[]),"baz",[IntLiteral(5),IntLiteral(10)]),"qux",[]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 241))

    def test_142(self):
        input = """
            func getValues() [3]int {
                a["s"][foo()] := 1
                
                return [3]int{1, 2, 3};
            }
        """
        expect = Program([
            FuncDecl("getValues",[],ArrayType([IntLiteral(3)],IntType()),Block([
                Assign(ArrayCell(Id("a"),[StringLiteral('"s"'),FuncCall("foo",[])]),IntLiteral(1)),
                Return(ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 242))

    def test_143(self):
        input = """
            type Car struct {
                wheels int;
                quangphu string
            }
        """
        expect = Program([
            StructType("Car",[
                ("wheels",IntType()),
                ("quangphu",StringType())
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 243))

    def test_144(self):
        input = """
            func foo(){
                a[1 + 1] := [2][3]int{{1, 2, 3}, {4, 5, 6}}
                a[1][2][3] := [2]ID{STRUCT{}};
            }            
                            
            func test() {
                x := arr[2].foo();
            }
        """
        # expect = Program([
        #     FuncDecl("foo",[],VoidType(),Block([
        #         Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]])),
        #         Assign(ArrayCell(ArrayCell(ArrayCell(Id("a"),[IntLiteral(1)]),[IntLiteral(2)]),[IntLiteral(3)]),ArrayLiteral([IntLiteral(2)],Id("ID"),[StructLiteral("STRUCT",[])]))
        #     ])),
		# 	FuncDecl("test",[],VoidType(),Block([
        #         Assign(Id("x"),MethCall(ArrayCell(Id("arr"),[IntLiteral(2)]),"foo",[]))
        #     ]))
		# ])
        expect = Program([
            FuncDecl("foo",[],VoidType(),Block([
                Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]])),
                Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(2)],Id("ID"),[StructLiteral("STRUCT",[])]))
            ])),
			FuncDecl("test",[],VoidType(),Block([
                Assign(Id("x"),MethCall(ArrayCell(Id("arr"),[IntLiteral(2)]),"foo",[]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 244))

    def test_145(self):
        input = """
            func createPoint() Point {
                return Point{x: 10, y: 20};
            }
        """
        expect = Program([
            FuncDecl("createPoint",[],Id("Point"),Block([
                Return(StructLiteral("Point",[("x",IntLiteral(10)),("y",IntLiteral(20))]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 245))

    def test_146(self):
        input = """
            const result = (a > b) && ((c < d) || (e == f)) && !(g < h);
        """
        expect = Program([
            ConstDecl("result",None,BinaryOp("&&", BinaryOp("&&", BinaryOp(">", Id("a"), Id("b")), BinaryOp("||", BinaryOp("<", Id("c"), Id("d")), BinaryOp("==", Id("e"), Id("f")))), UnaryOp("!",BinaryOp("<", Id("g"), Id("h")))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 246))

    def test_147(self):
        input = """
            func calculate(x int, y int) int {
                return (x + y) * (x - y) / (x % y);
            }
        """
        expect = Program([
            FuncDecl("calculate",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([
                Return(BinaryOp("/", BinaryOp("*", BinaryOp("+", Id("x"), Id("y")), BinaryOp("-", Id("x"), Id("y"))), BinaryOp("%", Id("x"), Id("y"))))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 247))

    def test_148(self):
        input = """
            func invalid() { return 10; }
        """
        expect = Program([
            FuncDecl("invalid",[],VoidType(),Block([
                Return(IntLiteral(10))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 248))

    def test_149(self):
        input = """
            func test() {
                if (1) { print("Hello"); }
            }
        """
        expect = Program([
            FuncDecl("test",[],VoidType(),Block([
                If(IntLiteral(1), Block([
                    FuncCall("print",[StringLiteral('"Hello"')])
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 249))

    def test_150(self):
        input = """
            func getValue() string { 
                return "string"; 
            }
        """
        expect = Program([
            FuncDecl("getValue",[],StringType(),Block([
                Return(StringLiteral('"string"'))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 250))

    def test_151(self):
        input = """
            func add(a int, b int) int { 
                return a + b; 
            }
            
            func add(a float, b float) float { 
                return a + b; 
            }
        """
        expect = Program([
            FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ])),
			FuncDecl("add",[ParamDecl("a",FloatType()),ParamDecl("b",FloatType())],FloatType(),Block([
                Return(BinaryOp("+", Id("a"), Id("b")))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 251))

    def test_152(self):
        input = """
            type Car struct {
                brand string
                wheels int
                dateBuy string
            }
            func main() {
                car := Car{}.start().drive();
            }
        """
        expect = Program([
            StructType("Car",[
                ("brand",StringType()),
                ("wheels",IntType()),
                ("dateBuy",StringType())
            ],
            []),
			FuncDecl("main",[],VoidType(),Block([
                Assign(Id("car"),MethCall(MethCall(StructLiteral("Car",[]),"start",[]),"drive",[]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 252))

    def test_153(self):
        input = """
            type Vehicle struct {
                wheels int
            }
        """
        expect = Program([
            StructType("Vehicle",[
                ("wheels",IntType())
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 253))

    def test_154(self):
        input = """
            type Person struct {
                listFriends [100]int
            }
        """
        expect = Program([
            StructType("Person",[
                ("listFriends",ArrayType([IntLiteral(100)],IntType()))
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 254))

    def test_155(self):
        input = """
            type Node struct {
                value int;
                next Node;
            }
        """
        expect = Program([
            StructType("Node",[
                ("value",IntType()),
                ("next",Id("Node"))
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 255))

    def test_156(self):
        input = """
            func add(a int, b int) [100]int { 
                var list [100]int;
                var i = 0;
                for i < b {
                    if (i > a) {
                        list[i] := i
                        i += 1
                    } else {
                        break
                    }   
                }
                return list; 
            }
            """
        expect = Program([
            FuncDecl("add",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],ArrayType([IntLiteral(100)],IntType()),Block([
                VarDecl("list",ArrayType([IntLiteral(100)],IntType()), None),
                VarDecl("i", None,IntLiteral(0)),
                ForBasic(BinaryOp("<", Id("i"), Id("b")),Block([
                    If(BinaryOp(">", Id("i"), Id("a")), Block([
                        Assign(ArrayCell(Id("list"),[Id("i")]),Id("i")),
                        Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1)))
                    ]), 
                    Block([
                        Break()
                    ]))
                ])),
                Return(Id("list"))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 256))

    def test_157(self):
        input = """
            const result = (a > b) + ab;
        """
        expect = Program([
            ConstDecl("result",None,BinaryOp("+", BinaryOp(">", Id("a"), Id("b")), Id("ab")))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 257))

    def test_158(self):
        input = """
            const person = Person{name: "Alice", age: 25};
            var t = person.greet();
        """
        expect = Program([
            ConstDecl("person",None,StructLiteral("Person",[("name",StringLiteral('"Alice"')),("age",IntLiteral(25))])),
			VarDecl("t", None,MethCall(Id("person"),"greet",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 258))

    def test_159(self):
        input = """
            func inner() { 
                return
            } 
            
            func outer() {
                hehehe()
                hahaha()
                huhuhu()
            }
        """
        expect = Program([
            FuncDecl("inner",[],VoidType(),Block([
                Return(None)
            ])),
			FuncDecl("outer",[],VoidType(),Block([
                FuncCall("hehehe",[]),
                FuncCall("hahaha",[]),
                FuncCall("huhuhu",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 259))

    def test_160(self):
        input = """
            func getAge(p Person) int {
                return a[2].b[2].c.d.age;
            }
        """
        expect = Program([
            FuncDecl("getAge",[ParamDecl("p",Id("Person"))],IntType(),Block([
                Return(FieldAccess(FieldAccess(FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),[IntLiteral(2)]),"c"),"d"),"age"))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 260))

    def test_161(self):
        input = """
            func factorial(n int) int {
                if (n == 0) { return 1; }
                return n * factorial(n - 1);
            }
        """
        expect = Program([
            FuncDecl("factorial",[ParamDecl("n",IntType())],IntType(),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(IntLiteral(1))
                ]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial",[BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 261))

    def test_162(self):
        input = """
            type Company struct {
                name string;
                count int;
            }
        """
        expect = Program([
            StructType("Company",[
                ("name",StringType()),
                ("count",IntType())
            ],
            [])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 262))

    def test_163(self):
        input = """
            type Node struct {
                value int;
            }
        """
        expect = Program([
            StructType("Node",[
                ("value",IntType())
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 263))

    def test_164(self):
        input = """
            func compute(a int, b int) int {
                return (a + (b * (a / b) - a) % b) + 5;
            }
        """
        expect = Program([
            FuncDecl("compute",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([
                Return(BinaryOp("+", BinaryOp("+", Id("a"), BinaryOp("%", BinaryOp("-", BinaryOp("*", Id("b"), BinaryOp("/", Id("a"), Id("b"))), Id("a")), Id("b"))), IntLiteral(5)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 264))

    def test_165(self):
        input = """
            type Person struct {
                name string;
                age int
            }
        """
        expect = Program([
            StructType("Person",[
                ("name",StringType()),
                ("age",IntType())
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 265))

    def test_166(self):
        input = """
            func isEven(n int) bool {
                if (n == 0) { return true; }
                return isOdd(n - 1);
            }
        """
        expect = Program([
            FuncDecl("isEven",[ParamDecl("n",IntType())],Id("bool"),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(BooleanLiteral(True))
                ]), None),
                Return(FuncCall("isOdd",[BinaryOp("-", Id("n"), IntLiteral(1))]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 266))

    def test_167(self):
        input = """
            func isEven(n int) bool {
                if (n == 0) { return true; }
                return isOdd(n - 1);
            }
            
            func isOdd(n int) bool {
                if (n == 0) { return false; }
                return isEven(n - 1);
            }
        """
        expect = Program([
            FuncDecl("isEven",[ParamDecl("n",IntType())],Id("bool"),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(BooleanLiteral(True))
                ]), None),
                Return(FuncCall("isOdd",[BinaryOp("-", Id("n"), IntLiteral(1))]))
            ])),
			FuncDecl("isOdd",[ParamDecl("n",IntType())],Id("bool"),Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([
                    Return(BooleanLiteral(False))
                ]), None),
                Return(FuncCall("isEven",[BinaryOp("-", Id("n"), IntLiteral(1))]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 267))

    def test_168(self):
        input = """
            func loop() {
                for true { 
                    print("Running"); 
                    break; 
                }
            }
        """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForBasic(BooleanLiteral(True),Block([
                    FuncCall("print",[StringLiteral('"Running"')]),
                    Break()
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 268))

    def test_169(self):
        input = """
            func checkDepth(n int) {
                if (n > 0) { 
                    if (n > 1) { 
                        if (n > 2) { 
                            if (n > 3) { 
                                print("larger than 3")
                                return; 
                            } 
                            print("larger than 2")
                        } 
                        print("larger than 1")
                    } 
                    print("larger than 0")
                }
            }
        """
        expect = Program([
            FuncDecl("checkDepth",[ParamDecl("n",IntType())],VoidType(),Block([
                If(BinaryOp(">", Id("n"), IntLiteral(0)), Block([
                    If(BinaryOp(">", Id("n"), IntLiteral(1)), Block([
                        If(BinaryOp(">", Id("n"), IntLiteral(2)), Block([
                            If(BinaryOp(">", Id("n"), IntLiteral(3)), Block([
                                FuncCall("print",[StringLiteral('"larger than 3"')]),
                                Return(None)
                            ]), None),
                            FuncCall("print",[StringLiteral('"larger than 2"')])
                        ]), None),
                        FuncCall("print",[StringLiteral('"larger than 1"')])
                    ]), None),
                    FuncCall("print",[StringLiteral('"larger than 0"')])
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 269))

    def test_170(self):
        input = """
            func loop() {
                for false { 
                    print("Running"); 
                    break; 
                }
            }
        """
        expect = Program([
            FuncDecl("loop",[],VoidType(),Block([
                ForBasic(BooleanLiteral(False),Block([
                    FuncCall("print",[StringLiteral('"Running"')]),
                    Break()
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 270))

    def test_171(self):
        input = """
            func quangphu(x int, y int) int { 
                return x + y; 
            };
        """
        expect = Program([
            FuncDecl("quangphu",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([
                Return(BinaryOp("+", Id("x"), Id("y")))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 271))

    def test_172(self):
        input = """
            func phuquang() {
                a += 1;
                b -= 2
                c *= 3
            }
        """
        expect = Program([
            FuncDecl("phuquang",[],VoidType(),Block([
                Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
                Assign(Id("b"),BinaryOp("-", Id("b"), IntLiteral(2))),
                Assign(Id("c"),BinaryOp("*", Id("c"), IntLiteral(3)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 272))

    def test_173(self):
        input = """
            func phuquang() {
                a += 1;
            }
        """
        expect = Program([
            FuncDecl("phuquang",[],VoidType(),Block([
                Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 273))

    def test_174(self):
        input = """
            func quangphu() {
                break;
                continue;
            }
        """
        expect = Program([
            FuncDecl("quangphu",[],VoidType(),Block([
                Break(),
                Continue()
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 274))

    def test_175(self):
        input = """const QuangPhu = foo( a(),b.a(2, 3) ); """
        expect = Program([
            ConstDecl("QuangPhu",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 275))

    def test_176(self):
        input = """
            func getPeople() [2]Person {
                return [2]Person{Person{name: "Alice"}, Person{name: "Bob"}};
            }
        """
        expect = Program([
            FuncDecl("getPeople",[],ArrayType([IntLiteral(2)],Id("Person")),Block([
                Return(ArrayLiteral([IntLiteral(2)],Id("Person"),[StructLiteral("Person",[("name",StringLiteral('"Alice"'))]),StructLiteral("Person",[("name",StringLiteral('"Bob"'))])]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 276))

    def test_177(self):
        input = """
            type Calculator struct {
                num1 int 
                num2 int
                op string 
                
            }
        """
        expect = Program([
            StructType("Calculator",[
                ("num1",IntType()),
                ("num2",IntType()),
                ("op",StringType())
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 277))

    def test_178(self):
        input = """
            type Team struct {
                members [5]Person;
            }
        """
        expect = Program([
            StructType("Team",[
                ("members",ArrayType([IntLiteral(5)],Id("Person")))
            ],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 278))

    def test_179(self):
        input = """
            type Address struct {
                city string;
            }
            type Person struct {
                addr Address;
            }
            var cityName string = Person{}.addr.city;
        """
        expect = Program([
            StructType("Address",[
                ("city",StringType())
            ],[]),
			StructType("Person",[
                ("addr",Id("Address"))
            ],[]),
			VarDecl("cityName",StringType(),FieldAccess(FieldAccess(StructLiteral("Person",[]),"addr"),"city"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 279))

    def test_180(self):
        input = """
            const team = Team{}.members[2].name;
        """
        expect = Program([
            ConstDecl("team",None,FieldAccess(ArrayCell(FieldAccess(StructLiteral("Team",[]),"members"),[IntLiteral(2)]),"name"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 280))

    def test_181(self):
        input = """
            func broken() {
                var x int = 10;
            }
        """
        expect = Program([
            FuncDecl("broken",[],VoidType(),Block([
                VarDecl("x",IntType(),IntLiteral(10))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 281))

    def test_182(self):
        input = """
            const result = a * 5 + 3;
        """
        expect = Program([
            ConstDecl("result",None,BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(5)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 282))

    def test_183(self):
        input = """
            func deepNest() {
                if (a > b) {
                    if (b > c) {
                        if (c > d) {
                            if (d > e) {
                                if (e > f) {
                                    if (f > g) {
                                        if (g > h) {
                                            if (h > i) {
                                                if (i > j) {
                                                    print("Too deep!");
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        expect = Program([
            FuncDecl("deepNest",[],VoidType(),Block([
                If(BinaryOp(">", Id("a"), Id("b")), Block([
                    If(BinaryOp(">", Id("b"), Id("c")), Block([
                        If(BinaryOp(">", Id("c"), Id("d")), Block([
                            If(BinaryOp(">", Id("d"), Id("e")), Block([
                                If(BinaryOp(">", Id("e"), Id("f")), Block([
                                    If(BinaryOp(">", Id("f"), Id("g")), Block([
                                        If(BinaryOp(">", Id("g"), Id("h")), Block([
                                            If(BinaryOp(">", Id("h"), Id("i")), Block([
                                                If(BinaryOp(">", Id("i"), Id("j")), Block([
                                                    FuncCall("print",[StringLiteral('"Too deep!"')])
                                                ]), None)
                                            ]), None)
                                        ]), None)
                                    ]), None)
                                ]), None)
                            ]), None)
                        ]), None)
                    ]), None)
                ]), None)
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 283))

    def test_184(self):
        input = """
            func sayHello() { return "Hello"; }
        """
        expect = Program([
            FuncDecl("sayHello",[],VoidType(),Block([
                Return(StringLiteral('"Hello"'))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 284))

    def test_185(self):
        input = """
            func phudepzai() {
                foo(1, 2);
                a[2].foo(1,3);
            }
        """
        expect = Program([
            FuncDecl("phudepzai",[],VoidType(),Block([
                FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),
                MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 285))

    def test_186(self):
        input = """
            func infiniteRecursion() {
                infiniteRecursion();
            }
        """
        expect = Program([
            FuncDecl("infiniteRecursion",[],VoidType(),Block([
                FuncCall("infiniteRecursion",[])
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 286))

    def test_187(self):
        input = """
            const value = 1 + 2 - 3 * 4 / 5 % 6 + 7 - 8 * 9 / 10 % 11;
        """
        expect = Program([
            ConstDecl("value",None,BinaryOp("-", BinaryOp("+", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(3), IntLiteral(4)), IntLiteral(5)), IntLiteral(6))), IntLiteral(7)), BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(8), IntLiteral(9)), IntLiteral(10)), IntLiteral(11))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 287))

    def test_188(self):
        input = """
            const x = 10
            const y = 20;
        """
        expect = Program([
            ConstDecl("x",None,IntLiteral(10)),
			ConstDecl("y",None,IntLiteral(20))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 288))

    def test_189(self):
        input = """
            func phudepzai() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
        """
        expect = Program([
            FuncDecl("phudepzai",[],VoidType(),Block([
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([
                    Assign(Id("a"),IntLiteral(1))
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 289))

    def test_190(self):
        input = """
            func phuquang() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
        """
        expect = Program([
            FuncDecl("phuquang",[],VoidType(),Block([
                ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([
                    Return(None)
                ])),
                ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([
                    Return(None)
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 290))

    def test_191(self):
        input = """
            func quangphu() {
                for index, value := range array[2] {return;}
            }
        """
        expect = Program([
            FuncDecl("quangphu",[],VoidType(),Block([
                ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([
                    Return(None)
                ]))
            ]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 291))

    def test_192(self):
        input = """
            const a = 1 && 2 || 3;
        """
        expect = Program([
            ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 292))

    def test_193(self):
        input = """
            const a = ID{a: [1]int{1}};
        """
        expect = Program([
            ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 293))

    def test_194(self):
        input = """
            const a = a[1 + 2];
        """
        expect = Program([
            ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 294))

    def test_195(self):
        input = """
            const a = a.b().c().d();
        """
        expect = Program([
            ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 295))

    def test_196(self):
        input = """
            const a = a[1].b.c()[2].d.e();
        """
        expect = Program([
            ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 296))
    
    def test_197(self):
        input = """
            const a = f() + f(1 + 2, 3.);
        """
        expect = Program([
            ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral(3.0)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 297))

    def test_198(self):
        input = """
            const a = foo()[2];
        """
        expect = Program([
            ConstDecl("a",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 298))

    def test_199(self):
        input = """
            const deepCalc = ((((((((10 + 5) * 2) / 3) % 4) - 1) + 6) * 7));
        """
        expect = Program([
            ConstDecl("deepCalc",None,BinaryOp("*", BinaryOp("+", BinaryOp("-", BinaryOp("%", BinaryOp("/", BinaryOp("*", BinaryOp("+", IntLiteral(10), IntLiteral(5)), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(1)), IntLiteral(6)), IntLiteral(7)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 299))

    def test_200(self):
        input = """
            var a [2][3]int;
        """
        expect = Program([
            VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 300))
    
