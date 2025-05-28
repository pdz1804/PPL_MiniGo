# 2252378
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const Meow = foo( 1 ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[IntLiteral(1)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 501))

    def test_002(self):
        input = """const Meow = foo( 1.0,true,false,nil,\"Meow\" ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("\"Meow\"")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 502))

    def test_003(self):
        input = """const Meow = foo( id ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[Id("id")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 503))

    def test_004(self):
        input = """const Meow = foo( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 504))

    def test_005(self):
        input = """const Meow = foo( a > b <= c ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 505))

    def test_006(self):
        input = """const Meow = foo( a[2][3] ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 506))

    def test_007(self):
        input = """const Meow = foo( a.b.c ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 507))

    def test_008(self):
        input = """const Meow = foo( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 508))

    def test_009(self):
        input = """const Meow = foo( a * (1+2) ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 509))

    def test_010(self):
        input = """const Meow = foo( Meow {}, Meow {a: 1} ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[StructLiteral("Meow",[]),StructLiteral("Meow",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 510))

    def test_011(self):
        input = """const Meow = foo( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 511))

    def test_012(self):
        input = """
            var Meow = 1;
            var Meow int;
            var Woof int = 1;
"""
        expect = Program([VarDecl("Meow", None,IntLiteral(1)),
			VarDecl("Meow",IntType(), None),
			VarDecl("Woof",IntType(),IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 512))

    def test_013(self):
        input = """
            func foo() int {return;}
            func foo(a int, b int) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 513))

    def test_014(self):
        input = """
            func (Meow v) foo(Meow int) {return;}
"""
        expect = Program([MethodDecl("Meow",Id("v"),FuncDecl("foo",[ParamDecl("Meow",IntType())],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 514))


    def test_015(self):
        input = """
            type Meow struct {
                a int;
            }
"""
        expect = Program([StructType("Meow",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 515))


    def test_016(self):
        input = """
            type Meow struct {
                a int;
            }
"""
        expect = Program([StructType("Meow",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 516))

    def test_017(self):
        input = """
            func Meow() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 517))

    def test_018(self):
        input = """
            func Meow() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 518))

    def test_019(self):
        input = """
            func Meow() {
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 519))

    def test_020(self):
        input = """
            func Meow() {
                foo(1, 2);
                a[2].foo(1,3);
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"foo",[IntLiteral(1),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 520))

    def test_021(self):
        input = """
            func Meow() {
                if(1) {return;}
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 521))

    def test_022(self):
        input = """
            func Meow() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 522))

    def test_023(self):
        input = """
            func Meow() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), 
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 523))


    def test_024(self):
        input = """
            func Meow() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 524))

    def test_025(self):
        input = """
            func Meow() {
                for index, value := range array[2] {return;}
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 525))

    def test_026(self):
        input = """
            const a = true + false - true;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 526))

    def test_027(self):
        input = """
            const a = 1 && 2 || 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 527))

    def test_028(self):
        input = """
            const a = 1 + 2 && 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 528))

    def test_029(self):
        input = """
            const a = 1 - 2 % 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 529))

    def test_030(self):
        input = """
            const a = 1 + -2 - 1;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 530))

    def test_031(self):
        input = """
            const a = [1]ID{Meow{}};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("Meow",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 531))

    def test_032(self):
        input = """
            const a = [1][3]float{1.0e+2};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral(100.0)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 532))

    def test_033(self):
        input = """
            const a = ID{a: 1, b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 533))
    
    def test_034(self):
        input = """
            const a = ID{a: [1]int{1}};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 534))


    def test_035(self):
        input = """
            const a = ID{b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 535))

    def test_036(self):
        input = """
            const a = 0 && 1 && 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("&&", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 536))

    def test_037(self):
        input = """
            const a = 0 || 1 || 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 537))

    def test_038(self):
        input = """
            const a = 0 >= 1 <= 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 538))

    def test_039(self):
        input = """
            const a = 0 + 1 - 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 539))

    def test_040(self):
        input = """
            const a = 0 * 1 / 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("/", BinaryOp("*", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 540))

    def test_041(self):
        input = """
            const a = !-!2;
