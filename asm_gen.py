from ast_builder import Number, Variable, BinOp, Assignment, Parser, Print
from tokeniser import tokenize

class AsmGen:
    def __init__(self):
        self.instructions = []
    def generate(self, node):
        if isinstance(node, Number):
            return str(node.value)
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, BinOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            return f'({left} {node.op} {right})'
        elif isinstance(node, Assignment):
            expr = self.match_cubemuladd(node.expr)
            cubemul = self.match_cubemuladd_instr(node.var_name, node.expr)
            if cubemul:
                self.instructions.append(cubemul)
            else:
                expr_code = self.generate(node.expr)
                self.instructions.append(f"MOV {node.var_name}, {expr_code}")
        elif isinstance(node, Print):
            expr = self.generate(node.expr)
            self.instructions.append(f'PRINT {expr}')
    def match_cubemuladd(self, expr):
        # Match pattern: x*x*x + x*y
        if (isinstance(expr, BinOp) and expr.op == '+' and
            isinstance(expr.left, BinOp) and expr.left.op == '*' and
            isinstance(expr.left.left, BinOp) and expr.left.left.op == '*' and
            isinstance(expr.right, BinOp) and expr.right.op == '*'):

            x1 = expr.left.left.left
            x2 = expr.left.left.right
            x3 = expr.left.right
            x4 = expr.right.left
            y = expr.right.right

            if (all(isinstance(x, Variable) and x.name == x1.name for x in [x1, x2, x3, x4])):
                return f"CUBEMULADD {x1.name}, {y.name}"
        
        # Fallback
        return self.generate(expr)
    def match_cubemuladd_instr(self, target, expr):
        if (isinstance(expr, BinOp) and expr.op == '+' and
            isinstance(expr.left, BinOp) and expr.left.op == '*' and
            isinstance(expr.left.left, BinOp) and expr.left.left.op == '*' and
            isinstance(expr.right, BinOp) and expr.right.op == '*'):

            x1 = expr.left.left.left
            x2 = expr.left.left.right
            x3 = expr.left.right
            x4 = expr.right.left
            y = expr.right.right

            if all(isinstance(x, Variable) and x.name == x1.name for x in [x1, x2, x3, x4]):
                return f"CUBEMULADD {target}, {x1.name}, {y.name}"
        
        return None