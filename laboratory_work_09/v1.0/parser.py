from ast import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def error(self, message):
        if self.pos < len(self.tokens):
            tok = self.tokens[self.pos]
            raise Exception(f'Parser error at {tok.line}:{tok.column}: {message}')
        raise Exception(f'Parser error at end of file: {message}')

    def peek(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def consume(self, expected_type=None):
        if self.pos >= len(self.tokens):
            self.error(f'Unexpected end of input')
        tok = self.tokens[self.pos]
        if expected_type and tok.type != expected_type:
            self.error(f'Expected {expected_type}, got {tok.type}')
        self.pos += 1
        return tok

    def match(self, expected_type):
        if self.peek() and self.peek().type == expected_type:
            self.pos += 1
            return True
        return False

    def parse_program(self):
        statements = []
        while self.peek():
            stmt = self.parse_statement()
            statements.append(stmt)
        return Block(statements)

    def parse_statement(self):
        tok = self.peek()
        if tok.type == 'READ':
            return self.parse_read()
        elif tok.type == 'WRITE':
            return self.parse_write()
        elif tok.type == 'IDENTIFIER':
            return self.parse_assign()
        elif tok.type == 'FOR':
            return self.parse_for()
        elif tok.type == 'IF':
            return self.parse_if()
        elif tok.type == 'LBRACE':
            return self.parse_block()
        else:
            self.error(f'Unexpected statement: {tok.type}')

    def parse_block(self):
        self.consume('LBRACE')
        statements = []
        while self.peek() and self.peek().type != 'RBRACE':
            statements.append(self.parse_statement())
        self.consume('RBRACE')
        return Block(statements)

    def parse_read(self):
        tok = self.consume('READ')
        var = self.consume('IDENTIFIER')
        self.consume('SEMICOLON')
        return Read(Variable(var.value))

    def parse_write(self):
        self.consume('WRITE')
        expr = self.parse_expression()
        self.consume('SEMICOLON')
        return Write(expr)

    def parse_assign(self):
        var = self.consume('IDENTIFIER')
        self.consume('ASSIGN')
        expr = self.parse_expression()
        self.consume('SEMICOLON')
        return Assign(Variable(var.value), expr)

    def parse_for(self):
        self.consume('FOR')
        var = self.consume('IDENTIFIER')
        self.consume('ASSIGN')
        start = self.parse_expression()
        self.consume('TO')
        end = self.parse_expression()
        body = self.parse_statement()
        return ForLoop(Variable(var.value), start, end, body)

    def parse_if(self):
        self.consume('IF')
        condition = self.parse_expression()
        body = self.parse_statement()
        else_body = None
        if self.match('ELSE'):
            else_body = self.parse_statement()
        return IfStatement(condition, body, else_body)

    def parse_expression(self):
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_add_sub()
        tok = self.peek()
        if tok and tok.type in ('LT', 'GT', 'NEQ'):
            self.consume()
            right = self.parse_add_sub()
            return BinOp(left, tok.value, right)
        return left

    def parse_add_sub(self):
        left = self.parse_mul_div()
        while self.peek() and self.peek().type in ('PLUS', 'MINUS'):
            op = self.consume()
            right = self.parse_mul_div()
            left = BinOp(left, op.value, right)
        return left

    def parse_mul_div(self):
        left = self.parse_factor()
        while self.peek() and self.peek().type in ('MUL', 'DIV'):
            op = self.consume()
            right = self.parse_factor()
            left = BinOp(left, op.value, right)
        return left

    def parse_factor(self):
        tok = self.peek()
        if tok.type == 'NUMBER':
            self.consume('NUMBER')
            return Number(tok.value)
        elif tok.type == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return Variable(tok.value)
        elif tok.type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
            return expr
        else:
            self.error(f'Unexpected factor: {tok.type}')