# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

import unittest
from TestUtils import TestCodeGen
import inspect
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    
    def test_001(self):
        """
        func main() {
            putInt(1)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[IntLiteral(1)])]))])
        self.assertTrue(TestCodeGen.test(input, "1", inspect.stack()[0].function))    

    def test_002(self):
        """
        func main() {
            putFloat(1.0)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", inspect.stack()[0].function))

    def test_003(self):
        input = """
        func main() {
            var a string = "tr"
            putStringLn("s" + a)
            putString("s" + a + a)
        }
        """
        self.assertTrue(TestCodeGen.test(input,"str\nstrtr",inspect.stack()[0].function)) 

    def test_004(self):
        input = """
        func main() {
            putBoolLn(5.0 > 2.0)
            putBoolLn(5.0 < 2.0)
            putBoolLn(5.0 <= 5.0)
            putBoolLn(5.0 >= 5.0)
            putBoolLn(5.0 == 5.0)
            putBoolLn(5.0 != 5.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",inspect.stack()[0].function)) 

    def test_005(self):
        input = """
        func main() {
            putBoolLn("apple" > "banana")     // False
            putBoolLn("apple" < "banana")     // True
            putBoolLn("apple" <= "apple")     // True
            putBoolLn("banana" >= "apple")    // True
            putBoolLn("hello" == "hello")     // True
            putBoolLn("hello" != "hello")     // False
        } 
        """ 
        output = """false\ntrue\ntrue\ntrue\ntrue\nfalse\n"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 

    def test_006(self):
        input = """
        func main() {
            var f = true;
            var g boolean;

            putBoolLn(f)
            putBool(g)
        }
        """ 
        output = """true\nfalse"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 

    def test_007(self):
        input = """
        var a int = 10; func main() { putInt(a);};
        """ 
        output = """10"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_008(self):
        input = """
        func main() {putBoolLn(true);putBool(false);};
        """ 
        output = """true\nfalse"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_009(self):
        input = """
        var a float = 3;
        func main() {
            putFloatLn(a)
            var a float = 4;
            putFloatLn(a)
            a := 2
            putFloat(a)
        }
                
        """ 
        output = """3.0\n4.0\n2.0"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_010(self):
        input = """
        func foo() int {return foo1();}
        var a = foo() + foo1();
        func main() {
            putInt(a)
            a := foo()
            putInt(a)
        }
        func foo1() int {return 1;}      
        """ 
        output = """21"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_011(self):
        input = """
        func foo() int {return 1;}        

        func main() {
            putInt(foo())
        }    
        """ 
        output = """1"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_012(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{10, 20, 30}, {40, 50, 60}};
            putInt(a[1][0])
        }
        """ 
        output = """40"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_013(self):
        input = """
        func main() {
            var a [2][3][2] int ;
            putInt(a[0][0][0])
        }
        """ 
        output = """0"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_014(self):
        input = """
        func main() {
            var a [2][3] float;
            a[0][0] += 2.0
            putFloat(a[0][0] + a[0][1])
        }
        """ 
        output = """2.0"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_015(self):
        input = """
        func main() {
            var a [2][3] string;
            a[0][0] := "QuangPhu"
            putString(a[0][0] + a[0][1])
        }
        """ 
        output = """QuangPhu"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
        
    def test_016(self):
        input = """
        func main() {
            var a [2][3] boolean;
            a[0][0] := true
            putBool(a[0][0])
        }
        """ 
        output = """true"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
    
    def test_017(self):
        input = """
        func createArray() [3] int {
            return [3] int {10, 20, 30};
        }

        func main() {
            var a [3] int = createArray();
            putInt(a[0]);
            putInt(a[1]);
            putInt(a[2]);
        }
        """ 
        output = """102030"""
        self.assertTrue(TestCodeGen.test(input, output, inspect.stack()[0].function)) 
    
    def test_018(self): # 90
        input = """
            func main() {
                var a [1] int ;
                a[0] := 1
                putInt(a[0]);
            }
        """
        self.assertTrue(TestCodeGen.test(input,"1",inspect.stack()[0].function))

    def test_019(self): # 91
        input = """
            func main() {
                var a [1][1][1] int  = [1][1][1] int {{{0}}};
                a[0][0][0] := 1
                putInt(a[0][0][0]);
            }
        """
        self.assertTrue(TestCodeGen.test(input,"1",inspect.stack()[0].function))
    
    # TASK 4
    
    def test_020(self): # 96
        input = """
            func main() {
                if (true) {
                    putBool(true)
                } 
            }
        """
        self.assertTrue(TestCodeGen.test(input,"true",inspect.stack()[0].function))
    
    def test_021(self): # 111
        input = """
            func main() {
                var i = 2;
                for i > 0 {
                    putInt(i);
                    i -= 1;
                }
                putInt(i);
            }
        """
        self.assertTrue(TestCodeGen.test(input,"210",inspect.stack()[0].function))
    
    def test_022(self): # 120
        input = """
            func main() {
                var i int;
                for i := 0; i < 2; i += 1 {
                    putInt(i)
                }
                putInt(i)
            }
        """
        self.assertTrue(TestCodeGen.test(input,"012",inspect.stack()[0].function))
    
    def test_023(self): # 125
        input = """
            func main() {
                var i int = 10;
                for var i int = 0; i < 2; i += 1 {
                    putIntLn(i)
                }
                putInt(i)
            }
        """
        self.assertTrue(TestCodeGen.test(input,"0\n1\n10",inspect.stack()[0].function))
    
    def test_024(self): # 130
        input = """
            const a = "QuangPhu"
            func main() {
                putString(a)
            }
        """
        self.assertTrue(TestCodeGen.test(input,"QuangPhu",inspect.stack()[0].function))
        
    def test_025(self): # 130
        input = """
            func fooInt(a int) int {  return a; }
            func fooFloat(a float) float {  return a; }
            func fooString(a string) string { return a; }
            func fooBool(a boolean) boolean { return a; }

            func main() {
                putInt(fooInt(2));
                putFloat(fooFloat(1.5));
                putString(fooString("S"));
                putBool(fooBool(true));
            }
        """
        self.assertTrue(TestCodeGen.test(input,"21.5Strue",inspect.stack()[0].function))
    
    def test_028(self): # 77
        input = """
            var a [2] int;
            func main() {
                a[0] := 100
                a[1] += a[0] + a[0]
                putInt(a[1])
            }
        """
        self.assertTrue(TestCodeGen.test(input, "200", inspect.stack()[0].function))
        
    def test_132(self): # 132
        input = """
            func main() {
                const a = 1 + 1
                var b [a] int = [a] int {10}
                putInt(b[0])
            }
            
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))
    
        
    def test_133(self): # 133
        input = """
            func main() {
                const a = 2
                var b [a][a] int = [a][a] int {{10, 20}, {30, 40}};
                putInt(b[0][1])
            }
            
        """
        self.assertTrue(TestCodeGen.test(input, "20", inspect.stack()[0].function))
        
    
    # TASK 5
    def test_141(self):
        input = """
        type Course interface {study();}
        type PPL3 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}

        func main(){
            var a PPL3 = PPL3 {number: 10}
            putIntLn(a.number)
            a.study()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n10", inspect.stack()[0].function))

    def test_142(self):
        input = """
        type Course interface {study();}
        type PPL3 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}

        func main(){
            var a Course = nil
            a := PPL3 {number: 10}
            a.study()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_143(self):
        input = """
        type PPL3 struct {number int;}

        func main(){
            var a PPL3 = PPL3 {number: 10}
            putInt(a.number)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_144(self):
        input = """
        type PPL3 struct {number int;}

        func main(){
            var a PPL3
            a.number := 10
            putInt(a.number)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_145(self):
        input = """
        type PPL2 struct {number int;}
        type PPL3 struct {number int; ppl PPL2;}

        func main(){
            var a PPL3
            a.ppl := PPL2 {number: 10}
        putInt(a.ppl.number)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_146(self):
        input = """
        type PPL2 struct {number int;}
        type PPL3 struct {number int; ppl PPL2;}

        func main(){
            var a PPL3
            a.ppl := PPL2 {number: 10}
            a.ppl.number := 100
        putInt(a.ppl.number)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100", inspect.stack()[0].function))        

    def test_147(self):
        input = """
        type Study interface { study(); }
        type Play interface { play(); }

        type PPL3 struct {number int;}

        func (p PPL3) study() { putInt(p.number); }
        func (p PPL3) play()  { putInt(p.number + 5); }

        func main() {
            var a PPL3 = PPL3 {number: 1}
            a.study()
            a.play()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "16", inspect.stack()[0].function))


    def test_148(self):
        input = """
        type Study interface { study(); }
        type Play interface { play(); }

        type PPL3 struct {number int;}

        func (p PPL3) study() { putInt(p.number); }
        func (p PPL3) play()  { putInt(p.number + 5); }

        func main() {
            var a PPL3 = PPL3 {number: 1}
            var b Study = a
            var c Play = a
            b.study()
            c.play()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "16", inspect.stack()[0].function))

    def test_148(self):
        input = """
        type Study interface { study(); }
        type Play interface { play(); }

        type PPL3 struct {number int;}

        func (p PPL3) study() { putInt(p.number); }
        func (p PPL3) play()  { putInt(p.number + 5); }

        func main() {
            var a PPL3 = PPL3 {number: 1}
            var b Study = a
            var c Play = a
            b.study()
            c.play()
        }
        """
        self.assertTrue(TestCodeGen.test(input, "16", inspect.stack()[0].function))

    def test_149(self):
        input = """
        type Worker interface { 
            study(); 
            play(); 
        }

        type PPL4 struct {number int;}
        type PPL5 struct {number int;}

        // Implement Worker cho PPL4
        func (p PPL4) study() { putInt(p.number); }
        func (p PPL4) play()  { putInt(p.number + 5); }

        // Implement Worker cho PPL5
        func (p PPL5) study() { putInt(p.number * 2); }
        func (p PPL5) play()  { putInt(p.number * 3); }

        func main() {
            var w1 Worker = PPL4 {number: 3}
            var w2 Worker = PPL5 {number: 4}

            w1.study(); // in: 3
            w1.play();  // in: 8

            w2.study(); // in: 8
            w2.play();  // in: 12
        }
        """
        self.assertTrue(TestCodeGen.test(input, "38" "812", inspect.stack()[0].function))

    def test_150(self):
        input = """
        type Worker interface { 
            study(); 
            play(); 
        }

        type PPL4 struct {number int;}
        type PPL5 struct {number int;}

        // Implement Worker cho PPL4
        func (p PPL4) study() { putInt(p.number); }
        func (p PPL4) play()  { putInt(p.number + 5); }

        // Implement Worker cho PPL5
        func (p PPL5) study() { putInt(p.number * 2); }

        func main() {
            var w1 Worker = PPL4 {number: 3}
            var w2 PPL5 = PPL5 {number: 4}

            w1.study(); // in: 3
            w1.play();  // in: 8

            w2.study(); // in: 8
        }
        """
        self.assertTrue(TestCodeGen.test(input, "38" "8", inspect.stack()[0].function))


    def test_151(self):
        input = """
        type Speaker interface { speak(); }

        type Human struct {name int; }

        func (h Human) speak() { putIntLn(h.name); }

        func saySomething(s Speaker) {
            s.speak();
        }

        func main() {
            var h Speaker = Human {name: 2025};
            saySomething(h);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2025\n", inspect.stack()[0].function))


    def test_152(self):
        input = """
        type Speaker interface { speak(); }

        type Human struct { name int; }

        func (h Human) speak() { putIntLn(h.name); }

        func main() {
            var people [3]Speaker;

            people[0] := Human {name: 1};
            people[1] := Human {name: 2};
            people[2] := Human {name: 3};

            people[0].speak(); // Output: 1
            people[1].speak(); // Output: 2
            people[2].speak(); // Output: 3
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", inspect.stack()[0].function))

    def test_153(self):
        input = """
        type Speaker interface { speak(); }

        type Human struct { name int; }

        func (h Human) speak() { putIntLn(h.name); }

        func main() {
            var people [3]Human;

            people[0] := Human {name: 1};
            people[1] := Human {name: 2};
            people[2] := Human {name: 3};

            people[0].speak(); // Output: 1
            people[1].speak(); // Output: 2
            people[2].speak(); // Output: 3
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", inspect.stack()[0].function))

    def test_154(self):
        input = """
        type Calculator struct { x int; y int; }

        func (c Calculator) sum() int {
            return c.x + c.y;
        }

        func main() {
            var cal Calculator = Calculator {x: 7, y: 8};
            var result int = cal.sum();
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", inspect.stack()[0].function))

    def test_155(self):
        input = """
        type Calculator interface { sum() int; }

        type BasicCalc struct { x int; y int; }

        func (b BasicCalc) sum() int {
            return b.x + b.y;
        }

        func main() {
            var c Calculator = BasicCalc {x: 5, y: 15};
            var result int = c.sum();
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", inspect.stack()[0].function))

    def test_156(self):
        input = """
        type Speaker interface { speak(); }

        type Human struct { name int; }

        func (h Human) speak() { putIntLn(h.name); }

        func sayHello(s Speaker) {
            s.speak();
        }

        func main() {
            var h Human = Human {name: 100};
            sayHello(h);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", inspect.stack()[0].function))

    def test_157(self):
        input = """
        type Calculator interface { sum() int; }

        type BasicCalc struct { x int; y int; }

        func (b BasicCalc) sum() int {
            return b.x + b.y;
        }

        func calculate(c Calculator) int {
            return c.sum();
        }

        func main() {
            var b BasicCalc = BasicCalc {x: 20, y: 30};
            var result int = calculate(b);
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "50\n", inspect.stack()[0].function))

    def test_158(self):
        input = """
        type Multiplier struct { factor int; }

        func (m Multiplier) multiply(value int) int {
            return m.factor * value;
        }

        func main() {
            var mul Multiplier = Multiplier {factor: 5};
            var result int = mul.multiply(4);
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", inspect.stack()[0].function))

    def test_159(self):
        input = """
        type Calculator interface { calculate(a int, b int) int; }

        type BasicCalc struct {number int;}

        func (b BasicCalc) calculate(a int, b int) int {
            return a + b;
        }

        func main() {
            var c Calculator = BasicCalc {};
            var result int = c.calculate(15, 25);
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", inspect.stack()[0].function))


    def test_160(self):
        input = """
        type Calculator interface { calculate(a int, b int); }

        type BasicCalc struct {number int;}

        func (b BasicCalc) calculate(a int, b int) {
            putIntLn(a+b);
        }

        func main() {
            var c Calculator = BasicCalc {};
            c.calculate(15, 25);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", inspect.stack()[0].function))

    def test_161(self):
        input = """
        type Calculator interface { calculate(a int, b int); }

        type BasicCalc struct {number int;}

        func (b BasicCalc) calculate(a int, b int) {
            putIntLn(a+b);
        }

        func main() {
            var c BasicCalc
            c.calculate(15, 25);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "40\n", inspect.stack()[0].function))

    def test_162(self):
        input = """
        type Speaker interface { speak(); }

        type Human struct { name int; }

        func (h Human) speak() {
            putIntLn(h.name);
        }

        type Classroom struct {
            student Human;
            guest Speaker;
        }

        func main() {
            var h Human = Human {name: 777};
            var k Speaker = Human {name: 999};
            var room Classroom = Classroom {student: h, guest: k};

            putIntLn(room.student.name);
            room.guest.speak();
        }
        """
        self.assertTrue(TestCodeGen.test(input, "777\n999\n", inspect.stack()[0].function))

    def test_163(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func main() {
            var p Person = Person{name: "Alice", age: 22};
            putStringLn(p.name);
            putIntLn(p.age);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice\n22\n", inspect.stack()[0].function))

    def test_164(self):
        input = """
        type Greeter interface { greet(); }

        type Person struct {
            name string;
            age int;
        }
        func (p Person) greet() {
            putStringLn(p.name);
        }

        func main() {
            var g Greeter = Person{name: "Bob", age: 30};
            g.greet();
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Bob\n", inspect.stack()[0].function))

    def test_165(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) agePlus(n int) int {
            return p.age + n;
        }
        func main() {
            var p Person = Person{name: "Charlie", age: 18};
            var result int = p.agePlus(5);
            putIntLn(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "23\n", inspect.stack()[0].function))

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

    def test_167(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) printInfo() {
            putStringLn(p.name);
            putIntLn(p.age);
        }
        func main() {
            var people [1]Person
            people[0] := Person{name: "Anna", age: 19};
            people[0].printInfo() 
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Anna\n19\n", inspect.stack()[0].function))

    def test_168(self):
        input = """
        type Speaker interface { speak(); }
        type Person struct {
            name string;
            age int;
        }
        func (p Person) speak() {
            putStringLn(p.name);
        }
        func announce(s Speaker) {
            s.speak();
        }
        func main() {
            var p Person = Person{name: "Grace", age: 27};
            announce(p);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Grace\n", inspect.stack()[0].function))

    def test_169(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func createPerson(n string, a int) Person {
            return Person{name: n, age: a};
        }
        func main() {
            var p Person = createPerson("Helen", 24);
            putStringLn(p.name);
            putIntLn(p.age);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Helen\n24\n", inspect.stack()[0].function))

    def test_170(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) isAdult() boolean {
            return p.age >= 18;
        }
        func main() {
            var p Person = Person{name: "Ivy", age: 17};
            if (p.isAdult()) {
                putStringLn("Adult");
            } else {
                putStringLn("Minor");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Minor\n", inspect.stack()[0].function))

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

    def test_172(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) printInfo() {
            putStringLn(p.name);
            putIntLn(p.age);
        }
        func main() {
            var people [2]Person = [2]Person{Person{name: "Anna", age: 19},Person{name: "Bill", age: 21}};
            people[0].printInfo();
            people[1].printInfo();
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Anna\n19\nBill\n21\n", inspect.stack()[0].function))

    def test_173(self):
        input = """
        var prefix string;

        type Person struct {
            name string;
            age int;
        }

        func getGreeting(name string) string {
            return prefix + name;
        }

        func (p Person) greet() string {
            return getGreeting(p.name);
        }

        func main() {
            var quangphu Person = Person{name: "QuangPhu", age: 19};
            prefix := "Hello, my name is ";
            var msg string = quangphu.greet();
            putStringLn(msg);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Hello, my name is QuangPhu\n", inspect.stack()[0].function))

    def test_174(self):
        input = """
        func foo() boolean {
            putStringLn("foo");
            return true;
        }

        func main() {
            var a = true && foo()
            putBoolLn(a)
            var b = false && foo()
            putBoolLn(b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "foo\ntrue\nfalse\n", inspect.stack()[0].function))

    def test_175(self):
        input = """
        func foo() boolean {
            putStringLn("foo");
            return false;
        }

        func main() {
            var a = true || foo()
            putBoolLn(a)
            var b = false || foo()
            putBoolLn(b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\nfoo\nfalse\n", inspect.stack()[0].function))

    def test_176(self):
        input = """
        type Course interface {print(a [2] int);}
        type PPL3 struct {number int;}
        func (p PPL3) print(a [2] int) {putInt(a[0]);}

        func main(){
            var a PPL3 = PPL3 {number: 10}
            a.print([2] int {10, 2})
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_177(self):
        input = """
        type PPL2 struct {number [1][1][1]int;}
        type PPL3 struct {ppl2 PPL2;}


        func main(){
            var a [2][2]PPL3 
            a[0][1] := PPL3 {ppl2: PPL2 {number: [1][1][1]int{{{10}}} }}
            putInt(a[0][1].ppl2.number[0][0][0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))
    
    def test_178(self):
        input = """
        var a = 10
        var b = true
        var c = 12.34
        var d = "Quang Phu"
        const f = "Hello"
        
        func main() {
            putStringLn(d)
            putStringLn(f)
            var e = 1
            const a = 1000
            const f = 2
            putIntLn(e)
            putIntLn(a)
        }
        
        """
        self.assertTrue(TestCodeGen.test(input, "Quang Phu\nHello\n1\n1000\n", inspect.stack()[0].function))
    
    def test_179(self):
        input = """
        var a = 10
        var b = true
        var c = 12.34
        var d = "Quang Phu"
        const f = "Hello"
        
        func foo() string {
            return "Quang Phu"
        }
        
        func main() {
            putStringLn(d)
            putStringLn(foo())
            var foo = 10
            putIntLn(foo)
        }
        
        """
        self.assertTrue(TestCodeGen.test(input, "Quang Phu\nQuang Phu\n10\n", inspect.stack()[0].function))
    
    def test_180(self):
        input = """
        var a = 10
        var d = "Quang Phu"
        const f = "Hello"
        
        func foo() [2][2]int {
            return [2][2]int{{10, 20}, {30, 40}}
        }
        
        func main() {
            putStringLn(d)
            putIntLn(foo()[1][1])
            var foo = 10
            putIntLn(foo)
        }
        
        """
        self.assertTrue(TestCodeGen.test(input, "Quang Phu\n40\n10\n", inspect.stack()[0].function))
    
    def test_181(self):
        input = """
        var a = 10 * 20 - 100 * 1000
        var d = "Quang Phu"
        const f = "Hello"
        
        func foo() [2][2]int {
            return [2][2]int{{10, 20}, {30, 40}}
        }
        
        func main() {
            putIntLn(a)
            putStringLn(d)
            putIntLn(foo()[1][1])
            var foo = 10
            putIntLn(foo)
        }
        
        """
        self.assertTrue(TestCodeGen.test(input, "-99800\nQuang Phu\n40\n10\n", inspect.stack()[0].function))
    
    def test_182(self):
        input = """
        type Student struct {
            name string;
            score int;
        }
        
        func sortStudents(students [3]Student, n int) {
            for i := 0; i < n - 1; i += 1 {
                for j := 0; j < n - i - 1; j += 1 {
                    if (students[j].score > students[j + 1].score) {
                        var temp Student = students[j];
                        students[j] := students[j + 1];
                        students[j + 1] := temp;
                    }
                }
            }
        }
        
        func main(){
            var students = [3] Student {Student{name: "John", score: 85}, Student{name: "Alice", score: 92}, Student{name: "Bob", score: 78}};
            sortStudents(students, 3);
            for i := 0; i < 3; i += 1 {
                putString(students[i].name + " ");
                putInt(students[i].score);
                putLn();
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Bob 78\nJohn 85\nAlice 92\n", inspect.stack()[0].function))
    
    def test_183(self):
        input = """
        func binarySearch(arr [10]int, low int, high int, target int) int {
            if (low > high) {
                return -1;
            }
            
            var mid = low + ((high - low) / 2);
            
            if (arr[mid] == target) {
                return mid;
            }
            
            if (arr[mid] < target) {
                return binarySearch(arr, mid + 1, high, target);
            } else {
                return binarySearch(arr, low, mid - 1, target);
            }
        }
        
        func main() {
            var arr = [10] int {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            var result int = binarySearch(arr, 0, 9, 5);
            putInt(result);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5", inspect.stack()[0].function))
    
    def test_184(self):
        input = """
        const MAX = 5;
        
        func bfs(graph [MAX][MAX]int, start int){
            var visited [MAX] boolean;
            var queue [MAX] int;
            var front = 0;
            var rear = 0;
            visited[start] := true;
            queue[rear] := start;
            rear += 1;
            
            for front < rear {
                var u = queue[front]
                front += 1;
                putInt(u)
                putString(" ")
                for v := 0; v < MAX; v += 1{
                    if (graph[u][v] == 1 && !visited[v]){
                        visited[v] := true;
                        queue[rear] := v;
                        rear += 1;
                    }
                }   
            }
        }
        
        func main(){
            var graph = [MAX][MAX] int {{0, 1, 0, 0, 0}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 1}, {0, 0, 0, 1, 0}};
            bfs(graph, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 2 3 4 ", inspect.stack()[0].function))
    
    def test_185(self):
        input = """
        const MAX = 10;
        
        func generateBinary(arr [MAX]int, n int, index int){
            if (index == n) {
                for i := 0; i < n; i += 1 {
                    putInt(arr[i]);
                }
                putLn();
            } else {
                arr[index] := 0;
                generateBinary(arr, n, index + 1);
                arr[index] := 1;
                generateBinary(arr, n, index + 1);
            }
        }
        
        func main() {
            var n = 3;
            var arr [MAX] int;
            putString("All binary strings of length = ")
            putInt(n)
            putLn()
            generateBinary(arr, n, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, """All binary strings of length = 3\n000\n001\n010\n011\n100\n101\n110\n111\n""", inspect.stack()[0].function))
    
    
    ########################################
    # GROK
    ########################################
    
    def test_301(self):
        """Tests interface implementation and method calls that modify struct fields. Tricky: Ensures proper interface method dispatching with pass-by-value semantics."""
        input = """
        type Counter interface { increment(); getValue() int; }
        type SimpleCounter struct { value int; }
        func (s SimpleCounter) increment() { s.value += 1; }
        func (s SimpleCounter) getValue() int { return s.value; }

        func main() {
            var c Counter = SimpleCounter{value: 5}
            c.increment()
            c.increment()
            putIntLn(c.getValue())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7\n", inspect.stack()[0].function))

    def test_302(self):
        """Tests recursive function calls with a base case. Tricky: Manages stack frames and return value propagation through recursion."""
        input = """
        func recursiveSum(n int) int {
            if (n <= 0) { return 0; }
            return n + recursiveSum(n - 1);
        }

        func main() {
            putIntLn(recursiveSum(5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", inspect.stack()[0].function))

    def test_303(self):
        """Tests pass-by-value semantics for structs. Tricky: Modifications in a function affect only a copy, not the original struct."""
        input = """
        type Container struct { data [2]int; }
        func modifyArray(c Container) { c.data[0] := 100; }

        func main() {
            var c Container = Container{data: [2]int{1, 2}}
            modifyArray(c)
            putIntLn(c.data[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", inspect.stack()[0].function))

    def test_304(self):
        """Tests variable shadowing in function scope versus global scope. Tricky: Distinguishes between global and local variables with the same name."""
        input = """
        var global int = 10;
        func shadow() int {
            var global int = 20;
            return global;
        }

        func main() {
            putIntLn(global)
            putIntLn(shadow())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n20\n", inspect.stack()[0].function))

    def test_305(self):
        """Tests interface polymorphism and function passing. Tricky: Ensures proper method resolution through an interface."""
        input = """
        type Adder interface { add(a int) int; }
        type Number struct { value int; }
        func (n Number) add(a int) int { return n.value + a; }

        func applyAdder(a Adder, x int) int {
            return a.add(x);
        }

        func main() {
            var n Adder = Number{value: 15}
            putIntLn(applyAdder(n, 5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", inspect.stack()[0].function))

    def test_306(self):
        """Tests multi-dimensional array indexing and assignment with expressions. Tricky: Handles nested array accesses and arithmetic."""
        input = """
        func main() {
            var a [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            a[0][1] := a[1][0] + a[0][0]
            putIntLn(a[0][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", inspect.stack()[0].function))

    def test_307(self):
        """Tests struct field access and return value assignment. Tricky: Handles struct creation and field assignments in return statements."""
        input = """
        type Pair struct { x int; y int; }
        func swap(p Pair) Pair {
            return Pair{x: p.y, y: p.x};
        }

        func main() {
            var p Pair = Pair{x: 10, y: 20}
            p := swap(p)
            putIntLn(p.x)
            putIntLn(p.y)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n10\n", inspect.stack()[0].function))

    def test_308(self):
        """Tests variable shadowing in a for loop. Tricky: Outer variable is affected by loop variable with the same name."""
        input = """
        func main() {
            var i int = 5;
            for i := 0; i < 3; i += 1 {
                putIntLn(i)
            }
            putIntLn(i)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0\n1\n2\n3\n", inspect.stack()[0].function))

    def test_309(self):
        """Tests an array of interface types with method calls. Tricky: Handles interface method invocation for array elements."""
        input = """
        type Processor interface { process() int; }
        type Data struct { value int; }
        func (d Data) process() int { return d.value * 2; }

        func main() {
            var arr [2]Processor = [2]Processor{Data{value: 3}, Data{value: 4}}
            putIntLn(arr[0].process())
            putIntLn(arr[1].process())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n8\n", inspect.stack()[0].function))

    def test_310(self):
        """Tests recursive function calls with multiplication. Tricky: Manages recursive stack frames and arithmetic operations."""
        input = """
        func factorial(n int) int {
            if (n == 0) { return 1; }
            return n * factorial(n - 1);
        }

        func main() {
            putIntLn(factorial(4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "24\n", inspect.stack()[0].function))

    def test_311(self):
        """Tests nested array initialization within a struct. Tricky: Handles multi-dimensional array initialization and field access."""
        input = """
        type Nested struct { innerfield [1][1]int; }
        func main() {
            var n Nested = Nested{innerfield: [1][1]int{{42}}}
            putIntLn(n.innerfield[0][0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "42\n", inspect.stack()[0].function))

    def test_312(self):
        """Tests array copying and pass-by-value semantics. Tricky: Modifications to a copied array do not affect the original."""
        input = """
        func main() {
            var a [2]int = [2]int{1, 2}
            var b [2]int = a
            b[0] := 10
            putIntLn(a[0])
            putIntLn(b[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n10\n", inspect.stack()[0].function))

    def test_313(self):
        """Tests struct method calls with pass-by-value semantics. Tricky: Modifications in a method affect."""
        input = """
        type Counter struct { count int; }
        func (c Counter) inc() int { c.count += 1; return c.count; }

        func main() {
            var c Counter = Counter{count: 0}
            putIntLn(c.inc())
            putIntLn(c.inc())
            putIntLn(c.count)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n2\n", inspect.stack()[0].function))

    def test_314(self):
        """Tests string concatenation and variable shadowing. Tricky: Handles string operations and scope resolution correctly."""
        input = """
        func main() {
            var s string = "hello"
            var t string = "world"
            putStringLn(s + " " + t)
            s := "goodbye"
            putStringLn(s + " " + t)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "hello world\ngoodbye world\n", inspect.stack()[0].function))

    def test_315(self):
        """Tests interface method calls with floating-point values. Tricky: Ensures proper type handling for float returns."""
        input = """
        type Evaluator interface { eval() float; }
        type Constant struct { value float; }
        func (c Constant) eval() float { return c.value; }

        func main() {
            var e Evaluator = Constant{value: 3.14}
            putFloatLn(e.eval())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.14\n", inspect.stack()[0].function))

    def test_316(self):
        """Tests variable shadowing within an if block. Tricky: Inner variable does not affect the outer variable."""
        input = """
        func main() {
            var x int = 10;
            if (x > 5) {
                var x int = 20;
                putIntLn(x);
            }
            putIntLn(x);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n10\n", inspect.stack()[0].function))

    def test_317(self):
        """Tests struct creation via a function return. Tricky: Handles struct initialization and return value assignment."""
        input = """
        type Box struct { content int; }
        func createBox(n int) Box { return Box{content: n}; }

        func main() {
            var b Box = createBox(50)
            putIntLn(b.content)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "50\n", inspect.stack()[0].function))

    def test_318(self):
        """Tests array updates in a loop with index arithmetic. Tricky: Modifies array elements based on previous values."""
        input = """
        func main() {
            var a [3]int = [3]int{1, 2, 3}
            
            var i int;
            
            for i := 0; i < 2; i += 1 {
                a[i + 1] := a[i] + a[i + 1]
            }
            putIntLn(a[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", inspect.stack()[0].function))

    def test_319(self):
        """Tests interface method calls through a function. Tricky: Handles interface dispatching and function call chains."""
        input = """
        type Processor interface { process() int; }
        type Multiplier struct { factor int; }
        func (m Multiplier) process() int { return m.factor * 2; }

        func apply(p Processor) int { return p.process(); }

        func main() {
            var p Processor = Multiplier{factor: 5}
            putIntLn(apply(p))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n", inspect.stack()[0].function))

    def test_320(self):
        """Tests floating-point arithmetic with operator precedence. Tricky: Ensures multiplication is evaluated before addition."""
        input = """
        func main() {
            var x float = 1.5;
            var y float = 2.5;
            putFloatLn(x + y * 2.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6.5\n", inspect.stack()[0].function))

    def test_321(self):
        """Tests nested struct initialization and field access. Tricky: Handles recursive struct definitions and nested field access."""
        input = """
        type Container struct { value int; next Container; }
        func main() {
            var c Container = Container{value: 10, next: Container{value: 20}}
            putIntLn(c.value)
            putIntLn(c.next.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n20\n", inspect.stack()[0].function))

    def test_322(self):
        """Tests logical operators with short-circuit evaluation. Tricky: Ensures correct evaluation of logical AND with negation."""
        input = """
        func main() {
            var b boolean = true;
            if (b && !b) {
                putStringLn("impossible")
            } else {
                putStringLn("possible")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "possible\n", inspect.stack()[0].function))

    def test_323(self):
        """Tests three-dimensional array initialization within a struct. Tricky: Handles complex array initialization syntax."""
        input = """
        type Wrapper struct { data [1][1][1]int; }
        func main() {
            var w Wrapper = Wrapper{data: [1][1][1]int{{{100}}}}
            putIntLn(w.data[0][0][0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", inspect.stack()[0].function))

    def test_324(self):
        """Tests a while-like for loop with array updates. Tricky: Loop condition depends on array elements."""
        input = """
        func main() {
            var a [2]int = [2]int{1, 2}
            var i int = 0;
            for a[i] < 3 {
                a[i] := a[i] + 1
                i += 1
                if (i == 2) {
                    break
                }
            }
            putIntLn(a[0])
            putIntLn(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n3\n", inspect.stack()[0].function))

    def test_325(self):
        """Tests an interface with an empty struct. Tricky: Handles method calls on structs with no fields."""
        input = """
        type Operator interface { apply(x int) int; }
        type Doubler struct { name string; }
        func (d Doubler) apply(x int) int { return x * 2; }

        func main() {
            var op Operator = Doubler{name: "PDZ"}
            putIntLn(op.apply(7))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "14\n", inspect.stack()[0].function))

    def test_326(self):
        """Tests integer division and modulo operations. Tricky: Ensures correct handling of arithmetic operations."""
        input = """
        func main() {
            var x int = 10;
            var y int = x / 3;
            putIntLn(y)
            putIntLn(x % 3)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n1\n", inspect.stack()[0].function))

    def test_327(self):
        """Tests pass-by-value for structs. Tricky: Modifications in a function affect."""
        input = """
        type Holder struct { value int; }
        func update(h Holder) { h.value := 100; }

        func main() {
            var h Holder = Holder{value: 50}
            update(h)
            putIntLn(h.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", inspect.stack()[0].function))

    def test_328(self):
        """Tests nested loops with multi-dimensional array updates. Tricky: Handles nested loop control and array indexing."""
        input = """
        func main() {
            var a [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            
            var i int ;
            var j int ;
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    a[i][j] := a[i][j] * 2
                }
            }
            putIntLn(a[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "8\n", inspect.stack()[0].function))

    def test_329(self):
        """Tests interface method calls with struct fields. Tricky: Handles field access within interface methods."""
        input = """
        type Processor interface { compute() int; }
        type Adder struct { a int; b int; }
        func (a Adder) compute() int { return a.a + a.b; }

        func main() {
            var p Processor = Adder{a: 10, b: 20}
            putIntLn(p.compute())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30\n", inspect.stack()[0].function))

    def test_330(self):
        """Tests floating-point comparisons and conditional branching. Tricky: Handles floating-point arithmetic and condition evaluation."""
        input = """
        func main() {
            var x float = 2.0;
            var y float = 3.0;
            if (x * y > 5.0) {
                putFloatLn(x * y)
            } else {
                putFloatLn(x + y)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6.0\n", inspect.stack()[0].function))

    def test_331(self):
        """Tests nested struct initialization and field access. Tricky: Handles recursive struct definitions and nested field access."""
        input = """
        type Inner struct { value int; }
        type Nested struct { innerfield Inner; }
        func main() {
            var n Nested = Nested{innerfield: Inner{value: 42}}
            putIntLn(n.innerfield.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "42\n", inspect.stack()[0].function))

    def test_332(self):
        input = """
        func main() {
            var a [2]int = [2]int{10, 20};
            var b [2]int = [2]int{100, 200};
            putIntLn(b[0])
            putIntLn(b[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n200\n", inspect.stack()[0].function))

    def test_333(self):
        """Tests method returning a struct with pass-by-value semantics. Tricky: Returned struct reflects modified value."""
        input = """
        type Counter struct { value int; }
        func (c Counter) inc() Counter { c.value += 1; return c; }

        func main() {
            var c Counter = Counter{value: 5}
            c := c.inc()
            putIntLn(c.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", inspect.stack()[0].function))

    def test_334(self):
        """Tests string assignment and shadowing. Tricky: Ensures separate variables after shadowing."""
        input = """
        func main() {
            var s string = "abc";
            var t string = s;
            t := "xyz";
            putStringLn(s)
            putStringLn(t)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "abc\nxyz\n", inspect.stack()[0].function))

    def test_335(self):
        """Tests interface method calls with arithmetic operations. Tricky: Handles multiplication within the method."""
        input = """
        type Evaluator interface { eval() int; }
        type Pair struct { x int; y int; }
        func (p Pair) eval() int { return p.x * p.y; }

        func main() {
            var e Evaluator = Pair{x: 4, y: 5}
            putIntLn(e.eval())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", inspect.stack()[0].function))

    def test_336(self):
        """Tests variable shadowing in both branches of an if-else statement. Tricky: Outer variable changed."""
        input = """
        func main() {
            var x int = 10;
            if (x > 5) {
                x := 20;
                putIntLn(x);
            } else {
                x := 30;
                putIntLn(x);
            }
            putIntLn(x);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n20\n", inspect.stack()[0].function))

    def test_337(self):
        """Tests struct creation with array initialization via a function. Tricky: Handles array initialization in return value."""
        input = """
        type Box struct { content [2]int; }
        func createBox() Box { return Box{content: [2]int{1, 2}}; }

        func main() {
            var b Box = createBox()
            putIntLn(b.content[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", inspect.stack()[0].function))

    def test_338(self):
        """Tests conditional array updates in a loop. Tricky: Handles modulo checks and array modifications."""
        input = """
        func main() {
            var a [3]int = [3]int{1, 2, 3}
            
            var i int; 
            for i := 0; i < 3; i += 1 {
                if (a[i] % 2 == 0) {
                    a[i] := a[i] * 2
                }
            }
            putIntLn(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", inspect.stack()[0].function))

    def test_339(self):
        """Tests interface method calls with parameters through a function. Tricky: Handles parameter passing and interface dispatching."""
        input = """
        type Processor interface { process(x int) int; }
        type Scaler struct { factor int; }
        func (s Scaler) process(x int) int { return s.factor * x; }

        func apply(p Processor, x int) int { return p.process(x); }

        func main() {
            var p Processor = Scaler{factor: 3}
            putIntLn(apply(p, 4))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "12\n", inspect.stack()[0].function))

    def test_340(self):
        """Tests floating-point division and parentheses for precedence. Tricky: Ensures correct order of operations."""
        input = """
        func main() {
            var x float = 1.0;
            var y float = 2.0;
            putFloatLn((x + y) / 2.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1.5\n", inspect.stack()[0].function))

    def test_341(self):
        """Tests recursive struct initialization and nested field access. Tricky: Handles deep field access correctly."""
        input = """
        type Container struct { value int; innerfield Container; }
        func main() {
            var c Container = Container{value: 10, innerfield: Container{value: 20, innerfield: nil}}
            putIntLn(c.innerfield.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n", inspect.stack()[0].function))

    def test_342(self):
        """Tests logical operators with short-circuit evaluation. Tricky: Ensures condition is always true due to OR with negation."""
        input = """
        func main() {
            var b boolean = false;
            if (b || !b) {
                putStringLn("true")
            } else {
                putStringLn("false")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", inspect.stack()[0].function))

    def test_343(self):
        """Tests two-dimensional array initialization within a struct. Tricky: Handles nested array access."""
        input = """
        type Wrapper struct { data [2][2]int; }
        func main() {
            var w Wrapper = Wrapper{data: [2][2]int{{1, 2}, {3, 4}}}
            putIntLn(w.data[1][0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", inspect.stack()[0].function))

    def test_344(self):
        """Tests a while-like for loop with array updates based on a condition. Tricky: Loop stops based on array element values."""
        input = """
        func main() {
            var a [3]int = [3]int{1, 2, 3}
            var i int = 0;
            for a[i] < 5 {
                a[i] := a[i] * 2
                i += 1
                if (i == 3) {
                    break
                }
            }
            putIntLn(a[0])
            putIntLn(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n4\n", inspect.stack()[0].function))

    def test_345(self):
        """Tests an interface with an empty struct and multiplication. Tricky: Handles empty structs and method calls."""
        input = """
        type Operator interface { apply(x int) int; }
        type Tripler struct { name string; }
        func (t Tripler) apply(x int) int { return x * 3; }

        func main() {
            var op Operator = Tripler{name: "PDZ"}
            putIntLn(op.apply(5))
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", inspect.stack()[0].function))

    def test_346(self):
        """Tests complex arithmetic with division and multiplication precedence. Tricky: Evaluates division before multiplication and subtraction."""
        input = """
        func main() {
            var x int = 15;
            var y int = x - 2 * (x / 3);
            putIntLn(y)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5\n", inspect.stack()[0].function))

    def test_347(self):
        """Tests struct return from a function with modification. Tricky: Returned struct reflects updated value."""
        input = """
        type Holder struct { value int; }
        func update(h Holder) Holder { h.value := 100; return h; }

        func main() {
            var h Holder = Holder{value: 50}
            h := update(h)
            putIntLn(h.value)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "100\n", inspect.stack()[0].function))

    def test_348(self):
        """Tests array updates with computed indices in a loop. Tricky: Handles index computation for array access."""
        input = """
        func main() {
            var a [2][2]int = [2][2]int{{1, 2}, {3, 4}}
            
            var i int;
            for i := 0; i < 2; i += 1 {
                a[i][i] := a[i][1 - i]
            }
            putIntLn(a[0][0])
            putIntLn(a[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n3\n", inspect.stack()[0].function))

    def test_349(self):
        """Tests interface method calls with floating-point division. Tricky: Handles division and float returns."""
        input = """
        type Processor interface { compute() float; }
        type Divider struct { a float; b float; }
        func (d Divider) compute() float { return d.a / d.b; }

        func main() {
            var p Processor = Divider{a: 10.0, b: 2.0}
            putFloatLn(p.compute())
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.0\n", inspect.stack()[0].function))

    def test_350(self):
        """Tests logical operators with modulo checks in a conditional. Tricky: Handles logical AND and modulo correctly."""
        input = """
        func main() {
            var x int = 10;
            var y int = 20;
            if (x < y && y % 2 == 0) {
                putStringLn("both true")
            } else {
                putStringLn("not both true")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "both true\n", inspect.stack()[0].function))
    
    ########################################
    # GROK SVIP :))
    ########################################
    
    def test_351(self):
        """Tests Bubble Sort on an array of integers. Tricky: Handles nested loops and array swaps."""
        input = """
        func bubbleSort(arr [5]int, n int) {
            var i int;
            var j int;
            for i := 0; i < n-1; i += 1 {
                for j := 0; j < n-i-1; j += 1 {
                    if (arr[j] > arr[j+1]) {
                        var temp int = arr[j];
                        arr[j] := arr[j+1];
                        arr[j+1] := temp;
                    }
                }
            }
        }
        func main() {
            var arr [5]int = [5]int{64, 34, 25, 12, 22};
            bubbleSort(arr, 5);
            
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "12 22 25 34 64 ", inspect.stack()[0].function))

    def test_352(self):
        """Tests Selection Sort on an array of integers. Tricky: Finds minimum element in each iteration."""
        input = """
        func selectionSort(arr [5]int, n int) {
            var i int ;
            var j int;
            for i := 0; i < n-1; i += 1 {
                var minIdx int = i;
                for j := i+1; j < n; j += 1 {
                    if (arr[j] < arr[minIdx]) {
                        minIdx := j;
                    }
                }
                var temp int = arr[i];
                arr[i] := arr[minIdx];
                arr[minIdx] := temp;
            }
        }
        func main() {
            var arr [5]int = [5]int{64, 25, 12, 22, 11};
            selectionSort(arr, 5);
            
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "11 12 22 25 64 ", inspect.stack()[0].function))

    def test_353(self):
        """Tests Insertion Sort on an array of integers. Tricky: Shifts elements to insert in sorted position."""
        input = """
        func insertionSort(arr [5]int, n int) {
            var i int ;
            var j int ;
            for i := 1; i < n; i += 1 {
                var key int = arr[i];
                var j int = i - 1;
                for arr[j] > key {
                    arr[j+1] := arr[j];
                    j -= 1;
                    if (j == -1) {
                        break
                    }
                }
                arr[j+1] := key;
            }
        }
        func main() {
            var arr [5]int = [5]int{12, 11, 13, 5, 6};
            insertionSort(arr, 5);
            
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5 6 11 12 13 ", inspect.stack()[0].function))

    def test_354(self):
        """Tests QuickSort on an array of integers. Tricky: Recursive partitioning and pivot selection."""
        input = """
        func partition(arr [5]int, low int, high int) int {
            var pivot int = arr[high];
            var i int = low - 1;
            
            var j int;
            for j := low; j < high; j += 1 {
                if (arr[j] <= pivot) {
                    i += 1;
                    var temp int = arr[i];
                    arr[i] := arr[j];
                    arr[j] := temp;
                }
            }
            var temp int = arr[i+1];
            arr[i+1] := arr[high];
            arr[high] := temp;
            return i + 1;
        }
        func quickSort(arr [5]int, low int, high int) {
            if (low < high) {
                var pi int = partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }
        func main() {
            var arr [5]int = [5]int{10, 7, 8, 9, 1};
            quickSort(arr, 0, 4);
            
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1 7 8 9 10 ", inspect.stack()[0].function))

    def test_355(self):
        """Tests MergeSort on an array of integers. Tricky: Recursive division and merging of subarrays."""
        input = """
        func merge(arr [6]int, l int, m int, r int) {
            var n1 int = m - l + 1;
            var n2 int = r - m;
            var L [3]int;
            var R [3]int;
            var i int = 0;
            var j int = 0;
            
            for i := 0; i < n1; i += 1 {
                L[i] := arr[l + i];
            }
            for j := 0; j < n2; j += 1 {
                R[j] := arr[m + 1 + j];
            }
            
            i := 0
            j := 0
            
            var k int = l;
            for i < n1 && j < n2 {
                if (L[i] <= R[j]) {
                    arr[k] := L[i];
                    i += 1;
                } else {
                    arr[k] := R[j];
                    j += 1;
                }
                k += 1;
            }
            for i < n1 {
                arr[k] := L[i];
                i += 1;
                k += 1;
            }
            for j < n2 {
                arr[k] := R[j];
                j += 1;
                k += 1;
            }
        }
        func mergeSort(arr [6]int, l int, r int) {
            if (l < r) {
                var m int = (l + r) / 2;
                mergeSort(arr, l, m);
                mergeSort(arr, m + 1, r);
                merge(arr, l, m, r);
            }
        }
        func main() {
            var arr [6]int = [6]int{12, 11, 13, 5, 6, 7};
            mergeSort(arr, 0, 5);
            
            var i int;
            for i := 0; i < 6; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5 6 7 11 12 13 ", inspect.stack()[0].function))

    def test_356(self):
        """Tests HeapSort on an array of integers. Tricky: Maintains heap property and extracts max elements."""
        input = """
        func heapify(arr [5]int, n int, i int) {
            var largest int = i;
            var l int = 2 * i + 1;
            var r int = 2 * i + 2;
            if (l < n) {
                if (arr[l] > arr[largest]) {
                    largest := l;
                }
            }
            if (r < n) {
                if (arr[r] > arr[largest]) {
                    largest := r;
                }
            }
            if (largest != i) {
                var temp int = arr[i];
                arr[i] := arr[largest];
                arr[largest] := temp;
                heapify(arr, n, largest);
            }
        }
        func heapSort(arr [5]int, n int) {
            var i int;
            for i := n / 2 - 1; i >= 0; i -= 1 {
                heapify(arr, n, i);
            }
            for i := n - 1; i >= 0; i -= 1 {
                var temp int = arr[0];
                arr[0] := arr[i];
                arr[i] := temp;
                heapify(arr, i, 0);
            }
        }
        func main() {
            var arr [5]int = [5]int{12, 11, 13, 5, 6};
            heapSort(arr, 5);
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5 6 11 12 13 ", inspect.stack()[0].function))

    def test_357(self):
        """Tests Counting Sort for small integers. Tricky: Uses auxiliary array for counting occurrences."""
        input = """
        func countingSort(arr [6]int, n int) {
            var output [6]int;
            var count [10]int;
            var i int;
            for i := 0; i < n; i += 1 {
                count[arr[i]] := count[arr[i]] + 1;
            }
            for i := 1; i < 10; i += 1 {
                count[i] := count[i] + count[i-1];
            }
            for i := n-1; i >= 0; i -= 1 {
                output[count[arr[i]] - 1] := arr[i];
                count[arr[i]] := count[arr[i]] - 1;
            }
            for i := 0; i < n; i += 1 {
                arr[i] := output[i];
            }
        }
        func main() {
            var arr [6]int = [6]int{4, 2, 2, 8, 3, 3};
            countingSort(arr, 6); 
            var i int;
            for i := 0; i < 6; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2 2 3 3 4 8 ", inspect.stack()[0].function))

    def test_358(self):
        """Tests Radix Sort for small integers. Tricky: Processes digits iteratively using counting sort."""
        input = """
        func countingSortForRadix(arr [5]int, n int, exp int) {
            var output [5]int;
            var count [10]int;
            var i int;
            for i := 0; i < n; i += 1 {
                count[(arr[i] / exp) % 10] := count[(arr[i] / exp) % 10] + 1;
            }
            for i := 1; i < 10; i += 1 {
                count[i] := count[i] + count[i-1];
            }
            for i := n-1; i >= 0; i -= 1 {
                output[count[(arr[i] / exp) % 10] - 1] := arr[i];
                count[(arr[i] / exp) % 10] := count[(arr[i] / exp) % 10] - 1;
            }
            for i := 0; i < n; i += 1 {
                arr[i] := output[i];
            }
        }
        func radixSort(arr [5]int, n int) {
            var max int = arr[0];
            var i int;
            for i := 1; i < n; i += 1 {
                if (arr[i] > max) {
                    max := arr[i];
                }
            }
            var exp int;
            for exp := 1; max / exp > 0; exp := exp * 10 {
                countingSortForRadix(arr, n, exp);
            }
        }
        func main() {
            var arr [5]int = [5]int{170, 45, 75, 90, 802};
            radixSort(arr, 5);
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "45 75 90 170 802 ", inspect.stack()[0].function))

    def test_359(self):
        """Tests Shell Sort on an array of integers. Tricky: Uses gap-based comparisons and insertions."""
        input = """
        func shellSort(arr [5]int, n int) {
            var gap int ;
            var i int;
            for gap := n/2; gap > 0; gap := gap/2 {
                for i := gap; i < n; i += 1 {
                    var temp int = arr[i];
                    var j int = i;
                    for arr[j-gap] > temp {
                        arr[j] := arr[j-gap];
                        j := j - gap;
                        if (j < gap) {
                            break
                        }
                    }
                    arr[j] := temp;
                }
            }
        }
        func main() {
            var arr [5]int = [5]int{12, 34, 54, 2, 3};
            shellSort(arr, 5);
            var i int ;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2 3 12 34 54 ", inspect.stack()[0].function))

    def test_360(self):
        """Tests Cocktail Sort (bidirectional bubble sort). Tricky: Reduces passes by sorting from both ends."""
        input = """
        func cocktailSort(arr [5]int, n int) {
            var swapped boolean = true;
            var start int = 0;
            var end int = n - 1;
            for swapped {
                var i int;
                swapped := false;
                for i := start; i < end; i += 1 {
                    if (arr[i] > arr[i + 1]) {
                        var temp int = arr[i];
                        arr[i] := arr[i + 1];
                        arr[i + 1] := temp;
                        swapped := true;
                    }
                }
                if (!swapped) {
                    break;
                }
                swapped := false;
                end := end - 1;
                for i := end - 1; i >= start; i -= 1 {
                    if (arr[i] > arr[i + 1]) {
                        var temp int = arr[i];
                        arr[i] := arr[i + 1];
                        arr[i + 1] := temp;
                        swapped := true;
                    }
                }
                start := start + 1;
            }
        }
        func main() {
            var arr [5]int = [5]int{64, 34, 25, 12, 22};
            cocktailSort(arr, 5);
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(arr[i]);
                putString(" ");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "12 22 25 34 64 ", inspect.stack()[0].function))
        
    def test_361(self):
        """Tests a singly linked list with insertion at head. Tricky: Handles recursive struct initialization."""
        input = """
        type Node struct { value int; next Node; }
        func insertHead(head Node, value int) Node {
            return Node{value: value, next: head};
        }
        func main() {
            var head Node = nil;
            head := insertHead(head, 30);
            head := insertHead(head, 20);
            head := insertHead(head, 10);
            putIntLn(head.value);
            putIntLn(head.next.value);
            putIntLn(head.next.next.value);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n20\n30\n", inspect.stack()[0].function))

    def test_362(self):
        """Tests linked list traversal and sum. Tricky: Recursive traversal of a linked list."""
        input = """
        type Node struct { value int; next Node; }
        func sumList(head Node) int {
            if (head == nil) {
                return 0;
            }
            return head.value + sumList(head.next);
        }
        func main() {
            var head Node = Node{value: 10, next: Node{value: 20, next: Node{value: 30, next: nil}}};
            putIntLn(sumList(head));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "60\n", inspect.stack()[0].function))

    def test_363(self):
        """Tests linked list reversal. Tricky: Iterative manipulation of next pointers."""
        input = """
        type Node struct { value int; next Node; }
        func reverseList(head Node) Node {
            var prev Node = nil;
            var curr Node = head;
            for curr != nil {
                var next Node = curr.next;
                curr.next := prev;
                prev := curr;
                curr := next;
            }
            return prev;
        }
        func main() {
            var head Node = Node{value: 10, next: Node{value: 20, next: Node{value: 30, next: nil}}};
            head := reverseList(head);
            putIntLn(head.value);
            putIntLn(head.next.value);
            putIntLn(head.next.next.value);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30\n20\n10\n", inspect.stack()[0].function))

    def test_364(self):
        """Tests a stack implementation using an array. Tricky: Manages stack operations with array indexing."""
        input = """
        type Stack struct { data [5]int; top int; }
        func (s Stack) push(value int) Stack {
            s.data[s.top] := value;
            s.top := s.top + 1;
            return s;
        }
        func (s Stack) pop() Stack {
            s.top := s.top - 1;
            return s;
        }
        func (s Stack) peek() int {
            return s.data[s.top - 1];
        }
        func main() {
            var s Stack = Stack{data: [5]int{0, 0, 0, 0, 0}, top: 0};
            s := s.push(10);
            s := s.push(20);
            s := s.push(30);
            putIntLn(s.peek());
            s := s.pop();
            putIntLn(s.peek());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30\n20\n", inspect.stack()[0].function))

    def test_365(self):
        """Tests a queue implementation using an array. Tricky: Manages front and rear indices."""
        input = """
        type Queue struct { data [5]int; front int; rear int; }
        func (q Queue) enqueue(value int) Queue {
            q.data[q.rear] := value;
            q.rear := q.rear + 1;
            return q;
        }
        func (q Queue) dequeue() Queue {
            q.front := q.front + 1;
            return q;
        }
        func (q Queue) frontValue() int {
            return q.data[q.front];
        }
        func main() {
            var q Queue = Queue{data: [5]int{0, 0, 0, 0, 0}, front: 0, rear: 0};
            q := q.enqueue(10);
            q := q.enqueue(20);
            q := q.enqueue(30);
            putIntLn(q.frontValue());
            q := q.dequeue();
            putIntLn(q.frontValue());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n20\n", inspect.stack()[0].function))

    def test_366(self):
        """Tests linked list deletion by value. Tricky: Handles edge cases like head deletion."""
        input = """
        type Node struct { value int; next Node; }
        func deleteNode(head Node, value int) Node {
            if (head == nil) {
                return nil;
            }
            if (head.value == value) {
                return head.next;
            }
            var curr Node = head;
            for curr.next != nil {
                if (curr.next.value == value) {
                    curr.next := curr.next.next;
                    return head;
                }
                curr := curr.next;
            }
            return head;
        }
        func main() {
            var head Node = Node{value: 10, next: Node{value: 20, next: Node{value: 30, next: nil}}};
            head := deleteNode(head, 20);
            putIntLn(head.value);
            putIntLn(head.next.value);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10\n30\n", inspect.stack()[0].function))

    def test_367(self):
        """Tests a circular linked list detection. Tricky: Uses Floyd’s cycle detection algorithm."""
        input = """
        type Node struct { value int; next Node; }
        func hasCycle(head Node) boolean {
            if (head == nil) {
                return false;
            }
            var slow Node = head;
            var fast1 Node = head;
            for fast1 != nil && fast1.next != nil {
                slow := slow.next;
                fast1 := fast1.next.next;
                
                if (slow == fast1) {
                    return true;
                }
            }
            return false;
        }
        func main() {
            var head Node = Node{value: 10, next: nil};
            head.next := Node{value: 20, next: nil};
            head.next.next := Node{value: 30, next: nil};
            head.next.next.next := head.next; // Creates cycle
            putBoolLn(hasCycle(head));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", inspect.stack()[0].function))

    def test_368(self):
        """Tests a stack-based expression evaluation. Tricky: Parses and evaluates a simple arithmetic expression."""
        input = """
        type Stack struct { data [10]int; top int; }
        func (s Stack) push(value int) Stack {
            s.data[s.top] := value;
            s.top := s.top + 1;
            return s;
        }
        func (s Stack) pop() Stack {
            s.top := s.top - 1;
            return s;
        }
        func (s Stack) peek() int {
            return s.data[s.top - 1];
        }
        func evaluate(expr [5]int) int {
            var i int;
            var s Stack = Stack{data: [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, top: 0};
            for i := 0; i < 5; i += 1 {
                s := s.push(expr[i]);
            }
            var result int = s.peek();
            s := s.pop();
            for s.top > 0 {
                result := result + s.peek();
                s := s.pop();
            }
            return result;
        }
        func main() {
            var expr [5]int = [5]int{1, 2, 3, 4, 5};
            putIntLn(evaluate(expr));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15\n", inspect.stack()[0].function))

    def test_369(self):
        """Tests a doubly linked list insertion. Tricky: Manages prev and next pointers."""
        input = """
        type Node struct { value int; next Node; prev Node; }
        func insertAfter(prevNode Node, value int) Node {
            var newNode Node = Node{value: value};
            newNode.next := prevNode.next;
            newNode.prev := prevNode;
            prevNode.next := newNode;
            if (newNode.next != nil) {
                newNode.next.prev := newNode;
            }
            return newNode;
        }
        func main() {
            var head Node = Node{value: 10, next: nil, prev: nil};
            var second Node = Node{value: 30, next: nil, prev: nil};
            head.next := second;
            second.prev := head;
            var newNode Node = insertAfter(head, 20);
            putIntLn(head.next.value);
            putIntLn(newNode.next.value);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n30\n", inspect.stack()[0].function))

    def test_370(self):
        """Tests a priority queue using a max heap. Tricky: Maintains heap property during insertions."""
        input = """
        type PriorityQueue struct { data [5]int; size int; }
        func (pq PriorityQueue) parent(i int) int { return (i - 1) / 2; }
        func (pq PriorityQueue) left(i int) int { return 2 * i + 1; }
        func (pq PriorityQueue) right(i int) int { return 2 * i + 2; }
        func (pq PriorityQueue) swap(i int, j int) PriorityQueue {
            var temp int = pq.data[i];
            pq.data[i] := pq.data[j];
            pq.data[j] := temp;
            return pq;
        }
        func (pq PriorityQueue) heapify(i int) {
            var largest int = i;
            var l int = pq.left(i);
            var r int = pq.right(i);
            if (l < pq.size && pq.data[l] > pq.data[largest]) {
                largest := l;
            }
            if (r < pq.size && pq.data[r] > pq.data[largest]) {
                largest := r;
            }
            if (largest != i) {
                // pq := pq.swap(i, largest);
                pq.swap(i, largest);
                // pq := pq.heapify(largest);
                pq.heapify(largest);
            }
            // return pq;
        }
        func (pq PriorityQueue) insert(value int) PriorityQueue {
            pq.data[pq.size] := value;
            pq.size := pq.size + 1;
            var i int = pq.size - 1;
            for i != 0 && pq.data[pq.parent(i)] < pq.data[i] {
                pq := pq.swap(i, pq.parent(i));
                i := pq.parent(i);
            }
            return pq;
        }
        func (pq PriorityQueue) print() PriorityQueue {
            var i int;
            for i := 0; i < pq.size; i += 1 {
                putIntLn(pq.data[i]);
            }
            return pq;
        }
        func main() {
            var pq PriorityQueue = PriorityQueue{data: [5]int{0, 0, 0, 0, 0}, size: 0};
            pq := pq.insert(10);
            pq := pq.insert(20);
            pq := pq.insert(15);
            putIntLn(pq.data[0]);
            pq := pq.print();
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20\n20\n10\n15\n", inspect.stack()[0].function))
    
    def test_371(self):
        """Tests binary tree inorder traversal. Tricky: Recursive traversal of a binary tree."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func inorder(root Node) {
            if (root != nil) {
                inorder(root.left);
                putInt(root.value);
                putString(" ");
                inorder(root.right);
            }
        }
        func main() {
            var root Node = Node{value: 1, left: nil, right: nil};
            root.left := Node{value: 2, left: nil, right: nil};
            root.right := Node{value: 3, left: nil, right: nil};
            root.left.left := Node{value: 4, left: nil, right: nil};
            root.left.right := Node{value: 5, left: nil, right: nil};
            inorder(root);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4 2 5 1 3 ", inspect.stack()[0].function))

    def test_372(self):
        """Tests binary search tree insertion. Tricky: Maintains BST property during insertion."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func insert(root Node, value int) Node {
            if (root == nil) {
                return Node{value: value};
            }
            if (value < root.value) {
                root.left := insert(root.left, value);
            } else {
                root.right := insert(root.right, value);
            }
            return root;
        }
        func inorder(root Node) {
            if (root != nil) {
                inorder(root.left);
                putInt(root.value);
                putString(" ");
                inorder(root.right);
            }
        }
        func main() {
            var root Node = nil;
            root := insert(root, 50);
            root := insert(root, 30);
            root := insert(root, 70);
            root := insert(root, 20);
            root := insert(root, 40);
            inorder(root);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "20 30 40 50 70 ", inspect.stack()[0].function))

    def test_373(self):
        """Tests binary tree height calculation. Tricky: Recursive computation of maximum depth."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func max(a int, b int) int {
            if (a > b) {
                return a;
            }
            return b;
        }
        func height(root Node) int {
            if (root == nil) {
                return 0;
            }
            return 1 + max(height(root.left), height(root.right));
        }
        func main() {
            var root Node = Node{value: 1, left: nil, right: nil};
            root.left := Node{value: 2, left: nil, right: nil};
            root.right := Node{value: 3, left: nil, right: nil};
            root.left.left := Node{value: 4, left: nil, right: nil};
            root.left.right := Node{value: 5, left: nil, right: nil};
            putIntLn(height(root));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", inspect.stack()[0].function))

    def test_374(self):
        """Tests Depth-First Search (DFS) on a graph using adjacency list. Tricky: Recursive exploration of nodes."""
        input = """
        type Graph struct { adj [4][4]int; }
        func dfsUtil(g Graph, v int, visited [4]boolean) {
            visited[v] := true;
            putInt(v);
            putString(" ");
            var i int;
            for i := 0; i < 4; i += 1 {
                if (g.adj[v][i] == 1 && !visited[i]) {
                    dfsUtil(g, i, visited);
                }
            }
        }
        func dfs(g Graph, start int) {
            var visited [4]boolean;
            dfsUtil(g, start, visited);
        }
        func main() {
            var g Graph = Graph{adj: [4][4]int{{0, 1, 1, 0}, {1, 0, 0, 1}, {1, 0, 0, 1}, {0, 1, 1, 0}}};
            dfs(g, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 3 2 ", inspect.stack()[0].function))

    def test_375(self):
        """Tests Breadth-First Search (BFS) on a graph using a queue. Tricky: Manages queue operations for level-order traversal."""
        input = """
        type Queue struct { data [4]int; front int; rear int; }
        func (q Queue) enqueue(value int) Queue {
            q.data[q.rear] := value;
            q.rear := q.rear + 1;
            return q;
        }
        func (q Queue) dequeue() Queue {
            q.front := q.front + 1;
            return q;
        }
        func (q Queue) frontValue() int {
            return q.data[q.front];
        }
        func (q Queue) isEmpty() boolean {
            return q.front == q.rear;
        }
        type Graph struct { adj [4][4]int; }
        func bfs(g Graph, start int) {
            var visited [4]boolean;
            var q Queue = Queue{data: [4]int{0,0,0,0}, front: 0, rear: 0};
            visited[start] := true;
            q := q.enqueue(start);
            for !q.isEmpty() {
                var v int = q.frontValue();
                q := q.dequeue();
                putInt(v);
                putString(" ");
                var i int;
                for i := 0; i < 4; i += 1 {
                    if (g.adj[v][i] == 1 && !visited[i]) {
                        visited[i] := true;
                        q := q.enqueue(i);
                    }
                }
            }
        }
        func main() {
            var g Graph = Graph{adj: [4][4]int{{0, 1, 1, 0}, {1, 0, 0, 1}, {1, 0, 0, 1}, {0, 1, 1, 0}}};
            bfs(g, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 2 3 ", inspect.stack()[0].function))

    def test_376(self):
        """Tests binary tree level-order traversal using a queue. Tricky: Manages queue for breadth-first traversal."""
        input = """
        type Node struct { value int; left Node; right Node; }
        type Queue struct { data [5]Node; front int; rear int; }
        func (q Queue) enqueue(n Node) Queue {
            q.data[q.rear] := n;
            q.rear := q.rear + 1;
            return q;
        }
        func (q Queue) dequeue() Queue {
            q.front := q.front + 1;
            return q;
        }
        func (q Queue) frontNode() Node {
            return q.data[q.front];
        }
        func (q Queue) isEmpty() boolean {
            return q.front == q.rear;
        }
        func levelOrder(root Node) {
            if (root == nil) {
                return;
            }
            var q Queue = Queue{data: [5]Node{nil, nil, nil, nil, nil}, front: 0, rear: 0};
            q := q.enqueue(root);
            for !q.isEmpty() {
                var n Node = q.frontNode();
                q := q.dequeue();
                putInt(n.value);
                putString(" ");
                if (n.left != nil) {
                    q := q.enqueue(n.left);
                }
                if (n.right != nil) {
                    q := q.enqueue(n.right);
                }
            }
        }
        func main() {
            var root Node = Node{value: 1, left: nil, right: nil};
            root.left := Node{value: 2, left: nil, right: nil};
            root.right := Node{value: 3, left: nil, right: nil};
            root.left.left := Node{value: 4, left: nil, right: nil};
            root.left.right := Node{value: 5, left: nil, right: nil};
            levelOrder(root);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1 2 3 4 5 ", inspect.stack()[0].function))

    def test_377(self):
        """Tests binary search tree search operation. Tricky: Recursive search with comparisons."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func search(root Node, value int) boolean {
            if (root == nil) {
                return false;
            }
            if (root.value == value) {
                return true;
            }
            if (value < root.value) {
                return search(root.left, value);
            }
            return search(root.right, value);
        }
        func main() {
            var root Node = Node{value: 50, left: nil, right: nil};
            root.left := Node{value: 30, left: nil, right: nil};
            root.right := Node{value: 70, left: nil, right: nil};
            root.left.left := Node{value: 20, left: nil, right: nil};
            root.left.right := Node{value: 40, left: nil, right: nil};
            putBoolLn(search(root, 40));
            putBoolLn(search(root, 100));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\nfalse\n", inspect.stack()[0].function))

    def test_378(self):
        """Tests checking if a binary tree is a BST. Tricky: Recursive validation of BST property."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func isBSTUtil(node Node, min int, max int) boolean {
            if (node == nil) {
                return true;
            }
            if (node.value < min || node.value > max) {
                return false;
            }
            return isBSTUtil(node.left, min, node.value - 1) && isBSTUtil(node.right, node.value + 1, max);
        }
        func isBST(root Node) boolean {
            return isBSTUtil(root, -1000, 1000);
        }
        func main() {
            var root Node = Node{value: 50, left: nil, right: nil};
            root.left := Node{value: 30, left: nil, right: nil};
            root.right := Node{value: 70, left: nil, right: nil};
            root.left.left := Node{value: 20, left: nil, right: nil};
            root.left.right := Node{value: 40, left: nil, right: nil};
            putBoolLn(isBST(root));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", inspect.stack()[0].function))

    def test_379(self):
        """Tests finding the lowest common ancestor in a binary tree. Tricky: Recursive path finding."""
        input = """
        type Node struct { value int; left Node; right Node; }
        func lca(root Node, n1 int, n2 int) int {
            if (root == nil) {
                return -1;
            }
            if (root.value == n1 || root.value == n2) {
                return root.value;
            }
            var left int = lca(root.left, n1, n2);
            var right int = lca(root.right, n1, n2);
            if (left != -1 && right != -1) {
                return root.value;
            }
            if (left != -1) {
                return left;
            }
            return right;
        }
        func main() {
            var root Node = Node{value: 1, left: nil, right: nil};
            root.left := Node{value: 2, left: nil, right: nil};
            root.right := Node{value: 3, left: nil, right: nil};
            root.left.left := Node{value: 4, left: nil, right: nil};
            root.left.right := Node{value: 5, left: nil, right: nil};
            putIntLn(lca(root, 4, 5));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", inspect.stack()[0].function))

    def test_380(self):
        """Tests Dijkstra’s algorithm using an adjacency matrix. Tricky: Manages distances and visited nodes."""
        input = """
        func minDistance(dist [4]int, visited [4]boolean) int {
            var min int = 1000;
            var minIndex int = -1;
            var v int;
            for v := 0; v < 4; v += 1 {
                if (!visited[v] && dist[v] <= min) {
                    min := dist[v];
                    minIndex := v;
                }
            }
            return minIndex;
        }
        func dijkstra(graph [4][4]int, src int) int {
            var dist [4]int;
            var visited [4]boolean;
            var i int;
            for i := 0; i < 4; i += 1 {
                dist[i] := 1000;
            }
            dist[src] := 0;
            for count := 0; count < 3; count += 1 {
                var u int = minDistance(dist, visited);
                visited[u] := true;
                var v int;
                for v := 0; v < 4; v += 1 {
                    if (!visited[v] && graph[u][v] != 0 && dist[u] != 1000 && dist[u] + graph[u][v] < dist[v]) {
                        dist[v] := dist[u] + graph[u][v];
                    }
                }
            }
            return dist[2];
        }
        func main() {
            var graph [4][4]int = [4][4]int{{0, 4, 8, 0}, {4, 0, 2, 5}, {8, 2, 0, 5}, {0, 5, 5, 0}};
            putIntLn(dijkstra(graph, 0));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6\n", inspect.stack()[0].function))
    
    def test_381(self):
        """Tests 0-1 Knapsack problem using dynamic programming. Tricky: Builds a 2D table for optimization."""
        input = """
        func knapsack(W int, wt [3]int, val [3]int, n int) int {
            var K [4][6]int;
            var i int;
            var w int;
            for i := 0; i <= n; i += 1 {
                for w := 0; w <= W; w += 1 {
                    if (i == 0 || w == 0) {
                        K[i][w] := 0;
                    } else if (wt[i-1] <= w) {
                        if (val[i-1] + K[i-1][w-wt[i-1]] > K[i-1][w]) {
                            K[i][w] := val[i-1] + K[i-1][w-wt[i-1]];
                        } else {
                            K[i][w] := K[i-1][w];
                        }
                    } else {
                        K[i][w] := K[i-1][w];
                    }
                }
            }
            return K[n][W];
        }
        func main() {
            var val [3]int = [3]int{60, 100, 120};
            var wt [3]int = [3]int{1, 2, 3};
            var W int = 5;
            putIntLn(knapsack(W, wt, val, 3));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "220\n", inspect.stack()[0].function))

    def test_382(self):
        """Tests Longest Common Subsequence (LCS) using dynamic programming. Tricky: Builds a 2D table for string comparison."""
        input = """
        func lcs(X [4]int, Y [4]int, m int, n int) int {
            var L [5][5]int;
            var i int ;
            var j int;
            for i := 0; i <= m; i += 1 {
                for j := 0; j <= n; j += 1 {
                    if (i == 0 || j == 0) {
                        L[i][j] := 0;
                    } else if (X[i-1] == Y[j-1]) {
                        L[i][j] := L[i-1][j-1] + 1;
                    } else {
                        if (L[i-1][j] > L[i][j-1]) {
                            L[i][j] := L[i-1][j];
                        } else {
                            L[i][j] := L[i][j-1];
                        }
                    }
                }
            }
            return L[m][n];
        }
        func main() {
            var X [4]int = [4]int{1, 2, 3, 4};
            var Y [4]int = [4]int{2, 3, 4, 5};
            putIntLn(lcs(X, Y, 4, 4));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", inspect.stack()[0].function))

    def test_383(self):
        """Tests Fibonacci sequence using dynamic programming. Tricky: Avoids recursion with iterative table."""
        input = """
        func fib(n int) int {
            var f [10]int;
            var i int ;
            f[0] := 0;
            f[1] := 1;
            for i := 2; i <= n; i += 1 {
                f[i] := f[i-1] + f[i-2];
            }
            return f[n];
        }
        func main() {
            putIntLn(fib(6));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "8\n", inspect.stack()[0].function))

    def test_384(self):
        """Tests Matrix Chain Multiplication order using dynamic programming. Tricky: Finds optimal parenthesization."""
        input = """
        func matrixChainOrder(p [4]int, n int) int {
            var m [4][4]int;
            var i int ;
            for i := 1; i < n; i += 1 {
                m[i][i] := 0;
            }
            for L := 2; L < n; L += 1 {
                for i := 1; i < n - L + 1; i += 1 {
                    var j int = i + L - 1;
                    m[i][j] := 1000000;
                    var k int;
                    for k := i; k < j; k += 1 {
                        var q int = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j];
                        if (q < m[i][j]) {
                            m[i][j] := q;
                        }
                    }
                }
            }
            return m[1][n-1];
        }
        func main() {
            var arr [4]int = [4]int{10, 20, 30, 40};
            putIntLn(matrixChainOrder(arr, 4));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "18000\n", inspect.stack()[0].function))

    def test_385(self):
        """Tests Longest Increasing Subsequence (LIS) using dynamic programming. Tricky: Tracks maximum length subsequence."""
        input = """
        func lis(arr [6]int, n int) int {
            var lis [6]int;
            var i int ;
            for i := 0; i < n; i += 1 {
                lis[i] := 1;
            }
            for i := 1; i < n; i += 1 {
                var j int ;
                for j := 0; j < i; j += 1 {
                    if (arr[i] > arr[j] && lis[i] < lis[j] + 1) {
                        lis[i] := lis[j] + 1;
                    }
                }
            }
            var max int = lis[0];
            for i := 1; i < n; i += 1 {
                if (max < lis[i]) {
                    max := lis[i];
                }
            }
            return max;
        }
        func main() {
            var arr [6]int = [6]int{10, 22, 9, 33, 21, 50};
            putIntLn(lis(arr, 6));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4\n", inspect.stack()[0].function))

    def test_386(self):
        """Tests binary search on a sorted array. Tricky: Iterative divide-and-conquer search."""
        input = """
        func binarySearch(arr [5]int, l int, r int, x int) int {
            for l <= r {
                var mid int = (l + r) / 2;
                if (arr[mid] == x) {
                    return mid;
                }
                if (arr[mid] > x) {
                    r := mid - 1;
                } else {
                    l := mid + 1;
                }
            }
            return -1;
        }
        func main() {
            var arr [5]int = [5]int{2, 3, 4, 10, 40};
            putIntLn(binarySearch(arr, 0, 4, 10));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3\n", inspect.stack()[0].function))

    def test_387(self):
        """Tests KMP string matching algorithm. Tricky: Builds LPS array for pattern matching."""
        input = """
        func computeLPS(pat [3]int, M int, lps [3]int) {
            var len int = 0;
            lps[0] := 0;
            var i int = 1;
            for i < M {
                if (pat[i] == pat[len]) {
                    len := len + 1;
                    lps[i] := len;
                    i := i + 1;
                } else {
                    if (len != 0) {
                        len := lps[len-1];
                    } else {
                        lps[i] := 0;
                        i := i + 1;
                    }
                }
            }
        }
        func kmpSearch(txt [5]int, pat [3]int) int {
            var M int = 3;
            var N int = 5;
            var lps [3]int;
            computeLPS(pat, M, lps);
            var i int = 0;
            var j int = 0;
            for i < N {
                if (pat[j] == txt[i]) {
                    j := j + 1;
                    i := i + 1;
                }
                if (j == M) {
                    return i - j;
                } else if (i < N && pat[j] != txt[i]) {
                    if (j != 0) {
                        j := lps[j-1];
                    } else {
                        i := i + 1;
                    }
                }
            }
            return -1;
        }
        func main() {
            var txt [5]int = [5]int{1, 2, 3, 2, 3};
            var pat [3]int = [3]int{2, 3, 2};
            putIntLn(kmpSearch(txt, pat));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n", inspect.stack()[0].function))

    def test_388(self):
        """Tests Edit Distance (Levenshtein) using dynamic programming. Tricky: Computes minimum operations for string transformation."""
        input = """
        func min(a int, b int, c int) int {
            if (a <= b && a <= c) {
                return a;
            }
            if (b <= c) {
                return b;
            }
            return c;
        }
        func editDistance(str1 [3]int, str2 [3]int, m int, n int) int {
            var dp [4][4]int;
            var i int ;
            var j int ;
            for i := 0; i <= m; i += 1 {
                for j := 0; j <= n; j += 1 {
                    if (i == 0) {
                        dp[i][j] := j;
                    } else if (j == 0) {
                        dp[i][j] := i;
                    } else if (str1[i-1] == str2[j-1]) {
                        dp[i][j] := dp[i-1][j-1];
                    } else {
                        dp[i][j] := 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]);
                    }
                }
            }
            return dp[m][n];
        }
        func main() {
            var str1 [3]int = [3]int{1, 2, 3};
            var str2 [3]int = [3]int{2, 3, 4};
            putIntLn(editDistance(str1, str2, 3, 3));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2\n", inspect.stack()[0].function))

    def test_389(self):
        """Tests Subset Sum problem using dynamic programming. Tricky: Determines if a subset sums to a target."""
        input = """
        const MAXINT = 100
        func isSubsetSum(set [4]int, n int, sum int) boolean {
            var subset [5][MAXINT]int;
            var i int ;
            var j int ;
            for i := 0; i <= n; i += 1 {
                subset[i][0] := 1;
            }
            for j := 1; j <= sum; j += 1 {
                subset[0][j] := 0;
            }
            for i := 1; i <= n; i += 1 {
                for j := 1; j <= sum; j += 1 {
                    if (j < set[i-1]) {
                        subset[i][j] := subset[i-1][j];
                    } else {
                        if (subset[i-1][j] == 1 || subset[i-1][j-set[i-1]] == 1) {
                            subset[i][j] := 1;
                        } else {
                            subset[i][j] := 0;
                        }
                    }
                }
            }
            return subset[n][sum] == 1;
        }
        func main() {
            var set [4]int = [4]int{3, 2, 4, 12};
            var sum int = 9;
            putBoolLn(isSubsetSum(set, 4, sum));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", inspect.stack()[0].function))

    def test_390(self):
        """Tests N-Queens problem (4x4 board). Tricky: Backtracking to place queens safely."""
        input = """
        func isSafe(board [4][4]int, row int, col int) boolean {
            var i int;
            var k int;
            for i := 0; i < col; i += 1 {
                if (board[row][i] == 1) {
                    return false;
                }
            }
            for k := 0; k <= row && k <= col; k += 1 {
                if (board[row - k][col - k] == 1) {
                    return false;
                }
            }
            for k := 0; row + k < 4 && k <= col; k += 1 {
                if (board[row + k][col - k] == 1) {
                    return false;
                }
            }
            return true;
        }
        func solveNQueensUtil(board [4][4]int, col int) boolean {
            if (col >= 4) {
                return true;
            }
            
            var i int;
            
            for i := 0; i < 4; i += 1 {
                safe := isSafe(board, i, col);
                if (isSafe(board, i, col)) {
                    board[i][col] := 1;
                    if (solveNQueensUtil(board, col + 1)) {
                        return true;
                    }
                    board[i][col] := 0;
                }
            }
            return false;
        }
        func solveNQueens() boolean {
            var board [4][4]int;
            return solveNQueensUtil(board, 0);
        }
        func main() {
            putBoolLn(solveNQueens());
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\n", inspect.stack()[0].function))
    
    def test_391(self):
        """Tests K-Means clustering (single iteration). Tricky: Computes centroids for clusters."""
        input = """
        func kMeans(points [4][2]float, k int) float {
            var centroids [2][2]float = [2][2]float{{0.0, 0.0}, {0.0, 0.0}};
            var count [2]int;
            var i int ;
            
            for i := 0; i < 4; i += 1 {
                var cluster int = 0;
                if (points[i][0] > 2.0) {
                    cluster := 1;
                }
                centroids[cluster][0] := centroids[cluster][0] + points[i][0];
                centroids[cluster][1] := centroids[cluster][1] + points[i][1];
                count[cluster] := count[cluster] + 1;
            }
            centroids[0][0] := centroids[0][0] / count[0];
            centroids[0][1] := centroids[0][1] / count[0];
            centroids[1][0] := centroids[1][0] / count[1];
            centroids[1][1] := centroids[1][1] / count[1];
            return centroids[0][0];
        }
        func main() {
            var points [4][2]float = [4][2]float{{1.0, 1.0}, {2.0, 2.0}, {3.0, 3.0}, {4.0, 4.0}};
            putFloatLn(kMeans(points, 2));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1.5\n", inspect.stack()[0].function))

    def test_392(self):
        """Tests linear regression slope calculation. Tricky: Computes statistical measures for regression."""
        input = """
        func linearRegression(x [3]float, y [3]float, n int) float {
            var sumX float = 0.0;
            var sumY float = 0.0;
            var sumXY float = 0.0;
            var sumXX float = 0.0;
            var i int ;
            
            for i := 0; i < n; i += 1 {
                sumX := sumX + x[i];
                sumY := sumY + y[i];
                sumXY := sumXY + x[i] * y[i];
                sumXX := sumXX + x[i] * x[i];
            }
            var slope float = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
            return slope;
        }
        func main() {
            var x [3]float = [3]float{1.0, 2.0, 3.0};
            var y [3]float = [3]float{2.0, 4.0, 6.0};
            putFloatLn(linearRegression(x, y, 3));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.0\n", inspect.stack()[0].function))

    def test_393(self):
        """Tests perceptron prediction (single step). Tricky: Computes weighted sum and activation."""
        input = """
        type Perceptron struct { weights [2]float; bias float; }
        func (p Perceptron) predict(x [2]float) int {
            var sum float = p.bias;
            var i int ;
            
            for i := 0; i < 2; i += 1 {
                sum := sum + p.weights[i] * x[i];
            }
            if (sum > 0.0) {
                return 1;
            }
            return 0;
        }
        func main() {
            var p Perceptron = Perceptron{weights: [2]float{0.5, 0.5}, bias: -1.0};
            var x [2]float = [2]float{2.0, 2.0};
            putIntLn(p.predict(x));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n", inspect.stack()[0].function))

    def test_394(self):
        """Tests decision tree classification (single level). Tricky: Uses conditional branching for classification."""
        input = """
        type DecisionTree struct { threshold float; }
        func (dt DecisionTree) classify(x float) int {
            if (x > dt.threshold) {
                return 1;
            }
            return 0;
        }
        func main() {
            var dt DecisionTree = DecisionTree{threshold: 2.5};
            putIntLn(dt.classify(3.0));
            putIntLn(dt.classify(2.0));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n0\n", inspect.stack()[0].function))

    def test_395(self):
        """Tests K-Nearest Neighbors (KNN) classification (k=1). Tricky: Computes Euclidean distance."""
        input = """
        func knn(data [3][2]float, labels [3]int, test [2]float) int {
            var minDist float = 1000.0;
            var minLabel int = 0;
            var i int ;
            
            for i := 0; i < 3; i += 1 {
                var dist float = (test[0] - data[i][0]) * (test[0] - data[i][0]) + (test[1] - data[i][1]) * (test[1] - data[i][1]);
                if (dist < minDist) {
                    minDist := dist;
                    minLabel := labels[i];
                }
            }
            return minLabel;
        }
        func main() {
            var data [3][2]float = [3][2]float{{1.0, 1.0}, {2.0, 2.0}, {3.0, 3.0}};
            var labels [3]int = [3]int{0, 1, 1};
            var test [2]float = [2]float{2.1, 2.1};
            putIntLn(knn(data, labels, test));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n", inspect.stack()[0].function))

    def test_396(self):
        """Tests mean calculation for a dataset. Tricky: Accumulates and divides floating-point values."""
        input = """
        func mean(data [4]float, n int) float {
            var sum float = 0.0;
            var i int ;
            
            for i := 0; i < n; i += 1 {
                sum := sum + data[i];
            }
            return sum / n;
        }
        func main() {
            var data [4]float = [4]float{1.0, 2.0, 3.0, 4.0};
            putFloatLn(mean(data, 4));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.5\n", inspect.stack()[0].function))

    def test_397(self):
        """Tests variance calculation for a dataset. Tricky: Computes squared differences from mean."""
        input = """
        func mean(data [4]float, n int) float {
            var sum float = 0.0;
            var i int;
            
            for i := 0; i < n; i += 1 {
                sum := sum + data[i];
            }
            return sum / n;
        }
        func variance(data [4]float, n int) float {
            var m float = mean(data, n);
            var sum float = 0.0;
            var i int ;
            
            for i := 0; i < n; i += 1 {
                sum := sum + (data[i] - m) * (data[i] - m);
            }
            return sum / n;
        }
        func main() {
            var data [4]float = [4]float{1.0, 2.0, 3.0, 4.0};
            putFloatLn(variance(data, 4));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1.25\n", inspect.stack()[0].function))

    def test_398(self):
        """Tests nested gradient descent with struct-based data. Tricky: Nested loops and field accesses."""
        input = """
        type DataPoint struct { x float; y float; }
        type LinearModel struct { points [3]DataPoint; m float; c float; }
        func (model LinearModel) computeGradient(learningRate float) LinearModel {
            var dm float = 0.0;
            var dc float = 0.0;
            var i int;
            var j int;
            for j := 0; j < 2; j += 1 {
                dm := 0.0;
                dc := 0.0;
                for i := 0; i < 3; i += 1 {
                    var pred float = model.m * model.points[i].x + model.c;
                    var error float = model.points[i].y - pred;
                    dm := dm + (-2.0 / 3.0) * error * model.points[i].x;
                    dc := dc + (-2.0 / 3.0) * error;
                }
                model.m := model.m - learningRate * dm;
                model.c := model.c - learningRate * dc;
            }
            return LinearModel{points: model.points, m: model.m, c: model.c};
        }
        func main() {
            var model LinearModel = LinearModel{
                points: [3]DataPoint{
                    DataPoint{x: 1.0, y: 2.0},
                    DataPoint{x: 2.0, y: 4.0},
                    DataPoint{x: 3.0, y: 6.0}},
                m: 0.0, c: 0.0};
            model := model.computeGradient(0.01);
            putFloatLn(model.m);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0.35271114\n", inspect.stack()[0].function))

    def test_399(self):
        """Tests logistic regression with nested sigmoid approximation. Tricky: Taylor series and normalization."""
        input = """
        type LogisticModel struct { weights [2]float; bias float; scales [2]float; }
        
        func sigmoidApprox(z float) float {
            var result float = 0.5;
            var term float = z / 2.0;
            result := result + term;
            term := term * z * z / 4.0;
            result := result - term;
            term := term * z * z / 6.0;
            result := result + term;
            if (result > 1.0) { return 1.0; }
            if (result < 0.0) { return 0.0; }
            return result;
        }
        
        func (model LogisticModel) predict(x [2]float) float {
            var z float = model.bias;
            var i int;
            for i := 0; i < 2; i += 1 {
                z := z + model.weights[i] * (x[i] / model.scales[i]);
            }
            return sigmoidApprox(z);
        }
        func main() {
            var model LogisticModel = LogisticModel{
                weights: [2]float{0.5, 0.5},
                bias: -0.5,
                scales: [2]float{2.0, 2.0}};
            var x [2]float = [2]float{2.0, 2.0};
            putFloatLn(model.predict(x));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0.73502606\n", inspect.stack()[0].function))
    
    def test_400(self):
        """Tests Naive Bayes with nested Gaussian and cross-validation. Tricky: Exponential approximation."""
        input = """
        type BayesModel struct { means [2]float; variances [2]float; }
        type NaiveBayes struct { models [2]BayesModel; }
        func expApprox(x float) float {
            var result float = 1.0;
            var term float = x;
            result := result - term;
            term := term * x / 2.0;
            result := result + term;
            term := term * x / 3.0;
            result := result - term;
            if (result < 0.0) { return 0.0; }
            return result;
        }
        func gaussian(x float, mean float, variance float) float {
            var diff float = x - mean;
            var denom float = 2.0 * 3.14159 * variance;
            var exponent float = (diff * diff) / (2.0 * variance);
            return 1.0 / (denom * 0.5) * expApprox(exponent);
        }
        func (nb NaiveBayes) predict(x float) float {
            var maxProb float = 0.0;
            var i int;
            var j int;
            for i := 0; i < 2; i += 1 {
                var prob float = 1.0;
                for j := 0; j < 2; j += 1 {
                    prob := prob * gaussian(x, nb.models[i].means[j], nb.models[i].variances[j]);
                }
                if (prob > maxProb) {
                    maxProb := prob;
                }
            }
            return maxProb;
        }
        func main() {
            var nb NaiveBayes = NaiveBayes{ models: [2]BayesModel{
                    BayesModel{means: [2]float{0.0, 1.0}, variances: [2]float{1.0, 1.0}},
                    BayesModel{means: [2]float{1.0, 2.0}, variances: [2]float{1.0, 1.0}}}};
                    
            putFloatLn(nb.predict(0.0));
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0.061214983\n", inspect.stack()[0].function))
    
    # -------------------------------------------------------
    
    def test_advance_float_to_int_arr_0(self):
        input = """
        func main() {
            var a [5]float = [5]float{1.0, 2.0, 3.0, 4.0, 5.0};
            var b [5]int = [5]int{5, 4, 3, 2, 1};
            
            a := b
            
            var i int;
            for i := 0; i < 5; i += 1 {
                putFloatLn(a[i]);
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.0\n4.0\n3.0\n2.0\n1.0\n", inspect.stack()[0].function))
    
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

    def test_global_init_4(self):
        input = """            var x [2][3]float = [2][3]int {{1,2,2} ,{2,3,3}};

            func main() {

                putFloat(x[0][2]);

            }
            """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
        
    def test_advance_stack_size_8(self):
        input = """            
            func main(){

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


# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu