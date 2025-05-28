# ------------------------------------------------
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# ------------------------------------------------     

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_101(self):
        """Simple Integer Constant"""
        self.assertTrue(TestParser.checkParser(""" const x = 10
                                            const y = foo( a(),b.a(2, 3) )
                                        """, "successful", 101))

    def test_102(self):
        """Simple Float Constant"""
        self.assertTrue(TestParser.checkParser("const y = 3.14;", "successful", 102))

    def test_103(self):
        """Simple Constant"""
        self.assertTrue(TestParser.checkParser("const a = a[1].b.c()[2].d.e();", "successful", 103))

    def test_104(self):
        """Simple String Constant"""
        self.assertTrue(TestParser.checkParser("const name = \"John Doe\";", "successful", 104))

    def test_105(self):
        """Simple Variable Declaration"""
        self.assertTrue(TestParser.checkParser("var age int = 25;", "successful", 105))

    def test_106(self):
        """Simple Variable without Initialization"""
        self.assertTrue(TestParser.checkParser("var counter int;", "successful", 106))

    def test_107(self):
        """Basic Addition Expression"""
        self.assertTrue(TestParser.checkParser("const result = 5 + 3;", "successful", 107))

    def test_108(self):
        """Basic Multiplication Expression"""
        self.assertTrue(TestParser.checkParser("const result = 6 * 7;", "successful", 108))

    def test_109(self):
        """Basic Logical Expression"""
        self.assertTrue(TestParser.checkParser("const check = true && false;", "successful", 109))

    def test_110(self):
        """Basic Comparison Expression"""
        self.assertTrue(TestParser.checkParser("const isEqual = 5 == 5;", "successful", 110))

    def test_111(self):
        """Empty Struct Declaration"""
        self.assertTrue(TestParser.checkParser("""
                                        type Person struct {
                                            
                                        }
                                        """, "Error on line 4 col 41: }", 111))

    def test_112(self):
        """Struct with Fields"""
        self.assertTrue(TestParser.checkParser("""
                                        type Person struct { 
                                            name string; 
                                            age int; 
                                        }
                                        """, "successful", 112))

    def test_113(self):
        """Simple Function Definition"""
        self.assertTrue(TestParser.checkParser("""
                                        func greet(name string) { 
                                            return "Hello " + name
                                        }
                                        
                                        func main() {
                                            var name = "Quang Phu Dep Trai"
                                            greet(name)
                                        }
                                        """, "successful", 113))

    def test_114(self):
        """Function with Parameters"""
        self.assertTrue(TestParser.checkParser("""
                                        func add(a int, b int) int { 
                                            return a + b; 
                                        };""", "successful", 114))

    def test_115(self):
        """Basic If Statement"""
        self.assertTrue(TestParser.checkParser("""
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
                                        """, "successful", 115))

    def test_116(self):
        """Basic If-Else Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        func check(x int) { 
                                            if (x > 0) { 
                                                return; 
                                            } else { 
                                                return; 
                                            } 
                                        }
                                        
                                        """, "successful", 116))

    def test_117(self):
        """Basic for Loop"""
        self.assertTrue(TestParser.checkParser("""
                                        func loop() { 
                                            foo(1, 2);
                                            a[2].foo(1,3);
                                            for x < 10 { 
                                                x += 1; 
                                            } 
                                        }
                                        """, "successful", 117))

    def test_118(self):
        """Basic For Loop"""
        self.assertTrue(TestParser.checkParser("""
                                        func loop() { 
                                            for i := 0; i < 10; i += 1 { 
                                                print(i) 
                                            } 
                                        }
                                        """, "successful", 118))

    def test_119(self):
        """Basic Return Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        func getValueDouble(num int) int { 
                                            return num*2; 
                                        }
                                        """, "successful", 119))

    def test_120(self):
        """Basic Function Call"""
        self.assertTrue(TestParser.checkParser("""
                                        func main() { 
                                            greet(); 
                                        }
                                        """, "successful", 120))

    def test_121(self):
        """Complex Arithmetic Expression"""
        self.assertTrue(TestParser.checkParser("""
                                        const value = (a + b) * (c - d) / e
                                        """, "successful", 121))

    def test_122(self):
        """Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""const p = Person{ name: \"Alice\", age: 30 };""", "successful", 122))

    def test_123(self):
        """Nested If Statements"""
        self.assertTrue(TestParser.checkParser("""
                                        func check(x int) { 
                                            if (x > 0) { 
                                                if (x < 10) { 
                                                    return; 
                                                } 
                                            } 
                                        }
                                        """, "successful", 123))

    def test_124(self):
        """For Loop with Continue"""
        self.assertTrue(TestParser.checkParser("""
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
                                        """, "successful", 124))

    def test_125(self):
        """Struct with Methods"""
        self.assertTrue(TestParser.checkParser("""
                                        type Car struct { 
                                            haha string
                                            hihi int
                                            hoho C
                                            
                                        }
                                        """, "successful", 125))

    def test_126(self):
        """Function Returning Struct"""
        self.assertTrue(TestParser.checkParser("""
                                        func createCar() Car { 
                                            return Car{}; 
                                        }
                                        """, "successful", 126))

    def test_127(self):
        """Multidimensional Array"""
        self.assertTrue(TestParser.checkParser("var matrix [3][3]int;", "successful", 127))

    def test_128(self):
        """Array Initialization"""
        self.assertTrue(TestParser.checkParser("var numbers [5]int = [5]int{1, 2, 3, 4, 5};", "successful", 128))

    def test_129(self):
        """Accessing Struct Fields"""
        self.assertTrue(TestParser.checkParser("const age = p.age;", "successful", 129))

    def test_130(self):
        """Function Calling Another Function"""
        self.assertTrue(TestParser.checkParser("""
                                        func main() { 
                                            add(minus(add(5, 10))); 
                                        }
                                        """, "successful", 130))

    def test_131(self):
        """Logical Expression Mixing Operators"""
        self.assertTrue(TestParser.checkParser("const result = (a > b) && (c < d) || (e == f);", "successful", 131))

    def test_132(self):
        """Complex Nested Loops"""
        self.assertTrue(TestParser.checkParser("""
                                        func nested() { 
                                            for i := 0; i < 10; i += 1 { 
                                                for j := 0; j < 5; j += 1 { 
                                                    print(i, j); 
                                                } 
                                            } 
                                        }
                                        """, "successful", 132))

    def test_133(self):
        """Function with Nested Struct"""
        self.assertTrue(TestParser.checkParser("""
                                        type House struct { rooms int; } 
                                        type City struct { houses [100]House; } 
                                        
                                        func build() { 
                                            print("Phu Dep Trai")
                                        }
                                        """, "successful", 133))

    def test_134(self):
        """Struct"""
        self.assertTrue(TestParser.checkParser("""
                                        type Person struct { 
                                            address Address
                                            name string
                                            dob string
                                            familyMember [10]Person
                                        }
                                        """, "successful", 134))

    def test_135(self):
        """Invalid Struct Declaration"""
        self.assertTrue(TestParser.checkParser("""
                                        type Car struct { 
                                            model string = \"Toyota\"; 
                                            wheels int = 4
                                            yaer int = 2025
                                        }
                                        """, "Error on line 3 col 58: =", 135))

    def test_136(self):
        """Invalid Function Definition"""
        self.assertTrue(TestParser.checkParser("func add(a int, b int) = { return a + b; }", "Error on line 1 col 24: =", 136))

    def test_137(self):
        """Invalid Array Declaration"""
        self.assertTrue(TestParser.checkParser("var numbers [int] = {1, 2, 3};", "Error on line 1 col 14: int", 137))

    def test_138(self):
        """Interface Declaration"""
        self.assertTrue(TestParser.checkParser("""
            type Shape interface {
                Area() float;
                Perimeter() float;
            }
        """, "successful", 138))

    def test_139(self):
        """Struct Implementing Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Circle struct {
                radius float;
                
            }
        """, "successful", 139))

    def test_140(self):
        """Multiple Nested Loops"""
        self.assertTrue(TestParser.checkParser("""
            func test() {
                for i := 0; i < 5; i += 1 {
                    for j := 0; j < 3; j += 1 {
                        for k := 0; k < 2; k += 1 {
                            print(i, j, k);
                        }
                    }
                }
            }
        """, "successful", 140))

    def test_141(self):
        """Complex Function Call Chain"""
        self.assertTrue(TestParser.checkParser("""
            func foo(){
                foo();
                foo(foo(), 2)
                a.foo();
                a[2].c.foo(foo(), 2)
            } 
                                     
            func main() {
                result := foo().bar().baz(5, 10).qux();
            }
        """, "successful", 141))

    def test_142(self):
        """Function Returning an Array"""
        self.assertTrue(TestParser.checkParser("""
            func getValues() [3]int {
                a["s"][foo()] := 1
                
                return [3]int{1, 2, 3};
            }
        """, "successful", 142))

    def test_143(self):
        """Struct with Method Calling Another Method"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                wheels int;
                quangphu string
            }
        """, "successful", 143))

    def test_144(self):
        """Array Access in Function Call"""
        self.assertTrue(TestParser.checkParser("""
            func foo(){
                a[1 + 1] := [2][3]int{{1, 2, 3}, {4, 5, 6}}
                a[1][2][3] := [2]ID{STRUCT{}};
            }            
                            
            func test() {
                x := arr[2].foo();
            }
        """, "successful", 144))

    def test_145(self):
        """Return Struct Instance"""
        self.assertTrue(TestParser.checkParser("""
            func createPoint() Point {
                return Point{x: 10, y: 20};
            }
        """, "successful", 145))

    def test_146(self):
        """Complex Logical Expression"""
        self.assertTrue(TestParser.checkParser("""
            const result = (a > b) && ((c < d) || (e == f)) && !(g < h);
        """, "successful", 146))

    def test_147(self):
        """Function with Complex Expressions"""
        self.assertTrue(TestParser.checkParser("""
            func calculate(x int, y int) int {
                return (x + y) * (x - y) / (x % y);
            }
        """, "successful", 147))

    def test_148(self):
        """Invalid Function Syntax"""
        self.assertTrue(TestParser.checkParser("""
            func invalid() = { return 10; }
        """, "Error on line 2 col 28: =", 148))

    def test_149(self):
        """Invalid If Condition"""
        self.assertTrue(TestParser.checkParser("""
            func test() {
                if () { print("Hello"); }
            }
        """, "Error on line 3 col 21: )", 149))

    def test_150(self):
        """Return statement"""
        self.assertTrue(TestParser.checkParser("""
            func getValue() string { 
                return "string"; 
            }
        """, "successful", 150))

    def test_151(self):
        """Function Overloading"""
        self.assertTrue(TestParser.checkParser("""
            func add(a int, b int) int { 
                return a + b; 
            }
            
            func add(a float, b float) float { 
                return a + b; 
            }
        """, "successful", 151))

    def test_152(self):
        """Method Chaining in Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                brand string
                wheels int
                dateBuy string
            }
            func main() {
                car := Car{}.start().drive();
            }
        """, "successful", 152))

    def test_153(self):
        """Struct Inheritance"""
        self.assertTrue(TestParser.checkParser("""
            type Vehicle struct {
                wheels int
                // func (v Vehicle) drive() { print("Driving..."); }
            }
            type Car struct : Vehicle {} // Incorrect Syntax
        """, "Error on line 6 col 29: :", 153))

    def test_154(self):
        """Method in Struct Returning Another Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                listFriends [100]int
            }
        """, "successful", 154))

    def test_155(self):
        """Struct itself appears inside the struct"""
        self.assertTrue(TestParser.checkParser("""
            type Node struct {
                value int;
                next Node;
            }
        """, "successful", 155))

    def test_156(self):
        """Return Multiple Values in Array from Function"""
        self.assertTrue(TestParser.checkParser("""
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
            """, "successful", 156))

    def test_157(self):
        """Missing Operators"""
        self.assertTrue(TestParser.checkParser("""
            const result = (a > b) ab;
        """, "Error on line 2 col 36: ab", 157))

    def test_158(self):
        """Error calling function cause it need a block (declarations)"""
        self.assertTrue(TestParser.checkParser("""
            const person = Person{name: "Alice", age: 25};
            person.greet();
        """, "Error on line 3 col 13: person", 158))

    def test_159(self):
        """Nested Function Definition not allowed"""
        self.assertTrue(TestParser.checkParser("""
            func inner() { 
                return
            } 
            
            func outer() {
                hehehe()
                func hihihi() {
                    print("Phu Quang")
                }
            }
        """, "Error on line 8 col 17: func", 159))

    def test_160(self):
        """Return Struct Field Directly"""
        self.assertTrue(TestParser.checkParser("""
            func getAge(p Person) int {
                return p.age;
            }
        """, "successful", 160))

    def test_161(self):
        """Recursive Function"""
        self.assertTrue(TestParser.checkParser("""
            func factorial(n int) int {
                if (n == 0) { return 1; }
                return n * factorial(n - 1);
            }
        """, "successful", 161))

    def test_162(self):
        """Deeply Nested Structs not valid"""
        self.assertTrue(TestParser.checkParser("""
            type Company struct {
                name string;
                department struct {
                    employees struct {
                        count int;
                    }
                }
            }
        """, "Error on line 4 col 28: struct", 162))

    def test_163(self):
        """Method Calling Another Method Recursively"""
        self.assertTrue(TestParser.checkParser("""
            type Node struct {
                value int;
            }
        """, "successful", 163))

    def test_164(self):
        """Complex Expression in Return Statement"""
        self.assertTrue(TestParser.checkParser("""
            func compute(a int, b int) int {
                return (a + (b * (a / b) - a) % b) + 5;
            }
        """, "successful", 164))

    def test_165(self):
        """Struct Method Modifying Another Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string;
                age int
            }
        """, "successful", 165))

    def test_166(self):
        """Invalid Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""
            const p = Person{name = "John", age = 30};
        """, "Error on line 2 col 35: =", 166))

    def test_167(self):
        """Mutual Recursion"""
        self.assertTrue(TestParser.checkParser("""
            func isEven(n int) bool {
                if (n == 0) { return true; }
                return isOdd(n - 1);
            }
            
            func isOdd(n int) bool {
                if (n == 0) { return false; }
                return isEven(n - 1);
            }
        """, "successful", 167))

    def test_168(self):
        """Infinite Loop (Parser Should Not Hang)"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for true { 
                    print("Running"); 
                    break; 
                }
            }
        """, "successful", 168))

    def test_169(self):
        """Extreme Nested If-Else"""
        self.assertTrue(TestParser.checkParser("""
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
        """, "successful", 169))

    def test_170(self):
        """Nested Structs with Methods"""
        self.assertTrue(TestParser.checkParser("""
            type Outer struct {
                type Inner struct {
                    func hello() { print("Hello"); }
                }
            }
        """, "Error on line 3 col 17: type", 170))

    def test_171(self):
        """Anonymous Functions (invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var add = func(x int, y int) int { return x + y; };
        """, "Error on line 2 col 23: func", 171))

    def test_172(self):
        """Anonymous Function (invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var result = (func(x int) int { return x * x; })(5);
        """, "Error on line 2 col 27: func", 172))

    # here
    def test_173(self):
        """Missing the receiver"""
        self.assertTrue(TestParser.checkParser("""
            func() () { 
                print("Error"); 
            } 
        """, "Error on line 2 col 18: )", 173))

    def test_174(self):
        """Struct with Self-Referencing element"""
        self.assertTrue(TestParser.checkParser("""
            type Node struct {
                value int;
                next Node;
            }
        """, "successful", 174))

    def test_175(self):
        """Array of Structs"""
        self.assertTrue(TestParser.checkParser("""
            var people [3]Person = [3]Person{Person{name: "Alice"}, Person{name: "Bob"}, Person{name: "Charlie"}};
        """, "successful", 175))

    def test_176(self):
        """Function Returning Array of Structs"""
        self.assertTrue(TestParser.checkParser("""
            func getPeople() [2]Person {
                return [2]Person{Person{name: "Alice"}, Person{name: "Bob"}};
            }
        """, "successful", 176))

    def test_177(self):
        """No Function definition inside the struct"""
        """If this is the method definition, so it misses the receiver"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator struct {
                num1 int 
                num2 int
                op string 
                
            }
        """, "successful", 177))

    def test_178(self):
        """Struct with Array of Another Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Team struct {
                members [5]Person;
            }
        """, "successful", 178))

    def test_179(self):
        """Multi-Level Struct References"""
        self.assertTrue(TestParser.checkParser("""
            type Address struct {
                city string;
            }
            type Person struct {
                addr Address;
            }
            var cityName string = Person{}.addr.city;
        """, "successful", 179))

    def test_180(self):
        """Invalid Struct Array Access"""
        self.assertTrue(TestParser.checkParser("""
            const team = Team{}.members[2].name;
        """, "successful", 180))

    
    def test_181(self):
        """Function with No Closing Bracket"""
        self.assertTrue(TestParser.checkParser("""
            func broken() {
                var x int = 10;
        """, "Error on line 4 col 9: <EOF>", 181))

    def test_182(self):
        """Invalid Operator Placement"""
        self.assertTrue(TestParser.checkParser("""
            const result = * 5 + 3;
        """, "Error on line 2 col 28: *", 182))

    def test_183(self):
        """Extreme Nesting (Should Fail)"""
        self.assertTrue(TestParser.checkParser("""
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
        """, "successful", 183))

    def test_184(self):
        """Return string literal in Function"""
        self.assertTrue(TestParser.checkParser("""
            func sayHello() { return "Hello"; }
        """, "successful", 184))

    def test_185(self):
        """Empty Program (Should Fail)"""
        self.assertTrue(TestParser.checkParser("", "Error on line 1 col 1: <EOF>", 185))

    def test_186(self):
        """Excessively Recursive Function (Should Parse, But Crash on Execution)"""
        self.assertTrue(TestParser.checkParser("""
            func infiniteRecursion() {
                infiniteRecursion();
            }
        """, "successful", 186))

    def test_187(self):
        """Excessive Operator Usage"""
        self.assertTrue(TestParser.checkParser("""
            const value = 1 + 2 - 3 * 4 / 5 % 6 + 7 - 8 * 9 / 10 % 11;
        """, "successful", 187))

    def test_188(self):
        """Missing Semicolon causes no problem as newline at the end of first const declaration changed into SEMICOLON"""
        self.assertTrue(TestParser.checkParser("""
            const x = 10
            const y = 20;
        """, "successful", 188))

    def test_189(self):
        """Missing Closing Brace"""
        self.assertTrue(TestParser.checkParser("""
            func broken() {
                var x int = 10;
        """, "Error on line 4 col 9: <EOF>", 189))

    def test_190(self):
        """Unmatched Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            const value = (5 + (3 * 2);
        """, "Error on line 2 col 39: ;", 190))

    def test_191(self):
        """Unmatched Curly Brace"""
        self.assertTrue(TestParser.checkParser("""
            func broken() {
                var x int = 10;
        """, "Error on line 4 col 9: <EOF>", 191))

    def test_192(self):
        """Unmatched Bracket in Array"""
        self.assertTrue(TestParser.checkParser("""
            var arr [5 int;
        """, "Error on line 2 col 24: int", 192))

    def test_193(self):
        """Method Without Name of the receiver (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func () { print("Error"); }
        """, "Error on line 2 col 19: )", 193))

    def test_194(self):
        """Struct Declaration Without Name (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            type struct { name string; }
        """, "Error on line 2 col 18: struct", 194))

    def test_195(self):
        """Calling Function in Function"""
        self.assertTrue(TestParser.checkParser("""
            func main() {
                result := undefinedFunction(10);
            }
        """, "successful", 195))  # No semantic checking in parser.

    def test_196(self):
        """Using Reserved Keyword as Identifier (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var if int = 5;
        """, "Error on line 2 col 17: if", 196))

    def test_197(self):
        """Error in Array Declaration"""
        self.assertTrue(TestParser.checkParser("""
            var arr [3]int = {1 2 3};
        """, "Error on line 2 col 30: {", 197))

    def test_198(self):
        """Misplaced Parentheses in Expression"""
        self.assertTrue(TestParser.checkParser("""
            const result = (5 + (3 * 2);
        """, "Error on line 2 col 40: ;", 198))

    def test_199(self):
        """Excessive Nesting in Expressions"""
        self.assertTrue(TestParser.checkParser("""
            const deepCalc = ((((((((10 + 5) * 2) / 3) % 4) - 1) + 6) * 7));
        """, "successful", 199))

    def test_200(self):
        """Completely Empty Program (Should Fail)"""
        self.assertTrue(TestParser.checkParser("", "Error on line 1 col 1: <EOF>", 200))    
    
    
    def test_201(self):
        """Completely Empty Program (Should Fail)"""
        input = """
        type Calculator struct {
            value int;
            value int
        }
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 201))    

import inspect

class ParserSuite(unittest.TestCase):
    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))
        
    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{}                    
""","Error on line 1 col 17: }", inspect.stack()[0].function))
        
    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 27: ;", inspect.stack()[0].function))
        
    def test_169(self):
        self.assertTrue(TestParser.checkParser("""
        const a = [1]int{1, 2 
""","Error on line 2 col 30: ;", inspect.stack()[0].function))
        
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {}                                                                       
        ""","Error on line 2 col 32: }", inspect.stack()[0].function))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","Error on line 11 col 35: }", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
       
    def test_021(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        ""","successful", inspect.stack()[0].function))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 1.;                         
        ""","successful", inspect.stack()[0].function))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN 1;                         
        ""","Error on line 2 col 25: 1", inspect.stack()[0].function))
    
    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int{1};                         
        ""","Error on line 2 col 27: int", inspect.stack()[0].function))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [true]int{1};                         
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", inspect.stack()[0].function))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        ""","Error on line 2 col 28: ]", inspect.stack()[0].function))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1;                         
        ""","Error on line 2 col 35: ;", inspect.stack()[0].function))
    
    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1,3,4;                         
        ""","Error on line 2 col 39: ;", inspect.stack()[0].function))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        ""","successful", inspect.stack()[0].function))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", inspect.stack()[0].function))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int {};                         
        ""","Error on line 2 col 27: int", inspect.stack()[0].function))

    def test_034(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID + 3;                         
        ""","successful", inspect.stack()[0].function))
    
    def test_035(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: };                         
        ""","Error on line 2 col 34: }", inspect.stack()[0].function))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", inspect.stack()[0].function))
    
    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a + b - [2]int{2} + c - z;                         
        ""","successful", inspect.stack()[0].function))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a * b / d % e * 2;                         
        ""","successful", inspect.stack()[0].function))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        ""","successful", inspect.stack()[0].function))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))

    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2, 3];                         
        ""","Error on line 2 col 30: ,", inspect.stack()[0].function))

    def test_043(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[];                         
        ""","Error on line 2 col 29: ]", inspect.stack()[0].function))

    def test_044(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo();                         
        ""","successful", inspect.stack()[0].function))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        ""","successful", inspect.stack()[0].function))

    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        ""","successful", inspect.stack()[0].function))

    def test_047(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1,);                         
        ""","Error on line 2 col 47: )", inspect.stack()[0].function))

    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        ""","successful", inspect.stack()[0].function))

    def test_049(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        ""","successful", inspect.stack()[0].function))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo().a[2].goo();                         
        ""","successful", inspect.stack()[0].function))

    def test_051(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = [2]int{1}[3][4].foo();                         
        ""","successful", inspect.stack()[0].function))

    def test_052(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        ""","successful", inspect.stack()[0].function))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_054(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);                         
        ""","successful", inspect.stack()[0].function))

    def test_055(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  int;                         
        ""","Error on line 2 col 23: int", inspect.stack()[0].function))

    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  (1, 2);                         
        ""","Error on line 2 col 25: ,", inspect.stack()[0].function))

    def test_057(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a VOTIEN = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))

    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [2][3]int = 2 + 3 / 4;
        ""","successful", inspect.stack()[0].function))

    def test_059(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [][3]int = 2 + 3 / 4;
        ""","Error on line 2 col 19: ]", inspect.stack()[0].function))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = a.foo()[2];
        ""","successful", inspect.stack()[0].function))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = ;
        ""","Error on line 2 col 20: ;", inspect.stack()[0].function))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a 1;
        ""","Error on line 2 col 18: 1", inspect.stack()[0].function))

    def test_063(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]int;
        ""","successful", inspect.stack()[0].function))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_065(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a;
        ""","Error on line 2 col 19: ;", inspect.stack()[0].function))

    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a := 1 + foo.a[2];
        ""","Error on line 2 col 20: :=", inspect.stack()[0].function))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a =;
        ""","Error on line 2 col 21: ;", inspect.stack()[0].function))

    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            
            var a int; var d = 2;
                                        
            var d = 2;
                                        
            const a = 2; var d int = 3;
                                        
            
            var d = 2;""","successful", inspect.stack()[0].function))
        
    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y [2]int) [2]id {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() [2]id {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a) [2]id {return ;}
""","Error on line 2 col 22: )", inspect.stack()[0].function))
        
    def test_072(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(int a) int {return ;}
""","Error on line 2 col 21: int", inspect.stack()[0].function))
        
    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_074(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a int, ) {}
""","Error on line 2 col 28: )", inspect.stack()[0].function))
        
    def test_075(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int}
