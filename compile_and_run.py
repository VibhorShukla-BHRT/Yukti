from tokeniser import tokenize
from ast_builder import Parser
from interpreter import Interpreter
from asm_gen import AsmGen

class Compile_And_Run():
    def __init__(self, src):
        print('\n<---Tokenisation--->\n')

        tokens = tokenize(src)
        for token in tokens:
            print(token)

        print('\n<---Abstract Parse Tree--->\n')

        parser = Parser(tokens)
        ast = parser.parse()
        for stmt in ast:
            print(stmt)

        print("\n<---ASM Output--->\n")

        generator = AsmGen()
        for stmt in ast:
            generator.generate(stmt)

        for instr in generator.instructions:
            print(instr)
        with open("output.asm", "w") as f:
            for instr in generator.instructions:
                f.write(instr + "\n")

        print("\n✅ Assembly code written to ./output.asm")
        print("Compilation Successful!")
        print('\n<---Result(s)--->\n')

        interpreter = Interpreter()
        for stmt in ast:
            interpreter.eval(stmt)