"""
        expect = Program([ConstDecl("a",None,UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2)))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 541))

    def test_042(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 542))

    def test_043(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 543))

    def test_044(self):
        input = """
            const a = 1 >= 2 + 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 544))

    def test_045(self):
        input = """
            const a = a[1][2][3][4];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 545))

    def test_046(self):
        input = """
            const a = a[1 + 2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 546))

    def test_047(self):
        input = """
            const a = a.b.c.d.e;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 547))

    def test_048(self):
        input = """
            const a = ID {}.a;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(StructLiteral("ID",[]),"a"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 548))

    def test_049(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 549))

    def test_050(self):
        input = """
            const a = a.b().c().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 550))

    def test_051(self):
        input = """
            const a = a().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(FuncCall("a",[]),"d",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 551))

    def test_052(self):
        input = """
            const a = a[1].b.c()[2].d.e();
"""
        expect = Program([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 552))
    
    def test_053(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("\"a\""))))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 553))

    def test_054(self):
        input = """
            const a = f() + f(1 + 2, 3.);
"""
        expect = Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral(3.0)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 554))

    def test_055(self):
        input = """
            const a = foo()[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 555))

    def test_056(self):
        input = """
            const a = a;
"""
        expect = Program([ConstDecl("a",None,Id("a"))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 556))

    def test_057(self):
        input = """
            var a Meow = 1.;
"""
        expect = Program([VarDecl("a",Id("Meow"),FloatLiteral(1.0))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 557))

    def test_058(self):
        input = """
            var a [2][3]int;
"""
        expect = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 558))
    
    def test_059(self):
        input = """
            var a = 1;
"""
        expect = Program([VarDecl("a", None,IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 559))

    def test_060(self):
        input = """
            type Meow struct {
                a int;
            }
"""
        expect = Program([StructType("Meow",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 560))
    
    def test_061(self):
        input = """
            type Meow struct {
                a int;
            }
"""
        expect = Program([StructType("Meow",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 561))

    def test_062(self):
        input = """
            type Meow struct {
                a  int;
                b  boolean;
                
            }
"""
        expect = Program([StructType("Meow",[("a",IntType()),("b",BoolType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 562))

    def test_063(self):
        input = """
            type Meow struct {
                a  int;
                b  boolean;
                c  [2]Meow;
            }
"""
        expect = Program([StructType("Meow",[("a",IntType()),("b",BoolType()),("c",ArrayType([IntLiteral(2)],Id("Meow")))],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 563))

    def test_064(self):
        input = """
            type Meow interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 564))

    def test_065(self):
        input = """
            type Meow interface {
                Add(a int) ;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 565))

    def test_066(self):
        input = """
            type Meow interface {
                Add(a int, b int) ;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 566))

    def test_067(self):
        input = """
            type Meow interface {
                Add(a, c int, b int) ;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[IntType(),IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 567))

    def test_068(self):
        input = """
            type Meow interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 568))

    def test_069(self):
        input = """
            type Meow interface {
                Add() [2]string;
                Add() ID;
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 569))

    def test_070(self):
        input = """
            type Meow interface {
                Add();
            }
