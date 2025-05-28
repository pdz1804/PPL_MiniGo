# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

import unittest
from TestUtils import TestChecker
from AST import *

# class CheckSuite(unittest.TestCase):
    
#     def test_0001(self):
#         input = """
#             func foo(a float) float {
#                 return a;
#             }
            
#             func main() {
#                 t := foo(1);
#             }
            
#             type Meow struct {
#                 a int;
#                 b Meow1
#             }
            
#             type Meow1 struct {
#                 c float;
#             } 
            
#             const a = Meow{a: 1, b: Meow1{c: 2.1}};
#             var t = foo( a.b.c );
#         """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input,expect,403))
    
#     def test_0001(self):
#         input = """
#             func QuangPhu (b int) {
#                 for var a = 1; a < 1; c += 1 {
#                     const cd = 2;
#                 }
#             }
#         """
#         expect = """Undeclared Identifier: c\n"""
#         self.assertTrue(TestChecker.test(input,expect,401))
    
#     def test_0002(self):
#         input = """
#             func (v PHUDZ) foo (a, b int) {
#                 const v = 1;
#                 const a = 1;
#             }

#             type PHUDZ struct {
#                 QuangPhu int;
#             }

#             func (v VO) foo () {
#                 const a = 1;
#             }

#             type VO struct {
#                 QuangPhu int;
#             }

#             func (v VO) foo (v, b int) {
#                 const a = 1;
#                 const v = 2
#             }
#         """
#         expect = """Redeclared Method: foo\n"""
#         self.assertTrue(TestChecker.test(input,expect,402))
    
#     def test_0003(self):
#         input = """
#             func foo() [3]float {
#                 var a float;
#                 a := 1;
#                 a := 2;
#             }
            
#             func QuangPhu (b int) [3]float {
#                 for var a = 1; a < 1; cd += 1 {
#                     const cd = 2 + 10000*123 - 12/4*2%3;
#                 }
#                 return foo()
#             }
#         """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input,expect,403))
    
#     def test_0004(self):
#         input = """
#             const a = 123.345
#             var b [a] float;
#         """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input,expect,404))
    
