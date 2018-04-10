# Generated from comfortclass.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .comfortclassParser import comfortclassParser
else:
    from comfortclassParser import comfortclassParser

# This class defines a complete generic visitor for a parse tree produced by comfortclassParser.

class comfortclassVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by comfortclassParser#imports.
    def visitImports(self, ctx:comfortclassParser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#enumdef.
    def visitEnumdef(self, ctx:comfortclassParser.EnumdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#param.
    def visitParam(self, ctx:comfortclassParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#paramlist.
    def visitParamlist(self, ctx:comfortclassParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#array.
    def visitArray(self, ctx:comfortclassParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#dict_.
    def visitDict_(self, ctx:comfortclassParser.Dict_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#magic.
    def visitMagic(self, ctx:comfortclassParser.MagicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#identifier.
    def visitIdentifier(self, ctx:comfortclassParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#call.
    def visitCall(self, ctx:comfortclassParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#return_.
    def visitReturn_(self, ctx:comfortclassParser.Return_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#modifier.
    def visitModifier(self, ctx:comfortclassParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#vardef.
    def visitVardef(self, ctx:comfortclassParser.VardefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#extvardef.
    def visitExtvardef(self, ctx:comfortclassParser.ExtvardefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#funcdef.
    def visitFuncdef(self, ctx:comfortclassParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#extfuncdef.
    def visitExtfuncdef(self, ctx:comfortclassParser.ExtfuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#eventdef.
    def visitEventdef(self, ctx:comfortclassParser.EventdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#classdef.
    def visitClassdef(self, ctx:comfortclassParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#if_.
    def visitIf_(self, ctx:comfortclassParser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#while_.
    def visitWhile_(self, ctx:comfortclassParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#for_.
    def visitFor_(self, ctx:comfortclassParser.For_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#switch_.
    def visitSwitch_(self, ctx:comfortclassParser.Switch_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#expression.
    def visitExpression(self, ctx:comfortclassParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#statement.
    def visitStatement(self, ctx:comfortclassParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#codeblock.
    def visitCodeblock(self, ctx:comfortclassParser.CodeblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#file_component.
    def visitFile_component(self, ctx:comfortclassParser.File_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#script.
    def visitScript(self, ctx:comfortclassParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by comfortclassParser#string.
    def visitString(self, ctx:comfortclassParser.StringContext):
        return self.visitChildren(ctx)



del comfortclassParser