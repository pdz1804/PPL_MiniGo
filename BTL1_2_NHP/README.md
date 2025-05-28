# BTL2_NHP: MiniGo Language Toolchain (Assignment 1 & 2)

This project contains the full implementation and test suites for two major assignments in the CO3005 Principles of Programming Languages course. The assignments involve constructing a toolchain for a subset of the MiniGo programming language using **ANTLR** and **Python**.

---

## 📁 Directory Structure

```
BTL2_NHP/
├── src/
│   └── main/minigo/
│       ├── astgen/               # Assignment 2: AST Generator
│       │   └── ASTGenerator.py   # Generates AST from parse tree using Visitor
│       ├── parser/               # Assignment 1: Lexer & Parser definitions
│       │   ├── MiniGo.g4         # ANTLR grammar file for MiniGo
│       │   └── lexererr.py       # Custom error handling for lexical errors
│       └── utils/                # Utility definitions
│           └── AST.py            # AST Node class definitions (do not modify)
├── test/
│   └── testcases/
│       ├── LexerSuite.py         # 100+ tests for lexer rules
│       ├── ParserSuite.py        # 100+ tests for parser rules
│       └── ASTGenSuite.py        # 100+ tests for AST generation
├── run.py                        # Main entry script to run generation or tests
└── set_para.txt                  # Parameter settings
```

---

## ▶️ How to Run

1. **Change directory** to the source folder:
   ```bash
   cd initial/src
   ```

2. **Generate ANTLR parser and lexer:**
   ```bash
   python run.py gen
   ```

3. **Run tests:**
   ```bash
   python run.py test LexerSuite      # Run lexer test cases
   python run.py test ParserSuite     # Run parser test cases
   python run.py test ASTGenSuite     # Run AST generation test cases
   ```

---

## 📘 Assignment 1: Lexer & Recognizer

This part requires creating a **lexer** and **parser** for the MiniGo language.

### Tasks
- Define lexical tokens and parser grammar rules in `MiniGo.g4`.
- Use **ANTLR 4.9.2** to generate lexer/parser from `MiniGo.g4`.
- Implement lexical error handling in `lexererr.py`, using:
  - `ErrorToken(char)`
  - `UnclosedString(string)`
  - `IllegalEscape(string)`
- Write 100+ test cases:
  - `LexerSuite.py` tests the correctness of token recognition and error detection.
  - `ParserSuite.py` tests the parsing of syntactically valid/invalid programs.

### Requirements
- Install: `antlr4-python3-runtime==4.9.2`
- Use `antlr-4.9.2-complete.jar` and set `ANTLR_JAR` env variable.

---

## 📗 Assignment 2: AST Generation

This part builds on the parser from Assignment 1 to generate an **Abstract Syntax Tree (AST)**.

### Tasks
- Implement the `ASTGenerator.py` using **Visitor pattern** to traverse the parse tree.
- Use the AST class definitions in `utils/AST.py` (you are NOT allowed to modify this file).
- Each valid MiniGo input must result in a correct AST instance.
- Write 100 test cases in `ASTGenSuite.py` to verify AST generation from correct input programs.

### Key Concepts
- Traverse parse tree nodes using `Visit` methods.
- Construct corresponding `AST` nodes as per MiniGo grammar.
- Only correct input programs are tested (no syntax errors here).

---

## 📦 Submission Requirements

You must submit exactly 3 files per assignment (do not compress):
- **Assignment 1:** `MiniGo.g4`, `LexerSuite.py`, `ParserSuite.py`
- **Assignment 2:** `MiniGo.g4`, `ASTGenerator.py`, `ASTGenSuite.py`

---

## ⚠️ Notes

- Work **must be individual**; any form of plagiarism results in disciplinary action.
- Ensure all tests pass before submission.
- AST node structures must match those in `AST.py` exactly.
- Grammar and AST designs must follow MiniGo language specification.

