import re

token_specs = [
    ('INT', r'int'),
    ('PRINT', r'print'),
    ('NUMBER', r'\d+'),
    ('ID', r'[a-zA-Z_]\w*'),
    ('ASSIGN', r'='),
    ('MUL', r'\*'),
    ('ADD', r'\+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    ('MISMATCH', r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
get_token = re.compile(token_regex).match

def tokenize(code):
    pos=0
    tokens=[]
    mo = get_token(code,pos)

    while(mo):
        kind=mo.lastgroup
        value=mo.group()
        if kind =='NEWLINE' or kind == 'SKIP':
            pass
        elif kind=='MISMATCH':
            raise RuntimeError(f'Unexpected token {value!r} at pos {pos}')
        else:
            tokens.append((kind,value))
        pos=mo.end()
        mo=get_token(code,pos)
    return tokens