""","Error on line 2 col 45: }", inspect.stack()[0].function))
        
    def test_076(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int;}
""","successful", inspect.stack()[0].function))
        
    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""","successful", inspect.stack()[0].function))
        
    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""","Error on line 4 col 22: a", inspect.stack()[0].function))
        
    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 22: =", inspect.stack()[0].function))
        
    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""","successful", inspect.stack()[0].function))
        
    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 46: }", inspect.stack()[0].function))
        
    def test_082(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()
        }
""","successful", inspect.stack()[0].function))
        
    def test_083(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}
""","successful", inspect.stack()[0].function))
        
    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""","successful", inspect.stack()[0].function))
        
    def test_085(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""","Error on line 3 col 33: {", inspect.stack()[0].function))
        
    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();} type Person struct{value int;}
""","Error on line 2 col 49: type", inspect.stack()[0].function))
        
    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}; type Person struct{value int;}
""","successful", inspect.stack()[0].function))
        
    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {return ;};
""","successful", inspect.stack()[0].function))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) Add(x int) int {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {return ;}
""","Error on line 2 col 20: int", inspect.stack()[0].function))
        
    def test_090(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_092(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c [2]c) Add(x int) {return ;}
""","Error on line 2 col 20: [", inspect.stack()[0].function))
        
    def test_093(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (int c) Add(x int) {return ;}
""","Error on line 2 col 18: int", inspect.stack()[0].function))
        
    def test_094(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;};
""","successful", inspect.stack()[0].function))
        
    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            func (c c) Add(x int) {return ;}
                                        
            func Add(x int) {return ;}; var c int;
                                        
            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""","Error on line 7 col 86: var", inspect.stack()[0].function))
        
    def test_096(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            var c int func (c c) Add(x int) {return ;}
""","Error on line 3 col 22: func", inspect.stack()[0].function))
        
    def test_097(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const a = 2 func (c c) Add(x int) {return ;}
""","Error on line 3 col 24: func", inspect.stack()[0].function))
        
    def test_098(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""

""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))
        
    def test_100(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                                        }
""","successful", inspect.stack()[0].function))
        
    def test_101(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int = 2;      
                                    };""","successful", inspect.stack()[0].function))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int;      
                                    };""","successful", inspect.stack()[0].function))
        
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""","successful", inspect.stack()[0].function))
        
    def test_104(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         const a = a[2].b;      
                                    };""","successful", inspect.stack()[0].function))
        
    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    };""","successful", inspect.stack()[0].function))
        
    def test_106(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";           
                                    };""","Error on line 4 col 55: var", inspect.stack()[0].function))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""","successful", inspect.stack()[0].function))
        

    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2].b := 2;       
                                    };""","successful", inspect.stack()[0].function))
        

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""","successful", inspect.stack()[0].function))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""","Error on line 3 col 48: +=", inspect.stack()[0].function))

    def test_111(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    };""","Error on line 3 col 40: 2", inspect.stack()[0].function))
        
    def test_112(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       ID {id:2}.c += 2;       
                                    };""","Error on line 3 col 42: {", inspect.stack()[0].function))
        
    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""","successful", inspect.stack()[0].function))
        
    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""","successful", inspect.stack()[0].function))
        
    def test_115(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        } 
                                    };""","Error on line 4 col 48: )", inspect.stack()[0].function))
        
    def test_116(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_117(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""","Error on line 4 col 50: )", inspect.stack()[0].function))
        
    def test_118(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return; 
                                        } else if(1){return; 
                                        }else if(1){return; 
                                        }else if(2){return
                                        }else {return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_119(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true {return; }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_121(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", inspect.stack()[0].function))
        
    def test_122(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""","Error on line 3 col 44: int", inspect.stack()[0].function))
        
    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_124(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_125(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 44: const", inspect.stack()[0].function))
        
    def test_126(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: [", inspect.stack()[0].function))
        
    def test_127(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };""","Error on line 3 col 76: {", inspect.stack()[0].function))
        
    def test_128(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 75: var", inspect.stack()[0].function))
        
    def test_129(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_130(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", inspect.stack()[0].function))
        
    def test_131(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""","Error on line 3 col 52: ,", inspect.stack()[0].function))
        
    def test_132(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return; 
                                        }
                                    };""","Error on line 3 col 56: [", inspect.stack()[0].function))
        
    def test_133(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_135(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""","successful", inspect.stack()[0].function))
        
    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""","successful", inspect.stack()[0].function))
        
    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""","successful", inspect.stack()[0].function))
        
    def test_138(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return return 2 + a[2].b()
                    
                                    };""","Error on line 3 col 47: return", inspect.stack()[0].function))
        
    def test_139(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break continue
                    
                                    };""","Error on line 3 col 46: continue", inspect.stack()[0].function))
        
    def test_140(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""","successful", inspect.stack()[0].function))
        
    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""","successful", inspect.stack()[0].function))
        
    def test_142(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 40: (", inspect.stack()[0].function))
        
    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))
        
    def test_144(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {break;}
                                    };""","Error on line 3 col 40: {", inspect.stack()[0].function))
        
    def test_145(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 40: break", inspect.stack()[0].function))
        
    def test_146(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""","Error on line 4 col 50: c", inspect.stack()[0].function))
        
    def test_147(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""","Error on line 4 col 50: c", inspect.stack()[0].function))
        
    def test_148(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""","Error on line 3 col 55: struct", inspect.stack()[0].function))
        
    def test_149(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""","Error on line 3 col 75: string", inspect.stack()[0].function))
        
    def test_150(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""","Error on line 3 col 75: string", inspect.stack()[0].function))
        
    def test_151(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{1+1}                    
""","Error on line 1 col 18: +", inspect.stack()[0].function))
        
    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", inspect.stack()[0].function))
        
    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{}                    
