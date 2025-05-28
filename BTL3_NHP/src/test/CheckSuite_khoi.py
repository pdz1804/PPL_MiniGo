
import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
        var Frankie = 1; 
        var Frankie = 2;
        """
        input = Program([VarDecl("Frankie", None,IntLiteral(1)),VarDecl("Frankie", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: Frankie\n", inspect.stack()[0].function))

    def test_002(self):
        """
        var Frankie = 1; 
        const Frankie = 2;
        """
        input = Program([VarDecl("Frankie", None,IntLiteral(1)),ConstDecl("Frankie",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: Frankie\n", inspect.stack()[0].function))

    def test_003(self):
        """
        const Frankie = 1; 
        var Frankie = 2;
        """
        input = Program([ConstDecl("Frankie",None,IntLiteral(1)),VarDecl("Frankie", None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: Frankie\n", inspect.stack()[0].function))

    def test_004(self):
        """
        const Frankie = 1; 
        func Frankie () {return;}
        """
        input = Program([ConstDecl("Frankie",None,IntLiteral(1)),FuncDecl("Frankie",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: Frankie\n", inspect.stack()[0].function))

    def test_005(self):
        """ 
        func Frankie () {return;}
        var Frankie = 1;
        """
        input = Program([FuncDecl("Frankie",[],VoidType(),Block([Return(None)])),VarDecl("Frankie", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: Frankie\n", inspect.stack()[0].function))

    def test_006(self):
        """ 
        var getInt = 1;
        """
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt\n", inspect.stack()[0].function))

    def test_007(self):
        """ 
        type  Frankie struct {
            Frankie int;
        }
        type Frank struct {
            Frankie string;
            Frank int;
            Frank float;
        }
        """
        input = Program([StructType("Frankie",[("Frankie",IntType())],[]),StructType("Frank",[("Frankie",StringType()),("Frank",IntType()),("Frank",FloatType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: Frank\n", inspect.stack()[0].function))

    def test_008(self):
        """ 
        func (v Frank) putIntLn () {return;}
        func (v Frank) getInt () {return;}
        func (v Frank) getInt () {return;}
        type Frank struct {
            Frankie int;
        }
        """
        input = Program([MethodDecl("v",Id("Frank"),FuncDecl("putIntLn",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("Frank"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("Frank"),FuncDecl("getInt",[],VoidType(),Block([Return(None)]))), StructType("Frank",[("Frankie",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt\n", inspect.stack()[0].function))

    def test_009(self):
        """ 
        type Frankie interface {
            Frankie ();
            Frankie (a int);
        }
        """
        input = Program([InterfaceType("Frankie",[Prototype("Frankie",[],VoidType()),Prototype("Frankie",[IntType()],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: Frankie\n", inspect.stack()[0].function))

    def test_010(self):
        """ 
        func Frankie (a, a int) {return;}
        """
        input = Program([FuncDecl("Frankie",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", inspect.stack()[0].function))

    def test_011(self):
        """ 
        func Frankie (b int) {
            var b = 1;
            var a = 1;
            const a = 1;
        }
        """
        input = Program([FuncDecl("Frankie",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a\n", inspect.stack()[0].function))

    def test_012(self):
        """ 
        func Frankie (b int) {
            for var a = 1; a < 1; a += 1 {
                const a = 2;
            }
        }
        """
        input = Program([FuncDecl("Frankie",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
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
        func Frankie () int {return 1;}

        fun foo () {
            var b = Frankie();
            foo_uwuuwu();
            return;
        }
        """
        input = Program([FuncDecl("Frankie",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Frankie",[])),FuncCall("foo_uwuuwu",[]),Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_uwuuwu\n", inspect.stack()[0].function))

    def test_015(self):
        """ 
        type Frank struct {
            Frankie int;
        }

        func (v Frank) getInt () {
            const c = v.Frankie;
            var d = v.Frank;
        }
        """
        input = Program([StructType("Frank",[("Frankie",IntType())],[]),MethodDecl("v",Id("Frank"),FuncDecl("getInt",[],VoidType(),Block([ConstDecl("c",None,FieldAccess(Id("v"),"Frankie")),VarDecl("d", None,FieldAccess(Id("v"),"Frank"))])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: Frank\n", inspect.stack()[0].function))

    def test_016(self):
        """ 
        type Frank struct {
            Frankie int;
        }

        func (v Frank) getInt () {
            v.getInt ();
            v.putInt ();
        }
        """
        input = Program([StructType("Frank",[("Frankie",IntType())],[]),MethodDecl("v",Id("Frank"),FuncDecl("getInt",[],VoidType(),Block([MethCall(Id("v"),"getInt",[]),MethCall(Id("v"),"putInt",[])])))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt\n", inspect.stack()[0].function))
    
    def test_017(self):
        """ 
        type Frank struct {Frankie int;}
        type Frank interface {Frankie ();}
        """
        input = Program([StructType("Frank",[("Frankie",IntType())],[]),InterfaceType("Frank",[Prototype("Frankie",[],VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Frank\n", inspect.stack()[0].function))
        
    def test_018(self):
        """ 
        type Frank struct {Frankie int;}
        type Frank struct {v int;}
        """
        input = Program([StructType("Frank",[("Frankie",IntType())],[]),StructType("Frank",[("v",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: Frank\n", inspect.stack()[0].function))
        
    def test_019(self):
        """ 
        type Frank struct {
            Frankie int;
        }
        func (v Frank) foo (a, b int) {return;}
        func foo (a, a int) {return;}
        """
        input = Program([StructType("Frank",[("Frankie",IntType())],[]),MethodDecl("v",Id("Frank"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a\n", inspect.stack()[0].function))
        
        
    def test_020(self): # 44
        """
        type FRANK struct {
            Frankie int;
        }
        func (v FRANK) foo (v int) {return;}
        func foo () {return;}
        """
        input = Program([StructType("FRANK",[("Frankie",IntType())],[]),MethodDecl("v",Id("FRANK"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
        
    def test_021(self): # 50
        """
        func (v Frank) foo (a, b int) {
            const v = 1;
            const a = 1;
        }

        type Frank struct {
            Frankie int;
        }

        func (v meow) foo () {
            const a = 1;
        }

        type meow struct {
            Frankie int;
        }

        func (v meow) foo (a, b int) {
            const a = 1;
        }
        """
        input = Program([MethodDecl("v",Id("Frank"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("v",None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))),StructType("Frank",[("Frankie",IntType())],[]),MethodDecl("v",Id("meow"),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))]))),StructType("meow",[("Frankie",IntType())],[]),MethodDecl("v",Id("meow"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([ConstDecl("a",None,IntLiteral(1))])))])
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
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b\n", inspect.stack()[0].function))
    
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
        var v Frank;
        const b = v.b;        
        type Frank struct {
            a int;
            b int;
            c int;
        }
        const a = v.a;
        const e = v.e;
        """
        input = Program([VarDecl("v",Id("Frank"), None),ConstDecl("b",None,FieldAccess(Id("v"),"b")),StructType("Frank",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("v"),"a")),ConstDecl("e",None,FieldAccess(Id("v"),"e"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", inspect.stack()[0].function))
        
    def test_025(self):
        """ 
        var v Frank;
        func foo ()  {
            var x = v;
            const a = x.a;
            const e = x.e;
        }
        type Frank struct {
            a int;
            b int;
            c int;
        }
        """
        input = Program([VarDecl("v",Id("Frank"), None),
			FuncDecl("foo",[],VoidType(),Block([VarDecl("x", None,Id("v")),ConstDecl("a",None,FieldAccess(Id("x"),"a")),ConstDecl("e",None,FieldAccess(Id("x"),"e"))])),
			StructType("Frank",[("a",IntType()),("b",IntType()),("c",IntType())],[])
		])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: e\n", inspect.stack()[0].function))
        
    def test_026(self): # 53
        """
        func foo () {
            var a = 1;
            var b = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    
    def test_026a(self): # 53
        """
        func foo () {
            var a = 1;
            var b = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
                a := 2;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1)),Assign(Id("a"),IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))

    def test_026b(self): # 53
        """
        func foo () {
            var a = 1;
            var b = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
                a := 2.5;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1)),Assign(Id("a"),FloatLiteral(2.5))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(a),FloatLiteral(2.5))\n", inspect.stack()[0].function))

    def test_026c(self): # 53
        """
        func foo () {
            var a = 1;
            var b = 1;
            for a, b := range [3]int {1, 2, 3} {
                var b = 1;
                var a = 2.5;
                
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,FloatLiteral(2.5))]))]))])
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
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
                         
    def test_028(self): # 69
        """
        var v Frank;       
        type Frank struct {
            a int;
        } 
        func (v Frank) foo() int {return 1;}
        func (b Frank) koo() {b.koo();}
        func foo() {
            const b = v.foo(); 
            v.koo(); 
            const d = v.zoo();
        }
        """
        input = Program([VarDecl("v",Id("Frank"), None),StructType("Frank",[("a",IntType())],[]),MethodDecl("v",Id("Frank"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("Frank"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("v"),"foo",[])),MethCall(Id("v"),"koo",[]),ConstDecl("d",None,MethCall(Id("v"),"zoo",[]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: zoo\n", inspect.stack()[0].function))
                 
    def test_029(self): # 49
        """
        func (v Frank) foo (a, b int) {
            var a = 1;
        }

        type Frank struct {
            Frankie int;
        }

        type meow struct {
            Frankie int;
        }

        func (v meow) foo (a, b int) {
            var a = 1;
        }
        """
        input = Program([MethodDecl("v",Id("Frank"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),StructType("Frank",[("Frankie",IntType())],[]),StructType("meow",[("Frankie",IntType())],[]),MethodDecl("v",Id("meow"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))

    def test_030(self):
        """
var a [2][3] int;
var b = a[1];
var c [3] int = b;
var d [1] string = b;
"""
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(1)]),Id(b))\n", inspect.stack()[0].function)) 
        
    def test_031(self):
        """
        type Frank struct {v int;}
        var v Frank;
        func foo(){
            for 1 {
                var a int = 1.2;
            }
        }
        """
        input = Program([StructType("Frank",[("v",IntType())],[]),VarDecl("v",Id("Frank"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
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
        func  Frankie() int {
            return Frankie();
            foo();
        }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("Frankie",[],IntType(),Block([Return(FuncCall("Frankie",[])),FuncCall("foo",[])]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(foo,[])\n", inspect.stack()[0].function))

    def test_035(self):
        """          
        type S1 struct {Frankie int;}
        type S2 struct {Frankie int;}
        var v S1;
        const x = v;
        var z S1 = x;
        var k S2 = x;
        """
        input = Program([StructType("S1",[("Frankie",IntType())],[]),StructType("S2",[("Frankie",IntType())],[]),VarDecl("v",Id("S1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("S1"),Id("x")),VarDecl("k",Id("S2"),Id("x"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(k,Id(S2),Id(x))\n", inspect.stack()[0].function))

    def test_036(self):
        """
func foo() {
    var a = 1.0 == 1
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,BinaryOp("==", FloatLiteral(1.0), IntLiteral(1)))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(FloatLiteral(1.0),==,IntLiteral(1))\n""", inspect.stack()[0].function))
    
    def test_037(self):
        """
func foo(a int) {
foo(1);
var foo = 1;
foo(2); // error
}
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([FuncCall("foo",[IntLiteral(1)]),VarDecl("foo", None,IntLiteral(1)),FuncCall("foo",[IntLiteral(2)])]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", inspect.stack()[0].function))
    
    def test_038(self):
        """
func main() {
    const a = 3
    var arr [2]int = [a]int{1, 2, 3}
    return ;
}
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(3)),VarDecl("arr",ArrayType([IntLiteral(2)],IntType()),ArrayLiteral([Id("a")],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Return(None)]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(arr,ArrayType(IntType,[IntLiteral(2)]),ArrayLiteral([Id(a)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n""", inspect.stack()[0].function))

    def test_039(self):
        """
var a int;
type a struct {
    name: string
}
        """
        input = Program([VarDecl("a",IntType(), None),StructType("a",[("name",StringType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: a\n""", inspect.stack()[0].function))
        
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

    def test_041(self): # 100
        """
var a = [1] S1  { S1 {v : z}};
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(1)],Id("S1"),[StructLiteral("S1",[("v",Id("z"))])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: S1\n", inspect.stack()[0].function))

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
        type I1 interface {Frankie();}
        type I2 interface {Frankie();}

        var v I1;
        const x = v;
        var z I1 = x;
        var k I2 = x; // sai o day
        """
        input = Program([InterfaceType("I1",[Prototype("Frankie",[],VoidType())]),InterfaceType("I2",[Prototype("Frankie",[],VoidType())]),VarDecl("v",Id("I1"), None),ConstDecl("x",None,Id("v")),VarDecl("z",Id("I1"),Id("x")),VarDecl("k",Id("I2"),Id("x"))])
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

    def test_047(self): # 96
        """ 
        var a = [2] int {1, 2}
        var c [3] int = a
        
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n", inspect.stack()[0].function))
    
    def test_048(self): # 102
        """ 
        var a [2][3] int;
        var b = a[1];
        var c [2] int = b;
        var d [1] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n", inspect.stack()[0].function))

    def test_049(self): # 107
        """ 
        type S1 struct {Frankie int;}
        type I1 interface {Frankie();}
        var a I1;
        var c I1 = nil;
        var d S1 = nil;
        func foo(){
            c := a;
            a := nil;
        }
        var e int = nil;
        """
        input = Program([StructType("S1",[("Frankie",IntType())],[]),InterfaceType("I1",[Prototype("Frankie",[],VoidType())]),VarDecl("a",Id("I1"), None),VarDecl("c",Id("I1"),NilLiteral()),VarDecl("d",Id("S1"),NilLiteral()),FuncDecl("foo",[],VoidType(),Block([Assign(Id("c"),Id("a")),Assign(Id("a"),NilLiteral())])),VarDecl("e",IntType(),NilLiteral())])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,IntType,Nil)\n", inspect.stack()[0].function))

    def test_050(self): # 124
        """ 
        func foo(){
            var arr [2] int;
            const a = 2
            b := 3
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),ConstDecl("a",None,IntLiteral(2)),Assign(Id("b"),IntLiteral(3)),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b")),VarDecl("e",StringType(),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,StringType,Id(a))\n", inspect.stack()[0].function))

    def test_050a(self): # 124
        """ 
        func foo(){
            var arr [2] int;
            const a = 2
            b := 3.5
            for a, b := range arr {
                var c int = a;
                var d int = b;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),ConstDecl("a",None,IntLiteral(2)),Assign(Id("b"),FloatLiteral(3.5)),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b"))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: ForEach(Id(a),Id(b),Id(arr),Block([VarDecl(c,IntType,Id(a)),VarDecl(d,IntType,Id(b))]))\n", inspect.stack()[0].function))

    def test_051(self): # 126
        """ 
        func foo(){
            var arr [2] int;
            var a int;
            const b = 1;
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),VarDecl("a",IntType(), None),ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b")),VarDecl("e",StringType(),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(e,StringType,Id(a))\n", inspect.stack()[0].function))

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
type FRANK struct {
    Frankie int;
}
func (v FRANK) foo (v int) {return;}
func foo () {return;}   
        """
        input = Program([StructType("FRANK",[("Frankie",IntType())],[]),MethodDecl("v",Id("FRANK"),FuncDecl("foo",[ParamDecl("v",IntType())],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
        
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
        """               
        func foo(){
            var arr [2] int;
            var b int = 3;
            for a, b := range arr {
                var c int = a;
                var d int = b;
                var e string = a;
            }
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2)],IntType()), None),VarDecl("b",IntType(), IntLiteral(3)),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",IntType(),Id("b")),VarDecl("e",StringType(),Id("a"))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: a\n", inspect.stack()[0].function))

    def test_058(self):
        """
func foo()  {return ;}
func frankie() int {
    foo();
    return frankie();
}
     
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("frankie",[],IntType(),Block([FuncCall("foo",[]),Return(FuncCall("frankie",[]))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_058a(self):
        input = """
        func foo()  {return ;}
        func frankie() int {
            foo();
            return frankie(foo());
        }
     
        """
        # input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("frankie",[],IntType(),Block([FuncCall("foo",[]),Return(FuncCall("frankie",[FuncCall("foo",[])]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(frankie,[FuncCall(foo,[])])\n""", inspect.stack()[0].function))
        
    def test_059(self):
        """               
        type Person struct {
            name string ;
            age int ;
        }
        func  Frankie()  {
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
            FuncDecl("Frankie", [], VoidType(), Block([
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
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    
    def test_060(self):
        """
func getString() {return;}
        """
        input = Program([FuncDecl("getString",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: getString\n", inspect.stack()[0].function))

    def test_061(self):
        """
var v Frank;      
type Frank struct {
    a int;
} 
type meow interface {
    foo() int;
}

func (v Frank) foo() int {return 1;}
func (b Frank) koo() {b.koo();}
func foo() {
    var x MEOW;  
    const b = x.foo(); 
    x.koo(); 
}
        """
        input = Program([VarDecl("v",Id("Frank"), None),StructType("Frank",[("a",IntType())],[]),InterfaceType("meow",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("Frank"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("Frank"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("meow"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo\n", inspect.stack()[0].function))

    def test_062(self):
        """
func (v Frankie) f1 (c A1) int {
    var e int = 10;
}
"""
        input = Program([
    MethodDecl(
        receiver="v",  # Receiver name
        recType=Id("Frankie"),  # Receiver type as an Id
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
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: Frankie\n", inspect.stack()[0].function))

    def test_063(self):
        """
var a [2][3] int;
var b = a[1];
var c [2] int = b;
var d [1] string = b;
"""
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(2)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(1)],StringType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n", inspect.stack()[0].function)) 

    def test_064(self):
        i = Program([
            VarDecl("x1", None, IntLiteral(0)),
            StructType("x1", [], [])
        ])
        self.assertTrue(TestChecker.test(i, "Redeclared Type: x1\n", inspect.stack()[0].function))

    def test_065(self):
        i = Program([
            VarDecl("x1", None, IntLiteral(0)),
            InterfaceType("x1", [])
        ])
        self.assertTrue(TestChecker.test(i, "Redeclared Type: x1\n", inspect.stack()[0].function))
    
    def test_066(self):
        """var A int; var B int; type A struct {Frankie int;}"""
        i = Program([VarDecl("A", IntType(), None), VarDecl("B", IntType(), None), StructType("A", [("Frankie", IntType())], [])])
        self.assertTrue(TestChecker.test(i, "Redeclared Type: A\n", inspect.stack()[0].function))

    def test_067(self):     # 176
        """
    type A interface {foo();}
    const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]), ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A\n""", inspect.stack()[0].function)) 

    def test_068(self):     # 181
        """
func foo(a [2] float) {
    foo([2] float {1.0,2.0})
    foo([2] int {1,2})
}
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)])])\n""", inspect.stack()[0].function)) 


    def test_069(self):     # 190
        """
const v = 3;
const a = v + v;
var b [a * 2 + a] int;
var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_070(self):     # 28
        """
type Frank interface {
    foo();
}
func Frank() {return;}
func foo() {return;}
func Frank() {return;}
        """
        input = Program([InterfaceType("Frank",[Prototype("foo",[],VoidType())]),FuncDecl("Frank",[],VoidType(),Block([Return(None)])),FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("Frank",[],VoidType(),Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Function: Frank\n""", inspect.stack()[0].function))

    def test_071(self):     # 167
        """
func foo() int {
    var a = 1;
    if (a < 3) {
        var a = 1;
    } else if(a > 2) {
        var a = 2;
    }
    return a;
}
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_072(self):
        """
type FRANK struct {
    Frankie int;
}
func (v FRANK) Frankie () {return ;}
        """
        input = Program([StructType("FRANK",[("Frankie",IntType())],[]),MethodDecl("v",Id("FRANK"),FuncDecl("Frankie",[],VoidType(),Block([Return(None)])))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Frankie\n""", inspect.stack()[0].function))
    
    def test_073(self):     # 97
        """
var a = [2] int {1, 2}
var c [2] float = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(2)],FloatType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_074(self):
        """
func foo() [2] float {
    return [2] float {1.0, 2.0};
    return [2] int {1, 2};
}
            
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(ArrayLiteral([IntLiteral(2)],IntType,[IntLiteral(1),IntLiteral(2)]))\n""", inspect.stack()[0].function))

    def test_075(self):
        """
var a [5 % 2] int;
var b [1] int = a;        
        """    
        input = Program([VarDecl("a",ArrayType([BinaryOp("%", IntLiteral(5), IntLiteral(2))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(1)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_076(self):     # 191
        """
const v = 3;
var c [3] int = [v * 1] int {1 , 2, 3};
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([BinaryOp("*", Id("v"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_077(self):     # 192
        """
const v = 3;
const k = v + 1;
func foo(a [1 + 2] int) {
    foo([k - 1] int {1,2,3})
}         
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_078(self):     # 192a
        """
const k = 4;
func foo(a [3] int) {
    foo([k - 1] int {1,2,3})
}                
        """
        input = Program([ConstDecl("k",None,IntLiteral(4)),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(3)],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_079(self):     # 192b
        """
const v = 3;
const k = v + 1;
func foo(a [3] int) {
    foo([k - 1] int {1,2,3})
}                
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("v"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(3)],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_080(self):     # 192c
        """
func foo(a [1 + 2] int) {
    foo([3] int {1,2,3})
}                
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_081(self):     # 144
        """

func foo() int {
    return [2] int {1, 2}[a];
}

var a = foo();
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(ArrayCell(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),[Id("a")]))])),VarDecl("a", None,FuncCall("foo",[]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: a\n""", inspect.stack()[0].function))
    
    def test_082(self):     # 194
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

    def test_083(self):     # 194a
        """
type K struct {a int;}
func (k K) koo(a [3] int) {return;}
type H interface {koo(a [3] int);}

const c = 4;
func foo() {
    var k H;
    k.koo([c - 1] int {1,2,3})
}         
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([IntLiteral(3)],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([IntLiteral(3)],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))


    def test_084(self):     # 195
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

    def test_085(self):     # 195a
        """
type K struct {a int;}
func (k K) koo(a [1 + 2] int) [3] int {return [3*1] int {1,2,3};}
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
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([IntLiteral(3)],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(4)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("foo",[])),VarDecl("k",Id("K"), None),Return(MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),VarDecl("h",Id("H"), None),Return(MethCall(Id("h"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_086(self): # 199
        """
        const a = 3;
        const b = -a;
        const c = -b;
        var d [c] int = [3] int {1,2,3}
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 
    
    def test_087(self): # 202
        """
        func foo() {
            a := 1;
            var a = 1;
        }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a\n""", inspect.stack()[0].function)) 

    def test_088(self): # 204
        """
        const a = 1;
        func foo() {
            a := 1.;
        }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Assign(Id(a),FloatLiteral(1.0))\n""", inspect.stack()[0].function)) 
            
    def test_089(self):     # Hao
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
        
    def test_090(self):     # Hao1
        """
        var v = 2 * 3;
        const a = v + 1;
        const b = a * 5;
        const c = ! (b > 3);
        """
        input = Program([VarDecl("v", None,BinaryOp("*", IntLiteral(2), IntLiteral(3))),ConstDecl("a",None,BinaryOp("+", Id("v"), IntLiteral(1))),ConstDecl("b",None,BinaryOp("*", Id("a"), IntLiteral(5))),ConstDecl("c",None,UnaryOp("!",BinaryOp(">", Id("b"), IntLiteral(3))))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 

    def test_091(self):
        input = """
        func main() {
            for i := 0; i < 10; c += 1 {
                var c = 5
                i += 1 
            }            
        }
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c\n""", inspect.stack()[0].function))
    
    def test_092(self):
        """
type Frank struct {a [2]int;} 
type MEOW interface {foo() int;}

func (v Frank) foo() int {return 1;}

func foo(a MEOW) {
    var b = Frank{a: [2]int{1, 2}};
    foo(b)
}
        """
        input = Program([StructType("Frank",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("MEOW",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("Frank"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[ParamDecl("a",Id("MEOW"))],VoidType(),Block([VarDecl("b",Id("Frank"), StructLiteral("Frank",[("a", ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1), IntLiteral(2)]))])),FuncCall("foo",[Id("b")])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[Id(b)])\n""", inspect.stack()[0].function))
    
    def test_093(self):
        """
func (v FRANK) MEOW () {return ;}
func (v FRANK) Frank () {return ;}
type FRANK struct {
    Frankie int;
    Frank int;
}
        """
        input = Program([MethodDecl("v",Id("FRANK"),FuncDecl("MEOW",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("FRANK"),FuncDecl("Frank",[],VoidType(),Block([Return(None)]))),StructType("FRANK",[("Frankie",IntType()),("Frank",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Frank\n""", inspect.stack()[0].function))
    
    def test_094(self):
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

    def test_095(self):
        """
var a [1 + 9] int;
var b [10] int = a;
        """
        input = Program([VarDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(9))],IntType()), None),VarDecl("b",ArrayType([IntLiteral(10)],IntType()),Id("a"))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function)) 

    def test_096(self):
        """
var A = 1;
type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Type: A\n""", inspect.stack()[0].function)) 

    def test_097(self):
        """
var a Frank;
func foo() Frank {
    return a;
    return Frank;
}

type Frank struct {Frank int;}
        """
        input = Program([VarDecl("a",Id("Frank"), None),FuncDecl("foo",[],Id("Frank"),Block([Return(Id("a")),Return(Id("Frank"))])),StructType("Frank",[("Frank",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: Frank\n""", inspect.stack()[0].function))
    
    def test_098(self):
        """
var v Frank;      
type Frank struct {
    a int;
} 
type MEOW interface {
    foo() int;
}

func (v Frank) foo() int {return 1;}
func (b Frank) koo() {b.koo();}
func foo() {
    var x MEOW;  
    const b = x.foo(); 
    x.koo(); 
}
        """
        input = Program([VarDecl("v",Id("Frank"), None),StructType("Frank",[("a",IntType())],[]),InterfaceType("MEOW",[Prototype("foo",[],IntType())]),MethodDecl("v",Id("Frank"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("Frank"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("MEOW"), None),ConstDecl("b",None,MethCall(Id("x"),"foo",[])),MethCall(Id("x"),"koo",[])]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: koo\n", inspect.stack()[0].function)) 

    def test_099(self):
        """
func foo () {
    const a = 1;
    for a, b := range [3]int {1, 2, 3} {
        var b = 1;
    }
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b\n", inspect.stack()[0].function))

    def test_100(self):
        """
for var x = 0; x < 10; x += 1 {
    if (x > 2) {
        var x float = 2.0
    }
}
        """
        input = Program([
    ForStep(
        init=VarDecl("x", IntType(), IntLiteral(0)),   # Initialization of x to 0 (Variable Declaration)
        cond=BinaryOp("<", Id("x"), IntLiteral(10)),    # Condition x < 10
        upda=Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),  # Update x += 1
        loop=Block([    # Loop body
            If(
                expr=BinaryOp(">", Id("x"), IntLiteral(2)),    # If condition: x > 2
                thenStmt=Block([
                    VarDecl("x", FloatType(), FloatLiteral(2.0))  # Declaration of a new variable x (shadowing)
                ]),
                elseStmt=None
            )
        ])
    )
])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))

    def test_101(self):    # 208
        """
func Frankie (b int) {
    for var a = 1; c < 1; a += c {
        const c = 2;
    }
}
        """
        input = Program([FuncDecl("Frankie",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c\n""", inspect.stack()[0].function)) 
    
    def test_102(self):     # 202
        """
func foo() {
    a := 1;
    var a = 1;
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Redeclared Variable: a\n""", inspect.stack()[0].function)) 
    
    def test_103(self):     # 210
        """
var v FRANK;
func (v FRANK) foo (v int) int {
    return v;
}

type FRANK struct {
    Frankie int;
}
        """
        input = Program([VarDecl("v",Id("FRANK"), None),MethodDecl("v",Id("FRANK"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("FRANK",[("Frankie",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "", inspect.stack()[0].function))
    
    def test_104(self):
        """
var a int;
func (v FRANK) foo () int {
    return a;
    return v;
}
type FRANK struct {
    Frankie int;
}
        """
        input = Program([VarDecl("a",IntType(), None),MethodDecl("v",Id("FRANK"),FuncDecl("foo",[],IntType(),Block([Return(Id("a")),Return(Id("v"))]))),StructType("FRANK",[("Frankie",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(Id(v))\n""", inspect.stack()[0].function))
    
    def test_105(self):
        """
var a int;
type b struct {c:int;};
func (x b) a() {return 1};
func (x b) c() {return 1};        
        """
        input = Program([VarDecl("a",IntType(), None),StructType("b",[("c",IntType())],[]),MethodDecl("x",Id("b"),FuncDecl("a",[],VoidType(),Block([Return(IntLiteral(1))]))),MethodDecl("x",Id("b"),FuncDecl("c",[],VoidType(),Block([Return(IntLiteral(1))])))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: c\n""", inspect.stack()[0].function))
    
    def test_106(self):
        """
func foo() {
    return;
}   
func frankie() {
    foo();
    return foo();
}     
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("frankie",[],VoidType(),Block([FuncCall("foo",[]),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", inspect.stack()[0].function))
    
    def test_107(self):
        """
type S1 struct {frank int;}
        
func foo() {
    return;
}   
func (s S1) frankie() int {
    foo();
    return 2.5;
}     
        """
        input = Program([StructType("S1",[("frank",IntType())],[]),FuncDecl("foo",[],VoidType(),Block([Return(None)])),MethodDecl("s",Id("S1"),FuncDecl("frankie",[],IntType(),Block([FuncCall("foo",[]),Return(FloatLiteral(2.5))])))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: Return(FloatLiteral(2.5))\n""", inspect.stack()[0].function))
    
    def test_108(self):
        """
func foo() int {
    const foo = 1;
    return foo()
}
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo\n""", inspect.stack()[0].function))
    
    def test_109(self):
        """var a int; func (x b) c() {...}; type b struct {c:int;}; func (x b) a() {...};"""
        input = Program([VarDecl("a",IntType(), None),MethodDecl("x",Id("b"),FuncDecl("c",[],VoidType(),Block([Return(None)]))),StructType("b",[("c",IntType())],[]),MethodDecl("x",Id("b"),FuncDecl("a",[],VoidType(),Block([Return(None)])))])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: c\n""", inspect.stack()[0].function))
    
    def test_110(self):
        """
func foo(){
    return;
}
func foo1 (x int) int {
    return 1;
}
func main(){
    foo1(foo())
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)])),FuncDecl("foo1",[ParamDecl("x",IntType())],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("main",[],VoidType(),Block([FuncCall("foo1",[FuncCall("foo",[])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", inspect.stack()[0].function))
    
    def test_111(self):
        input = """
        func main() {
            var a int; var b int; var c int; 
            for a,b := range c {var d = 0;}
        }
        """
        self.assertTrue(TestChecker.test(input, """Type Mismatch: ForEach(Id(a),Id(b),Id(c),Block([VarDecl(d,IntLiteral(0))]))\n""", inspect.stack()[0].function))
    
    def test_112(self):
        input = """
            func main() {
                var a int; a := a + "str";
            }
        """
        # Type Mismatch: BinaryOp(Id(a),+,StringLiteral("str"))
        self.assertTrue(TestChecker.test(input, """Type Mismatch: BinaryOp(Id(a),+,StringLiteral("str"))\n""", inspect.stack()[0].function))
    
    def test_113(self):
        input = """
        func main() {
            arr := [3]int{10, 20, 30}
            value := 0
            for _, value := range arr {
                break;
            }
        }
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
        
    
    def test_114(self):
        """
type S struct {}
var a = [5]int{1,2,3,4,5};
func (s S) foo() [2+3]int { return a; }
        """
        input = Program([StructType("S",[],[]),VarDecl("a",ArrayType([IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),MethodDecl("s",Id("S"),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(2), IntLiteral(3))],IntType()),Block([Return(Id("a"))])))])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_115(self):
        input = """
type X struct {
    x X;
}
const x = X{}.x.x.x.x.x.x;
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_116(self):
        input = """
type X struct {y Y;}
type Y struct {x X;}
const x = X{}.y.x.y.x.y.x;
        """
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))

    def test_117(self):
        input = """
type X struct {y Y;}
type Y struct {x X;}
const x = X{}.y.x.y.x.y.y;
        """
        self.assertTrue(TestChecker.test(input, """Undeclared Field: y\n""", inspect.stack()[0].function))
    
#     def test_118(self):
#         """
# const q = X{}.y
# type X struct {
#     y [q]int
# }
#         """
#         input = Program([
#                 ConstDecl("q", None, FieldAccess(StructLiteral("X", []), "y")),
#                 StructType("X", [("y", ArrayType([Id("q")], IntType()))], [])
#             ])
#         self.assertTrue(TestChecker.test(input, "Type Mismatch: Id(q)\n", inspect.stack()[0].function))

    def test_118(self):
        """var a [3][2]int = [3][2]int {{2,3},{1,2},{4,5}}"""
        input = Program([
    VarDecl(
        "a",
        ArrayType([IntLiteral(3), IntLiteral(2)], IntType()),
        ArrayLiteral(
            [IntLiteral(3), IntLiteral(2)],
            IntType(),
            [
                [IntLiteral(2), IntLiteral(3)],
                [IntLiteral(1), IntLiteral(2)],
                [IntLiteral(4), IntLiteral(5)]
            ]
        )
    )
])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_119(self):
        """var a [3][3]int = [3][2]int {{2,3},{1,2},{4,5}}"""
        input = Program([
    VarDecl(
        "a",
        ArrayType([IntLiteral(3), IntLiteral(3)], IntType()),
        ArrayLiteral(
            [IntLiteral(3), IntLiteral(2)],
            IntType(),
            [
                [IntLiteral(2), IntLiteral(3)],
                [IntLiteral(1), IntLiteral(2)],
                [IntLiteral(4), IntLiteral(5)]
            ]
        )
    )
])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: VarDecl(a,ArrayType(IntType,[IntLiteral(3),IntLiteral(3)]),ArrayLiteral([IntLiteral(3),IntLiteral(2)],IntType,[[IntLiteral(2),IntLiteral(3)],[IntLiteral(1),IntLiteral(2)],[IntLiteral(4),IntLiteral(5)]]))\n""", inspect.stack()[0].function))

    def test_120(self):
        """var a [3][2]int = [3][2]int {1,2,3,4,5}"""
        input = Program([
    VarDecl(
        "a",
        ArrayType([IntLiteral(3), IntLiteral(2)], IntType()),
        ArrayLiteral(
            [IntLiteral(3), IntLiteral(2)],
            IntType(),
            [
                [IntLiteral(1), IntLiteral(2)],
                [IntLiteral(3), IntLiteral(4)],
                [IntLiteral(5)]
            ]
        )
    )
])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_121(self):
        """
var e  = 3 ;
var d  [2]int
func c(a int,b int) [e]int {
    e += 1 ;
    var a [e]int
    return a
}     
        """
        input = Program([
    VarDecl("e", None, IntLiteral(3)),
    VarDecl("d", ArrayType([IntLiteral(2)], IntType()), None),
    FuncDecl("c", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], ArrayType([Id("e")], IntType()), Block([
        Assign(Id("e"), BinaryOp("+", Id("e"), IntLiteral(1))),
        VarDecl("a", ArrayType([Id("e")], IntType()), None),
        Return(Id("a"))
    ]))
])
        self.assertTrue(TestChecker.test(input, """""", inspect.stack()[0].function))
    
    def test_122(self):
        """
        func foo() {
            return foo()
        };
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo,[])\n""", inspect.stack()[0].function))
    
    def test_123(self):
        """
func foo1 (x int){
    return ;
}
func main(){
    foo1(2.5)
}
        """
        input = Program([FuncDecl("foo1",[ParamDecl("x",IntType())],VoidType(),Block([Return(None)])),FuncDecl("main",[],VoidType(),Block([FuncCall("foo1",[FloatLiteral(2.5)])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall(foo1,[FloatLiteral(2.5)])\n""", inspect.stack()[0].function))
    
    def test_124(self):
        """

        func main(a int, b int){
            var x int
            var y int
            var a [6]float = [6]int{1,2,3,4,5,6};     
            for x,y := range a{
                c:=5;
            }
            var d = x
        };
        """
        input = Program([
            FuncDecl("main",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([
                VarDecl("x",IntType(), None),
                VarDecl("y",IntType(), None),
                VarDecl("a", ArrayType([IntLiteral(6)], FloatType()), ArrayLiteral([IntLiteral(6)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5), IntLiteral(6)])),
                ForEach(Id("x"), Id("y"), Id("a"), Block([
                    Assign(Id("c"), IntLiteral(5))
                ])),
                VarDecl("d", None, Id("x"))
            ]))
        ])
        expect = "Type Mismatch: ForEach(Id(x),Id(y),Id(a),Block([Assign(Id(c),IntLiteral(5))]))\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_125(self):
        input = """
        func foo() {
            foo := 1
            foo()
        }
        """
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    
        
        