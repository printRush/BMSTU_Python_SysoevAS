from rply import ParserGenerator
from ast import Number, String, Sum, Sub, Mul, Div, Print


class Parser:
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            [
                'NUMBER', 'STRING', 'PRINT',
                'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON',
                'SUM', 'SUB', 'MUL', 'DIV'
            ],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV']),
            ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):

        @self.pg.production('program : instructions')
        def program(p):
            class Program:
                def __init__(self, instructions):
                    self.instructions = instructions

                def eval(self):
                    for instr in self.instructions:
                        instr.eval()

            return Program(p[0])

        @self.pg.production('instructions : instruction')
        def instructions_single(p):
            return [p[0]]

        @self.pg.production('instructions : instruction instructions')
        def instructions_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('instruction : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def instruction_print(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            op_type = operator.gettokentype()

            if op_type == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif op_type == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif op_type == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif op_type == 'DIV':
                return Div(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            value = int(p[0].value)
            return Number(self.builder, self.module, value)

        @self.pg.production('expression : STRING')
        def string(p):
            value = p[0].value
            return String(self.builder, self.module, value)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def parens(p):
            return p[1]

        @self.pg.production('program : ')
        def empty_program():
            class EmptyProgram:
                def eval(self):
                    print("Пустая программа")
            return EmptyProgram()

        @self.pg.error
        def error_handle(token):
            if token:
                raise ValueError(token.getstr(), token.gettokentype())
            else:
                raise ValueError("Error!")

    def get_parser(self):
        return self.pg.build()
