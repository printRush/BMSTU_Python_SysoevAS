from lexer import Lexer
from parser import Parser
from codegen import CodeGen

file_name = "main.lol"
with open(file_name) as f:
    text_input = f.read()

codegen = CodeGen()
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
token_list = list(tokens)
print_tokens = token_list
for token in print_tokens:
    print(token)

pg = Parser(codegen.module, codegen.builder, codegen.printf)
pg.parse()
parser = pg.get_parser()

ast = parser.parse(iter(token_list))
ast.eval()
codegen.create_ir()
codegen.save_ir("output.ll")
