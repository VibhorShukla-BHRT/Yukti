from compile_and_run import Compile_And_Run
src = """
int x = 2;
int y = 3;
int z = x * x * x + x * y;
print(z);
"""
Compile_And_Run(src)