""","Error on line 1 col 17: }", inspect.stack()[0].function))
        
    def test_154(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", inspect.stack()[0].function))
        
    def test_155(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""","successful", inspect.stack()[0].function))
        
    def test_156(self):
        self.assertTrue(TestParser.checkParser("""
        func Add(x, y int, b float) {return ;}           
""","successful", inspect.stack()[0].function))
        
    def test_157(self):
        self.assertTrue(TestParser.checkParser("""
        func (c c) Add(x, y int, b float) {return ;}           
""","successful", inspect.stack()[0].function))
        
    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""","successful", inspect.stack()[0].function))
        
    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            c int  c int;                                                    
        }      
""","Error on line 3 col 19: c", inspect.stack()[0].function))
        
    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 27: ;", inspect.stack()[0].function))
        
    def test_160(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
""","Error on line 4 col 16: else", inspect.stack()[0].function))
        
    def test_161(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else if (1) {}
            };  
""","successful", inspect.stack()[0].function))
        
    def test_162(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else {}
            };  
""","successful", inspect.stack()[0].function))
        
    def test_163(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {}
            };  
""","successful", inspect.stack()[0].function))
        
    def test_164(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };  
""","successful", inspect.stack()[0].function))
        
    def test_165(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0; i < 10; i += 1 {
// loop body
}
            };  
""","successful", inspect.stack()[0].function))
        
    def test_166(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body                                   
};
            };  
