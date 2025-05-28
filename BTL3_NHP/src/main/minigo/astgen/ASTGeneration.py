# 2252621
# Nguyen Quang Phu
# 2252621
# Nguyen Quang Phu

from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    # program: program_lst EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.program_lst()))
    

    # Visit a parse tree produced by MiniGoParser#program_lst.
    # program_lst: program_mem program_lst | program_mem;
    def visitProgram_lst(self, ctx:MiniGoParser.Program_lstContext):
        prog_lst = []
        if ctx.program_mem():
            prog_mem = self.visit(ctx.program_mem())
            prog_lst.append(prog_mem)
        
        if ctx.program_lst():
            prog_lst1 = self.visit(ctx.program_lst())
            if isinstance(prog_lst1, list):
                prog_lst.extend(prog_lst1)
            else:
                prog_lst.append(prog_lst1)
        return prog_lst


    # Visit a parse tree produced by MiniGoParser#program_mem.
    # program_mem: declared | var_decl | const_decl;
    def visitProgram_mem(self, ctx:MiniGoParser.Program_memContext):
        if ctx.declared():
            return self.visit(ctx.declared())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.var_decl():
            return self.visit(ctx.var_decl())


    # Visit a parse tree produced by MiniGoParser#declared.
    # declared: func_decl | method_decl | struct_type | interface_type;
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        if ctx.func_decl():
            return self.visit(ctx.func_decl())
        elif ctx.method_decl():
            return self.visit(ctx.method_decl())
        elif ctx.struct_type():
            return self.visit(ctx.struct_type())
        elif ctx.interface_type():
            return self.visit(ctx.interface_type())


    # Visit a parse tree produced by MiniGoParser#literal.
    # literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            return IntLiteral(int(text, base=0))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            text = ctx.STRING_LIT().getText()
            return StringLiteral(text)  
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#array_lit.
    # array_lit: array_type CUR_OPEN array_lit_lst CUR_CLOSE;
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        array_type = self.visit(ctx.array_type())       
        elements = self.visit(ctx.array_lit_lst())    

        dimensions = array_type.dimens              
        element_type = array_type.eleType                  

        return ArrayLiteral(dimens=dimensions, eleType=element_type, value=elements)


    # Visit a parse tree produced by MiniGoParser#array_type.
    # array_type: 
    # (SQ_OPEN (INT_LIT | ID) SQ_CLOSE) (array_type | prim_type | ID);
    def visitArray_type(self, ctx: MiniGoParser.Array_typeContext):
        if ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            size_lit = IntLiteral(int(text, base=0))
            
        elif ctx.ID():
            # Check if ctx.ID() returns a list
            id_token = ctx.ID()[0] if isinstance(ctx.ID(), list) else ctx.ID()
            size_lit = Id(id_token.getText())  # Extracts text correctly

        if ctx.array_type():                                    
            nested_array_type = self.visit(ctx.array_type())    
            dimensions = [size_lit] + nested_array_type.dimens
            element_type = nested_array_type.eleType            
        elif ctx.prim_type():                                   
            dimensions = [size_lit]
            element_type = self.visit(ctx.prim_type())  
        # Handle final ID as element type correctly
        else:
            id_tokens = ctx.ID()  # Get all ID tokens
            if isinstance(id_tokens, list) and len(id_tokens) > 1:
                element_type = Id(id_tokens[-1].getText())  # Last ID is the element type
            else:
                element_type = Id(ctx.ID()[0].getText())  # Single ID case

            dimensions = [size_lit]
        
        return ArrayType(dimens=dimensions, eleType=element_type)
           

    # Visit a parse tree produced by MiniGoParser#array_lit_lst.
    # array_lit_lst: array_lit_mem COMMA array_lit_lst | array_lit_mem;
    def visitArray_lit_lst(self, ctx: MiniGoParser.Array_lit_lstContext):
        elements = [self.visit(ctx.array_lit_mem())]  # Visit the first element

        if ctx.array_lit_lst():  # Recursively process the rest of the list
            rest_elements = self.visit(ctx.array_lit_lst())
            elements.extend(rest_elements)  # Append to preserve structure
        
        return elements  # Maintain correct nesting


    # Visit a parse tree produced by MiniGoParser#array_lit_mem.
    # array_lit_mem: 
    # CUR_OPEN array_lit_lst CUR_CLOSE 
    # | array_lit_mem_single;
    def visitArray_lit_mem(self, ctx: MiniGoParser.Array_lit_memContext):
        if ctx.array_lit_mem_single():
            return self.visit(ctx.array_lit_mem_single())  # Single element case

        elif ctx.array_lit_lst():
            return self.visit(ctx.array_lit_lst())  # Wrap in a list to maintain nesting

        return None  # Should never reach here


    # Visit a parse tree produced by MiniGoParser#array_lit_mem_single.
    # array_lit_mem_single: literal | struct_lit | ID;
    # NestedList = PrimLit | list['NestedList']
    def visitArray_lit_mem_single(self, ctx:MiniGoParser.Array_lit_mem_singleContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        # not sure these 2 below cases
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
        elif ctx.ID():
            name = ctx.ID().getText()
            return Id(name=name)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    # struct_lit: ID CUR_OPEN list_struct_elem_lst? CUR_CLOSE;
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        struct_name = ctx.ID().getText()
        elements = self.visit(ctx.list_struct_elem_lst()) if ctx.list_struct_elem_lst() else []
        return StructLiteral(name=struct_name, elements=elements)


    # Visit a parse tree produced by MiniGoParser#list_struct_elem_lst.
    # list_struct_elem_lst: list_struct_elem_mem COMMA list_struct_elem_lst | list_struct_elem_mem;
    def visitList_struct_elem_lst(self, ctx:MiniGoParser.List_struct_elem_lstContext):
        elements = []

        # Visit the first list_struct_elem_mem
        elements.append(self.visit(ctx.list_struct_elem_mem()))

        # Recursively process the rest of the list
        if ctx.list_struct_elem_lst():
            element_lst = self.visit(ctx.list_struct_elem_lst())
            elements.extend(element_lst)
        return elements


    # Visit a parse tree produced by MiniGoParser#list_struct_elem_mem.
    # list_struct_elem_mem: ID COLON expr;
    def visitList_struct_elem_mem(self, ctx:MiniGoParser.List_struct_elem_memContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return (name, value)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    # struct_type: TYPE ID STRUCT CUR_OPEN struct_attribute_lst CUR_CLOSE SEMI_COLON;
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        struct_name = ctx.ID().getText()
        
        # now force to have struct_attribute_lst
        if ctx.struct_attribute_lst():
            attributes = self.visit(ctx.struct_attribute_lst())
        else:
            attributes = []
        elements = []
        methods = []
        for attr in attributes:
            if isinstance(attr, MethodDecl):
                methods.append(attr)
            else:
                elements.append(attr)
        
        return StructType(name=struct_name, elements=elements, methods=methods)


    # Visit a parse tree produced by MiniGoParser#struct_attribute_lst.
    # struct_attribute_lst: struct_attribute_mem struct_attribute_lst | struct_attribute_mem;
    def visitStruct_attribute_lst(self, ctx:MiniGoParser.Struct_attribute_lstContext):
        attributes = []
        attr_mem = self.visit(ctx.struct_attribute_mem())
        attributes.append(attr_mem)
        if ctx.struct_attribute_lst():
            attr_lst = self.visit(ctx.struct_attribute_lst())
            attributes.extend(attr_lst)
        return attributes


    # Visit a parse tree produced by MiniGoParser#struct_attribute_mem.
    # struct_attribute_mem: 
    # ID var_type SEMI_COLON;
    def visitStruct_attribute_mem(self, ctx:MiniGoParser.Struct_attribute_memContext):
        name = ctx.ID().getText()
        type = self.visit(ctx.var_type())
        return (name, type)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    # interface_type: 
    # TYPE ID INTERFACE CUR_OPEN interface_method_lst CUR_CLOSE SEMI_COLON;
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        interface_name = ctx.ID().getText()
        methods = self.visit(ctx.interface_method_lst())
        return InterfaceType(name=interface_name, methods=methods)


    # Visit a parse tree produced by MiniGoParser#interface_method_lst.
    # interface_method_lst: 
    # interface_method_mem interface_method_lst | interface_method_mem;
    def visitInterface_method_lst(self, ctx:MiniGoParser.Interface_method_lstContext):
        methods = []
        method_mem = self.visit(ctx.interface_method_mem())
        methods.append(method_mem)
        if ctx.interface_method_lst():
            method_lst = self.visit(ctx.interface_method_lst())
            methods.extend(method_lst)
        return methods


    # Visit a parse tree produced by MiniGoParser#interface_method_mem.
    # interface_method_mem: 
    # ID (R_OPEN interface_method_param_lst? R_CLOSE) var_type? SEMI_COLON;
    def visitInterface_method_mem(self, ctx:MiniGoParser.Interface_method_memContext):
        name = ctx.ID().getText()
        
        if ctx.interface_method_param_lst():
            params = self.visit(ctx.interface_method_param_lst())
        else:
            params = []
            
        if ctx.var_type():
            returnType = self.visit(ctx.var_type())
        else:
            returnType = VoidType()
            
        return Prototype(name=name, params=params, retType=returnType)


    # Visit a parse tree produced by MiniGoParser#interface_method_param_lst.
    # interface_method_param_lst:
	# interface_method_param_lst_mem COMMA interface_method_param_lst
	# | interface_method_param_lst_mem;
    def visitInterface_method_param_lst(self, ctx:MiniGoParser.Interface_method_param_lstContext):
        params = []
        param_mem = self.visit(ctx.interface_method_param_lst_mem())
        
        if isinstance(param_mem, list):
            params.extend(param_mem)
        else:
            params.append(param_mem)
        
        if ctx.interface_method_param_lst():
            param_lst = self.visit(ctx.interface_method_param_lst())
            params.extend(param_lst)
        return params


    # Visit a parse tree produced by MiniGoParser#interface_method_param_lst_mem.
    # interface_method_param_lst_mem: 
    # id_lst var_type;
    def visitInterface_method_param_lst_mem(self, ctx:MiniGoParser.Interface_method_param_lst_memContext):
        names = self.visit(ctx.id_lst())
        type = self.visit(ctx.var_type())
        type_lst = []
        
        for i in range(len(names)):
            type_lst.append(type)

        return type_lst


    # Visit a parse tree produced by MiniGoParser#id_lst.
    # id_lst: ID COMMA id_lst | ID;
    def visitId_lst(self, ctx:MiniGoParser.Id_lstContext):
        names = []
        names.append(ctx.ID().getText())
        if ctx.id_lst():
            name_lst = self.visit(ctx.id_lst())
            names.extend(name_lst)
        return names


    # Visit a parse tree produced by MiniGoParser#var_decl.
    # var_decl: var_decl_non_init | var_decl_with_init;
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        if ctx.var_decl_non_init():
            return self.visit(ctx.var_decl_non_init())
        elif ctx.var_decl_with_init():
            return self.visit(ctx.var_decl_with_init())


    # Visit a parse tree produced by MiniGoParser#var_decl_with_init.
    # var_decl_with_init: VAR ID (var_type)? ASSIGN (expr) SEMI_COLON;
    def visitVar_decl_with_init(self, ctx:MiniGoParser.Var_decl_with_initContext):
        name = ctx.ID().getText()
        if ctx.var_type():
            type = self.visit(ctx.var_type())
        else:
            type = None
        init = self.visit(ctx.expr())
        return VarDecl(varName=name, varType=type, varInit=init)


    # Visit a parse tree produced by MiniGoParser#var_decl_non_init.
    # var_decl_non_init: VAR ID (var_type) SEMI_COLON;
    def visitVar_decl_non_init(self, ctx:MiniGoParser.Var_decl_non_initContext):
        name = ctx.ID().getText()
        if ctx.var_type():
            type = self.visit(ctx.var_type())
        else:
            type = None
        return VarDecl(varName=name, varType=type, varInit=None)


    # Visit a parse tree produced by MiniGoParser#prim_type.
    # prim_type: STRING | BOOL | INT | FLOAT;
    def visitPrim_type(self, ctx:MiniGoParser.Prim_typeContext):
        if ctx.STRING():
            return StringType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()


    # Visit a parse tree produced by MiniGoParser#var_type.
    # var_type: prim_type | array_type | ID;
    def visitVar_type(self, ctx:MiniGoParser.Var_typeContext):
        if ctx.prim_type():
            return self.visit(ctx.prim_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#const_decl.
    # const_decl: CONST ID (ASSIGN) (expr | num_expr) SEMI_COLON;
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        name = ctx.ID().getText()
        # expr = self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.num_expr())
        expr = self.visit(ctx.expr())
        return ConstDecl(conName=name, conType=None, iniExpr=expr)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    # func_decl:
	# FUNC ID R_OPEN (para_lst)? R_CLOSE (var_type)? block_func SEMI_COLON;
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        name = ctx.ID().getText()
        if ctx.var_type():
            returnType = self.visit(ctx.var_type())
        else:
            returnType = VoidType()
        params = self.visit(ctx.para_lst()) if ctx.para_lst() else []
        body = self.visit(ctx.block_func())
        return FuncDecl(name=name, params=params, retType=returnType, body=body)


    # Visit a parse tree produced by MiniGoParser#para_lst.
    # para_lst: para_mem COMMA para_lst | para_mem;
    def visitPara_lst(self, ctx:MiniGoParser.Para_lstContext):
        params = []
        param_mem = self.visit(ctx.para_mem())
        params.extend(param_mem)
        if ctx.para_lst():
            param_lst = self.visit(ctx.para_lst())
            params.extend(param_lst)
        return params


    # Visit a parse tree produced by MiniGoParser#para_mem.
    # para_mem: id_lst var_type;
    def visitPara_mem(self, ctx:MiniGoParser.Para_memContext):
        names = self.visit(ctx.id_lst())
        type = self.visit(ctx.var_type())
        type_lst = []
        for i in range(len(names)):
            elem = ParamDecl(parName=names[i], parType=type)
            type_lst.append(elem)
        return type_lst


    # Visit a parse tree produced by MiniGoParser#method_decl.
    # method_decl:
	# FUNC R_OPEN (method_receiver_lst) R_CLOSE 
    # ID (R_OPEN (para_lst)? R_CLOSE) (var_type)? block_func SEMI_COLON;
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        id1, id2 = self.visit(ctx.method_receiver_lst())
        func_name = ctx.ID().getText()
        
        if ctx.var_type():
            returnType = self.visit(ctx.var_type())
        else:
            returnType = VoidType()
            
        params = self.visit(ctx.para_lst()) if ctx.para_lst() else []
        body = self.visit(ctx.block_func())
        func_obj = FuncDecl(name=func_name, params=params, retType=returnType, body=body)
        
        return MethodDecl(receiver=id1, recType=id2, fun=func_obj)


    # Visit a parse tree produced by MiniGoParser#method_receiver_lst.
    # method_receiver_lst:
    # method_receiver_lst: method_receiver_mem;
    def visitMethod_receiver_lst(self, ctx:MiniGoParser.Method_receiver_lstContext):
        return self.visit(ctx.method_receiver_mem())


    # Visit a parse tree produced by MiniGoParser#method_receiver_mem.
    # method_receiver_mem: ID ID;
    def visitMethod_receiver_mem(self, ctx:MiniGoParser.Method_receiver_memContext):
        id1 = ctx.ID(0).getText()    
        id2 = Id(ctx.ID(1).getText()) 
        return (id1, id2)


    # Visit a parse tree produced by MiniGoParser#block_func.
    # block_func: CUR_OPEN block_func_lst? CUR_CLOSE;
    def visitBlock_func(self, ctx:MiniGoParser.Block_funcContext):
        if ctx.block_func_lst():
            member = self.visit(ctx.block_func_lst())
        else:
            member = []
        return Block(member)


    # Visit a parse tree produced by MiniGoParser#block_func_lst.
    # block_func_lst: block_func_mem block_func_lst | block_func_mem;
    def visitBlock_func_lst(self, ctx:MiniGoParser.Block_func_lstContext):
        members = []
        mem = self.visit(ctx.block_func_mem())
        members.append(mem)
        if ctx.block_func_lst():
            mem_lst = self.visit(ctx.block_func_lst())
            members.extend(mem_lst)
        return members


    # Visit a parse tree produced by MiniGoParser#block_func_mem.
    # block_func_mem: var_decl | const_decl | stmt_block;
    def visitBlock_func_mem(self, ctx:MiniGoParser.Block_func_memContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.stmt_block():
            return self.visit(ctx.stmt_block())


    # Visit a parse tree produced by MiniGoParser#stmt_block.
    # stmt_block: stmt | break_stmt | cont_stmt;
    def visitStmt_block(self, ctx:MiniGoParser.Stmt_blockContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.cont_stmt():
            return self.visit(ctx.cont_stmt())


    # Visit a parse tree produced by MiniGoParser#stmt.
    # stmt:
	# for_stmt | if_stmt | return_stmt | call_func | assign_stmt_semi | increase_stmt_semi;
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_func():
            return self.visit(ctx.call_func())
        elif ctx.assign_stmt_semi():
            return self.visit(ctx.assign_stmt_semi())
        elif ctx.increase_stmt_semi():
            return self.visit(ctx.increase_stmt_semi())


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    # for_stmt:
	# FOR (for_stmt_01 | for_stmt_02 | for_stmt_03) block_func SEMI_COLON;
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        block = self.visit(ctx.block_func())  # Wrap block properly

        if ctx.for_stmt_01():
            for_stmt_parts = self.visit(ctx.for_stmt_01())  # Returns a tuple (init, cond, update)
            return ForStep(init=for_stmt_parts[0], cond=for_stmt_parts[1], upda=for_stmt_parts[2], loop=block)
        
        elif ctx.for_stmt_02():
            index_var, value_var, array_expr = self.visit(ctx.for_stmt_02())
            return ForEach(idx=index_var, value=value_var, arr=array_expr, loop=block)

        elif ctx.for_stmt_03():
            cond_expr = self.visit(ctx.for_stmt_03())
            return ForBasic(cond=cond_expr, loop=block)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01.
    # for_stmt_01: for_stmt_01_init for_stmt_01_cond for_stmt_01_upda;
    def visitFor_stmt_01(self, ctx:MiniGoParser.For_stmt_01Context):
        init = self.visit(ctx.for_stmt_01_init())
        cond = self.visit(ctx.for_stmt_01_cond())
        upda = self.visit(ctx.for_stmt_01_upda())
        return (init, cond, upda)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_init.
    # Something not right here :) 
    # for_stmt_01_init: 
    # (for_stmt_01_upda SEMI_COLON) | for_stmt_01_var_decl_init;
    def visitFor_stmt_01_init(self, ctx:MiniGoParser.For_stmt_01_initContext):
        if ctx.for_stmt_01_upda():
            return self.visit(ctx.for_stmt_01_upda())
        elif ctx.for_stmt_01_var_decl_init():
            return self.visit(ctx.for_stmt_01_var_decl_init())


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_cond.
    # for_stmt_01_cond: (expr | num_expr) SEMI_COLON;
    def visitFor_stmt_01_cond(self, ctx:MiniGoParser.For_stmt_01_condContext):
        # return self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.num_expr())
        return self.visit(ctx.expr()) 


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_upda.
    # for_stmt_01_upda: (for_stmt_01_upda_incr | for_stmt_01_assign);
    def visitFor_stmt_01_upda(self, ctx:MiniGoParser.For_stmt_01_updaContext):
        if ctx.for_stmt_01_upda_incr():
            return self.visit(ctx.for_stmt_01_upda_incr())
        elif ctx.for_stmt_01_assign():
            return self.visit(ctx.for_stmt_01_assign())


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_var_decl_init.
    # for_stmt_01_var_decl_init:
	# VAR ID (var_type)? ASSIGN (expr | num_expr) SEMI_COLON;
    def visitFor_stmt_01_var_decl_init(self, ctx:MiniGoParser.For_stmt_01_var_decl_initContext):
        name = ctx.ID().getText()
        if ctx.var_type():
            type = self.visit(ctx.var_type())
        else:
            type = None
        # init = self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.num_expr())
        init = self.visit(ctx.expr()) 
        return VarDecl(varName=name, varType=type, varInit=init)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_upda_incr.
    # for_stmt_01_upda_incr:
	# ID (ADDVAL | SUBVAL | MULVAL | DIVVAL | MODVAL) expr;
    def visitFor_stmt_01_upda_incr(self, ctx:MiniGoParser.For_stmt_01_upda_incrContext):
        lhs = Id(ctx.ID().getText())
        op = None
        
        if ctx.ADDVAL():
            op = ctx.ADDVAL().getText()
        elif ctx.SUBVAL():
            op = ctx.SUBVAL().getText()
        elif ctx.MULVAL():
            op = ctx.MULVAL().getText()
        elif ctx.DIVVAL():
            op = ctx.DIVVAL().getText()
        elif ctx.MODVAL():
            op = ctx.MODVAL().getText()
        
        if op == "+=": op = "+"
        elif op == "-=": op = "-"
        elif op == "*=": op = "*"
        elif op == "/=": op = "/"
        elif op == "%=": op = "%"
        
        rhs = self.visit(ctx.expr())
        
        obj_rhs = BinaryOp(op, lhs, rhs)
        
        return Assign(lhs=lhs, rhs=obj_rhs)


    # Visit a parse tree produced by MiniGoParser#for_stmt_01_assign.
    # for_stmt_01_assign: ID (NEWASS) expr;
    def visitFor_stmt_01_assign(self, ctx:MiniGoParser.For_stmt_01_assignContext):
        lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        return Assign(lhs=lhs, rhs=rhs)


    # Visit a parse tree produced by MiniGoParser#for_stmt_02.
    # for_stmt_02:
	# ID COMMA ID NEWASS RANGE (expr);
    def visitFor_stmt_02(self, ctx:MiniGoParser.For_stmt_02Context):
        idx_var = Id(ctx.ID(0).getText())  # Extract first ID
        value_var = Id(ctx.ID(1).getText())  # Extract second ID
        arr_expr = self.visit(ctx.expr())
        
        return (idx_var, value_var, arr_expr)  # Return as tuple


    # Visit a parse tree produced by MiniGoParser#for_stmt_03.
    # for_stmt_03: expr | num_expr;
    def visitFor_stmt_03(self, ctx:MiniGoParser.For_stmt_03Context):
        # return self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.num_expr())
        return self.visit(ctx.expr()) 


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    # if_stmt: if_stmt_rec SEMI_COLON;
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visit(ctx.if_stmt_rec())


    # Visit a parse tree produced by MiniGoParser#if_stmt_rec.
    # if_stmt_rec: (if_stmt_type1 | if_stmt_type2);
    def visitIf_stmt_rec(self, ctx: MiniGoParser.If_stmt_recContext):
        if ctx.if_stmt_type1():
            return self.visit(ctx.if_stmt_type1())  # Returns a list of `(expr, block_func)`
        elif ctx.if_stmt_type2():
            return self.visit(ctx.if_stmt_type2()) 
        

    # Visit a parse tree produced by MiniGoParser#if_stmt_type1.
    # if_stmt_type1:
	# IF R_OPEN (expr | num_expr) R_CLOSE block_func else_stmt;
    # Like NHP Spec
    def visitIf_stmt_type1(self, ctx:MiniGoParser.If_stmt_type1Context):
        # condition = self.visit(ctx.expr() or ctx.num_expr())
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block_func())
        else_block = self.visit(ctx.else_stmt())
        return If(expr=condition, thenStmt=block, elseStmt=else_block)


    # Visit a parse tree produced by MiniGoParser#if_stmt_type2.
    # if_stmt_type2: IF R_OPEN (expr | num_expr) R_CLOSE block_func;
    def visitIf_stmt_type2(self, ctx:MiniGoParser.If_stmt_type2Context):
        # condition = self.visit(ctx.expr() or ctx.num_expr())
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.block_func())
        return If(expr=condition, thenStmt=block, elseStmt=None)
    

    # Visit a parse tree produced by MiniGoParser#else_stmt.
    # else_stmt: ELSE (if_stmt_rec | block_func);
    # Like NHP Spec
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        if ctx.if_stmt_rec():
            return self.visit(ctx.if_stmt_rec())
        elif ctx.block_func():
            return self.visit(ctx.block_func())


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    # break_stmt: BREAK SEMI_COLON;
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#cont_stmt.
    # cont_stmt: CONTINUE SEMI_COLON;
    def visitCont_stmt(self, ctx:MiniGoParser.Cont_stmtContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    # return_stmt: RETURN (expr | num_expr)? SEMI_COLON;
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        # elif ctx.num_expr():
        #     return Return(self.visit(ctx.num_expr()))
        else:
            return Return(None)


    # Visit a parse tree produced by MiniGoParser#call_func.
    # call_func: 
    # ( ID method_args? array_access? property_chain? POINT func_call
	# | func_call ) SEMI_COLON;
    def visitCall_func(self, ctx:MiniGoParser.Call_funcContext):
        if ctx.ID():
            name = Id(ctx.ID().getText())
            if ctx.method_args():
                args = self.visit(ctx.method_args())
                name = FuncCall(funName=name, args=args)
            if ctx.array_access():
                indexes = self.visit(ctx.array_access())
                if type(name) == str:
                    temp = Id(name)
                    temp = ArrayCell(arr=temp, idx=indexes)
                    name = temp
                else:
                    name = ArrayCell(arr=name, idx=indexes)
                    
            if ctx.property_chain():
                attrs = self.visit(ctx.property_chain())
                
                for attr in attrs:
                    field = attr["field"]
                    idx = attr["array_idx"]
                    method_args = attr["method_args"]
                    
                    if method_args is not None and idx:
                        name = MethCall(receiver=name, metName=field, args=method_args)
                        name = ArrayCell(arr=name, idx=idx)
                    elif idx:
                        name = FieldAccess(receiver=name, field=field)
                        name = ArrayCell(arr=name, idx=idx)
                    elif field:
                        name = FieldAccess(receiver=name, field=field)
            
            func_call = self.visit(ctx.func_call())
            
            return MethCall(receiver=name, metName=func_call.funName, args=func_call.args)
        else:
            return self.visit(ctx.func_call())


    # Visit a parse tree produced by MiniGoParser#func_call.
    # func_call: ID method_args;
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.method_args())
        return FuncCall(funName=name, args=args)


    # Visit a parse tree produced by MiniGoParser#assign_stmt_semi.
    # assign_stmt_semi: assign_stmt SEMI_COLON;
    def visitAssign_stmt_semi(self, ctx:MiniGoParser.Assign_stmt_semiContext):
        return self.visit(ctx.assign_stmt())


    # Visit a parse tree produced by MiniGoParser#assign_stmt.
    # assign_stmt: lhs_expr (NEWASS) expr;
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs_expr())
        rhs = self.visit(ctx.expr())
        return Assign(lhs, rhs)


    # Visit a parse tree produced by MiniGoParser#increase_stmt.
    # lhs (ADDVAL | SUBVAL | MULVAL | DIVVAL | MODVAL) expr;
    # Note attribute_chain return: List( {field, array_idx} ... )
    def visitIncrease_stmt(self, ctx:MiniGoParser.Increase_stmtContext):
        # print("visitIncrease_stmt")
        lhs = self.visit(ctx.lhs_expr())
        
        if ctx.ADDVAL():
            op = ctx.ADDVAL().getText()
            op = "+"
        elif ctx.SUBVAL():
            op = ctx.SUBVAL().getText()
            op = "-"
        elif ctx.MULVAL():
            op = ctx.MULVAL().getText()
            op = "*"
        elif ctx.DIVVAL():
            op = ctx.DIVVAL().getText()
            op = "/"
        elif ctx.MODVAL():
            op = ctx.MODVAL().getText()
            op = "%"
        
        rhs = self.visit(ctx.expr())
        op_rhs = BinaryOp(op, lhs, rhs)
        
        return Assign(lhs=lhs, rhs=op_rhs)    


    # Visit a parse tree produced by MiniGoParser#increase_stmt_semi.
    # increase_stmt_semi: increase_stmt SEMI_COLON;
    def visitIncrease_stmt_semi(self, ctx:MiniGoParser.Increase_stmt_semiContext):
        return self.visit(ctx.increase_stmt())


    # Visit a parse tree produced by MiniGoParser#expr_list.
    # expr_list: expr COMMA expr_list | expr;
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        if ctx.expr_list():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())
        else:
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by MiniGoParser#expr.
    # expr: expr OR expr1 | expr1;
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        # print("visitExpr OR")
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visit(ctx.expr())
            right = self.visit(ctx.expr1())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#expr1.
    # expr1: expr1 AND expr2 | expr2;
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        # print("visitExpr1 AND")
        if ctx.AND():
            op = op = ctx.AND().getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr2())


    # Visit a parse tree produced by MiniGoParser#expr2.
    # expr2: expr2 comp_op expr3 | expr3;
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        # print("visitExpr2 comp_op")
        if ctx.comp_op():
            op = self.visit(ctx.comp_op())
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr3())


    # Visit a parse tree produced by MiniGoParser#comp_op.
    # comp_op: EQ | NEQ | LT | LTE | GT | GTE;
    def visitComp_op(self, ctx:MiniGoParser.Comp_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#expr3.
    # expr3: expr3 add_op expr4 | expr4;
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        # print("visitExpr3 add_op")
        if ctx.add_op():
            op = self.visit(ctx.add_op())
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr4())


    # Visit a parse tree produced by MiniGoParser#add_op.
    # add_op: ADD | SUB;
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#expr4.
    # expr4: expr4 mul_op expr5 | expr5;
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        # print("visitExpr4 mul_op")
        if ctx.mul_op():
            op = self.visit(ctx.mul_op())
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr5())


    # Visit a parse tree produced by MiniGoParser#mul_op.
    # mul_op: MUL | DIV | MOD;
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#expr5.
    # expr5: unary_op expr5 | expr6;
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        # print("visitExpr5 unary_op")
        if ctx.unary_op():
            op = self.visit(ctx.unary_op())
            expr = self.visit(ctx.expr5())
            return UnaryOp(op, expr)
        else:
            return self.visit(ctx.expr6())


    # Visit a parse tree produced by MiniGoParser#unary_op.
    # unary_op: NEGATION | SUB;
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#expr6.
    # old
    # expr6: expr7 expr6_postfix_lst?;
    # new
    # expr6: expr6 expr6_postfix_lst | expr7;
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        # print("visitExpr6")
        if ctx.expr7():
            return self.visit(ctx.expr7())
        else:
            base_expr = self.visit(ctx.expr6())
            
            # list of expr6_postfix_mem
            # List( {field, args, idx}, {field, args, idx} ...)
            # nếu có field thì hong có idx và reverse
            if ctx.expr6_postfix_lst(): 
                store = self.visit(ctx.expr6_postfix_lst())
                temp = base_expr
                
                for i in range(len(store)):
                    field = store[i]["field"]
                    args = store[i]["args"]
                    idx_tmp = store[i]["idx"]
                    
                    if field and args != None:
                        base_expr = MethCall(receiver=temp, metName=field, args=args)
                    elif field and (not args):
                        base_expr = FieldAccess(receiver=temp, field=field)
                    elif idx_tmp:
                        # base_expr = ArrayCell(arr=base_expr, idx=[idx_tmp])
                        if type(base_expr) == ArrayCell:
                            base_expr = ArrayCell(arr=base_expr.arr, idx=base_expr.idx + [idx_tmp])
                        # not this case
                        else:
                            base_expr = ArrayCell(arr=base_expr, idx=[idx_tmp])
                    
                    temp = base_expr
            return base_expr


    # Visit a parse tree produced by MiniGoParser#expr6_postfix_lst.
    # expr6_postfix_lst:
	# expr6_postfix_mem expr6_postfix_lst
	# | expr6_postfix_mem;
    def visitExpr6_postfix_lst(self, ctx:MiniGoParser.Expr6_postfix_lstContext):
        # print("visitExpr6_postfix_lst")
        if ctx.expr6_postfix_lst():
            return [self.visit(ctx.expr6_postfix_mem())] + self.visit(ctx.expr6_postfix_lst())
        else:
            return [self.visit(ctx.expr6_postfix_mem())]


    # Visit a parse tree produced by MiniGoParser#expr6_postfix_mem.
    # expr6_postfix_mem:
	# POINT ID
	# | POINT ID method_args
	# | array_index;
    def visitExpr6_postfix_mem(self, ctx:MiniGoParser.Expr6_postfix_memContext):
        # print("visitExpr6_postfix_mem")
        field = None
        args = None
        idx = None
        
        if ctx.ID():
            # print("has ID")
            field = ctx.ID().getText()
            if ctx.method_args():
                # print("has method_args")
                args = self.visit(ctx.method_args())
                
        elif ctx.array_index():
            # print("has array_index")
            idx = self.visit(ctx.array_index())
        
        return {"field": field, "args": args, "idx": idx}


    # Visit a parse tree produced by MiniGoParser#method_args.
    # method_args: R_OPEN expr_list? R_CLOSE;
    # when have this, sure that u now have MethCall
    def visitMethod_args(self, ctx:MiniGoParser.Method_argsContext):
        # print("visitMethod_args")
        if ctx.expr_list():
            return self.visit(ctx.expr_list())
        elif ctx.R_OPEN() and ctx.R_CLOSE():
            return []
        else:
            return None


    # Visit a parse tree produced by MiniGoParser#expr7.
    # expr7:
	# TRUE | FALSE | NIL 
    # | num_expr array_access? | FLOAT_LIT 
    # | STRING_LIT | func_call | R_OPEN expr R_CLOSE;
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        # print("visitExpr7")
        if ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            text = ctx.STRING_LIT().getText()
            return StringLiteral(text) 
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.R_OPEN() and ctx.R_CLOSE():
            return self.visit(ctx.expr())
        elif ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            return IntLiteral(int(text, base=0))
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        

    # Visit a parse tree produced by MiniGoParser#array_access.
    # array_access: 
    # array_index array_access?;
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        idx = self.visit(ctx.array_index())
        if ctx.array_access():
            return [idx] + self.visit(ctx.array_access())
        else:
            return [idx]


    # Visit a parse tree produced by MiniGoParser#array_index.
    # array_index: SQ_OPEN expr SQ_CLOSE;
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MiniGoParser#attribute_chain.
    # attribute_chain: 
    # POINT ID array_access? attribute_chain?;
    # need this to give us: List( {field, array_idx} ... )
    def visitAttribute_chain(self, ctx:MiniGoParser.Attribute_chainContext):
        field = ctx.ID().getText()
        array_idx = []
        
        if ctx.array_access():
            array_idx = self.visit(ctx.array_access())
        if ctx.attribute_chain():
            return [{"field": field, "array_idx": array_idx}] + self.visit(ctx.attribute_chain())
        
        return [{"field": field, "array_idx": array_idx}]
        
            
    # Visit a parse tree produced by MiniGoParser#lhs_expr.
    # lhs_expr: 
    # ID array_access? attribute_chain?;
    def visitLhs_expr(self, ctx:MiniGoParser.Lhs_exprContext):
        lhs = Id(ctx.ID().getText())
        if ctx.array_access():
            indexes = self.visit(ctx.array_access())
            lhs = ArrayCell(arr=lhs, idx=indexes)
        
        # attribute_chain give us: List( {field, array_idx} ... )
        if ctx.attribute_chain():
            field_idx_attr = self.visit(ctx.attribute_chain())
            
            for i in range(len(field_idx_attr)):
                field = field_idx_attr[i]["field"]
                idx = field_idx_attr[i]["array_idx"]
                
                lhs = FieldAccess(receiver=lhs, field=field)
                if idx:
                    lhs = ArrayCell(arr=lhs, idx=idx)
                
        return lhs


    # Visit a parse tree produced by MiniGoParser#property_chain.
    # property_chain:
	# POINT ID property_chain?
	# | POINT ID array_access property_chain?
	# | POINT ID (method_args array_access) property_chain?;
    def visitProperty_chain(self, ctx:MiniGoParser.Property_chainContext):
        field = ctx.ID().getText()
        array_idx = [] # list of idx
        method_args = None # list of arguments
        
        if ctx.method_args():
            method_args = self.visit(ctx.method_args())
        
        if ctx.array_access():
            array_idx = self.visit(ctx.array_access())

        if ctx.property_chain():
            property_chain_lst = self.visit(ctx.property_chain())
            return [{"field": field, "array_idx": array_idx, "method_args": method_args}] + property_chain_lst
        
        return [{"field": field, "array_idx": array_idx, "method_args": method_args}]
    
# 2252621
# Nguyen Quang Phu
# 2252621
# Nguyen Quang Phu