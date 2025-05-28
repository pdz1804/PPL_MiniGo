import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_redeclared(self):
        input = """
        func a (){
        var a int
        }
        type s struct{
        b int
        }
        func (c s) a(){
        var a int
        }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_94(self):
    
        input = Program([FuncDecl("main", [ParamDecl("a", IntType())], VoidType(), Block([VarDecl("a", IntType(), None)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared1(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_type_mismatch1(self):
        input = """
            func a (){
            return
            }
            func b() {
                return a()            
            }
"""
        expect = """Type Mismatch: FuncCall(a,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,404)) 



    def test_func_1(self):
        input = """

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
        expect = "Type Mismatch: ForEach(Id(x),Id(y),Id(a),Block([Assign(Id(c),IntLiteral(5))]))\n"
        self.assertTrue(TestChecker.test(input,expect,405))


             


    def test_struct_def_2(self):
        input = """

        type Calculator interface {
                 Add(x, y int) int;
                Sub(a, a float, a int) float;
                 };
        type Person struct {
                friends Person;
                arr [4][2]int;
                }
        
        func (c Person) Add(x int) int  {
        c.Sub(1.1,2.1,3)
        var value int;

        }
        func (c Person) Sub(a, b Calculator, c int) float {
        var value int;
   
        }
                """

        expect = "Type Mismatch: MethodCall(Id(c),Sub,[FloatLiteral(1.1),FloatLiteral(2.1),IntLiteral(3)])\n"
        self.assertTrue(TestChecker.test(input,expect,406))


    



    def test_1(self):
        input = """

        type a interface {
                 Add(x, y int) int;
                 };
        type Person struct {
          a int
                }
        var c =  "1" > "3"
   
        
        func (c Person) Add(x,y float) int  {
        var value int;
        }
        func main(){
          return 
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))
  
    def test_2(self):
        input = """
        func Add() {
         return
         }
        func main(){
          var a = 5
          a:= Add()
          
        }

                """
        expect = "Type Mismatch: FuncCall(Add,[])\n"
        self.assertTrue(TestChecker.test(input,expect,408))


    def test_3(self):
        input = """
        const c = 5
        const a = 3 + c -6
        var b [a]int
        var e [4]int = b

                """
        expect = "Type Mismatch: VarDecl(e,ArrayType(IntType,[IntLiteral(4)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,409))

  


    def test_4(self):
        input = """
        func Add() {
         return
         }
        const a = 3
        const b = a +2
        var arr [b]int
        var d [5]int = arr
            func main(){
          var c = b
          for c := c; b>3; c:=4 {
            return
          }
          
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_5(self):
        input = """

          func main(){
          var c = 5
          for var b = c; b>3; b:=4 {
            const b =4.5
            return
          }
          
        }

                """
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_6(self):
        input = """
        
            var a2 string
          var a = 3
          const b = a 
          var e [a]int = [b] int{1}
            func c (a int) int{
            e :=5;
            var b = e
            }
            var in = c(a+b)

                """
        expect = "Type Mismatch: Assign(Id(e),IntLiteral(5))\n"
        self.assertTrue(TestChecker.test(input,expect,412))


    
    def test_7(self):
        input = """
        
          var a2 = "str"
          var a = 3
          const b = a 
          var e [a2]int = [b] int{1}
            func c (a int) int{
            e :=5;
            var b = e
            }
            var in = c(a+b)

                """
        expect = "Type Mismatch: ArrayType(IntType,[Id(a2)])\n"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_8(self):
        input = """
            var a1 = 3
            var a2 string = a1
                """
        expect = "Type Mismatch: VarDecl(a2,StringType,Id(a1))\n"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_9(self):
        input = """
        
            var a = "str"
            var a1 = 3
            var a2 = a1 + a
                """
        expect = "Type Mismatch: BinaryOp(Id(a1),+,Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_10(self):
        input = """
            var a = "str"
            var a1 = 3
            var a2 string = a
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))


    def test_11(self):
        input = """
            const a = "str"
            var a = 3
                """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_12(self):
        input = """
            var a = "str"
            const a = 3
                """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,418))


    def test_13(self):
        input = """
            var a = "str"
            func a (){
            return
            }
                """
        expect = "Redeclared Function: a\n"
        self.assertTrue(TestChecker.test(input,expect,419))


    def test_14(self):
        input = """
            var a = "str"
            type a struct {
                a int
            }
            func a (){
            return
            }
                """
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,420))        
            

    def test_15(self):
        input = """
            var ca = "str"
            func a (a int){
            return
            }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))


    def test_16(self):
        input = """
            var a = "str"
            func b (a int){
             var a = 5
            }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))


    def test_17(self):
        input = """
            var a = "str"
            func b (a,a int){
             var a = 5
            }
                """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,423))


    def test_18(self):
        input = """
            var a = "str"
            type a struct {
                a int
            }
                """
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,424))



    def test_19(self):
        input = """
            var a = "str"
            type a interface {
                Add(a,b int) int 
            }
                """
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,425))


    def test_20(self):
        input = """
            type a struct {
                a int
                a float
            }
                """
        expect = "Redeclared Field: a\n"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_21(self):
        input = """
            type a struct {
                a int
                b float
            }
            func (c a) a(){
            return
            }
                """
        expect = "Redeclared Method: a\n"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_22(self):
        input = """
            type a struct {
                a int
                b float
            }
            func (c a) e(){
            return
            }
            func (d a) e(){
            return
            }
                """
        expect = "Redeclared Method: e\n"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_23(self):
        input = """
            type a struct {
                a int
                b float
            }
            func (c a) e(){
                var c = c.a
            }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))


    def test_24(self):
        input = """
            var a = "str"
            type a interface {
                Add(a,a int) int
                Sub(a,b float) string 
            }
                """
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_25(self):
        input = """
            var a = "str"
            type b interface {
                Add(a,a int) int
                Add(a,b float) string 
            }
                """
        expect = "Redeclared Prototype: Add\n"
        self.assertTrue(TestChecker.test(input,expect,431))


    def test_26(self):
        input = """
            type a struct {
                a a
                b float
            }
            type b interface{
                c(e a)
            }
            func (a a) c(e a){
                a.b :=5 +e.b / a.a.b
               a.b :=5 +e.a / e.b
            }

                """
        expect = "Type Mismatch: BinaryOp(FieldAccess(Id(e),a),/,FieldAccess(Id(e),b))\n"
        self.assertTrue(TestChecker.test(input,expect,432))


    def test_27(self):
        input = """
            type a struct {
                a a
                b float
            }
            type b interface{
                c(e a)
            }
            func (a a) c(a a){
               a.b :=5
            }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_28(self):
        input = """
            type a struct {
                a a
                b float
            }
            type b interface{
                c(e a)
            }
            func (a a) c(a a) a{
               a.a := a.c(a)
            }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))


    def test_29(self):
        input = """
            type a struct {
                a [3]a
                b int
            }
            type b interface{
                c(e a)
            }
            func (a a) c(a a){
               a.b :=a.a[a.a[2].b].a[a.a[1].a[2].b].b
            }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_30(self):
        input = """
            var a = c + 5

                """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_31(self):
        input = """
            var c = c + 5

                """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,437))


    def test_32(self):
        input = """
            var a = 5
            func main(){
            a:= a +3
            } 
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))


    def test_33(self):
        input = """
            var b = a
            var a = 5
            func main(){
            a:= a +3
            } 
                """
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect,439))


    def test_34(self):
        input = """
            var a = abc()
            func abc() int{
                a +=5
            }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))


    def test_35(self):
        input = """
            var a abc
            type abc struct{
                a int
            }
            var b = a.e()
                """
        expect = "Undeclared Method: e\n"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_36(self):
        input = """
            var a abc
            type abc struct{
                a int
            }
            var b = a.e
                """
        expect = "Undeclared Field: e\n"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_37(self):
        input = """
            var a int 
            func b(){
            a:= a +3
            } 

            func main(){
            c(1,2,3)
            }
                """
        expect = "Undeclared Function: c\n"
        self.assertTrue(TestChecker.test(input,expect,443))


    def test_38(self):
        input = """
            var a int 
            func b(){
            a:= a +3
            } 

            func main(){
            c(1,2,3)
            }
                """
        expect = "Undeclared Function: c\n"
        self.assertTrue(TestChecker.test(input,expect,444))


    def test_39(self):
        input = """
            var a int = "abc"
                """
        expect = "Type Mismatch: VarDecl(a,IntType,StringLiteral(\"abc\"))\n"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_40(self):
        input = """
            var a float = 123
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_41(self):
        input = """
            var a float = 1+ 2.5 
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_42(self):
        input = """
            var a string = "abc"
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_43(self):
        input = """
            var a  = !(true || false && (1 == 2) && ("a" > "n"))
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_44(self):
        input = """
            var b = 1.2
            var a  = !(true || false && (b == 2) && ("a" > "n"))
                """
        expect = "Type Mismatch: BinaryOp(Id(b),==,IntLiteral(2))\n"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_45(self):
        input = """
            var a  = [3]int{1,2,3}
            var b [3]int = a
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_46(self):
        input = """
            var a  = 3/4+ 5
            var c [5]int = [a]int{1,2,3,4,5}
            var d [5]int = c
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_47(self):
        input = """
            const a  = 3/4+ 5
            var b [a]int
            var d [7]int = b
                """
        expect = "Type Mismatch: VarDecl(d,ArrayType(IntType,[IntLiteral(7)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_48(self):
        input = """
            func add(a,b int) int{ 
            return a+b;
            }
            var a  = add(3,4)
            var b [a]int
            var d [5]int = b
                """
        expect = "Type Mismatch: VarDecl(d,ArrayType(IntType,[IntLiteral(5)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,454))


    def test_49(self):
        input = """
            var a  = 6
            var b [a]int
            var d int = b[1+3]
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))


    def test_50(self):
        input = """
            func add(a,b int) int{ 
            return a+b;
            }
            var a  = 6
            var b [a]int
            var d int = b[add(1,2)]
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_51(self):
        input = """

        type a interface {
                 a(x, y int) int;
                 };
        type Person struct {
          b int
                }
        
        func (c Person) a(x,y int) int  {
        var value int;
        }
        func main(){
          var a a;
          var b Person;
          a := b

        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_52(self):
        input = """

        type a interface {
                 a(x, y int) int;
                 };
        type Person struct {
          b int
                }
        
        func (c Person) a(x,y float) int  {
        var value int;
        }
        func main(){
          var a a;
          var b Person;
          a := b

        }

                """
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,458))


    def test_53(self):
        input = """

        type a interface {
                 a(x, y float) int;
                 };
        type Person struct {
          b int
                }
        type Person2 struct {
          b int
                }
        
        func (c Person) a(x,y float) int  {
        var value int;
        }
        func (c Person2) a(x,y float) int  {
        var value int;
        }
        func main(){
          var a a;
          var b Person;
          a := b
          var c Person2;
          a:= c
          b := c

        }

                """
        expect = "Type Mismatch: Assign(Id(b),Id(c))\n"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_54(self):
        input = """

        type a interface {
                 a(x, y int) int;
                 b()
                 };
        type Person struct {
          b int
                }
        
        func (c Person) a(x,y int) int  {
        var value int;
        }
        func main(){
          var a a;
          var b Person;
          a := b

        }

                """
        expect = "Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,460))


    def test_55(self):
        input = """
        var a int
        func main(){
            b := a

        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_56(self):
        input = """
        type Person struct {
          a int
                }
        var a int
        var c[3]int
        var d Person
        func main(){
            b := a
            c[2]:= b
            d.a := b
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))


    def test_57(self):
        input = """
        var s = 5
        func main(){

            for i := 0; i < 10; c :=  1 {
                c := 5
                i += 1 
                }
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_58(self):
        input = """
        type Person struct {
          a int
                }
        var c = 5
        func (e Person) add( d int)int{
            e.a := c
        }
        func (e Person) sub( d int)int{
            e.a := e.add(3)
        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_59(self):
        input = """
        var x = 5
        func main(){
            if (x > 10) {
            putString("x is greater than 10");
            } else if (x == 10) {
             putString("x is equal to 10");
            } else {
            putString("x is less than 10");
            }
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_60(self):
        input = """
        var x = 5
        func main(){
            if (x + 10) {
            putString("x is greater than 10");
            } else if (x == 10) {
             putString("x is equal to 10");
            } else {
            putString("x is less than 10");
            }
        }
                """
        expect = "Type Mismatch: If(BinaryOp(Id(x),+,IntLiteral(10)),Block([FuncCall(putString,[StringLiteral(\"x is greater than 10\")])]),If(BinaryOp(Id(x),==,IntLiteral(10)),Block([FuncCall(putString,[StringLiteral(\"x is equal to 10\")])]),Block([FuncCall(putString,[StringLiteral(\"x is less than 10\")])])))\n"
        self.assertTrue(TestChecker.test(input,expect,466))



    def test_61(self):
        input = """
        var x = 5
        func main(){
            for x>5 {
            x +=3
            }
            for false {
            x +=3
            }
            for 3 {
            x +=3
            }
        }
                """
        expect = "Type Mismatch: For(IntLiteral(3),Block([Assign(Id(x),BinaryOp(Id(x),+,IntLiteral(3)))]))\n"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_62(self):
        input = """
        var x = 5
        func main(){
            for i := 0; i < 10; c :=  1 {
                c := c;
                i := i;
                }
            for i := 0; d < 10; c :=  1 {
                var c = c;
                var i = i;
                }
        }
                """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_63(self):
        input = """
        var x = 5
        func main(){
            var value = 5
            arr := [3]int{10, 20, 30}
            for _, value := range arr {
                var b = 1
                var c = value
            }

        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_64(self):
        input = """
        var x = 5
        func main(){
            var value int
            arr := [3]int {10, 20, 30}
            for index, value := range arr {
                var b = index
                var c = value
            }

        }
                """
        expect = "Undeclared Identifier: index\n"
        self.assertTrue(TestChecker.test(input,expect,470))


    def test_65(self):
        input = """
        const x = 1
        var y [x]int
        func main(){
            var arr [3]int
            var index int
            var value int
            for index, value := range arr {
                var b = index
                var c = value
            }
            for index, values := range arr {
                var b = index
                var c = value
            }

        }
        """
        expect = "Undeclared Identifier: values\n"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_66(self):
        input = """
            var a [3][4]int = [3][4]int {1,2,3,4,5}
            
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_67(self):
        input = """
            const b = true
            var a [3][4]int = [b][4]int {1,2,3,4,5}
            
                """
        expect = "Type Mismatch: ArrayLiteral([Id(b),IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])\n"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_68(self):
        input = """
            const b = 6
            var a [b][4]int = [2][4]int {1,2,3,4,5}
            
                """
        expect = "Type Mismatch: VarDecl(a,ArrayType(IntType,[Id(b),IntLiteral(4)]),ArrayLiteral([IntLiteral(2),IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))\n"
        self.assertTrue(TestChecker.test(input,expect,474))


    def test_69(self):
        input = """
            var b a = a{}
            var c = a{a:3}
            var d = a{b:"3"}
            type a struct {
                a int
                b float
            }
            
                """
        expect = "Type Mismatch: StructLiteral(a,[(b,StringLiteral(\"3\"))])\n"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_70(self):
        input = """
            var b a = a{}
            var c = a{a:3}
            var d = a{b:3.5,c:5}
            type a struct {
                a int
                b float
            }
            
                """
        expect = "Undeclared Field: c\n"
        self.assertTrue(TestChecker.test(input,expect,476))


    def test_71(self):
        input = """
            var b [3][4]a
            type a struct {
                a int
                b float
            }
            var c = b[b[2][3].a+3]
            var d = b[b[2].a+3]
                """
        expect = "Type Mismatch: FieldAccess(ArrayCell(Id(b),[IntLiteral(2)]),a)\n"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_72(self):
        input = """
            var b [3][4]a
            type a struct {
                a int
                b float
            }
            var c = b[b[2][3].b+3]
            
                """
        expect = "Type Mismatch: ArrayCell(Id(b),[BinaryOp(FieldAccess(ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)]),b),+,IntLiteral(3))])\n"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_73(self):
        input = """
            type a struct {
                a int
                b float
            }
            var b a
            var c int
            var e = b.a +b.b
            
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_74(self):
        input = """
            var b [3][3]int
            
            func a(){
                var c [3][4]int
                c[1]:= b[2]
                continue
                break
            }
                """
        expect = "Type Mismatch: Assign(ArrayCell(Id(c),[IntLiteral(1)]),ArrayCell(Id(b),[IntLiteral(2)]))\n"
        self.assertTrue(TestChecker.test(input,expect,480))



    def test_75(self):
        input = """
            var b [3][4]int
            
            func a(){
                var c [3][4]int
                c[2]:= b[2]
                c[2] := b[3] + [4]int{1,2,3}
                
            }
                """
        expect = "Type Mismatch: BinaryOp(ArrayCell(Id(b),[IntLiteral(3)]),+,ArrayLiteral([IntLiteral(4)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_76(self):
        input = """
            func a(){
                return;
                return 1+3
            }
            
                """
        expect = "Type Mismatch: Return(BinaryOp(IntLiteral(1),+,IntLiteral(3)))\n"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_77(self):
        input = """
            func a() int{
                return 
                return 4.5
            }
            
                """
        expect = "Type Mismatch: Return()\n"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_78(self):
        input = """
            func a() int{
                return 4
                return 4.5
            }
            
                """
        expect = "Type Mismatch: Return(FloatLiteral(4.5))\n"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_79(self):
        input = """
            func a() int{
                return 4
            }
            func a2(){
                return
            }
            func b() {
                a2()
                a()
            }
                """
        expect = "Type Mismatch: FuncCall(a,[])\n"
        self.assertTrue(TestChecker.test(input,expect,485))


    def test_80(self):
        input = """
            func a() int{
                return 4
            }
            func a2(){
                return
            }
            func b() {
                return a()
            }
                """
        expect = "Type Mismatch: Return(FuncCall(a,[]))\n"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_81(self):
        input = """
            func a() int{
                return 4
            }
            func a2(){
                return
            }
            func b() {
                var d = a2()
            }
                """
        expect = "Type Mismatch: FuncCall(a2,[])\n"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_82(self):
        input = """
            func a(a int ,b int,c float) int{
                return 4
            }
            func b() {
                c := a(3,4,5.5)
            }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_83(self):
        input = """
            func a(a int ,b int,c float) int{
                return 4
            }
            func b() {
                c := a(3,4,5)
            }
                """
        expect = "Type Mismatch: FuncCall(a,[IntLiteral(3),IntLiteral(4),IntLiteral(5)])\n"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_84(self):
        input = """
            func a(a int ,b int,c float) int{
                return 4
            }
            func b() {
                c := a(3,4)
            }
                """
        expect = "Type Mismatch: FuncCall(a,[IntLiteral(3),IntLiteral(4)])\n"
        self.assertTrue(TestChecker.test(input,expect,490))  

    def test_85(self):
        input = """

        type i interface {
                 Add(x, y int) int;
                 };
        type s struct {
          a int
                }
        func (c s) Add(x,y int) int  {
        var value int;
        }
        func main(){
          var a i
          var b s
          a := b
          c := a.Add(1,1) + b.Add(2,2)
          a.Add(1,2)
        }

                """
        expect = "Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_86(self):
        input = """

        type i interface {
                 Add(x, y int) int;
                 };
        type s struct {
          a int
                }
        func (c s) Add(x,y int) int  {
        var value int;
        }
        func main(){
          var a i
          var b s
          a := b
          var c = a.Add(1,1.2) + b.Add(2,2)
        }

                """
        expect = "Type Mismatch: MethodCall(Id(a),Add,[IntLiteral(1),FloatLiteral(1.2)])\n"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_87(self):
        input = """

        type i interface {
                 Add(x, y int);
                 };
        type s struct {
          a int
                }
        func (c s) Add(x,y int)  {
        var value int;
        }
        func main(){
          var a i
          var b s
          a := b
          a.Add(1,2)
          b.Add(2)
        }

                """
        expect = "Type Mismatch: MethodCall(Id(b),Add,[IntLiteral(2)])\n"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_88(self):
        input = """
        type s struct {
          a int
          b float
                }

        func main(){
          var a [3]s
          var b = a[2].a +a[3].b
        }

                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_89(self):
        input = """
        func main(){
            putInt(3)
            putIntLn(3)
            getInt()

        }

                """
        expect = "Type Mismatch: FuncCall(getInt,[])\n"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_90(self):
        input = """
        type s struct {
          a int
          b float
                }
        var a  [3] s ;
        var b int
        func c()int{
        return a[2].a
        return a[2].b
        }


                """
        expect = "Type Mismatch: Return(FieldAccess(ArrayCell(Id(a),[IntLiteral(2)]),b))\n"
        self.assertTrue(TestChecker.test(input,expect,496))


    def test_91(self):
        input = """
        type s struct {
          a int
          b float
                }
        var a  [2] s ;
        var b int
        func c() [2] s {
        return a
        return a[2]
        }


                """
        expect = "Type Mismatch: Return(ArrayCell(Id(a),[IntLiteral(2)]))\n"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_92(self):
        input = """
        type s struct {
            a int
            b float
        }
        var e  [3] s ;
        var d  [2]int
        func c(a [2]int,b [3]s) int {
            return b[1].a + c(d,e)
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))


    # Nay hao no kh test nua 
    def test_93(self):
        input = """
        var e  = 3 ;
        var d  [2]int
        func c(a int,b int) [e]int {
            e +=1;
            var a [e]int
            return a
        }
        """
        expect = "" # t ra: pass
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_95(self):
        input = """
        func a() int{
            return 1
        }
        type b struct{
            c int
        }
        func (b b) a() int{
            return 1
        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))

    