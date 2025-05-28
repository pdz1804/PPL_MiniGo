# BTL4_NHP: MiniGo Code Generator (Assignment 4)

This project implements **Assignment 4: Code Generator** from the CO3005 Principles of Programming Languages course. The task is to transform an Abstract Syntax Tree (AST) of a MiniGo program into **Jasmin code**, which can then be converted into **JVM bytecode**.

---

## 📁 Directory Structure

```
BTL4_NHP/
├── src/
│   ├── main/minigo/
│   │   ├── astgen/                 # From Assignment 2 (AST Generation)
│   │   ├── checker/                # From Assignment 3 (Static Checker)
│   │   ├── codegen/                # Assignment 4: Code Generator
│   │   │   ├── CodeGenerator.py    # Entry class for AST traversal and code emission
│   │   │   ├── Emitter.py          # Utility for emitting Jasmin instructions
│   │   │   ├── Frame.py            # Manages JVM stack frame information
│   │   │   ├── CodeGenError.py     # Custom error types (if needed)
│   │   │   └── MachineCode.py      # Jasmin helper functions
│   │   ├── parser/                 # Grammar & lexer
│   │   └── utils/                  # AST node and base visitor definitions
├── test/
│   ├── testcases/
│   │   ├── CodeGenSuite.py         # Main test suite (edit this)
│   │   ├── CodeGenSuite_init.py    # Init test examples
│   │   ├── CodeGenSuite_submit.py  # Submit test examples
│   │   └── CodeGenSuite_trung.py   # Other tests
│   └── solutions/                  # Reference Jasmin or expected output
├── lib/                            # (Optional) External JARs like Jasmin.jar
├── external/                       # Supporting tools or data
├── run.py                          # Script to run test and generate code
└── version 1.0.txt                 # Assignment specification info
```

---

## ▶️ How to Run

1. **Navigate to project root:**
   ```bash
   cd initial/src
   ```

2. **Run code generation test suite:**
   ```bash
   python run.py test CodeGenSuite
   ```

3. **To compile Jasmin output into JVM bytecode:**
   ```bash
   java -jar lib/jasmin.jar MiniGoClass.j
   ```

4. **Run the generated `.class` file with JVM:**
   ```bash
   java MiniGoClass
   ```

---

## 📘 Assignment 4: Code Generation

### Objective
Transform ASTs from valid MiniGo programs into Jasmin assembly code that is valid and runnable on the Java Virtual Machine (JVM). This is the final compilation phase.

### Components
- `CodeGenerator.py`: Traverses AST nodes using visitor pattern and generates intermediate code.
- `Emitter.py`: Low-level helper for emitting Jasmin code (e.g. `iload`, `invokevirtual`, `ireturn`, etc.)
- `Frame.py`: Manages stack size, label generation, local variable tracking.
- `MachineCode.py`: Converts MiniGo logic into JVM-compatible Jasmin instructions.

### Requirements
- Output must define a class called `MiniGoClass` with a valid `main` method.
- Handle expression evaluations, function calls, control flow (if, for), array operations, etc.
- **Limitation:** "for-each" statements are not supported in testcases.

### Testing
- Write 100 test cases in `CodeGenSuite.py` and related files.
- Each test should verify the generated Jasmin code against expected output.
- All valid MiniGo programs should compile and run as expected.

---

## 📝 Submission

You must submit exactly 3 files:
- `CodeGenerator.py`
- `Emitter.py`
- `CodeGenSuite.py`

Do not compress the files. Submit via the course’s official platform.

---

## ⚠️ Notes

- You can reuse `AST.py` from Assignment 2 and `Visitor.py` to traverse nodes.
- Ensure correct stack manipulation: every push must be balanced with appropriate return/invoke.
- Any violation in semantics or structure will make the compiled class unusable in JVM.