import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
        var zPhuDZz = 1; 
        var zPhuDZz = 2;
        """
        input = Program([VarDecl("zPhuDZz", None,IntLiteral(1)),VarDecl("zPhuDZz", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: zPhuDZz\n", inspect.stack()[0].function))

    def test_002(self):
        """
        var zPhuDZz = 1; 
        const zPhuDZz = 2;
        """
        input = Program([VarDecl("zPhuDZz", None,IntLiteral(1)),ConstDecl("zPhuDZz",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: zPhuDZz\n", inspect.stack()[0].function))

    def test_003(self):
        """
        const zPhuDZz = 1; 
        var zPhuDZz = 2;
        """
        input = Program([ConstDecl("zPhuDZz",None,IntLiteral(1)),VarDecl("zPhuDZz", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: zPhuDZz\n", inspect.stack()[0].function))

    def test_004(self):
        """
        const zPhuDZz = 1; 
        func zPhuDZz () {return;}
        """
        input = Program([ConstDecl("zPhuDZz",None,IntLiteral(1)),FuncDecl("zPhuDZz",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: zPhuDZz\n", inspect.stack()[0].function))

    def test_005(self):
        """ 
        func zPhuDZz () {return;}
        var zPhuDZz = 1;
        """
        input = Program([FuncDecl("zPhuDZz",[],VoidType(),Block([Return(None)])),VarDecl("zPhuDZz", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: zPhuDZz\n", inspect.stack()[0].function))

    def test_006(self):
        """ 
        var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", inspect.stack()[0].function))

    def test_007(self):
        """ 
        type  QuangPhu struct {
            QuangPhu int;
        }
        type PHUDZ struct {
            QuangPhu string;
            PHUDZ int;
            PHUDZ float;
        }
        """
        input = Program([StructType("QuangPhu",[("QuangPhu",IntType())],[]),StructType("PHUDZ",[("QuangPhu",StringType()),("PHUDZ",IntType()),("PHUDZ",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: PHUDZ\n", inspect.stack()[0].function))

    def test_008(self):
        """ 
        func (v PHUDZ) putIntLn () {return;}
        func (v PHUDZ) getInt () {return;}
        func (v PHUDZ) getInt () {return;}
        type PHUDZ struct {
            QuangPhu int;
        }
        """
        input = Program([MethodDecl("v",Id("PHUDZ"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("PHUDZ"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("PHUDZ"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("PHUDZ",[("QuangPhu",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", inspect.stack()[0].function))

    def test_009(self):
        """ 
        type zPhuDZz interface {
            zPhuDZz ();
            zPhuDZz (a int);
        }
        """
        input = Program([InterfaceType("zPhuDZz",[Prototype("zPhuDZz",[],VoidType()),Prototype("zPhuDZz",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: zPhuDZz\n", inspect.stack()[0].function))

    def test_010(self):
        """ 
        func QuangPhu (a, a int) {return;}
        """
        input = Program([FuncDecl("QuangPhu",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", inspect.stack()[0].function))

    def test_011(self):
        """ 
        func QuangPhu (b int) {
            var b = 1;
            var a = 1;
            const a = 1;
        }
        """
        input = Program([FuncDecl("QuangPhu",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))

    def test_012(self):
        """ 
        func QuangPhu (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("QuangPhu",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))

    def test_013(self):
        """ 
        var a = 1;
        var b = a;
        var c = d;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d\n", inspect.stack()[0].function))

    def test_014(self):
        """ 
        func QuangPhu () int {return 1;}

        fun foo () {
            var b = QuangPhu();
            foo_votine();
            return;
        }
        """
        input = Program([FuncDecl("QuangPhu",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("QuangPhu",[])),FuncCall("foo_votine",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine\n", inspect.stack()[0].function))

    def test_015(self):
        """ 
        type PHUDZ struct {
            QuangPhu int;
        }

        func (v PHUDZ) getInt () {
            const c = v.QuangPhu;
            var d = v.quangphiu;
        }
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("PHUDZ"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"QuangPhu")),VarDecl("d", None,FieldAccess(Id("v"),"quangphiu"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: quangphiu\n", inspect.stack()[0].function))

    def test_016(self):
        """ 
        type PHUDZ struct {
            QuangPhu int;
        }

        func (v PHUDZ) getInt () {
            v.getInt ();
            v.putInt ();
        }
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("PHUDZ"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt\n", inspect.stack()[0].function))
    
    def test_017(self):
        """ 
        type PHUDZ struct {QuangPhu int;}
        type PHUDZ interface {zPhuDZz ();}
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),InterfaceType("PHUDZ",[Prototype("zPhuDZz",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: PHUDZ\n", inspect.stack()[0].function))
        
    def test_018(self):
        """ 
        type PHUDZ struct {QuangPhu int;}
        type PHUDZ struct {v int;}
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),StructType("PHUDZ",[("v",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: PHUDZ\n", inspect.stack()[0].function))
        
    def test_019(self):
        """ 
        type PHUDZ struct {
            QuangPhu int;
        }
        func (v PHUDZ) foo (a, b int) {return;}
        func foo (a, a int) {return;}
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", inspect.stack()[0].function))
        
        
    def test_020(self): # 44
        """
        type PHUDZ struct {
            QuangPhu int;
        }
        func (v PHUDZ) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("PHUDZ",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        # self.assertTrue(TestChecker.test(input, "Redeclared Parameter: v\n", inspect.stack()[0].function))
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    def test_021(self): # 50
        """
        func (v PHUDZ) foo (a, b int) {
            const v = 1;
            const a = 1;
        }

        type PHUDZ struct {
            QuangPhu int;
        }

        func (v VO) foo () {
            const a = 1;
        }

        type VO struct {
            QuangPhu int;
        }

        func (v VO) foo (a, b int) {
            const a = 1;
        }
        """
        input = Program([MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("v",None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))),StructType("PHUDZ",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("VO"),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))]))),StructType("VO",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("VO"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo\n", inspect.stack()[0].function))
    
    def test_022(self): # 51
        """
        const a = 2;
        func foo () {
            const a = 1;
            for var a = 1; a < 1; b += 2 {
                const b = 1;
            }
        }
        """
        input = Program([
            ConstDecl("a", None, IntLiteral(2)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(1)),
                ForStep(
                    VarDecl("a", None, IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(1)),
                    Assign(Id("b"), BinaryOp("+", Id("b"), IntLiteral(2))),
                    Block([ConstDecl("b", None, IntLiteral(1))])
                )
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: b\n""", inspect.stack()[0].function))
    
    def test_023(self): # 52
        """
        const a = 2;
        func foo () {
            const a = 1;
            for a < 1 {
                const a = 1;
                for a < 1 {
                    const a = 1;
                    const b = 1;
                }
                const b = 1;
                var a = 1;
            }
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)),Block([ConstDecl("a",None,IntLiteral(1)),ConstDecl("b",None,IntLiteral(1))])),ConstDecl("b",None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", inspect.stack()[0].function))
    
    def test_024(self):
        """ 
        var v PHUDZ;
        const b = v.b;        
        type PHUDZ struct {
            a int;
            b int;
            c int;
        }
        const a = v.a;
        const e = v.e;
        """
        input = Program([VarDecl("v",Id("PHUDZ"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("PHUDZ",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", inspect.stack()[0].function))
        
    def test_025(self):
        """ 
        var v PHUDZ;
        func foo ()  {
            var x = v;
            const a = x.a;
            const e = x.e;
        }
        type PHUDZ struct {
            a int;
            b int;
            c int;
        }
        """
        input = Program([VarDecl("v",Id("PHUDZ"), None),
			FuncDecl("foo",[],VoidType(),Block([VarDecl("x", None,Id("v")),ConstDecl("a",None,FieldAccess(Id("x"),"a")),ConstDecl("e",None,FieldAccess(Id("x"),"e"))])),
			StructType("PHUDZ",[("a",IntType()),("b",IntType()),("c",IntType())],[])
		])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", inspect.stack()[0].function))
        
    def test_026(self): # 53
        input = """
        func foo () {
            const a = 1;
            var b int
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    
    def test_027(self): # 61
        """
        var a = foo();
        func foo () int {
            var a =  koo();
            var c = getInt();
            putInt(c);
            putIntLn(c);
            return 1;
        }
        var d = foo();
        func koo () int {
            var a =  foo ();
            return 1;
        }
        """
        input = Program([VarDecl("a", None,FuncCall("foo",[])),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,FuncCall("koo",[])),VarDecl("c", None,FuncCall("getInt",[])),FuncCall("putInt",[Id("c")]),FuncCall("putIntLn",[Id("c")]),Return(IntLiteral(1))])),VarDecl("d", None,FuncCall("foo",[])),FuncDecl("koo",[],IntType(),Block([VarDecl("a", None,FuncCall("foo",[])),Return(IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
                         
    def test_028(self): # 69
        """
        var v PHUDZ;       
        type PHUDZ struct {
            a int;
        } 
        func (v PHUDZ) foo() int {return 1;}
        func (b PHUDZ) koo() {b.koo();}
        func foo() {
            const b = v.foo(); 
            v.koo(); 
            const d = v.zoo();
        }
        """
        input = Program([VarDecl("v",Id("PHUDZ"), None),StructType("PHUDZ",[("a",IntType())],[]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("PHUDZ"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("v"),"foo",[])),MethCall(Id("v"),"koo",[]),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: zoo\n", inspect.stack()[0].function))
                 
    def test_029(self): # 49
        """
        func (v PHUDZ) foo (a, b int) {
            var a = 1;
        }

        type PHUDZ struct {
            QuangPhu int;
        }

        type VO struct {
            QuangPhu int;
        }

        func (v VO) foo (a, b int) {
            var a = 1;
        }
        """
        input = Program([MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),StructType("PHUDZ",[("QuangPhu",IntType())],[]),StructType("VO",[("QuangPhu",IntType())],[]),MethodDecl("v",Id("VO"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_030(self):
        """     
        func foo() int {return 1;}
        func nqpdpu() int {
            return nqpdpu();
            foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("nqpdpu",[],IntType(),Block([Return(FuncCall("nqpdpu",[])),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])\n", inspect.stack()[0].function))
        
    def test_031(self):
        """
        type PHUDZ struct {v int;}
        var v PHUDZ;
        func foo(){
            for 1 {
                var a int = 1.2;
            }
        }
        """
        input = Program([StructType("PHUDZ",[("v",IntType())],[]),VarDecl("v",Id("PHUDZ"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n", inspect.stack()[0].function))  

    def test_032(self):
        """
        func foo(){
            var v int;
            const x = v;
            var k float = x;
            var y boolean = x;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("v",IntType(), None),ConstDecl("x",None,Id("v")),VarDecl("k",FloatType(),Id("x")),VarDecl("y",BoolType(),Id("x"))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(y,BoolType,Id(x))\n", inspect.stack()[0].function)) 

    def test_033(self):
        """
        var a int = 1 % 2;
        var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n", inspect.stack()[0].function)) 

    def test_034(self):
        """
        func foo() int {return 1;}
        func  nqpdpu() int {
            return nqpdpu();
            foo();
        }
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),MethodDecl("s",Id("S1"),FuncDecl("vo",[],VoidType(),Block([Return(None)]))),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],VoidType(),Block([MethCall(Id("s"),"nqpdpu",[]),VarDecl("a", None,MethCall(Id("s"),"vo",[]))])))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(s),vo,[])\n", inspect.stack()[0].function))
        
    def test_035(self):
        """          
        type S1 struct {nqpdpu int;}
        type S2 struct {nqpdpu int;}
        var v S1;
        const x = v;
        var z S1 = x;
        var k S2 = x;
        """
        input = Program([StructType("S1",[("nqpdpu",IntType())],[]),StructType("S2",[("nqpdpu",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n", inspect.stack()[0].function))
        
    def test_036(self):
        """
        type S1 struct {nqpdpu1 int;}
        type S2 struct {nqpdpu int;}
        type I1 interface {nqpdpu();}
        type I2 interface {nqpdpu();}

        func (s S1) nqpdpu() {return;}

        var a S1;
        var b S2;
        var c I1 = a;
        var d I2 = b;
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),StructType("S2",[("nqpdpu",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[],VoidType())]),InterfaceType("I2",[Prototype("nqpdpu",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(b))\n", inspect.stack()[0].function))

    def test_037(self):
        """
        type S1 struct {nqpdpu1 int;}
        type S2 struct {nqpdpu int;}
        type I1 interface {nqpdpu(e, e int) S1;}
        type I2 interface {nqpdpu(a int) S1;}

        func (s S1) nqpdpu(a, b int) S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),StructType("S2",[("nqpdpu",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("nqpdpu",[IntType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n", inspect.stack()[0].function))

    def test_038(self):
        """
        type S1 struct {nqpdpu1 int;}
        type S2 struct {nqpdpu int;}
        type I1 interface {nqpdpu(e, e int) S1;}
        type I2 interface {nqpdpu(a int, b float) S1;}

        func (s S1) nqpdpu(a, b int) S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),StructType("S2",[("nqpdpu",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("nqpdpu",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n", inspect.stack()[0].function))

    def test_039(self):
        """          
                
        type S1 struct {nqpdpu1 int;}
        type S2 struct {nqpdpu int;}
        type I1 interface {nqpdpu() S1;}
        type I2 interface {nqpdpu() S2;}

        func (s S1) nqpdpu() S1 {return s;}

        var a S1;
        var c I1 = a;
        var d I2 = a;
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),StructType("S2",[("nqpdpu",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[],Id("S1"))]),InterfaceType("I2",[Prototype("nqpdpu",[],Id("S2"))]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,Id(I2),Id(a))\n", inspect.stack()[0].function))
        
    def test_040(self):
        """
        func foo(){
            if (true) {
                var a float = 1.2;
            } else {
                var a int = 1.2;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(BooleanLiteral(True), Block([VarDecl("a",FloatType(),FloatLiteral(1.2))]), Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n", inspect.stack()[0].function))

    def test_041(self):
        """ 
        type PHUDZ struct {v int;}
        var v PHUDZ;
        func foo(){
            for 1 {
                var a int = 1.2;
            }
        }
        """
        input = Program([StructType("PHUDZ",[("v",IntType())],[]),VarDecl("v",Id("PHUDZ"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n", inspect.stack()[0].function))

    def test_042(self):
        """ 
        type S1 struct {v int; t int;}

        var a = S1 {v : 1, t: 2}
        var b S1 = a;
        var c int = b;
        """
        input = Program([StructType("S1",[("v",IntType()),("t",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",IntLiteral(1)),("t",IntLiteral(2))])),VarDecl("b",Id("S1"),Id("a")),VarDecl("c",IntType(),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,IntType,Id(b))\n", inspect.stack()[0].function))

    def test_043(self): # 97
        """ 
        var a = [2] int {1, 2}
        var c [3] float = a
        
        """
        input = Program([VarDecl("a", None, ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(FloatType,[IntLiteral(3)]),Id(a))\n", inspect.stack()[0].function))

    def test_044(self): # 77
        """ 
        type I1 interface {nqpdpu();}
        type I2 interface {nqpdpu();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x; // sai o day
        """
        input = Program([InterfaceType("I1",[Prototype("nqpdpu",[],VoidType())]),InterfaceType("I2",[Prototype("nqpdpu",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(I2),Id(x))\n", inspect.stack()[0].function))

    def test_045(self): # 87
        """ 
        func foo(){
            if (1) {
                var a float = 1.2;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([If(IntLiteral(1), Block([VarDecl("a",FloatType(),FloatLiteral(1.2))]), None)]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: If(IntLiteral(1),Block([VarDecl(a,FloatType,FloatLiteral(1.2))]))\n", inspect.stack()[0].function))

    def test_046(self):
        """          
        var v int = 1.2;
        """
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.2))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n", inspect.stack()[0].function))

    def test_047(self): 
        """ 
        var a = [2] int {1, 2}
        var c [3] int = a // error [3] int != [2] int
        
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n", inspect.stack()[0].function))
    
    def test_048(self): # 102
        """ 
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b; // error [2] int != [3] int
        var d [1] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n", inspect.stack()[0].function))

    def test_049(self): # 107
        """ 
        type S1 struct {nqpdpu int;}
        type I1 interface {nqpdpu();}
        var a I1;
        var c I1 = nil;
        var d S1 = nil;
        func foo() {
            c := a;
            a := nil;
        }
        var e int = nil;
        """
        input = Program([StructType("S1",[("nqpdpu",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,IntType,Nil)\n", inspect.stack()[0].function))

    def test_050(self): # 124
        input = """ 
        func foo(){
            var arr [2] int;
            var a int; var b int;
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,StringType,Id(a))\n", inspect.stack()[0].function))

    def test_051(self): # 126
        input = """ 
        func foo(){
            var arr [2][3] int;
            var a int; var b [3]int;
            for a, b := range arr {
                var c int = a;
                var d [2]int = b;
                var e [2]string = a;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n", inspect.stack()[0].function))

    def test_052(self):
        """               
        func foo(){
            return
        }
        func foo1() int{
            return 1
        }
        func foo2() float{
            return 2
        }      
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo1",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo2",[],FloatType(),Block([Return(IntLiteral(2))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(IntLiteral(2))\n", inspect.stack()[0].function))
        
    def test_053(self):
        """               
        type S1 struct {v int;}
        var a = S1 {v :  z}
        """
        input = Program([StructType("S1",[("v",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",Id("z"))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: z\n", inspect.stack()[0].function))
        
    def test_054(self):
        """               
        type S1 struct {v int; t int;}
        var a = S1 {v : 1, t: 2}
        var b S1 = a;
        var c int = b;
        """
        input = Program([StructType("S1",[("v",IntType()),("t",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",IntLiteral(1)),("t",IntLiteral(2))])),VarDecl("b",Id("S1"),Id("a")),VarDecl("c",IntType(),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,IntType,Id(b))\n", inspect.stack()[0].function))

    def test_055(self):
        """               
        type S1 struct {v int; x S1;}
        var b S1;
        var c = b.x.v;
        var d = c.x;
        """
        input = Program([StructType("S1",[("v",IntType()),("x",Id("S1"))],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"v")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FieldAccess(Id(c),x)\n", inspect.stack()[0].function))

    def test_056(self):
        """               
        var a = -1;
        var b = -1.2;
        var c = - true;
        """
        input = Program([VarDecl("a", None,UnaryOp("-",IntLiteral(1))),VarDecl("b", None,UnaryOp("-",FloatLiteral(1.2))),VarDecl("c", None,UnaryOp("-",BooleanLiteral(True)))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n", inspect.stack()[0].function))
        
    def test_057(self):
        input = """               
        func foo(){
            var arr [2] int;
            var a int; var b int;
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,StringType,Id(a))\n", inspect.stack()[0].function))
        
    def test_058(self):
        """               
        type S1 struct {nqpdpu1 int;}
        type I1 interface {nqpdpu() int;}
        func (s S1) nqpdpu() int {return 1;}

        var i I1;
        var s S1;
        var a int = i.nqpdpu();
        var b int = s.nqpdpu();
        var c int = a.nqpdpu();
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("i",Id("I1"), None),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("i"),"nqpdpu",[])),VarDecl("b",IntType(),MethCall(Id("s"),"nqpdpu",[])),VarDecl("c",IntType(),MethCall(Id("a"),"nqpdpu",[]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(a),nqpdpu,[])\n", inspect.stack()[0].function))
        
    def test_059(self):
        """               
        type Person struct {
            name string ;
            age int ;
        }
        func  nqpdpu()  {
            var person = Person{name: "Alice", age: 30}
            person.name := "John";
            person.age := 30;
            putStringLn(person.name)
            putStringLn(person.Greet())
        }
        func (p Person) Greet() string {
            return "Hello, " + p.name
        }
        """
        input = Program([
            StructType("Person", [("name", StringType()), ("age", IntType())], []),
            FuncDecl("nqpdpu", [], VoidType(), Block([
                VarDecl("person", None, StructLiteral("Person", [("name", StringLiteral("Alice")), ("age", IntLiteral(30))])),
                Assign(FieldAccess(Id("person"), "name"), StringLiteral("John")),
                Assign(FieldAccess(Id("person"), "age"), IntLiteral(30)),
                FuncCall("putStringLn", [FieldAccess(Id("person"), "name")]),
                FuncCall("putStringLn", [MethCall(Id("person"), "Greet", [])])
            ])),
            MethodDecl("p", Id("Person"), 
                FuncDecl("Greet", [], StringType(), Block([
                    Return(BinaryOp("+", StringLiteral("Hello, "), FieldAccess(Id("p"), "name")))
                ]))
            )
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_060(self):
        """
        type S1 struct {nqpdpu1 int;}
        func (s S1) nqpdpu() int {
            s.nqpdpu();
            return 1;
        }
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],IntType(),Block([MethCall(Id("s"),"nqpdpu",[]),Return(IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(s),nqpdpu,[])\n", inspect.stack()[0].function))
    
    def test_061(self):
        """
        func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString\n", inspect.stack()[0].function))

    def test_062(self):
        """
        var v PHUDZ;      
        type PHUDZ struct {
            a int;
        } 
        type VO interface {
            foo() int;
        }

        func (v PHUDZ) foo() int {return 1;}
        func (b PHUDZ) koo() {b.koo();}
        func foo() {
            var x VO;  
            const b = x.foo(); 
            x.koo(); 
        }
        """
        input = Program([VarDecl("v",Id("PHUDZ"), None),StructType("PHUDZ",[("a",IntType())],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("PHUDZ"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("VO"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo\n", inspect.stack()[0].function))

    def test_063(self):
        """
        func (v PHUDZ) f1 (c A1) int {
            var e int = 10;
        }
        """
        input = Program([
            MethodDecl(
                receiver="v",  # Receiver name
                recType=Id("PHUDZ"),  # Receiver type as an Id
                fun=FuncDecl(
                    name="f1",
                    params=[ParamDecl("c", Id("A1"))],  # Parameter 'c' of type 'A1'
                    retType=IntType(),  # Return type 'int'
                    body=Block([
                        VarDecl("e", IntType(), IntLiteral(10))  # var e int = 10
                    ])
                )
            )
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: PHUDZ\n", inspect.stack()[0].function))

    def test_064(self):
        """
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b; // error as [2] int != [3] int
        var d [1] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n", inspect.stack()[0].function)) 

    def test_065(self):
        """ 
        // Complex nested struct with method call and type mismatch in return
        type S1 struct { x S2; }
        type S2 struct { y int; }
        func (s S1) getY() float { return s.x.y; }
        """
        input = Program([
            StructType("S1", [("x", Id("S2"))], []),
            StructType("S2", [("y", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("getY", [], FloatType(), Block([Return(FieldAccess(FieldAccess(Id("s"), "x"), "y"))])))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(FieldAccess(FieldAccess(Id(s),x),y))\n", inspect.stack()[0].function))

    def test_066(self):
        """ 
        // Interface with mismatched method signature in struct implementation
        type I1 interface { foo(a int) string; }
        type S1 struct { x int; }
        func (s S1) foo(a float) string { return "test"; }
        var i I1 = S1{x: 1};
        """
        input = Program([
            InterfaceType("I1", [Prototype("foo", [IntType()], StringType())]),
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [ParamDecl("a", FloatType())], StringType(), Block([Return(StringLiteral("test"))]))),
            VarDecl("i", Id("I1"), StructLiteral("S1", [("x", IntLiteral(1))]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(i,Id(I1),StructLiteral(S1,[(x,IntLiteral(1))]))\n", inspect.stack()[0].function))

    def test_067(self):
        """ 
        // Redeclared variable in nested block with function call
        func foo() {
            var a = 1;
            { 
                var a = getInt();
                var a = 2; 
            }
        }
        """
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("a", None, IntLiteral(1)),
                Block([
                    VarDecl("a", None, FuncCall("getInt", [])),
                    VarDecl("a", None, IntLiteral(2))
                ])
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a\n", inspect.stack()[0].function))

    def test_068(self):
        """ 
        // Type mismatch in array literal with nested dimensions
        var a = [2][2]int { {1, 2}, {1, "str"} };
        """
        input = Program([
            VarDecl("a", None, ArrayLiteral([IntLiteral(2), IntLiteral(2)], IntType(), [
                [IntLiteral(1), IntLiteral(2)],
                [IntLiteral(1), StringLiteral("str")]
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayLiteral([IntLiteral(2),IntLiteral(2)],IntType,[[IntLiteral(1),IntLiteral(2)],[IntLiteral(1),StringLiteral(str)]])\n", inspect.stack()[0].function))

    def test_069(self):
        """ 
        // Undeclared struct type in method declaration
        func (s Unknown) foo() { return; }
        """
        input = Program([
            MethodDecl("s", Id("Unknown"), FuncDecl("foo", [], VoidType(), Block([Return(None)])))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: Unknown\n", inspect.stack()[0].function))

    def test_070(self):
        """ 
        // Type mismatch with nested array access and assignment
        var a [2][2]int;
        func foo() {
            a[0] := [2]int{1, "str"};
        }
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(2)], IntType()), None),
            FuncDecl("foo", [], VoidType(), Block([
                Assign(ArrayCell(Id("a"), [IntLiteral(0)]), ArrayLiteral([IntLiteral(2)], IntType(), [IntLiteral(1), StringLiteral("str")]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),StringLiteral(str)])\n", inspect.stack()[0].function))

    def test_071(self):
        """ 
        // Interface compatibility with missing method
        type I1 interface { foo(); bar(); }
        type S1 struct { x int; }
        func (s S1) foo() { return; }
        var i I1 = S1{x: 1};
        """
        input = Program([
            InterfaceType("I1", [Prototype("foo", [], VoidType()), Prototype("bar", [], VoidType())]),
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [], VoidType(), Block([Return(None)]))),
            VarDecl("i", Id("I1"), StructLiteral("S1", [("x", IntLiteral(1))]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(i,Id(I1),StructLiteral(S1,[(x,IntLiteral(1))]))\n", inspect.stack()[0].function))

    def test_072(self):
        """ 
        // Type mismatch in binary operation with struct type
        type S1 struct { x int; }
        var a S1;
        var b = a + 1;
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            VarDecl("a", Id("S1"), None),
            VarDecl("b", None, BinaryOp("+", Id("a"), IntLiteral(1)))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(Id(a),+,IntLiteral(1))\n", inspect.stack()[0].function))

    def test_073(self):
        """ 
        // Redeclared method in struct with parameter conflict
        type S1 struct { x int; }
        func (s S1) foo(a int) { return; }
        func (s S1) foo(a int) { return; }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([Return(None)])))
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: foo\n", inspect.stack()[0].function))

    def test_074(self):
        input = """ 
        // ForEach with incompatible array type
        func foo() {
            var arr [2]string;
            var i int;
            var v string;
            for i, v := range arr {
                var x int = v;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(x,IntType,Id(v))\n", inspect.stack()[0].function))

    def test_075(self):
        """ 
        // Undeclared field access in nested struct
        type S1 struct { x S2; }
        type S2 struct { y int; }
        var s S1;
        var a = s.x.z;
        """
        input = Program([
            StructType("S1", [("x", Id("S2"))], []),
            StructType("S2", [("y", IntType())], []),
            VarDecl("s", Id("S1"), None),
            VarDecl("a", None, FieldAccess(FieldAccess(Id("s"), "x"), "z"))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: z\n", inspect.stack()[0].function))

    def test_076(self):
        """ 
        // Type mismatch in method call argument
        type S1 struct { x int; }
        func (s S1) foo(a int) { return; }
        var s S1;
        func bar() { s.foo("str"); }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))),
            VarDecl("s", Id("S1"), None),
            FuncDecl("bar", [], VoidType(), Block([MethCall(Id("s"), "foo", [StringLiteral("str")])]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(s),foo,[StringLiteral(str)])\n", inspect.stack()[0].function))

    def test_077(self):
        """ 
        // Return type mismatch with nil in struct method
        type S1 struct { x int; }
        func (s S1) foo() S1 { return nil; }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [], Id("S1"), Block([Return(NilLiteral())])))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))  # Should pass as nil is compatible with struct

    def test_078(self):
        """ 
        // Nested function call with undeclared function
        func foo() int {
            return bar();
        }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([Return(FuncCall("bar", []))]))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: bar\n", inspect.stack()[0].function))

    def test_079(self):
        """ 
        // Type mismatch in conditional expression
        func foo() {
            if 1 + "str" {
                return;
            }
        }
        """
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                If(BinaryOp("+", IntLiteral(1), StringLiteral("str")), Block([Return(None)]), None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(IntLiteral(1),+,StringLiteral(str))\n", inspect.stack()[0].function))

    def test_080(self):
        """ 
        // Redeclared parameter in method with receiver conflict
        type S1 struct { x int; }
        func (x S1) foo(x int) { return; }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("x", Id("S1"), FuncDecl("foo", [ParamDecl("x", IntType())], VoidType(), Block([Return(None)])))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_081(self):
        """ 
        // Array index out of bounds type mismatch
        var a [2]int;
        var b = a[2];
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2)], IntType()), None),
            VarDecl("b", None, ArrayCell(Id("a"), [IntLiteral(2)]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))  # Static checker doesn't check bounds, so no error expected

    def test_082(self):
        """ 
        // Struct literal with undeclared field
        type S1 struct { x int; }
        var a = S1 { y: 1 };
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            VarDecl("a", None, StructLiteral("S1", [("y", IntLiteral(1))]))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: y\n", inspect.stack()[0].function))

    def test_083(self):
        """ 
        // Type mismatch in ForStep condition
        func foo() {
            for var i = 1; i + 1; i += 1 {
                return;
            }
        }
        """
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ForStep(VarDecl("i", None, IntLiteral(1)), BinaryOp("+", Id("i"), IntLiteral(1)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([Return(None)]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: For(VarDecl(i,IntLiteral(1)),BinaryOp(Id(i),+,IntLiteral(1)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Return()]))\n", inspect.stack()[0].function))

    def test_084(self):
        """ 
        // Method call on non-struct/interface type
        var a int;
        func foo() { a.bar(); }
        """
        input = Program([
            VarDecl("a", IntType(), None),
            FuncDecl("foo", [], VoidType(), Block([MethCall(Id("a"), "bar", [])]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(a),bar,[])\n", inspect.stack()[0].function))

    def test_085(self):
        """ 
        // Nested struct with circular reference and type mismatch
        type S1 struct { x S2; }
        type S2 struct { y S1; }
        func foo() S1 { return S2{y: 1}; }
        """
        input = Program([
            StructType("S1", [("x", Id("S2"))], []),
            StructType("S2", [("y", Id("S1"))], []),
            FuncDecl("foo", [], Id("S1"), Block([Return(StructLiteral("S2", [("y", IntLiteral(1))]))]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: StructLiteral(S2,[(y,IntLiteral(1))])\n", inspect.stack()[0].function))

    def test_086(self):
        """ 
        // Unary operation on incompatible type
        var a = !"str";
        """
        input = Program([
            VarDecl("a", None, UnaryOp("!", StringLiteral("str")))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: UnaryOp(!,StringLiteral(str))\n", inspect.stack()[0].function))

    def test_087(self):
        """ 
        // Type mismatch in array cell assignment with wrong index type
        var a [2]int;
        func foo() { a["str"] := 1; }
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2)], IntType()), None),
            FuncDecl("foo", [], VoidType(), Block([Assign(ArrayCell(Id("a"), [StringLiteral("str")]), IntLiteral(1))]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(Id(a),[StringLiteral(str)])\n", inspect.stack()[0].function))

    def test_088(self):
        """ 
        // Redeclared prototype in interface
        type I1 interface { 
            foo();
            foo(a int);
        }
        """
        input = Program([
            InterfaceType("I1", [Prototype("foo", [], VoidType()), Prototype("foo", [IntType()], VoidType())])
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: foo\n", inspect.stack()[0].function))

    def test_089(self):
        """ 
        // Type mismatch with nil assignment to primitive
        var a int = nil;
        """
        input = Program([
            VarDecl("a", IntType(), NilLiteral())
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,Nil)\n", inspect.stack()[0].function))

    def test_090(self):
        input = """ 
        // Complex nested ForEach with type mismatch
        func foo() {
            var arr [2][2]int;
            var i int;
            var v [2]int;
            for i, v := range arr {
                var j int;
                var w int;
                for j, w := range v {
                    var x string = w;
                }
            }
        }
        """
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(x,StringType,Id(w))\n", inspect.stack()[0].function))

    def test_091(self):
        """ 
        // Method call with wrong number of arguments
        type S1 struct { x int; }
        func (s S1) foo(a int, b int) { return; }
        var s S1;
        func bar() { s.foo(1); }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], VoidType(), Block([Return(None)]))),
            VarDecl("s", Id("S1"), None),
            FuncDecl("bar", [], VoidType(), Block([MethCall(Id("s"), "foo", [IntLiteral(1)])]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: MethodCall(Id(s),foo,[IntLiteral(1)])\n", inspect.stack()[0].function))

    def test_092(self):
        """ 
        // Type mismatch in return with function call
        func foo() int {
            return putInt(1);
        }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([Return(FuncCall("putInt", [IntLiteral(1)]))]))
        ])
        # Type Mismatch: Return(FuncCall(putInt,[IntLiteral(1)]))
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(putInt,[IntLiteral(1)])\n", inspect.stack()[0].function))
        # self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(FuncCall(putInt,[IntLiteral(1)]))\n", inspect.stack()[0].function))

    def test_093(self):
        """ 
        // Circular method call causing type mismatch
        type S1 struct { x int; }
        func (s S1) foo() int { return s.foo(); }
        """
        input = Program([
            StructType("S1", [("x", IntType())], []),
            MethodDecl("s", Id("S1"), FuncDecl("foo", [], IntType(), Block([Return(MethCall(Id("s"), "foo", []))])))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))  # Infinite recursion not caught statically

    def test_094(self):
        """ 
        // Type mismatch in field access chain
        type S1 struct { x S2; }
        type S2 struct { y int; }
        var s S1;
        var a string = s.x.y;
        """
        input = Program([
            StructType("S1", [("x", Id("S2"))], []),
            StructType("S2", [("y", IntType())], []),
            VarDecl("s", Id("S1"), None),
            VarDecl("a", StringType(), FieldAccess(FieldAccess(Id("s"), "x"), "y"))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,StringType,FieldAccess(FieldAccess(Id(s),x),y))\n", inspect.stack()[0].function))
    
    def test_095(self):
        """ 
        // Deeply nested array cell with method call and type mismatch in assignment
        type S1 struct { arr [2][3]int; }
        type S2 struct { s S1; }
        func (s S2) getArr() [3]int { return s.s.arr[1]; }
        func foo() {
            var s S2;
            var x [2]int = s.getArr()[0][1];  // Indexing a [3]int with 2 levels
        }
        """
        input = Program([
            StructType("S1", [("arr", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()))], []),
            StructType("S2", [("s", Id("S1"))], []),
            MethodDecl("s", Id("S2"), FuncDecl("getArr", [], ArrayType([IntLiteral(3)], IntType()), 
                Block([Return(ArrayCell(FieldAccess(FieldAccess(Id("s"), "s"), "arr"), [IntLiteral(1)]))]))),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("s", Id("S2"), None),
                VarDecl("x", ArrayType([IntLiteral(2)], IntType()), 
                        ArrayCell(ArrayCell(MethCall(Id("s"), "getArr", []), [IntLiteral(0)]), [IntLiteral(1)]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(ArrayCell(MethodCall(Id(s),getArr,[]),[IntLiteral(0)]),[IntLiteral(1)])\n", inspect.stack()[0].function))

    def test_096(self):
        """ 
        // Nested function and method calls with field access and interface mismatch
        type I1 interface { compute() int; }
        type S1 struct { x int; next S2; }
        type S2 struct { data [2]S1; }
        func (s S1) compute() int { return s.x; }
        func process(i I1) int { return i.compute(); }
        func foo() {
            var s S2;
            var result int = process(s.data[0].next.data[1]);  // S1 not compatible with I1 due to nesting
        }
        """
        input = Program([
            InterfaceType("I1", [Prototype("compute", [], IntType())]),
            StructType("S1", [("x", IntType()), ("next", Id("S2"))], []),
            StructType("S2", [("data", ArrayType([IntLiteral(2)], Id("S1")))], []),
            MethodDecl("s", Id("S1"), FuncDecl("compute", [], IntType(), Block([Return(FieldAccess(Id("s"), "x"))]))),
            FuncDecl("process", [ParamDecl("i", Id("I1"))], IntType(), Block([Return(MethCall(Id("i"), "compute", []))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("s", Id("S2"), None),
                VarDecl("result", IntType(), FuncCall("process", [
                    ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id("s"), "data"), [IntLiteral(0)]), "next"), [IntLiteral(1)])
                ]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(FieldAccess(ArrayCell(FieldAccess(Id(s),data),[IntLiteral(0)]),next),[IntLiteral(1)])\n", inspect.stack()[0].function))

    def test_097(self):
        """ 
        // Super nested array cell and field access with method call in ForEach loop
        type S1 struct { arr [2][2][3]int; }
        type S2 struct { s S1; }
        func (s S2) getInner() [3]int { return s.s.arr[0][1]; }
        func foo() {
            var s S2;
            for i, v := range s.getInner()[1][0] {  // Invalid indexing on int
                var x int = v;
            }
        }
        """
        input = Program([
            StructType("S1", [("arr", ArrayType([IntLiteral(2), IntLiteral(2), IntLiteral(3)], IntType()))], []),
            StructType("S2", [("s", Id("S1"))], []),
            MethodDecl("s", Id("S2"), FuncDecl("getInner", [], ArrayType([IntLiteral(3)], IntType()), 
                Block([Return(ArrayCell(ArrayCell(FieldAccess(FieldAccess(Id("s"), "s"), "arr"), [IntLiteral(0)]), [IntLiteral(1)]))]))),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("s", Id("S2"), None),
                ForEach(Id("i"), Id("v"), ArrayCell(ArrayCell(MethCall(Id("s"), "getInner", []), [IntLiteral(1)]), [IntLiteral(0)]), 
                    Block([VarDecl("x", IntType(), Id("v"))]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(ArrayCell(MethodCall(Id(s),getInner,[]),[IntLiteral(1)]),[IntLiteral(0)])\n", inspect.stack()[0].function))

    def test_098(self):
        """ 
        // Complex nested method calls with field access and type mismatch in return
        type S1 struct { x int; next S2; }
        type S2 struct { s S1; arr [2]S1; }
        func (s S1) getX() int { return s.x; }
        func (s S2) getNested() int { return s.s.getX(); }
        func foo() int {
            var s S2;
            return s.arr[0].next.getNested();  // int vs int match
        }
        """
        input = Program([
            StructType("S1", [("x", IntType()), ("next", Id("S2"))], []),
            StructType("S2", [("s", Id("S1")), ("arr", ArrayType([IntLiteral(2)], Id("S1")))], []),
            MethodDecl("s", Id("S1"), FuncDecl("getX", [], IntType(), Block([Return(FieldAccess(Id("s"), "x"))]))),
            MethodDecl("s", Id("S2"), FuncDecl("getNested", [], IntType(), Block([Return(MethCall(FieldAccess(Id("s"), "s"), "getX", []))]))),
            FuncDecl("foo", [], IntType(), Block([
                VarDecl("s", Id("S2"), None),
                Return(MethCall(FieldAccess(ArrayCell(FieldAccess(Id("s"), "arr"), [IntLiteral(0)]), "next"), "getNested", []))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_099(self):
        """ 
        // Nested function calls with array cells and interface type mismatch
        type I1 interface { process() [2]int; }
        type S1 struct { data [3][2]int; }
        func (s S1) process() [2]int { return s.data[0]; }
        func compute(i I1) int { return i.process()[1]; }
        func foo() {
            var s S1;
            var x string = compute(s.data[1]);  // [2]int not compatible with I1
        }
        """
        input = Program([
            InterfaceType("I1", [Prototype("process", [], ArrayType([IntLiteral(2)], IntType()))]),
            StructType("S1", [("data", ArrayType([IntLiteral(3), IntLiteral(2)], IntType()))], []),
            MethodDecl("s", Id("S1"), FuncDecl("process", [], ArrayType([IntLiteral(2)], IntType()), 
                Block([Return(ArrayCell(FieldAccess(Id("s"), "data"), [IntLiteral(0)]))]))),
            FuncDecl("compute", [ParamDecl("i", Id("I1"))], IntType(), Block([Return(ArrayCell(MethCall(Id("i"), "process", []), [IntLiteral(1)]))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("s", Id("S1"), None),
                VarDecl("x", StringType(), FuncCall("compute", [ArrayCell(FieldAccess(Id("s"), "data"), [IntLiteral(1)])]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(compute,[ArrayCell(FieldAccess(Id(s),data),[IntLiteral(1)])])\n", inspect.stack()[0].function))

    def test_100(self):
        """
        type A interface {foo();}
        const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A\n""", inspect.stack()[0].function))
    
    def test_101(self):
        """
        func foo(a [2] float) {
            foo([2] float {1.0,2.0})
            foo([2] int {1,2})
        }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])\n""", inspect.stack()[0].function)) 
    
    def test_102(self):
        """
        const v = 3;
        const a = v + v;
        var b [a * 2 + a] int;
        var c [17] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(17)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(17)]),Id(b))\n""", inspect.stack()[0].function)) 
    
    def test_103(self): # 143
        """
        var a PHUDZ;
        func foo() PHUDZ {
            return a;
            return PHUDZ;
        }

        type PHUDZ struct {quangphiu int;}
        """
        input = Program([VarDecl("a",Id("PHUDZ"), None),FuncDecl("foo",[],Id("PHUDZ"),Block([Return(Id("a")),Return(Id("PHUDZ"))])),StructType("PHUDZ",[("quangphiu",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: PHUDZ\n""", inspect.stack()[0].function)) 
    
    def test_104(self): # 154
        """
        func foo() {
            putFloat(getInt());
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("putFloat",[FuncCall("getInt",[])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(putFloat,[FuncCall(getInt,[])])\n""", inspect.stack()[0].function)) 
    
    def test_105(self): # 158
        """
        func foo() [2] float {
            return [2] float {1.0, 2.0};
            return [2] int {1, 2};
        }
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))\n""", inspect.stack()[0].function)) 
    
    def test_106(self): # 159
        """
        type PHUDZ struct {a [2]int;} 
        type VO interface {foo() int;}

        func (v PHUDZ) foo() int {return 1;}

        func foo() PHUDZ {
            return PHUDZ{a: [2]int{1, 2}};
        }
        func coco() PHUDZ {
            var a VO = foo();
            return a;
        }
        """
        input = Program([StructType("PHUDZ",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],Id("PHUDZ"),Block([Return(StructLiteral("PHUDZ",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])),FuncDecl("coco",[],Id("PHUDZ"),Block([VarDecl("a",Id("VO"),FuncCall("foo",[])),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(a))\n""", inspect.stack()[0].function)) 
    
    def test_107(self): # 160
        """
        type PHUDZ struct {a [2]int;} 
        type VO interface {foo() int;}

        func (v PHUDZ) foo() int {return 1;}

        func foo() {
            var b VO = PHUDZ{a: [2]int{1, 2}};
            var a PHUDZ = b;
        }

        """
        input = Program([StructType("PHUDZ",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("VO",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("PHUDZ"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b",Id("VO"),StructLiteral("PHUDZ",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",Id("PHUDZ"),Id("b"))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(a,Id(PHUDZ),Id(b))\n""", inspect.stack()[0].function)) 
    
    def test_108(self): # 160
        """
        func foo() int {
            if (true) {
                var a = 1;
            } else {
                var a = 2;
            }
            return a;
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([If(BooleanLiteral(True), Block([VarDecl("a", None,IntLiteral(1))]), Block([VarDecl("a", None,IntLiteral(2))])),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: a\n""", inspect.stack()[0].function)) 
    
    def test_109(self): # 170
        """
        func foo() int {
            var arr [3] int;
            var marr [2][3] int;
            arr := [3]int{10, 20, 30}
            marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
            return arr[2] + marr[1][2]
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("arr",ArrayType([IntLiteral(3)],IntType()), None),VarDecl("marr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),Assign(Id("arr"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30)])),Assign(Id("marr"),ArrayLiteral([IntLiteral(2),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3)],[IntLiteral(4),IntLiteral(5),IntLiteral(6)]])),Return(BinaryOp("+", ArrayCell(Id("arr"),[IntLiteral(2)]), ArrayCell(Id("marr"),[IntLiteral(1),IntLiteral(2)])))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_110(self): # 38
        """
        const a = 1;
        func foo() {
            var a = 1;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_111(self): # 172
        """ 
        type Person struct {
            name string;
            age  int;
        };
        func (p Person) getAge() int {
            p := Person{name: "Alice", age: 30}
            q := Person{}
            return p.age
        };
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),Assign(Id("q"),StructLiteral("Person",[])),Return(FieldAccess(Id("p"),"age"))])))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_112(self): # 174
        """
        var A = 1;
        type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: A\n""", inspect.stack()[0].function)) 
    
    def test_113(self): # 179
        """
        type A interface {foo();}

        func foo() {
            return A;
        }      
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),FuncDecl("foo",[],VoidType(),Block([Return(Id("A"))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: A\n""", inspect.stack()[0].function)) 
    
    def test_114(self): # 182
        """
        type S1 struct {nqpdpu1 int;}
        type I1 interface {nqpdpu();}

        func (s S1) nqpdpu() {return;}

        var b [2] S1;
        var a [2] I1 = b;    
        """
        input = Program([StructType("S1",[("nqpdpu1",IntType())],[]),InterfaceType("I1",[Prototype("nqpdpu",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("nqpdpu",[],VoidType(),Block([Return(None)]))),VarDecl("b",ArrayType([IntLiteral(2)],Id("S1")), None),VarDecl("a",ArrayType([IntLiteral(2)],Id("I1")),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(a,ArrayType(Id(I1),[IntLiteral(2)]),Id(b))\n""", inspect.stack()[0].function)) 
        
    def test_115(self): # 96
        """
        var a = [2] int {1, 2}
        var c [2] float = a  
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
        
    def test_116(self): # 192
        """
        const v = 3;
        const k = v + 1;
        func foo(a [1 + 2] int) {
            foo([k - 1] int {1,2,3})
        }      
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
      
    def test_117(self): # 194
        """
        type K struct {a int;}
        func (k K) koo(a [1 + 2] int) {return;}
        type H interface {koo(a [1 + 2] int);}

        const c = 4;
        func foo() {
            var k H;
            k.koo([c - 1] int {1,2,3})
        } 
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_118(self): # 199
        """
        const a = 3;
        const b = -a;
        const c = -b;
        var d [c] int = [3] int {1,2,3}
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_119(self): # 202
        """
        func foo() {
            a := 1;
            var a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a\n""", inspect.stack()[0].function)) 
    
    def test_120(self): # 204
        """
        const a = 1;
        func foo() {
            a := 1.;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),FloatLiteral(1.0))\n""", inspect.stack()[0].function)) 
            
    def test_121(self):
        """
        func foo() {
            var a [5][6] int;
            var b [2] float;
            b[2] := a[2][3]
            a[2][3] := b[2] + 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(6)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],FloatType()), None),Assign(ArrayCell(Id("b"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+", ArrayCell(Id("b"),[IntLiteral(2)]), IntLiteral(1)))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(2),IntLiteral(3)]),BinaryOp(ArrayCell(Id(b),[IntLiteral(2)]),+,IntLiteral(1)))\n""", inspect.stack()[0].function)) 
        
    def test_122(self):
        """
        var v = 2 * 3;
        const a = v + 1;
        const b = a * 5;
        const c = ! (b > 3);
        """
        input = Program([VarDecl("v", None,BinaryOp("*", IntLiteral(2), IntLiteral(3))),ConstDecl("a",None,BinaryOp("+", Id("v"), IntLiteral(1))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5))),ConstDecl("c",None,UnaryOp("!",BinaryOp(">", Id("b"), IntLiteral(3))))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    
    def test_123(self):     # 195
        """
        type K struct {a int;}
        func (k K) koo(a [1 + 2] int) [1 + 2] int {return [3*1] int {1,2,3};}
        type H interface {koo(a [1 + 2] int) [1 + 2] int;}

        const c = 4;
        func foo() [1 + 2] int{
            return foo()
            var k K;
            return k.koo([c - 1] int {1,2,3})
            var h H;
            return h.koo([c - 1] int {1,2,3})
        }  
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("foo",[])),VarDecl("k",Id("K"), None),Return(MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),VarDecl("h",Id("H"), None),Return(MethCall(Id("h"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    def test_124(self): 
        """
        func f() {
            for (i = 0; i < 10; i = i + 1) {
                var i float = 0.0;
            }
        }
        """
        input = Program([
            FuncDecl("f", [], VoidType(), Block([
                ForStep(
                    Assign(Id("i"), IntLiteral(0)),
                    BinaryOp("<", Id("i"), IntLiteral(10)),
                    Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                    Block([
                        VarDecl("i", FloatType(), FloatLiteral(0.0))
                    ])
                )
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: i\n""", inspect.stack()[0].function)) 
     
    def test_125(self): 
        input = """
        func f() {
            var i int = 0;
            var it int = 0;
            for i, it := range [10] int {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} {
                var i float = 0.0;
                var it float = 0.0;
            }
        }        
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
           
    
    def test_126(self):
        """
        var a [1 + 9] int;
        var b [10] int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 

    def test_127(self):
        """
        type Node struct {
            value int;
            next Node;
        }
        
        type Tree struct {
            root Node;
        }

        type Traversal interface {
            traverse();
        }

        func (t Tree) traverse() {return;}
        func (t Tree) find(x int) int {return 0;}
        """
        input = Program([
            StructType("Node", [("value", IntType()), ("next", Id("Node"))], []),
            StructType("Tree", [("root", Id("Node"))], []),
            InterfaceType("Traversal", [Prototype("traverse", [], VoidType())]),
            MethodDecl("t", Id("Tree"), FuncDecl("traverse", [], VoidType(), Block([Return(None)]))),
            MethodDecl("t", Id("Tree"), FuncDecl("find", [ParamDecl("x", IntType())], IntType(), Block([Return(IntLiteral(0))])))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_128(self):
        """
        func foo() {
            var x int = 0;
            for x < 10 {
                var x int = 1;
                for x > 0 {
                    var x int = 2;
                    if x == 2 {
                        var x int = 3;
                    }
                }
            }
        }
        """
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(0)),
                ForBasic(BinaryOp("<", Id("x"), IntLiteral(10)), Block([
                    VarDecl("x", IntType(), IntLiteral(1)),
                    ForBasic(BinaryOp(">", Id("x"), IntLiteral(0)), Block([
                        VarDecl("x", IntType(), IntLiteral(2)),
                        If(BinaryOp("==", Id("x"), IntLiteral(2)), Block([
                            VarDecl("x", IntType(), IntLiteral(3))
                        ]), None)
                    ]))
                ]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_129(self):
        """
        type Shape struct {
            area float;
        }
        
        type Drawable interface {
            draw();
        }

        type Circle struct {
            radius float;
        }

        func (c Circle) draw() {return;}
        
        var s Shape;
        var c Circle;
        var d Drawable = c;
        """
        input = Program([
            StructType("Shape", [("area", FloatType())], []),
            InterfaceType("Drawable", [Prototype("draw", [], VoidType())]),
            StructType("Circle", [("radius", FloatType())], []),
            MethodDecl("c", Id("Circle"), FuncDecl("draw", [], VoidType(), Block([Return(None)]))),
            VarDecl("s", Id("Shape"), None),
            VarDecl("c", Id("Circle"), None),
            VarDecl("d", Id("Drawable"), Id("c"))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_130(self):
        """
        func fact(n int) int {
            if n == 0 {return 1;}
            return n * fact(n - 1);
        }

        func main() {
            var x int = fact(5);
            return;
        }
        """
        input = Program([
            FuncDecl("fact", [ParamDecl("n", IntType())], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([Return(IntLiteral(1))]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("fact", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ])),
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("x", IntType(), FuncCall("fact", [IntLiteral(5)])),
                Return(None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_131(self):
        """
        var a [2][3]int;
        var b [2][3]int;
        var c = a[1][2];
        var d = b[1][2];
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
            VarDecl("b", ArrayType([IntLiteral(2)], ArrayType([IntLiteral(3)], IntType())), None),
            VarDecl("c", None, ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)])),
            VarDecl("d", None, ArrayCell(Id("b"), [IntLiteral(1), IntLiteral(2)]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ArrayCell(Id(b),[IntLiteral(1),IntLiteral(2)])\n", inspect.stack()[0].function))

    def test_132(self):
        """
        type Drawable interface {
            draw();
        }

        type Circle struct {
            radius float;
        }

        func (c Circle) draw() {return;}
        
        var d Drawable = c;
        """
        input = Program([
            InterfaceType("Drawable", [Prototype("draw", [], VoidType())]),
            StructType("Circle", [("radius", FloatType())], []),
            MethodDecl("c", Id("Circle"), FuncDecl("draw", [], VoidType(), Block([Return(None)]))),
            VarDecl("d", Id("Drawable"), Id("c"))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: c\n", inspect.stack()[0].function))
    
    def test_133(self):
        """
        func outer() int {
            func inner() {return;}
            return 1;
        }
        """
        input = Program([
            FuncDecl("outer", [], IntType(), Block([
                FuncDecl("inner", [], VoidType(), Block([Return(None)])),
                Return(IntLiteral(1))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_134(self):
        """
        type Rectangle struct {
            width int;
            height int;
        }

        type Drawable interface {
            draw();
        }

        func (r Rectangle) draw() {return;}

        func (r Rectangle) resize(w int, h int) {return;}

        var d Drawable = r;
        var rect Rectangle;
        """
        input = Program([
            StructType("Rectangle", [("width", IntType()), ("height", IntType())], []),
            InterfaceType("Drawable", [Prototype("draw", [], VoidType())]),
            MethodDecl("r", Id("Rectangle"), FuncDecl("draw", [], VoidType(), Block([Return(None)]))),
            MethodDecl("r", Id("Rectangle"), FuncDecl("resize", [ParamDecl("w", IntType()), ParamDecl("h", IntType())], VoidType(), Block([Return(None)]))),
            VarDecl("d", Id("Drawable"), Id("r")),
            VarDecl("rect", Id("Rectangle"), None)
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: r\n", inspect.stack()[0].function))

    def test_135(self):
        """
        func foo(x int) {
            for x < 10 {
                if x == 5 {
                    break;
                } else {
                    continue;
                }
            }
        }
        """
        input = Program([
            FuncDecl("foo", [ParamDecl("x", IntType())], VoidType(), Block([
                ForBasic(BinaryOp("<", Id("x"), IntLiteral(10)), Block([
                    If(BinaryOp("==", Id("x"), IntLiteral(5)), 
                       Block([Break()]), 
                       Block([Continue()]))
                ]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_136(self):
        """
        var a [3][2]int;
        var b = a[1][0];
        var c = a[1][2];
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(3), IntLiteral(2)], IntType()), None),
            VarDecl("b", None, ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(0)])),
            VarDecl("c", None, ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_137(self):
        """
        type A struct {
            x int;
        }

        type B struct {
            x float;
        }

        func (a A) getX() int {return a.x;}
        func (b B) getX() float {return b.x;}

        var a A;
        var b B;
        var x = a.getX();
        var y = b.getX();
        var z = a.getY();
        """
        input = Program([
            StructType("A", [("x", IntType())], []),
            StructType("B", [("x", FloatType())], []),
            MethodDecl("a", Id("A"), FuncDecl("getX", [], IntType(), Block([Return(FieldAccess(Id("a"), "x"))]))),
            MethodDecl("b", Id("B"), FuncDecl("getX", [], FloatType(), Block([Return(FieldAccess(Id("b"), "x"))]))),
            VarDecl("a", Id("A"), None),
            VarDecl("b", Id("B"), None),
            VarDecl("x", None, MethCall(Id("a"), "getX", [])),
            VarDecl("y", None, MethCall(Id("b"), "getX", [])),
            VarDecl("z", None, MethCall(Id("a"), "getY", []))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: getY\n", inspect.stack()[0].function))

    def test_138(self):
        """
        func foo() int {
            return foo() + 1;
        }

        func bar() int {
            return bar() + foo();
        }

        func baz() {
            bar();
            foo();
            return;
        }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([Return(BinaryOp("+", FuncCall("foo", []), IntLiteral(1)))])),
            FuncDecl("bar", [], IntType(), Block([Return(BinaryOp("+", FuncCall("bar", []), FuncCall("foo", [])))])),
            FuncDecl("baz", [], VoidType(), Block([
                FuncCall("bar", []),
                FuncCall("foo", []),
                Return(None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(bar,[])\n", inspect.stack()[0].function))

    def test_139(self):
        """
        type List struct {
            head int;
            tail List;
        }

        func (l List) getHead() int {return l.head;}

        var l List;
        var h = l.getHead();
        var t = l.getTail();
        """
        input = Program([
            StructType("List", [("head", IntType()), ("tail", Id("List"))], []),
            MethodDecl("l", Id("List"), FuncDecl("getHead", [], IntType(), Block([Return(FieldAccess(Id("l"), "head"))]))),
            VarDecl("l", Id("List"), None),
            VarDecl("h", None, MethCall(Id("l"), "getHead", [])),
            VarDecl("t", None, MethCall(Id("l"), "getTail", []))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: getTail\n", inspect.stack()[0].function))

    def test_140(self):
        """
        var arr [2][2]float;
        var v = arr[1][1];
        var x = arr[2][2];
        """
        input = Program([
            VarDecl("arr", ArrayType([IntLiteral(2), IntLiteral(2)], FloatType()), None),
            VarDecl("v", None, ArrayCell(Id("arr"), [IntLiteral(1), IntLiteral(1)])),
            VarDecl("x", None, ArrayCell(Id("arr"), [IntLiteral(2), IntLiteral(2)]))
        ])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    def test_141(self):
        """
        var a int;
        func (v PDZ) foo () int {
            return a;
            return v;
        }
        type PDZ struct {
            Votien int;
        }   
        """
        input = Program([VarDecl("a",IntType(), None),MethodDecl("v",Id("PDZ"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))]))),StructType("PDZ",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(v))\n""", inspect.stack()[0].function))
        
    def test_142(self):
        """
        var v PDZ;
        const b = v.foo();        
        type PDZ struct {
            a int;
        } 
        func (v PDZ) foo() int {return 1;}
        func (v PDZ) koo() int {return 1;}
        const c = v.koo();  
        const d = v.zoo();
        """
        input = Program([VarDecl("v",Id("PDZ"), None),ConstDecl("b",None,MethCall(Id("v"),"foo",[])),StructType("PDZ",[("a",IntType())],[]),MethodDecl("v",Id("PDZ"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("v",Id("PDZ"),FuncDecl("koo",[],IntType(),Block([Return(IntLiteral(1))]))),ConstDecl("c",None,MethCall(Id("v"),"koo",[])),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Method: zoo\n""", inspect.stack()[0].function))
        
    def test_143(self):
        input = """
            const a = 2;
            func foo () {
                const a = 1;
                for var a = 1; a < 1; b := 2 {
                    const b = 1;
                }
            }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: b\n""", inspect.stack()[0].function))
        
    
    def test_201(self):
        input = """
            func test() {
                var a int;
                a := a + "str"
            }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(a),+,StringLiteral("str"))\n""", inspect.stack()[0].function))
        
    def test_202(self):
        input = """
            func test() {
                var a int
                var b int
                var c int
                for a, b := range c {
                    var d int;
                }
            }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id(a),Id(b),Id(c),Block([VarDecl(d,IntType)]))\n""", inspect.stack()[0].function))
        
    def test_203(self):
        input = """
            var a int; 
            
            type b struct {
                c int;
            }; 
            
            func (x b) a() {
                
            }; 
            
            func (x b) c() {
                
            };
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: c\n""", inspect.stack()[0].function))
    
    def test_204(self):
        input = """
            func foo() { return; }
            
            func pdz() {
                foo()
                return pdz()
            }
            
        """
        # self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(FuncCall(pdz,[]))\n""", inspect.stack()[0].function))
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(pdz,[])\n""", inspect.stack()[0].function))
        
    
    def test_205(self):
        input = """
            var a int; 
            
            func (x b) c() {
                
            };
            
            func (x b) a() {
                
            }; 
            
            type b struct {
                z string;
                a int;
            }; 
            
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Method: a\n""", inspect.stack()[0].function))
    
    def test_206(self): # 216
        """
        func (v TIEN) VO () {return ;}
        func (v TIEN) Tien () {return ;}
        type TIEN struct {
            Votien int;
            Tien int;
        }
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Tien\n""", inspect.stack()[0].function))
    
    def test_207(self): # 216
        """
        var foo = 1;
        func foo1() int {
            return foo()
        }
        """
        input = Program([VarDecl("foo", None,IntLiteral(1)),FuncDecl("foo1",[],IntType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", inspect.stack()[0].function))
    
    def test_208(self): 
        input = """
        var y int = 4;
        func Add(x int) int {
            y := 3;
            var y = 5;
            return 4;
        }
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    def test_209(self): 
        input = """
        func Add(x int) int {
            for y := 1; y<5; y += 1 {
                var y = 10;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: y\n""", inspect.stack()[0].function))
        
    def test_210(self): 
        input = """
        func Add(x int) int {
            var y = 5;
            for y := 1; y<5; y += 1 {
                var y = 10;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    
    def test_211(self): # 217
        input = """
        func foo(a int) {
            foo(1);
            var foo = 1;
            foo(2); // error
        }
        """
        # input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1)),FuncCall("foo",[IntLiteral(2)])]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", inspect.stack()[0].function))
           
           
           
    # def test_200(self): # 206
    #     """
    #     // Thank you for participating in the PPL2 course
    #     // The teacher won't check this, just ignore it, testing too much.
    #     const a = 2;
    #     type STRUCT struct {x [a] int;}
    #     func (s STRUCT) foo(x [a] int) [a] int {return s.x;}
    #     func foo(x [a] int) [a] int  {
    #         const a = 3;
    #         return [a] int {1,2};
    #     }
    #     """
    #     input = Program([ConstDecl("a",None,IntLiteral(2)),StructType("STRUCT",[("x",ArrayType([Id("a")],IntType()))],[]),MethodDecl("s",Id("STRUCT"),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([Return(FieldAccess(Id("s"),"x"))]))),FuncDecl("foo",[ParamDecl("x",ArrayType([Id("a")],IntType()))],ArrayType([Id("a")],IntType()),Block([ConstDecl("a",None,IntLiteral(3)),Return(ArrayLiteral([Id("a")],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
    #     self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),FloatLiteral(1.0))\n""", inspect.stack()[0].function)) 
              
    
    
    


# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu