# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program_lst.
    def visitProgram_lst(self, ctx:MiniGoParser.Program_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program_mem.
    def visitProgram_mem(self, ctx:MiniGoParser.Program_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_lst.
    def visitArray_lit_lst(self, ctx:MiniGoParser.Array_lit_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_mem.
    def visitArray_lit_mem(self, ctx:MiniGoParser.Array_lit_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit_mem_single.
    def visitArray_lit_mem_single(self, ctx:MiniGoParser.Array_lit_mem_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_elem_lst.
    def visitList_struct_elem_lst(self, ctx:MiniGoParser.List_struct_elem_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_elem_mem.
    def visitList_struct_elem_mem(self, ctx:MiniGoParser.List_struct_elem_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_attribute_lst.
    def visitStruct_attribute_lst(self, ctx:MiniGoParser.Struct_attribute_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_attribute_mem.
    def visitStruct_attribute_mem(self, ctx:MiniGoParser.Struct_attribute_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_lst.
    def visitInterface_method_lst(self, ctx:MiniGoParser.Interface_method_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_mem.
    def visitInterface_method_mem(self, ctx:MiniGoParser.Interface_method_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_param_lst.
    def visitInterface_method_param_lst(self, ctx:MiniGoParser.Interface_method_param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method_param_lst_mem.
    def visitInterface_method_param_lst_mem(self, ctx:MiniGoParser.Interface_method_param_lst_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_lst.
    def visitId_lst(self, ctx:MiniGoParser.Id_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_with_init.
    def visitVar_decl_with_init(self, ctx:MiniGoParser.Var_decl_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_non_init.
    def visitVar_decl_non_init(self, ctx:MiniGoParser.Var_decl_non_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prim_type.
    def visitPrim_type(self, ctx:MiniGoParser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_type.
    def visitVar_type(self, ctx:MiniGoParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para_lst.
    def visitPara_lst(self, ctx:MiniGoParser.Para_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para_mem.
    def visitPara_mem(self, ctx:MiniGoParser.Para_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_receiver_lst.
    def visitMethod_receiver_lst(self, ctx:MiniGoParser.Method_receiver_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_receiver_mem.
    def visitMethod_receiver_mem(self, ctx:MiniGoParser.Method_receiver_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_func.
    def visitBlock_func(self, ctx:MiniGoParser.Block_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_func_lst.
    def visitBlock_func_lst(self, ctx:MiniGoParser.Block_func_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_func_mem.
    def visitBlock_func_mem(self, ctx:MiniGoParser.Block_func_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_block.
    def visitStmt_block(self, ctx:MiniGoParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01.
    def visitFor_stmt_01(self, ctx:MiniGoParser.For_stmt_01Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_init.
    def visitFor_stmt_01_init(self, ctx:MiniGoParser.For_stmt_01_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_cond.
    def visitFor_stmt_01_cond(self, ctx:MiniGoParser.For_stmt_01_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_upda.
    def visitFor_stmt_01_upda(self, ctx:MiniGoParser.For_stmt_01_updaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_var_decl_init.
    def visitFor_stmt_01_var_decl_init(self, ctx:MiniGoParser.For_stmt_01_var_decl_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_upda_incr.
    def visitFor_stmt_01_upda_incr(self, ctx:MiniGoParser.For_stmt_01_upda_incrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_assign.
    def visitFor_stmt_01_assign(self, ctx:MiniGoParser.For_stmt_01_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_02.
    def visitFor_stmt_02(self, ctx:MiniGoParser.For_stmt_02Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt_03.
    def visitFor_stmt_03(self, ctx:MiniGoParser.For_stmt_03Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt_rec.
    def visitIf_stmt_rec(self, ctx:MiniGoParser.If_stmt_recContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt_type1.
    def visitIf_stmt_type1(self, ctx:MiniGoParser.If_stmt_type1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt_type2.
    def visitIf_stmt_type2(self, ctx:MiniGoParser.If_stmt_type2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt.
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#cont_stmt.
    def visitCont_stmt(self, ctx:MiniGoParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_func.
    def visitCall_func(self, ctx:MiniGoParser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt_semi.
    def visitAssign_stmt_semi(self, ctx:MiniGoParser.Assign_stmt_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#increase_stmt.
    def visitIncrease_stmt(self, ctx:MiniGoParser.Increase_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#increase_stmt_semi.
    def visitIncrease_stmt_semi(self, ctx:MiniGoParser.Increase_stmt_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#comp_op.
    def visitComp_op(self, ctx:MiniGoParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_op.
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6_postfix_lst.
    def visitExpr6_postfix_lst(self, ctx:MiniGoParser.Expr6_postfix_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6_postfix_mem.
    def visitExpr6_postfix_mem(self, ctx:MiniGoParser.Expr6_postfix_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_args.
    def visitMethod_args(self, ctx:MiniGoParser.Method_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access.
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#attribute_chain.
    def visitAttribute_chain(self, ctx:MiniGoParser.Attribute_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_expr.
    def visitLhs_expr(self, ctx:MiniGoParser.Lhs_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#property_chain.
    def visitProperty_chain(self, ctx:MiniGoParser.Property_chainContext):
        return self.visitChildren(ctx)



del MiniGoParser