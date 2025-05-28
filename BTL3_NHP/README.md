# BTL3_NHP: MiniGo Static Checker (Assignment 3)

This project implements **Assignment 3: Static Checker** from the CO3005 Principles of Programming Languages course. It builds upon the previous lexer, parser, and AST generator to verify semantic correctness of MiniGo programs using static analysis.

---

## 📁 Directory Structure

```
BTL3_NHP/
├── src/
│   └── main/minigo/
│       ├── astgen/                # ASTGenerator from Assignment 2
│       ├── checker/               # Static checking logic
│       │   ├── StaticCheck.py     # Main static checker implementation (edit this)
│       │   └── StaticError.py     # Contains predefined exception classes to raise
│       ├── parser/                # MiniGo grammar and lexer
│       │   └── MiniGo.g4
│       └── utils/                 # AST and Visitor base classes
│           ├── AST.py             # AST node structure (do not modify)
│           └── Visitor.py         # Visitor base class (used in Assignment 2/3)
├── test/
│   ├── testcases/
│   │   ├── CheckSuite.py          # Main test suite (edit this)
│   │   └── CheckSuite_*.py        # Additional test files per group member
│   └── solutions/                 # Expected result or ASTs
├── run.py                         # Script to run the checker
├── submission/                    # Folder for final submission files
└── version 1.0.txt                # Assignment release info
```

---

## ▶️ How to Run

1. **Navigate to project root:**
   ```bash
   cd initial/src
   ```

2. **Run static checker test suite:**
   ```bash
   python run.py test CheckSuite
   ```

---

## 📘 Assignment 3: Static Checker

### Purpose
To verify semantic constraints of MiniGo programs at **compile time** (i.e. statically), and raise the appropriate error if violated. The input to the static checker is the AST of a valid MiniGo program (generated in Assignment 2).

### Key Tasks
- Implement static checking logic in `StaticCheck.py` inside the class `StaticChecker`.
- Each semantic violation must raise a corresponding exception from `StaticError.py`:
  - `Redeclared(kind, name)` – when duplicate declarations occur.
  - `Undeclared(kind, name)` – when a variable, function, field, etc. is used without declaration.
  - `TypeMismatch(exp/stmt)` – when type rules are violated in assignment, call, or expression.

### Semantic Rules Checked
- **Redeclarations:** Variables, Constants, Parameters, Functions, Types, Fields, etc. must be unique in scope.
- **Undeclared Identifiers:** All used variables, functions, and fields must be declared beforehand.
- **Type Compatibility:**
  - Assignment: RHS must match LHS (or be integer to float, etc.)
  - Function/method call: Argument types must match parameter types.
  - Return: Return types must match function signature.
  - Array access: Indices must be integers.
  - Field access: Receiver must be a struct type.
  - Conditionals: Must be of boolean type.
- **Implicit Declarations:** Scalars undeclared on LHS may be implicitly declared with RHS type.

### Testing
- Write 100 test cases in `CheckSuite.py` that:
  - Validate correct MiniGo ASTs (should pass with no output)
  - Verify proper exceptions are raised for incorrect ASTs

---

## 📝 Submission

You must submit the following 2 files:
- `StaticCheck.py` — implements semantic checks using AST visitor
- `CheckSuite.py` — contains 100 well-formed test cases (positive and negative)

Do not submit any compressed files. Submissions are via the official course platform.

---

## ⚠️ Notes

- This project builds on ASTs from Assignment 2 (ASTGenerator).
- If your Assignment 2 is incomplete, you can still test using direct AST inputs (testcases 402–403).
- Always stop and raise at the first detected semantic error.
- All exception messages and structures must match those in `StaticError.py` exactly.

