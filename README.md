## 👤 Author

**Vibhor Shukla**  
📧 Email: vshukla107.btech2023@cse.nitrr.ac.in <br>
🎓 Roll No: 23115107  
📚 Semester: 4th  
🏫 College: NIT Raipur  
🧠 Branch: Computer Science and Engineering

---

# Custom Instruction Compiler Project

This project demonstrates a minimal compiler pipeline for a C-like language that detects a specific pattern in expressions and replaces it with a custom assembly instruction `CUBEMULADD`.

---

## 🔧 Features

- **Lexical Analysis:** Tokenizes source code using regular expressions.
- **Parsing:** Builds an Abstract Syntax Tree (AST) using a recursive descent parser.
- **Custom Optimization:** Detects `x*x*x + x*y` patterns and replaces them with `CUBEMULADD x, y`.
- **Assembly Code Generation:** Outputs pseudo-assembly instructions to `./output.asm`.
- **Interpreter:** Executes the code to simulate actual results.

---

## 📁 File Overview

| File                | Purpose |
|---------------------|---------|
| `tokeniser.py`      | Converts raw source code into a stream of tokens. |
| `ast_builder.py`    | Builds the AST using a recursive descent parser. Defines AST node classes. |
| `asm_gen.py`        | Generates pseudo-assembly code. Detects specific patterns. |
| `interpreter.py`    | Executes the AST directly using an interpreter. |
| `compile_and_run.py`| Orchestrates tokenization, parsing, assembly generation, and interpretation. |
| `Code.py`           | Sample input code and main runner for the pipeline. |

---

## 🧩 Dependencies:
 - **OS:** Linux, MacOS, Windows(8+)
 - **Python :** 3.10+

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
    git clone https://github.com/VibhorShukla-BHRT/Yukti.git
    cd Yukti
```

### Step 2: Run the Compiler
```bash
    python Code.py
```

This will:
- Print token stream
- Print AST
- Generate and save `output.asm`
- Print result of simulated execution
---

## 💡 Example

### Sample Input (Code.py)
```c
    int x = 2;
    int y = 3;
    int z = x * x * x + x * y;
    print(z);
```
### Generated ./output.asm
```asm
    MOV x, 2
    MOV y, 3
    CUBEMULADD z, x, y
    PRINT z
```
### Console Output
```bash
    <---Tokenisation--->

    ('INT', 'int')
    ('ID', 'x')
    ('ASSIGN', '=')
    ('NUMBER', '2')
    ('SEMICOLON', ';')
    ('INT', 'int')
    ('ID', 'y')
    ('ASSIGN', '=')
    ('NUMBER', '3')
    ('SEMICOLON', ';')
    ('INT', 'int')
    ('ID', 'z')
    ('ASSIGN', '=')
    ('ID', 'x')
    ('MUL', '*')
    ('ID', 'x')
    ('MUL', '*')
    ('ID', 'x')
    ('ADD', '+')
    ('ID', 'x')
    ('MUL', '*')
    ('ID', 'y')
    ('SEMICOLON', ';')
    ('PRINT', 'print')
    ('LPAREN', '(')
    ('ID', 'z')
    ('RPAREN', ')')
    ('SEMICOLON', ';')

    <---Abstract Parse Tree--->

    Assignment(x, Number(2))
    Assignment(y, Number(3))
    Assignment(z, BinOp(BinOp(BinOp(Variable(x), *, Variable(x)), *, Variable(x)), +, BinOp(Variable(x), *, Variable(y))))
    Print(Variable(z))

    <---ASM Output--->

    MOV x, 2
    MOV y, 3
    CUBEMULADD z, x, y
    PRINT z

    ✅ Assembly code written to ./output.asm
    Compilation Successful!

    <---Result(s)--->

    14
```

---
## Why create a simulation? Why not just implement it in real machine?
Simply because it's not feasible. A CPU has predefined instructions like `ADD`, `IMUL` etc. To implement a custom instruction like `CUBEMULADD` would mean one would have to make a new CPU from scratch.So the options are:<br>
    1. Build a new CPU from scratch(not feasible)<br>
    2. One could trick the compiler to produce a custom assembly, but again it won't execute because it's not a valid system instruction(due to point 1)<br>
    3. Create a virtual cpu and a virtual compiler-cum-interpreter(this project).
## Why `objdump` would not work?
Since this is a virtual maching you could directly see the assembly code when you run the `Code.py` file. It's save in `./ouput.asm` file in the current directory.
You couldn't use `objdump` in it cuz this command simply doesn't exist in the virtual machine. You could directly view the .asm code as explained above.
## ⚙️ Why It Doesn’t Produce `.exe`
I chose not to simulate `.exe` creation because `.exe` implies a platform-specific binary, while my instruction set targets a virtual architecture not tied to actual hardware. Adding a fake `.exe` wouldn't improve functionality and could confuse the abstraction.
This compiler is a **simulation**. It stops at the code generation phase and does **not produce actual executables (.exe)**, because:
- The custom instruction `CUBEMULADD` doesn’t exist in real hardware.
- No real machine code or binary backend is implemented.
- The output is designed for a custom virtual architecture, not physical execution.

The goal is to demonstrate compiler design principles, pattern recognition, and custom instruction integration — not low-level compilation.

---

## 🎓 Project Objective

This project was built for an academic assignment:

> Design a custom instruction for a given equation in a compiler.

It showcases a working frontend + backend compiler flow and integrates a hand-designed instruction to optimize a specific computation pattern.

---
