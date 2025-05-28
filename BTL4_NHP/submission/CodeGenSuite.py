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

    # def test_174(self):
    #     input = """
    #     func foo() boolean {
    #         putStringLn("foo");
    #         return true;
    #     }

    #     func main() {
    #         var a = true && foo()
    #         putBoolLn(a)
    #         var b = false && foo()
    #         putBoolLn(b)
    #     }
    #     """
    #     self.assertTrue(TestCodeGen.test(input, "foo\ntrue\nfalse\n", inspect.stack()[0].function))

    # def test_175(self):
    #     input = """
    #     func foo() boolean {
    #         putStringLn("foo");
    #         return false;
    #     }

    #     func main() {
    #         var a = true || foo()
    #         putBoolLn(a)
    #         var b = false || foo()
    #         putBoolLn(b)
    #     }
    #     """
    #     self.assertTrue(TestCodeGen.test(input, "true\nfoo\nfalse\n", inspect.stack()[0].function))

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
    

# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu