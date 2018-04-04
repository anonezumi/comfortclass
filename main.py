import sys
from antlr4 import *
from comfortclassLexer import comfortclassLexer
from comfortclassParser import comfortclassParser
from comfortclassVisitor import comfortclassVisitor


class MainVisitor(comfortclassVisitor):
    def __init__(self):
        print("Visitor Initialized.")


def main():
    inp = FileStream(sys.argv[1])
    lexer = comfortclassLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = comfortclassParser(stream)
    script = parser.script()
    visitor = MainVisitor()
    visitor.visit(script)


if __name__ == '__main__':
    main()
