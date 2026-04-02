class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Assign(Node):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr


class Read(Node):
    def __init__(self, var):
        self.var = var


class Write(Node):
    def __init__(self, expr):
        self.expr = expr


class ForLoop(Node):
    def __init__(self, var, start, end, body):
        self.var = var
        self.start = start
        self.end = end
        self.body = body


class IfStatement(Node):
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body


class Block(Node):
    def __init__(self, statements):
        self.statements = statements