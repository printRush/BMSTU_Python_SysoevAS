from rply import ParserGenerator
from ast import Number, Sum, Sub, Print


class Parser:
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            [
                'NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB'
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
            return [p[0]]  # Возвращаем список с одной инструкцией

        @self.pg.production('instructions : instruction instructions')
        def instructions_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('instruction : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def instruction_print(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.production('program : ')
        def empty_program(p):
            class EmptyProgram:
                def eval(self):
                    pass
            return EmptyProgram()

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Ошибка: неожиданный токен '{token.getstr()}'")

    def get_parser(self):
        return self.pg.build()