"""
        expect = Program([InterfaceType("Meow",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 570))


    def test_071(self):
        input = """
            func foo() {return;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 571))

    def test_072(self):
        input = """
            func foo(a [2]ID) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 572))


    def test_073(self):
        input = """
            func foo(a int, b [1]int) {return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 573))

    def test_074(self):
        input = """
            func foo() [2]int {return;}
"""
        expect = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 574))

    def test_075(self):
        input = """
            func (Cat c) foo() {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 575))

    def test_076(self):
        input = """
            func  (Cat c) foo(a [2]ID) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 576))


    def test_077(self):
        input = """
            func  (Cat c) foo(a int, b [1]int) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 577))

    def test_078(self):
        input = """
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 578))

    def test_079(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {foo();} 
            func foo(){return;}
            func  (Cat c) foo() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("foo",[],VoidType())]),
			FuncDecl("foo",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 579))

    def test_080(self):
        input = """
            func foo(a,b,c,d [ID][2][c] ID ){return;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 580))

    def test_081(self):
        input = """
            func foo(){
                const a = 1.;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 581))


    def test_082(self):
        input = """
            func foo(){
                var a = 1.;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 582))

    def test_083(self):
        input = """
            func foo(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 583))

    def test_084(self):
        input = """
            func foo(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 584))

    def test_085(self):
        input = """
            func foo(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 585))

    def test_086(self):
        input = """
            func foo(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 586))

    def test_087(self):
        input = """
            func foo(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 587))

    def test_088(self):
        input = """
            func foo(){
                a["s"][foo()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("\"s\""),FuncCall("foo",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 588))

    def test_089(self):
        input = """
            func foo(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 589))

    def test_090(self):
        input = """
            func foo(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 590))

    def test_091(self):
        input = """
            func foo(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 591))

    def test_092(self):
        input = """
            func foo(){
                return;
                return foo() + 2;
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("foo",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 592))

    def test_093(self):
        input = """
            func foo(){
                foo();
                foo(foo(), 2);
                a.foo();
                a[2].c.foo(foo(), 2);
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([FuncCall("foo",[]),FuncCall("foo",[FuncCall("foo",[]),IntLiteral(2)]),MethCall(Id("a"),"foo",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"foo",[FuncCall("foo",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 593))

    def test_094(self):
        input = """
            func foo(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 594))

    def test_095(self):
        input = """
            func foo(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 595))

    def test_096(self):
        input = """
            func foo(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 596))

    def test_097(self):
        input = """
            func Meow() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 597))

    def test_098(self):
        input = """
            func Meow() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 598))

    def test_099(self):
        input = """
            func Meow() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 599))

    def test_100(self):
        input = """
            func Meow() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return " MEWING ";
            };
"""
        expect = Program([FuncDecl("Meow",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("\"2\"")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("\" MEWING \""))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 600))
    
    def test_101(self):
        input = """const Meow = 1; """
        expect = Program([ConstDecl("Meow", None, IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 601))

    def test_102(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const Meow = 0b11; """
        expect = Program([ConstDecl("Meow", None, IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 602))

    def test_103(self):
        input = """const Meow = 0o70; """
        expect = Program([ConstDecl("Meow", None, IntLiteral(56))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 603))

    def test_104(self):
        input = """const Meow = 0Xa1; """
        expect = Program([ConstDecl("Meow", None, IntLiteral("161"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 604))

    def test_105(self):
        input = """const Meow = 01.e-1; """
        expect = Program([ConstDecl("Meow", None, FloatLiteral("0.1"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 605))

    def test_106(self):
        input = """const Meow = true; """
        expect = Program([ConstDecl("Meow", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 606))

    def test_107(self):
        input = """const Meow = false; """
        expect = Program([ConstDecl("Meow", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 607))

    def test_108(self):
        input = """const Meow = "Meow"; """
        expect = Program([ConstDecl("Meow", None, StringLiteral("\"Meow\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 608))

    def test_109(self):
        input = """const Meow = nil; """
        expect = Program([ConstDecl("Meow", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 609))
    
    def test_110(self):
        input = """const Meow = STRUCT {}; """
        expect = Program([ConstDecl("Meow", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 610))

    def test_111(self):
        input = """const Meow = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("Meow", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 611))

    def test_112(self):
        input = """const Meow = [ID] int {1}; """
        expect = Program([ConstDecl("Meow", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 612))

    def test_113(self):
        input = """const Meow = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("Meow", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 613))

    def test_114(self):
        input = """const Meow = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("Meow", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 614))

    def test_115(self):
        input = """const Meow = 1 || 2 || 3; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 615))

    def test_116(self):
        input = """const Meow = 1 && 2 && 3; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 616))

    def test_117(self):
        input = """const Meow = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 617))
    
    def test_118(self):
        input = """const Meow = 1 + 2 - 3; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 618))

    def test_119(self):
        input = """const Meow = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 619))

    def test_120(self):
        input = """const Meow = ! - 1; """
        expect = Program([ConstDecl("Meow", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 620))

    def test_121(self):
        input = """const Meow = a; """
        expect = Program([ConstDecl("Meow", None, Id("a"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 621))

    def test_122(self):
        input = """const Meow = (1+2)*3; """
        expect = Program([ConstDecl("Meow", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 622))

    def test_123(self):
        input = """const Meow = foo(); """
        expect = Program([ConstDecl("Meow", None, FuncCall("foo",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 623))

    def test_124(self):
        input = """const Meow = foo(1, 2); """
        expect = Program([ConstDecl("Meow", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 624))

    def test_125(self):
        input = """const Meow = a[2][3]; """
        expect = Program([ConstDecl("Meow",None,ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 625))

    def test_126(self):
        input = """const Meow = a.b.c; """
        expect = Program([ConstDecl("Meow", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 626))

    def test_127(self):
        input = """const Meow = a.b().c(1, 2); """
        expect = Program([ConstDecl("Meow", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 627))

    def test_128(self):
        input = """const Meow = a.b[2].c.d(); """
        expect = Program([ConstDecl("Meow", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 628))

    def test_129(self):
        input = """
    var a int = 1;
    var a float = 1;
    var a boolean;
    var a string = 1;
    var a = 1;
    var a ID = 1;
    var a [ID][1] int = 1;