""","successful", inspect.stack()[0].function))

    def test_167(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.2; 
""","Error on line 2 col 20: 2", inspect.stack()[0].function))
        
    def test_168(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.b.c().d().e[2].k()[2]; 
""","successful", inspect.stack()[0].function))
        
    def test_169(self):
        self.assertTrue(TestParser.checkParser("""
        const a = [1]int{1, 2 
""","Error on line 2 col 30: ;", inspect.stack()[0].function))
        
    def test_170(self):
        self.assertTrue(TestParser.checkParser("""
        const a = foo(1, 2
""","Error on line 2 col 26: ;", inspect.stack()[0].function))

    def test_171(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i.b := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: .", inspect.stack()[0].function))
        
    def test_172(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[2].c += 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 77: [", inspect.stack()[0].function))

    def test_173(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 49: :=", inspect.stack()[0].function))
        
    def test_174(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 51: :=", inspect.stack()[0].function))
        
    def test_175(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 51: :=", inspect.stack()[0].function))
        
    def test_176(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            };                                                 
        }      
""","Error on line 3 col 12: func", inspect.stack()[0].function))
        
    def test_177(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 49: ;", inspect.stack()[0].function))

    def test_178(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 53: ;", inspect.stack()[0].function))

    def test_179(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))

    def test_180(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{{{1}}, ID, a, {b}}                              
                                        ""","successful", inspect.stack()[0].function))

    def test_181(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a;
                                        ""","Error on line 2 col 49: ;", inspect.stack()[0].function))
    def test_182(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))
                                                                                          
    def test_183(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        ""","Error on line 2 col 52: {", inspect.stack()[0].function))
                                                                                          
    def test_184(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {
                                            return;
                                        }
                                    };""","Error on line 3 col 40: {", inspect.stack()[0].function))

    def test_185(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{a, b, {c}}                              
                                        ""","successful", inspect.stack()[0].function))
        
    def test_186(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                            return;
                                    };""","successful", inspect.stack()[0].function))
  

    
# ------------------------------------------------
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# Nguyen Quang Phu - 2252621 - CSE K22
# ------------------------------------------------      