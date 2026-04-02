import sys
from lexer import Lexer
from parser import Parser
from ast import Block, Number, Variable, BinOp, Assign, Read, Write, ForLoop, IfStatement


class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def error(self, message):
        raise Exception(f'Runtime error: {message}')

    def eval(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, Variable):
            if node.name not in self.variables:
                self.error(f'Variable {node.name} not initialized')
            return self.variables[node.name]
        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                if right == 0:
                    self.error('Division by zero')
                return left // right
            elif node.op == '<':
                return 1 if left < right else 0
            elif node.op == '>':
                return 1 if left > right else 0
            elif node.op == '<>':
                return 1 if left != right else 0
            else:
                self.error(f'Unknown operator {node.op}')
        else:
            self.error(f'Unknown node type: {type(node)}')

    def execute(self, node):
        if isinstance(node, Block):
            for stmt in node.statements:
                self.execute(stmt)
        elif isinstance(node, Assign):
            value = self.eval(node.expr)
            self.variables[node.var.name] = value
        elif isinstance(node, Read):
            try:
                val = int(input(f'Enter {node.var.name}: '))
                self.variables[node.var.name] = val
            except ValueError:
                self.error('Invalid input, integer expected')
        elif isinstance(node, Write):
            print(self.eval(node.expr))
        elif isinstance(node, ForLoop):
            start = self.eval(node.start)
            end = self.eval(node.end)
            var_name = node.var.name
            if start <= end:
                for i in range(start, end + 1):
                    self.variables[var_name] = i
                    self.execute(node.body)
            else:
                for i in range(start, end - 1, -1):
                    self.variables[var_name] = i
                    self.execute(node.body)
        elif isinstance(node, IfStatement):
            cond = self.eval(node.condition)
            if cond != 0:
                self.execute(node.body)
            elif node.else_body:
                self.execute(node.else_body)
        else:
            self.error(f'Unknown statement type: {type(node)}')

    def run(self):
        self.execute(self.ast)


def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <source_file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        source = f.read()

    lexer = Lexer(source)
    tokens = lexer.tokenize()
    print('Tokens:')
    for tok in tokens:
        print(f'  {tok}')

    parser = Parser(tokens)
    ast = parser.parse_program()
    print('\nAST parsed successfully')

    interpreter = Interpreter(ast)
    print('\nProgram output:')
    interpreter.run()


if __name__ == '__main__':
    main()