"""
        expect = Program([VarDecl("a",IntType(),IntLiteral(1)),
			VarDecl("a",FloatType(),IntLiteral(1)),
			VarDecl("a",BoolType(), None),
			VarDecl("a",StringType(),IntLiteral(1)),
			VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",Id("ID"),IntLiteral(1)),
			VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 629))


    def test_130(self):
        input = """
    const a = 1;
"""
        expect = Program([ConstDecl("a",None,IntLiteral(1))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 630))

    def test_131(self):
        input = """
    type ID struct {
        a int;
        b ID;
        c [2]int;
    }
"""
        expect = Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 631))

    def test_132(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 632))

    def test_133(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 633))


    def test_134(self):
        input = """
    func (ID ID) foo () {var a = 1;}
    func (ID ID) foo () int {var a = 1;}
    func (ID ID) foo () [2] ID {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 634))

    def test_135(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 635))

    def test_136(self):
        input = """
        type INTERFACE interface {
            foo();
            foo() int;
            foo() [2]ID;
            foo(a int);
            foo(a int, b int);
            foo(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 636))

    def test_137(self):
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 637))


    def test_138(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 638))

    def test_139(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 639))


    def test_140(self):
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 640))

    def test_141(self):
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 641))
    
    def test_142(self):
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 642))

    def test_143(self):
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 643))

    def test_144(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 644))

    def test_145(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 645))

    def test_146(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 646))


    def test_147(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 647))

    def test_148(self):
        input = """
        func foo () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 648))

    def test_149(self):
        input = """
        func foo () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 649))

    def test_150(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 650))
    def test_151(self):
        input = """const Meow = foo( a[0b1][3] ); """
        expect = Program([ConstDecl("Meow",None,FuncCall("foo",[ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(3)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 651))

    def test_152(self):
        input = """
            type Widget interface {
                OnLoad(
                    stack ResourceStack,
                    force boolean)
                OnUnload()

                OnUpdate()
                OnInput(event InputEvent)

                OnDraw(canvas Canvas)
            }

            type MyWidget struct {
                fixedSizeHint SizeHint
                currentSize Size
            }

            func (mw MyWidget) OnLoad(
                stack ResourceStack,
                force boolean) {
                // TODO
            }

            func (mw MyWidget) OnUnload() {
                // TODO
            }

            func (mw MyWidget) OnUpdate() {
                println("update")
            }

            func (mw MyWidget) OnInput(event InputEvent) {
                println("Got an event:")
                println(event.toString())
            }
        """
        expect = "Program([InterfaceType(Widget,[Prototype(OnLoad,[Id(ResourceStack),BoolType],VoidType),Prototype(OnUnload,[],VoidType),Prototype(OnUpdate,[],VoidType),Prototype(OnInput,[Id(InputEvent)],VoidType),Prototype(OnDraw,[Id(Canvas)],VoidType)]),StructType(MyWidget,[(fixedSizeHint,Id(SizeHint)),(currentSize,Id(Size))],[]),MethodDecl(mw,Id(MyWidget),FuncDecl(OnLoad,[ParDecl(stack,Id(ResourceStack)),ParDecl(force,BoolType)],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUnload,[],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUpdate,[],VoidType,Block([FuncCall(println,[StringLiteral(\"update\")])]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnInput,[ParDecl(event,Id(InputEvent))],VoidType,Block([FuncCall(println,[StringLiteral(\"Got an event:\")]),FuncCall(println,[MethodCall(Id(event),toString,[])])])))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 652))

    def test_153(self):
        input = """
                    type Widget interface {
                        OnLoad(
                            stack ResourceStack,
                            force boolean)
                        OnUnload()

                        OnUpdate()
                        OnInput(event InputEvent)

                        OnDraw(canvas Canvas)
                    }

                    type MyWidget struct {
                        fixedSizeHint SizeHint
                        currentSize Size
                    }

                    func (mw MyWidget) OnLoad(
                        stack ResourceStack,
                        force boolean) {
                        // TODO
                    }

                    func (mw MyWidget) OnUnload() {
                        // TODO
                    }

                    func (mw MyWidget) OnUpdate() {
                        println("update")
                    }

                    func (mw MyWidget) OnInput(event InputEvent) {
                        println(event.toString())
                    }

                    func (mw MyWidget) OnDraw(canvas Canvas) {
                        canvas.drawRect(currentSize.toRect(), makeBluePaint())
                    }
                """
        expect = "Program([InterfaceType(Widget,[Prototype(OnLoad,[Id(ResourceStack),BoolType],VoidType),Prototype(OnUnload,[],VoidType),Prototype(OnUpdate,[],VoidType),Prototype(OnInput,[Id(InputEvent)],VoidType),Prototype(OnDraw,[Id(Canvas)],VoidType)]),StructType(MyWidget,[(fixedSizeHint,Id(SizeHint)),(currentSize,Id(Size))],[]),MethodDecl(mw,Id(MyWidget),FuncDecl(OnLoad,[ParDecl(stack,Id(ResourceStack)),ParDecl(force,BoolType)],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUnload,[],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUpdate,[],VoidType,Block([FuncCall(println,[StringLiteral(\"update\")])]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnInput,[ParDecl(event,Id(InputEvent))],VoidType,Block([FuncCall(println,[MethodCall(Id(event),toString,[])])]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnDraw,[ParDecl(canvas,Id(Canvas))],VoidType,Block([MethodCall(Id(canvas),drawRect,[MethodCall(Id(currentSize),toRect,[]),FuncCall(makeBluePaint,[])])])))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 653))

    def test_154(self):
        input = """
                    type Widget interface {
                        OnLoad(
                            stack ResourceStack,
                            force boolean)
                        OnUnload()

                        OnUpdate()
                        OnInput(event InputEvent)

                        OnDraw(canvas Canvas)
                    }

                    type MyWidget struct {
                        fixedSizeHint SizeHint
                        currentSize Size
                    }

                    func (mw MyWidget) OnLoad(
                        stack ResourceStack,
                        force boolean) {
                        // TODO
                    }

                    func (mw MyWidget) OnUnload() {
                        // TODO
                    }

                    func (mw MyWidget) OnUpdate() {
                        println("update")
                    }

                    func (mw MyWidget) OnInput(event InputEvent) {
                        println(event.toString())
                    }

                    func (mw MyWidget) OnDraw(canvas Canvas) {
                        canvas.drawRect(currentSize.toRect(), makeBluePaint())
                    }

                    func main() {
                        var framework Framework = makeFramework()
                        framework.setTopLevelWidget(MyWidget{})
                    }
                """
        expect = "Program([InterfaceType(Widget,[Prototype(OnLoad,[Id(ResourceStack),BoolType],VoidType),Prototype(OnUnload,[],VoidType),Prototype(OnUpdate,[],VoidType),Prototype(OnInput,[Id(InputEvent)],VoidType),Prototype(OnDraw,[Id(Canvas)],VoidType)]),StructType(MyWidget,[(fixedSizeHint,Id(SizeHint)),(currentSize,Id(Size))],[]),MethodDecl(mw,Id(MyWidget),FuncDecl(OnLoad,[ParDecl(stack,Id(ResourceStack)),ParDecl(force,BoolType)],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUnload,[],VoidType,Block([]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnUpdate,[],VoidType,Block([FuncCall(println,[StringLiteral(\"update\")])]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnInput,[ParDecl(event,Id(InputEvent))],VoidType,Block([FuncCall(println,[MethodCall(Id(event),toString,[])])]))),MethodDecl(mw,Id(MyWidget),FuncDecl(OnDraw,[ParDecl(canvas,Id(Canvas))],VoidType,Block([MethodCall(Id(canvas),drawRect,[MethodCall(Id(currentSize),toRect,[]),FuncCall(makeBluePaint,[])])]))),FuncDecl(main,[],VoidType,Block([VarDecl(framework,Id(Framework),FuncCall(makeFramework,[])),MethodCall(Id(framework),setTopLevelWidget,[StructLiteral(MyWidget,[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 654))

    def test_155(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 655))
        