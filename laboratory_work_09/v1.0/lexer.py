import re


class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'Token({self.type}, {self.value}, {self.line}, {self.column})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def error(self, message):
        raise Exception(f'Lexer error at {self.line}:{self.column}: {message}')

    def peek(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def advance(self):
        if self.pos >= len(self.text):
            return None
        char = self.text[self.pos]
        self.pos += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def skip_whitespace(self):
        while self.peek() and self.peek() in ' \t\r':
            self.advance()

    def read_number(self):
        start_line = self.line
        start_col = self.column
        num = ''
        while self.peek() and self.peek().isdigit():
            num += self.advance()
        return Token('NUMBER', int(num), start_line, start_col)

    def read_identifier(self):
        start_line = self.line
        start_col = self.column
        ident = ''
        while self.peek() and (self.peek().isalpha() or self.peek().isdigit()):
            ident += self.advance()
        if ident == 'for':
            return Token('FOR', ident, start_line, start_col)
        elif ident == 'if':
            return Token('IF', ident, start_line, start_col)
        elif ident == 'else':
            return Token('ELSE', ident, start_line, start_col)
        elif ident == 'write':
            return Token('WRITE', ident, start_line, start_col)
        elif ident == 'read':
            return Token('READ', ident, start_line, start_col)
        else:
            return Token('IDENTIFIER', ident, start_line, start_col)

    def tokenize(self):
        while self.pos < len(self.text):
            char = self.peek()

            if char in ' \t\r':
                self.skip_whitespace()
                continue
            if char == '\n':
                self.advance()
                continue

            if char.isdigit():
                self.tokens.append(self.read_number())
                continue

            if char.isalpha():
                self.tokens.append(self.read_identifier())
                continue

            if char == '=':
                self.tokens.append(Token('ASSIGN', '=', self.line, self.column))
                self.advance()
                continue

            if char == '+':
                self.tokens.append(Token('PLUS', '+', self.line, self.column))
                self.advance()
                continue

            if char == '-':
                self.tokens.append(Token('MINUS', '-', self.line, self.column))
                self.advance()
                continue

            if char == '*':
                self.tokens.append(Token('MUL', '*', self.line, self.column))
                self.advance()
                continue

            if char == '/':
                self.tokens.append(Token('DIV', '/', self.line, self.column))
                self.advance()
                continue

            if char == '(':
                self.tokens.append(Token('LPAREN', '(', self.line, self.column))
                self.advance()
                continue

            if char == ')':
                self.tokens.append(Token('RPAREN', ')', self.line, self.column))
                self.advance()
                continue

            if char == '{':
                self.tokens.append(Token('LBRACE', '{', self.line, self.column))
                self.advance()
                continue

            if char == '}':
                self.tokens.append(Token('RBRACE', '}', self.line, self.column))
                self.advance()
                continue

            if char == ';':
                self.tokens.append(Token('SEMICOLON', ';', self.line, self.column))
                self.advance()
                continue

            if char == '<':
                self.advance()
                if self.peek() == '>':
                    self.tokens.append(Token('NEQ', '<>', self.line, self.column - 1))
                    self.advance()
                else:
                    self.tokens.append(Token('LT', '<', self.line, self.column - 1))
                continue

            if char == '>':
                self.advance()
                self.tokens.append(Token('GT', '>', self.line, self.column - 1))
                continue

            self.error(f'Unknown character: {char}')

        return self.tokens


    def read_identifier(self):
        start_line = self.line
        start_col = self.column
        ident = ''
        while self.peek() and (self.peek().isalpha() or self.peek().isdigit()):
            ident += self.advance()
        if ident == 'for':
            return Token('FOR', ident, start_line, start_col)
        elif ident == 'to':
            return Token('TO', ident, start_line, start_col)
        elif ident == 'if':
            return Token('IF', ident, start_line, start_col)
        elif ident == 'else':
            return Token('ELSE', ident, start_line, start_col)
        elif ident == 'write':
            return Token('WRITE', ident, start_line, start_col)
        elif ident == 'read':
            return Token('READ', ident, start_line, start_col)
        else:
            return Token('IDENTIFIER', ident, start_line, start_col)