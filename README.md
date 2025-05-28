# MiniGo 

This repository is a complete implementation of the **MiniGo compiler**, built across four course assignments as part of the **CO3005 – Principles of Programming Languages** course at Ho Chi Minh City University of Technology.

---

## 📘 Overview

**MiniGo** is a simplified subset of the Go programming language tailored for compiler construction education. It retains essential features—like basic types, control structures, structs, and interfaces—while removing complex ones like goroutines and the full standard library.

The goal is to provide students with a manageable yet real-world language for implementing all key compiler phases: **Lexical Analysis**, **Syntax Parsing**, **Abstract Syntax Tree (AST) Generation**, **Static Semantic Checking**, and **Code Generation**.

---

## 🏆 Achievements

| Assignment              | Topic                      | Grade      |
|-------------------------|----------------------------|------------|
| Assignment 1            | Lexer & Parser             | 100/100    |
| Assignment 2            | AST Generation             | 98/100     |
| Assignment 3            | Static Semantic Checker    | 125/125    |
| Assignment 4            | JVM Code Generator         | 101/101    |

---

## ⚙️ Features

MiniGo supports a rich set of language features, including:

### ✅ Type System
- **Primitive Types**: `int`, `float`, `boolean`, `string`
- **Composite Types**: `array`, `struct`, `interface`
- **Type inference** and type-safe assignments

### ✅ Control Structures
- `if`, `else if`, `else` statements
- `for` loops:
  - Simple condition loop
  - C-style loop with initialization and update
  - `for-range` loop over arrays

### ✅ Functions & Methods
- Supports multiple parameters and optional return values
- Receiver-based methods for `struct` types
- Methods support interface-based polymorphism

### ✅ Expressions & Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Relational: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Logical: `&&`, `||`, `!`
- Assignment: `=`, `+=`, `:=` (declaration+assignment)
- Struct and array indexing via `.` and `[]`

### ✅ Statements
- Variable and constant declarations (with and without type)
- Assignment, call, return, break, continue statements

### ✅ Built-in Functions
```go
getInt(), putInt(), putIntLn()
getFloat(), putFloat(), putFloatLn()
getBool(), putBool(), putBoolLn()
getString(), putString(), putStringLn()
putLn()
```

---

## 📦 Directory Structure

```
.
├── BTL1_2_NHP/         # Lexer & Parser (Assignment 1 & 2)
├── BTL3_NHP/           # Static Checker (Assignment 3)
├── BTL4_NHP/           # JVM Code Generator (Assignment 4)
├── docs/               # Assignment specs and MiniGo Language Specification
├── LICENSE
└── README.md           # This file
```

---

## ▶️ How to Run

> Make sure Python 3.12+ and Java (with Jasmin if running Assignment 4) are installed.

1. **Change to the appropriate source directory** for the assignment:
   ```bash
   cd BTL1_2_NHP/src    # or BTL3_NHP/src or BTL4_NHP/src
   ```

2. **Generate parser and lexer (for first-time setup):**
   ```bash
   python run.py gen
   ```

3. **Run test suites for each phase:**
   ```bash
   python run.py test LexerSuite         # Assignment 1 - Lexer
   python run.py test ParserSuite        # Assignment 1 - Parser
   python run.py test ASTGenSuite        # Assignment 2 - AST Generation
   python run.py test CheckSuite         # Assignment 3 - Static Checker
   python run.py test CodeGenSuite       # Assignment 4 - JVM Code Generation
   ```

4. **(Assignment 4 only)** Compile and run the Jasmin output on JVM:
   ```bash
   java -jar lib/jasmin.jar MiniGoClass.j
   java MiniGoClass
   ```

---

## 📚 Language Specification

MiniGo’s full syntax and semantics are defined in `docs/MiniGo Spec_v3_1.0.2.pdf`, including:
- Token set (keywords, operators, separators, literals)
- Expression and statement grammar
- Scoping rules and typing
- Built-in functions and method resolution

---

## 📜 License

This project is licensed for educational use only under the terms outlined by the university.

