import sys
from antlr4 import *
from comfortclassLexer import comfortclassLexer
from comfortclassParser import comfortclassParser
from comfortclassVisitor import comfortclassVisitor
codeController = None


class CodeController():
    def __init__(self):
        self.globalScope = CCScope()
        self.currentScope = self.globalScope
        self.callStack = []
        self.classes = {}
        self.currentClass = None
        print("CodeController Initialized.")


class CCObject():
    def __init__(self, name, cl=None):
        self.name = name
        self.cl = cl
        if cl is None:
            self.vars = {}
        else:
            self.vars = cl.vars
            codeController.currentScope = self.cl.functions


class CCScope(CCObject):
    def __init__(self, parent=None):
        self.cl = None
        self.name = "Scope Object"
        self.vars = {}
        self.parent = parent


class CCClass(CCScope):
    def __init__(self, name, parents=[]):
        print("Initializing Class...")
        self.cl = None
        self.name = name
        self.vars = {}
        self.functions = {}
        for parent in parents:
            for key, var in parent.vars:
                if key not in self.vars.keys():
                    self.vars[key] = var
            for func, var in parent.functions:
                if key not in self.functions.keys():
                    self.functions[key] = func


class MainVisitor(comfortclassVisitor):
    def visitScript(self, ctx):
        print("Visited Script.")
        return self.visitChildren(ctx)

    def visitClassdef(self, ctx):
        print("Visited Class.")
        name = ctx.getToken(comfortclassLexer.IDENTIFIER, 0)
        parents = []
        children = ctx.getChildren()
        if children[2].getText() == "(":
            for child in children[3:]:
                if child.getText == ")":
                    break
                parents.append()
        cl = CCClass(name, [])
        codeController.classes[name] = cl
        codeController.currentClass = cl
        return self.visitChildren(ctx)

    def visitFuncdef(self, ctx):
        codeController.currentClass.functions.append(ctx)


def main():
    global codeController
    codeController = CodeController()
    inp = FileStream(sys.argv[1])
    lexer = comfortclassLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = comfortclassParser(stream)
    script = parser.script()
    visitor = MainVisitor()
    visitor.visit(script)


if __name__ == '__main__':
    main()
