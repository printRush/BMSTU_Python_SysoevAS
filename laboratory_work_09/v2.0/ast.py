from llvmlite import ir


class Number:
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        return ir.Constant(ir.IntType(32), int(self.value))


class String:
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        clean_value = self.value[1:-1]
        str_name = f".str.{abs(hash(clean_value)) % 10000}"

        existing = self.module.globals.get(str_name, None)
        if existing:
            return existing

        str_type = ir.ArrayType(ir.IntType(8), len(clean_value) + 1)
        str_const = ir.Constant(str_type, bytearray((clean_value + "\0").encode("utf8")))
        str_global = ir.GlobalVariable(self.module, str_type, name=str_name)
        str_global.linkage = 'internal'
        str_global.global_constant = True
        str_global.initializer = str_const
        return str_global


class BinaryOp:
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        left_desc = self.left.value if hasattr(self.left, 'value') else 'expr'
        right_desc = self.right.value if hasattr(self.right, 'value') else 'expr'
        return self.builder.add(left_val, right_val)


class Sub(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        left_desc = self.left.value if hasattr(self.left, 'value') else 'expr'
        right_desc = self.right.value if hasattr(self.right, 'value') else 'expr'
        return self.builder.sub(left_val, right_val)


class Mul(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        left_desc = self.left.value if hasattr(self.left, 'value') else 'expr'
        right_desc = self.right.value if hasattr(self.right, 'value') else 'expr'
        return self.builder.mul(left_val, right_val)


class Div(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        left_desc = self.left.value if hasattr(self.left, 'value') else 'expr'
        right_desc = self.right.value if hasattr(self.right, 'value') else 'expr'
        return self.builder.sdiv(left_val, right_val)


class Print:
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value
        self.counter = 0

    def eval(self):
        value = self.value.eval()

        Print.counter = getattr(Print, 'counter', 0) + 1
        counter = Print.counter

        if isinstance(value.type, ir.IntType):
            voidptr_ty = ir.IntType(8).as_pointer()
            fmt = "%d\n\0"
            c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))

            fmt_name = f"fstr_int_{counter}"

            global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_name)
            global_fmt.linkage = 'internal'
            global_fmt.global_constant = True
            global_fmt.initializer = c_fmt

            fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
            self.builder.call(self.printf, [fmt_arg, value])
        else:
            voidptr_ty = ir.IntType(8).as_pointer()
            fmt = "%s\n\0"
            c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))

            fmt_name = f"fstr_str_{counter}"

            global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_name)
            global_fmt.linkage = 'internal'
            global_fmt.global_constant = True
            global_fmt.initializer = c_fmt

            fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
            str_ptr = self.builder.bitcast(value, voidptr_ty)
            self.builder.call(self.printf, [fmt_arg, str_ptr])
