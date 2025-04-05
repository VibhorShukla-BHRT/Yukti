#Abstract Syntax Tree(AST) using Recurrsive Descent Parser
from tokeniser import tokenize
class Number:
    def __init__(self,value):
        self.value = int(value)
    def __repr__(self):
        return f'Number({self.value})'
class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Variable({self.name})'
class BinOp:
    def __init__ (self, left, op, right):
        self.left=left
        self.right=right
        self.op=op
    def __repr__(self):
        return f'BinOp({self.left}, {self.op}, {self.right})'
class Assignment:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr
    def __repr__(self):
        return f'Assignment({self.var_name}, {self.expr})'
class Print:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f'Print({self.expr})'
class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos=0
    def current(self):
        return self.tokens[self.pos] if self.pos<len(self.tokens) else ('EOF', '')
    def eat(self, expected_type):
        tok_type, tok_value = self.current()
        if tok_type == expected_type:
            self.pos+=1
            return tok_value
        else:
            raise SystemError(f"Expected {expected_type} got {tok_type}")
    def parse(self):
        statements = []
        while self.current()[0] != 'EOF':
            statements.append(self.statement())
        return statements
    def statement(self):
        tok_type, _ = self.current()

        if tok_type == 'INT':
            self.eat('INT')
            var_name = self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expression()
            self.eat('SEMICOLON')
            return Assignment(var_name, expr)

        elif tok_type == 'PRINT':
            self.eat('PRINT')
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            self.eat('SEMICOLON')
            return Print(expr)

        else:
            raise SyntaxError(f"Unexpected statement start: {tok_type}")
    def expression(self):
        node = self.term()
        while self.current()[0] == 'ADD':
            op = self.eat('ADD')
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current()[0] == 'MUL':
            op = self.eat('MUL')
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        tok_type, tok_val = self.current()
        if tok_type == 'NUMBER':
            self.eat('NUMBER')
            return Number(tok_val)
        elif tok_type == 'ID':
            self.eat('ID')
            return Variable(tok_val)
        elif tok_type == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token in factor: {tok_type}")

