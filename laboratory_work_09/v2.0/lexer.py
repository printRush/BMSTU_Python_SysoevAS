from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT', r'draw')
        self.lexer.add('LET', r'let')

        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('STRING', r'\^[^\^]*\^')

        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*')

        self.lexer.add('EQ', r'==')
        self.lexer.add('NE', r'!=')
        self.lexer.add('GT', r'>')
        self.lexer.add('LT', r'<')

        self.lexer.add('ASSIGN', r'=')

        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')

        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        self.lexer.add('SEMI_COLON', r'\;')

        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'//[^\n]*')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
