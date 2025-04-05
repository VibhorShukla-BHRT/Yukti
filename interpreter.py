from ast_builder import Number, Variable, BinOp, Assignment, Print, Parser
class Interpreter:
    def __init__(self):
        self.env = {} #Map(Symbol table) for storing values
    def eval(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, Variable):
            if node.name in self.env:
                return self.env[node.name]
            else:
                raise NameError(f'Undefined variable: {node.name}')
        elif isinstance(node, BinOp):
            left=self.eval(node.left)
            right=self.eval(node.right)
            if node.op=='+':
                return left+right
            elif node.op=='*':
                return left*right
            else:
                raise ValueError(f'Unsupported operator: {node.op}')
        elif isinstance(node, Assignment):
            value = self.eval(node.expr)
            self.env[node.var_name] = value
        elif isinstance(node, Print):
            value = self.eval(node.expr)
            print(value)
        else :
            raise TypeError(f"Unknown node type: {type(node)}")

