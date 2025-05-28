# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        
        self.lst_type = []
        self.lst_function = []
        
        self.global_envi = [
            [
                Symbol("getInt",MType([],IntType())),
                Symbol("putInt",MType([IntType()],VoidType())),
                Symbol("putIntLn",MType([IntType()],VoidType())),
                
                Symbol("getFloat",MType([],FloatType())),
                Symbol("putFloat",MType([FloatType()],VoidType())),
                Symbol("putFloatLn",MType([FloatType()],VoidType())),
                
                Symbol("getBool",MType([],BoolType())),
                Symbol("putBool",MType([BoolType()],VoidType())),
                Symbol("putBoolLn",MType([BoolType()],VoidType())),
                
                Symbol("getString",MType([],StringType())),
                Symbol("putString",MType([StringType()],VoidType())),
                Symbol("putStringLn",MType([StringType()],VoidType())),
                
                Symbol("putLn",MType([],VoidType())),
            ]
        ]
        self.function_current: FuncDecl = None
        self.struct_current: StructType = None
        self.is_call_stmt = False  # New flag to track call context
        self.dict_struct = {} # key = name, elements = list of names and methods
    
    def check(self): 
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        # print("================================")
        # print(f"\nI am at the start at the Program\n")
        self.helper_debug(c)
        self.helper_debug([self.lst_function])
        self.helper_debug([self.lst_type])
        
        # First pass: Collect types and functions
        list_str = ["getInt", "putInt", "putIntLn", "getFloat", "putFloat", "putFloatLn",
                    "getBool", "putBool", "putBoolLn", "getString", "putString", "putStringLn", "putLn"]
        
        # Second pass: Process all declarations, including variables/constants and method bodies
        for decl in ast.decl:
            # print(list_str)
            if isinstance(decl, StructType):
                # print("struct")
                if decl.name in list_str:
                    raise Redeclared(Type(), decl.name)
                list_str.append(decl.name)
            elif isinstance(decl, InterfaceType):
                # print("interface")
                if decl.name in list_str:
                    raise Redeclared(Type(), decl.name)
                list_str.append(decl.name)
            elif isinstance(decl, FuncDecl):
                # print("func")
                if decl.name in list_str:
                    raise Redeclared(Function(), decl.name)
                list_str.append(decl.name)
            elif isinstance(decl, VarDecl):
                # print("var")
                if decl.varName in list_str:
                    raise Redeclared(Variable(), decl.varName)
                list_str.append(decl.varName)
            elif isinstance(decl, ConstDecl):
                # print("const")
                if decl.conName in list_str:
                    raise Redeclared(Constant(), decl.conName)
                list_str.append(decl.conName)
            
            # print("----------------------")
            self.helper_debug(c)
            # self.helper_debug([self.lst_function])
            # self.helper_debug([self.lst_type])
            
        def visitMethodDeclLocal(ast, c):
            # print("visitMethodDeclLocal")
            # print(f"check method {ast.fun.name}")
            struct = self.lookup(ast.recType.name, self.lst_type, lambda x: x.name)
            if not struct or not isinstance(struct, StructType):
                # print("No struct defined before method")
                # print(ast)
                if ast.recType.name not in self.dict_struct:
                    self.dict_struct[ast.recType.name] = [ast]
                else:
                    self.dict_struct[ast.recType.name].append(ast)
                return ast
            
            # here the struct already appear, check if any method appears before the struct, if yes
            lst_for_check = [x.fun.name for x in struct.methods] + [x[0] for x in struct.elements]
            if self.lookup(ast.fun.name, lst_for_check, lambda x: x):
                # print("Redeclare with the methods")
                raise Redeclared(Method(), ast.fun.name)
            
            struct.methods.append(ast)
            return ast
        
        # First pass: Collect types and functions (global scope throughout program)
        for decl in ast.decl:
            if isinstance(decl, StructType):
                if self.lookup(decl.name, self.lst_type, lambda x: x.name):
                    raise Redeclared(Type(), decl.name)
                self.lst_type.append(decl)
            elif isinstance(decl, InterfaceType):
                if self.lookup(decl.name, self.lst_type, lambda x: x.name):
                    raise Redeclared(Type(), decl.name)
                self.lst_type.append(decl)
            elif isinstance(decl, FuncDecl):
                if self.lookup(decl.name, self.lst_function, lambda x: x.name):
                    raise Redeclared(Function(), decl.name)
                self.lst_function.append(decl)
            # print("----------------------")
            self.helper_debug(c)
            self.helper_debug([self.lst_function])
            self.helper_debug([self.lst_type])
            # print("----------------------")
        
        # Then visit types
        for decl in ast.decl:
            if isinstance(decl, StructType):
                res = self.visit(decl, c)
                c[0].append(res)
                # print(f"Struct {res.name} added to global env")
                # print(f"res: {res}")
                # print("----------------------")
                self.helper_debug(c)
                self.helper_debug([self.lst_function])
                self.helper_debug([self.lst_type])
            elif isinstance(decl, InterfaceType):
                res = self.visit(decl, c)
                c[0].append(res)
                # print(f"Interface {res.name} added to global env")
                # print(f"res: {res}")
                # print("----------------------")
                self.helper_debug(c)
                self.helper_debug([self.lst_function])
                self.helper_debug([self.lst_type])
            
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                visitMethodDeclLocal(decl, c)
        
        # print("================================")
        # print(f"\nI am at the after visit method decl at the Program\n")
        
        # append those predefine method before struct type
        for dict_struct_name in list(self.dict_struct.keys()):
            struct = self.lookup(dict_struct_name, self.lst_type, lambda x: x.name)
            if not struct or not isinstance(struct, StructType):
                raise Undeclared(Identifier(), dict_struct_name)
            
            for method in self.dict_struct[dict_struct_name]:
                # new
                lst_for_check = [x.fun.name for x in struct.methods] + [x[0] for x in struct.elements]
                if self.lookup(method.fun.name, lst_for_check, lambda x: x):
                    # print("Redeclare with the methods in visit struct type")
                    raise Redeclared(Method(), method.fun.name)
                
                struct.methods.append(method)
        
        self.helper_debug(c)
        self.helper_debug([self.lst_function])
        self.helper_debug([self.lst_type])
                
        # Second pass: Process all declarations, including variables/constants and method bodies
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                if self.lookup(decl.name, c[0], lambda x: x.name):
                    raise Redeclared(Function(), decl.name)
                func_sym = self.visit(decl, c)
                c[0].append(func_sym)  # Add function symbol to global env for calls
            elif isinstance(decl, VarDecl):
                if self.lookup(decl.varName, c[0], lambda x: x.name):
                    raise Redeclared(Variable(), decl.varName)
                var_sym = self.visit(decl, c)
                c[0].append(var_sym)
            elif isinstance(decl, ConstDecl):
                if self.lookup(decl.conName, c[0], lambda x: x.name):
                    raise Redeclared(Constant(), decl.conName)
                const_sym = self.visit(decl, c)
                c[0].append(const_sym)
            elif isinstance(decl, MethodDecl):
                self.visit(decl, c)
            
            # print("----------------------")
            # print("\nAfter Visit 2nd pass in program\n")
            self.helper_debug(c)
            # self.helper_debug([self.lst_function])
            # self.helper_debug([self.lst_type])
            
        return c
    
    def visitParamDecl(self, ast, c):
        if self.lookup(ast.parName, c, lambda x: x.name):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.varName, c[0], lambda x: x.name):
            raise Redeclared(Variable(), ast.varName)
        
        # Here we check type compatibility between the declared type and the initializer
        # Not recheck yet
        if ast.varInit:
            temp = self.is_call_stmt
            self.is_call_stmt = False
            
            init_type = self.visit(ast.varInit, c)
            init_type = self.resolve_type(init_type, c)
            # print(f"Init type of var {ast.varName}: {init_type}")
            
            value = None
            if isinstance(init_type, (IntType, FloatType)):
                try:
                    value = self.evaluate_ast(ast.varInit, c)
                    # print(f"value: {value}")
                except TypeMismatch:
                    pass  # Not a constant expression, value remains None
            
            if ast.varType:
                # self.visit(ast.varType, c) # added 9/4
                # print(f"Before Resolved var type: {ast.varType}")
                resolved_var_type = self.resolve_type(ast.varType, c)
                # print(f"Resolved var type: {resolved_var_type}")
                if isinstance(resolved_var_type, VoidType):
                    raise TypeMismatch(ast)
                
                if isinstance(resolved_var_type, ArrayType):
                    try:
                        self.visit(ast.varType, c) # added 9/4
                    except TypeMismatch:
                        raise TypeMismatch(ast.varType)
                    
                if not self.is_compatible(resolved_var_type, init_type):
                    raise TypeMismatch(ast)
                self.is_call_stmt = temp
                return Symbol(ast.varName, resolved_var_type, value)
            else:
                if isinstance(init_type, VoidType):
                    raise TypeMismatch(ast)
                self.is_call_stmt = temp
                return Symbol(ast.varName, init_type, value)
            
        if ast.varType:
            # new 9/4
            # print("In visitvardecl -> ast.vartype")
            # print(f"Before Resolved var type: {ast.varType}")
            resolved_var_type = self.resolve_type(ast.varType, c)
            # print(f"Resolved var type: {resolved_var_type}")
            
            if isinstance(resolved_var_type, VoidType):
                raise TypeMismatch(ast)
            
            if isinstance(resolved_var_type, ArrayType):
                # print("In visitvardecl -> ast.vartype -> arraytype")
                try:
                    resolved_var_type = self.visit(ast.varType, c) # added 9/4
                except TypeMismatch:
                    raise TypeMismatch(ast.varType)
                
            return Symbol(ast.varName, resolved_var_type)
        return Symbol(ast.varName, None)  # Untyped without initializer
    
    def visitConstDecl(self, ast, c ):
        if self.lookup(ast.conName, c[0], lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)
        
        self.is_call_stmt = False  # Expression context
        
        init_type = self.visit(ast.iniExpr, c)
        
        # print(f"Init type of const {ast.conName}: {init_type}")
        
        # added - eval 
        value = None
        # print(f"init_type: {init_type}")
        if isinstance(init_type, (IntType, FloatType)):
            try:
                value = self.evaluate_ast(ast.iniExpr, c)
                # print(f"value: {value}")
            except TypeMismatch:
                pass  # Not a constant expression, value remains None
        
        # original
        if ast.conType:
            resolved_con_type = self.resolve_type(ast.conType, c)
            if isinstance(resolved_con_type, VoidType):
                raise TypeMismatch(ast.iniExpr)
            
            if isinstance(resolved_con_type, ArrayType):
                try:
                    resolved_con_type = self.visit(ast.conType, c) # added 9/4
                except TypeMismatch:
                    raise TypeMismatch(ast.conType)
            
            if not self.is_compatible(resolved_con_type, init_type):
                raise TypeMismatch(ast.iniExpr)
            return Symbol(ast.conName, resolved_con_type, value)
        return Symbol(ast.conName, init_type, value)
   
    def visitFuncDecl(self, ast, c ):
        self.function_current = ast
        
        # Create a separate scope for parameters and a local scope for the body
        param_list = []
        param_env = []  # Parameters go here
        local_env = [[]] + [param_env] + c  # [local, params, outer scopes]
        
        for param in ast.params:
            param_sym = self.visit(param, param_env)
            param_env.append(param_sym)
            param_list.append(param_sym.mtype)
        
        # print("Visit body of func decl")
        
        self.visit(ast.body, local_env)
        self.function_current = None
        
        # old
        return Symbol(ast.name, MType(param_list, ast.retType))
    
        # new 9/4: check if retType is arraytype and need to resolve
        # # print("ast.retType", ast.retType)
        # if isinstance(ast.retType, ArrayType):
        #     rettype = ast.retType
        #     rettype = self.visit(ast.retType, c)
        #     return Symbol(ast.name, MType(param_list, rettype))
        # else:
        #     # print("rettype", rettype)
        #     return Symbol(ast.name, MType(param_list, ast.retType))

    def visitStructType(self, ast, c):
        self.struct_current = ast
        field_env = []         # New environment to track fields
        method_env_local = []  # New environment to track methods
        
        method_before = []
        
        # print(f"I am checking the StructType {ast.name}")
        # print(f"dict struct: {self.dict_struct}")
        
        # check if any methods declare before struct type
        if ast.name in self.dict_struct:
            # print("THere is methods declare before struct type")
            for method in self.dict_struct[ast.name]:
                method_before.append(method.fun.name)
        
        for name, typ in ast.elements:
            # Check if the field type is valid
            temp_check = field_env + method_before
            # print(f"temp_check: {temp_check}")
            resolved_type = self.resolve_type(typ, c)
            
            if isinstance(typ, Id) and not isinstance(resolved_type, (StructType, InterfaceType)):
                # If typ is an Id and not resolved to a known struct/interface, it’s undeclared
                raise Undeclared(Identifier(), typ.name)
            elif not isinstance(resolved_type, (IntType, FloatType, BoolType, StringType, ArrayType, StructType, InterfaceType)):
                # If resolved type isn’t a valid type (including primitives), raise error
                raise Undeclared(Identifier(), str(typ))
            
            if self.lookup(name, temp_check, lambda x: x.name if isinstance(x, Symbol) else x):
                # Check if the field name is already declared in the field environment
                # If yes, raise redeclared error
                raise Redeclared(Field(), name)
            field_env.append(Symbol(name, typ))
          
        for method in ast.methods:
            method_decl = self.visit(method, c)
            
            # Check for redeclared method within the struct
            if self.lookup(method.fun.name, method_env_local, lambda x: x.fun.name):
                raise Redeclared(Method(), method.fun.name)
            method_env_local.append(method_decl)
            
        self.struct_current = None
        return ast

    def visitMethodDecl(self, ast, c):
        # print(f"I am checking the MethodDecl {ast.fun.name}")
        struct = self.lookup(ast.recType.name, self.lst_type, lambda x: x.name)
        if not struct or not isinstance(struct, StructType):
            raise Undeclared(Identifier(), ast.recType.name)
        
        self.function_current = ast.fun
        
        receiver_sym = Symbol(ast.receiver, StructType(struct.name, struct.elements, struct.methods))
        
        param_list = []
        param_env = []
        local_env = [[]] + [param_env] + [[receiver_sym]] + c
        
        # old 9/4
        param_list.append(receiver_sym)  # Optional: Include receiver type in param_list if needed
        
        for param in ast.fun.params:
            # Check if parameter name conflicts with receiver
            if self.lookup(param.parName, local_env[0], lambda x: x.name):
                raise Redeclared(Parameter(), param.parName)
            # Check if parameter is redeclared among parameters
            param_sym = self.visit(param, param_env)
            param_env.append(param_sym)
            param_list.append(param_sym.mtype)
        
        # print("Visit body of method decl")
        self.helper_debug(local_env)
        self.visit(ast.fun.body, local_env)
        self.function_current = None
        return ast
    
    def visitPrototype(self, ast, c):
        if self.lookup(ast.name, c, lambda x: x.name):
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast, c):
        method_env = []
        for proto in ast.methods:
            self.visit(proto, method_env)
            method_env.append(proto)
        return ast

    def visitForBasic(self, ast, c): 
        # Check that the condition is of boolean type
        self.is_call_stmt = False  # Expression context
        cond_type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        
        # print("Check in for basic")
        self.helper_debug(c)
        
        # Visit the loop body with the current environment
        self.visit(Block(ast.loop.member), c)
        
    def visitForStep(self, ast, c): 
        # print(f"Entering ForStep: {ast}")
        # Create a new scope for the initialization
        
        init_env = [[]] + c
        if isinstance(ast.init, VarDecl):
            init_sym = self.visit(ast.init, init_env)
            init_env[0].append(init_sym)
        else:
            self.visit(ast.init, init_env)
    
        # Create a new scope for the loop body that includes the init variables
        loop_env = [init_env[0].copy()] + c[1:]

        self.is_call_stmt = False  # Expression context
    
        # Check the condition with the loop environment
        cond_type = self.visit(ast.cond, loop_env)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
    
        # new 
        # print("I am here")
        self.visit(Block([ast.init] + [ast.upda] + ast.loop.member), c)
        
    def visitForEach(self, ast, c): 
        # print("I am here to check arr type")
        
        arr_type = self.visit(ast.arr, c)
        
        # old
        if not isinstance(arr_type, ArrayType):
            # raise TypeMismatch(ast.arr)
            raise TypeMismatch(ast)
        
        # print("DONE I am here to check arr type")
        
        # Determine the type of the idx variable (always IntType)
        idx_type = IntType()
        
        # Determine the type of the value variable
        if len(arr_type.dimens) == 1:
            # 1D array: value type is the element type
            value_type = arr_type.eleType
        else:
            # Multi-dimensional array: value type is an array with the remaining dimensions
            remaining_dims = arr_type.dimens[1:]
            value_type = ArrayType(remaining_dims, arr_type.eleType)
        
        # now new - 9/4
        # idx and value must define before 
        idx_name = None
        
        for scope in c:
            idx_name = self.lookup(ast.idx.name, scope, lambda x: x.name)
            if idx_name:
                break
        
        if ast.idx.name == "_":
            idx_name = "_"
        
        # print("idx_name", idx_name)
        # print("idx_type", idx_type)
        
        if not idx_name:
            raise Undeclared(Identifier(), ast.idx.name)
        elif ast.idx.name != "_" and not self.is_compatible(idx_name.mtype, idx_type, True):
            # print("idx_name", idx_name)
            # print("idx_name type", idx_name.mtype)
            raise TypeMismatch(ast) # 1 minh thg nay thi kh sai nhung bo vao for each sai
        
        value_name = None
        for scope in c:
            value_name = self.lookup(ast.value.name, scope, lambda x: x.name)
            if value_name:
                break
            
        if not value_name:
            raise Undeclared(Identifier(), ast.value.name)
        elif not self.is_compatible(value_name.mtype, value_type, True): # same type
            # print("value_name", value_name)
            # print("value_name type", value_name.mtype)
            raise TypeMismatch(ast)
        # print("I am here to check arr type")
        
        self.visit(Block(ast.loop.member), c)
        
    def visitBlock(self, ast, c):
        # print(f"Entering Block: {ast}")
        local_env = c
        
        # print("----------------")
        # print(f"Block initial env")
        self.helper_debug(local_env)
        
        for member in ast.member:
            if isinstance(member, VarDecl):
                if self.lookup(member.varName, local_env[0], lambda x: x.name):
                    raise Redeclared(Variable(), member.varName)
                sym = self.visit(member, local_env)
                local_env[0].append(sym)
            elif isinstance(member, ConstDecl):
                if self.lookup(member.conName, local_env[0], lambda x: x.name):
                    raise Redeclared(Constant(), member.conName)
                sym = self.visit(member, local_env)
                local_env[0].append(sym)
            elif isinstance(member, (ForStep, ForEach, ForBasic, If)):
                self.visit(member, [[]] + local_env)
            elif isinstance(member, (FuncCall, MethCall)):
                self.is_call_stmt = True
                self.visit(member, local_env)
                self.is_call_stmt = False
            elif isinstance(member, Assign):
                sym = self.visit(member, local_env)
                if sym:
                    local_env[0].append(sym)
            else:
                self.visit(member, local_env)
                
            # print("----------------")
            # print(f"Block curr env")
            self.helper_debug(local_env)
        
        # # print(f"Final initial env: {[str(sym) for sym in local_env[0]]}")
        # print("----------------")
        # print(f"Final initial env")
        self.helper_debug(local_env)
        
    def visitIf(self, ast, c): 
        self.is_call_stmt = False  # Expression context
        expr_type = self.visit(ast.expr, c)
        if not isinstance(expr_type, BoolType):
            raise TypeMismatch(ast)
        
        self.visit(Block(ast.thenStmt.member), c)
        
        if ast.elseStmt:
            # print("Let's visit Else block")
            self.visit(ast.elseStmt, [[]] + c)
    
    def visitIntType(self, ast, c): return IntType()
    def visitFloatType(self, ast, c): return FloatType()
    def visitBoolType(self, ast, c): return BoolType()
    def visitStringType(self, ast, c): return StringType()
    def visitVoidType(self, ast, c): return VoidType()
    
    def visitArrayType(self, ast, c): 
        # new code from here
        # Check each dimension to ensure it's either an Id or IntLiteral
        newdim = []
        for dim in ast.dimens:
            if not isinstance(dim, (IntLiteral, Id, BinaryOp, UnaryOp)):
                raise TypeMismatch(ast)
            
            # If it's an Id, try to evaluate it to ensure it's a valid constant
            if isinstance(dim, (IntLiteral, Id, BinaryOp, UnaryOp)):
                # print(f"dim: {dim}")
                try:
                    ele = self.evaluate_ast(dim, c)
                    if not isinstance(ele, int):
                        raise TypeMismatch(ast)
                    newdim.append(ele)
                except TypeMismatch:
                    raise TypeMismatch(ast)
                    # pass
            else:
                newdim.append(dim.value)
        
        # print(f"newdim: {newdim}")
        return ArrayType(newdim, ast.eleType)

    def visitAssign(self, ast, c):
        # Helper to check if Id appears in RHS
        def contains_id(expr, id_name):
            if isinstance(expr, Id):
                return expr.name == id_name
            if hasattr(expr, 'left') and hasattr(expr, 'right'):  # BinaryOp
                return contains_id(expr.left, id_name) or contains_id(expr.right, id_name)
            if hasattr(expr, 'body'):  # UnaryOp
                return contains_id(expr.body, id_name)
            if hasattr(expr, 'args'):  # FuncCall, MethCall
                return any(contains_id(arg, id_name) for arg in expr.args)
            if hasattr(expr, 'arr'):  # ArrayCell
                return contains_id(expr.arr, id_name) or any(contains_id(idx, id_name) for idx in expr.idx)
            if hasattr(expr, 'receiver'):  # FieldAccess
                return contains_id(expr.receiver, id_name)
            return False

        # Get RHS type first (for implicit declaration)
        self.is_call_stmt = False  # Expression context
        rhs_type = self.visit(ast.rhs, c)
        rhs_type = self.resolve_type(rhs_type, c)
        # print(f"visitassign->RHS type: {rhs_type}")

        # Check LHS
        if isinstance(ast.lhs, Id):
            lhs_sym = None
            for scope in c:
                lhs_sym = self.lookup(ast.lhs.name, scope, lambda x: x.name)
                if lhs_sym:
                    break
            
            if not lhs_sym:  # Undeclared
                # print("LHS is ID but undeclared")
                if contains_id(ast.rhs, ast.lhs.name):
                    raise Undeclared(Identifier(), ast.lhs.name)
                if not isinstance(rhs_type, VoidType):
                    c[0].append(Symbol(ast.lhs.name, rhs_type))
                    value = None
                    if isinstance(rhs_type, (IntType)):
                        try:
                            value = self.evaluate_ast(ast.rhs, c)
                        except TypeMismatch:
                            pass
                    return Symbol(ast.lhs.name, rhs_type, value)
                raise TypeMismatch(ast)
            else:
                # print("LHS is ID but declared")
                # Check if lhs_sym corresponds to a constant in the program’s declarations
                is_constant = False
                is_function = False
                for decl in self.ast.decl:  # self.ast is the Program AST
                    if isinstance(decl, ConstDecl) and decl.conName == ast.lhs.name:
                        is_constant = True
                        break
                    if isinstance(decl, FuncDecl) and decl.name == ast.lhs.name:
                        is_function = True
                        break
                    
                if is_function:
                    # 1) 0 cho phep che function 
                    # raise Redeclared(Variable(), ast.lhs.name) 
                    # 2) cho phep che function 
                    # print("LHS is function now bi che")
                    if not isinstance(rhs_type, VoidType):
                        c[0].append(Symbol(ast.lhs.name, rhs_type))
                        value = None
                        if isinstance(rhs_type, (IntType)):
                            try:
                                value = self.evaluate_ast(ast.rhs, c)
                            except TypeMismatch:
                                pass
                        return Symbol(ast.lhs.name, rhs_type, value)
                    raise TypeMismatch(ast)
                
                # Only update value if not a constant and not name of func
                if not is_constant:
                    init_type = self.visit(ast.rhs, c)
                    value = None
                    if isinstance(init_type, (IntType)):
                        try:
                            value = self.evaluate_ast(ast.rhs, c)
                            lhs_sym.value = value  # Update only for variables
                        except TypeMismatch:
                            pass

        lhs_type = self.visit(ast.lhs, c)
        if isinstance(lhs_type, VoidType):
            raise TypeMismatch(ast)
        if not self.is_compatible(lhs_type, rhs_type):
            raise TypeMismatch(ast)
        return None
    
    def visitContinue(self, ast, c): return None
    def visitBreak(self, ast, c): return None
    
    def visitReturn(self, ast, c): 
        if not self.function_current:
            return None
        
        # print("I am in the visit return")
        
        ret_type = self.function_current.retType
        ret_type = self.resolve_type(ret_type, c)
        
        if ast.expr:
            # print("I am checking exp in the visit return")
            
            self.is_call_stmt = False  # Expression context
            expr_type = self.visit(ast.expr, c)
            
            expr_type = self.resolve_type(expr_type, c)
            
            if isinstance(ret_type, VoidType):
                raise TypeMismatch(ast)
            
            # print("ret_type", ret_type)
            # print("expr_type", expr_type)  
            # print(type(ret_type) != type(expr_type))
            
            if not self.is_compatible(ret_type, expr_type, True):
                raise TypeMismatch(ast)
        elif not isinstance(ret_type, VoidType):
            raise TypeMismatch(ast)
        return None

    def visitBinaryOp(self, ast, c): 
        self.is_call_stmt = False  # Expression context
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)
        
        if isinstance(left_type, VoidType) or isinstance(right_type, VoidType):
            raise TypeMismatch(ast)
        
        if ast.op in ['+', '-', '*', '/', '%']:
            if ast.op == '+' and isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            if ast.op == '%' and isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()
            if ast.op == '%' and (isinstance(left_type, FloatType) or isinstance(right_type, FloatType)):
                raise TypeMismatch(ast)
            if not isinstance(left_type, (IntType, FloatType)) or not isinstance(right_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
        
        if ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            if (isinstance(left_type, IntType) and isinstance(right_type, IntType)) or \
               (isinstance(left_type, FloatType) and isinstance(right_type, FloatType)) or \
               (isinstance(left_type, StringType) and isinstance(right_type, StringType)):
                return BoolType()
            else:
                raise TypeMismatch(ast)
            
        if ast.op in ['&&', '||']:
            if not isinstance(left_type, BoolType) or not isinstance(right_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()
        
        raise TypeMismatch(ast)
    
    def visitUnaryOp(self, ast, c): 
        self.is_call_stmt = False  # Expression context
        body_type = self.visit(ast.body, c)
        
        if ast.op == '!':
            if not isinstance(body_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()
        
        if ast.op == '-':
            if not isinstance(body_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            return body_type
        
        raise TypeMismatch(ast)
    
    def visitFuncCall(self, ast, c):
        # original - Look up the function in self.lst_function (stores FuncDecl)
        func_decl = self.lookup(ast.funName, self.lst_function, lambda x: x.name)
        
        if not func_decl:
            # Fallback: Check scopes for a Symbol (e.g., a function passed as a variable, if applicable)
            func_sym = None
            for scope in c:
                func_sym = self.lookup(ast.funName, scope, lambda x: x.name)
                if func_sym:
                    break
                
            # print(f"func_sym: {func_sym}")
            # print(f"func_decl: {func_decl}")
            
            if func_sym and isinstance(func_sym.mtype, MType):
                func_mtype = func_sym.mtype
            elif not func_sym or not isinstance(func_sym.mtype, MType):
                raise Undeclared(Function(), ast.funName)
            else:
                raise TypeMismatch(ast)  # If found but not an MType
        else:
            # new - 11/4
            if len(c) > 1:
                # 11/4
                func_sym = None
                for scope in c[0:len(c)-1]:
                    func_sym = self.lookup(ast.funName, scope, lambda x: x.name)
                    if func_sym:
                        break
                
                if func_sym:
                    raise Undeclared(Function(), ast.funName)
                
            # Construct MType from FuncDecl
            param_types = [param.parType for param in func_decl.params]
            func_mtype = MType(param_types, func_decl.retType)

        # Check number of arguments
        if len(func_mtype.partype) != len(ast.args):
            raise TypeMismatch(ast)
        
        # Check argument types
        temp = self.is_call_stmt
        for param_type, arg in zip(func_mtype.partype, ast.args):
            self.is_call_stmt = False  # Arguments are expressions
            
            arg_type = self.visit(arg, c)
            arg_type = self.resolve_type(arg_type, c)
            
            param_type = self.resolve_type(param_type, c)
            
            if not self.is_compatible(param_type, arg_type, True):
                raise TypeMismatch(ast)
            
        self.is_call_stmt = temp
        
        # Check return type based on context (statement or expression)
        rettype = func_mtype.rettype
        
        # print("Return type:", rettype)
        # print("Is call stmt:", self.is_call_stmt)
        if self.is_call_stmt and not isinstance(rettype, VoidType):
            # print("1st if")
            raise TypeMismatch(ast)
        # do this, i think not
        if not self.is_call_stmt and isinstance(rettype, VoidType):
            # print("2nd if")
            raise TypeMismatch(ast)
        
        return rettype

    def visitMethCall(self, ast, c):
        temp = self.is_call_stmt
        
        self.is_call_stmt = False  # Receiver is an expression
        receiver_type = self.visit(ast.receiver, c)
        # print(f"Receiver type: {receiver_type}")
        receiver_type = self.resolve_type(receiver_type, c)
        # print(f"Resolved receiver type: {receiver_type}")
        
        self.is_call_stmt = temp
        
        if isinstance(receiver_type, StructType):
            struct = self.lookup(receiver_type.name, self.lst_type, lambda x: x.name)
            if not struct:
                raise Undeclared(Identifier(), receiver_type.name)
            
            method = self.lookup(ast.metName, struct.methods, lambda x: x.fun.name)
            if not method:
                raise Undeclared(Method(), ast.metName)
                
            if len(method.fun.params) != len(ast.args):
                raise TypeMismatch(ast)
            
            temp = self.is_call_stmt
            for param, arg in zip(method.fun.params, ast.args):
                self.is_call_stmt = False  # Arguments are expressions
                arg_type = self.visit(arg, c)
                
                # new 9/4
                if not hasattr(param, 'parType'):
                    if not self.is_compatible(param, arg_type):
                        raise TypeMismatch(ast)
                    
                elif not self.is_compatible(param.parType, arg_type):
                    raise TypeMismatch(ast)
                
            self.is_call_stmt = temp
                    
            # added for check is_stmt or not
            rettype = method.fun.retType
            
            if self.is_call_stmt and not isinstance(rettype, VoidType):
                # print("Method call (rcv struct) is a statement but the method does not return void")
                raise TypeMismatch(ast)
            if not self.is_call_stmt and isinstance(rettype, VoidType):
                # print("Method call (rcv struct) is an expression but the method returns void")
                raise TypeMismatch(ast)
            return rettype
        
        # added
        if isinstance(receiver_type, InterfaceType):
            interface = self.lookup(receiver_type.name, self.lst_type, lambda x: x.name)
            if not interface:
                raise Undeclared(Identifier(), receiver_type.name)
            
            method = self.lookup(ast.metName, interface.methods, lambda x: x.name)
            if not method:
                raise Undeclared(Method(), ast.metName)
                
            if len(method.params) != len(ast.args):
                raise TypeMismatch(ast)
            
            temp = self.is_call_stmt
            for param, arg in zip(method.params, ast.args):
                self.is_call_stmt = False  # Arguments are expressions
                arg_type = self.visit(arg, c)
                
                # new 9/4
                if not hasattr(param, 'parType'):
                    if not self.is_compatible(param, arg_type):
                        raise TypeMismatch(ast)
                    
                elif not self.is_compatible(param.parType, arg_type):
                    raise TypeMismatch(ast)
                
            self.is_call_stmt = temp
            
            # added for check is_stmt or not        
            rettype = method.retType
            if self.is_call_stmt and not isinstance(rettype, VoidType):
                # print("Method call (rcv interface) is a statement but the method does not return void")
                raise TypeMismatch(ast)
            if not self.is_call_stmt and isinstance(rettype, VoidType):
                # print("Method call (rcv interface) is an expression but the method returns void")
                raise TypeMismatch(ast)
            return rettype
            
        raise TypeMismatch(ast)
    
    def visitId(self, ast, c): 
        # print("Checking ID in visit ID")
        for scope in c:
            sym = self.lookup(ast.name, scope, lambda x: x.name)
            # print(f"ID found in scope: {sym}")
            if sym and (isinstance(sym, StructType) or isinstance(sym, InterfaceType)):
                continue # old 
            elif sym:
                return sym.mtype  
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self, ast, c):
        self.is_call_stmt = False  # Expression context
        array_type = self.visit(ast.arr, c)
        
        # print("visitArrayCell")
        # print(f"Array type: {array_type}")
        
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
        
        # Check that all indices are IntType using map
        if not all(map(lambda item: isinstance(self.visit(item, c), IntType), ast.idx)):
            raise TypeMismatch(ast)
        
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            remaining_dims = array_type.dimens[len(ast.idx):]
            return ArrayType(remaining_dims, array_type.eleType)
        
        raise TypeMismatch(ast)
    
    def visitFieldAccess(self, ast, c):
        self.is_call_stmt = False
        receiver_type = self.visit(ast.receiver, c)
        
        # print("visitFieldAccess")
        # print(f"Receiver type: {receiver_type}")
        
        # Resolve receiver type if it's an Id (e.g., from a previous FieldAccess or Id)
        if isinstance(receiver_type, Id):
            resolved = self.lookup(receiver_type.name, self.lst_type, lambda x: x.name)
            if not resolved or not isinstance(resolved, StructType):
                raise Undeclared(Identifier(), receiver_type.name)
            receiver_type = resolved
        
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)
        
        struct = self.lookup(receiver_type.name, self.lst_type, lambda x: x.name)
        if not struct:
            raise Undeclared(Identifier(), receiver_type.name)
        
        field = self.lookup(ast.field, struct.elements, lambda x: x[0])
        
        # print(f"Field: {field}")
        if not field:
            raise Undeclared(Field(), ast.field)
        
        # Resolve the field type if it's an Id (e.g., Meow1)
        field_type = field[1]
        if isinstance(field_type, Id):
            resolved_field_type = self.lookup(field_type.name, self.lst_type, lambda x: x.name)
            if not resolved_field_type or not isinstance(resolved_field_type, StructType):
                raise Undeclared(Identifier(), field_type.name)
            return resolved_field_type
        return field_type
    
    def visitIntLiteral(self, ast, c): return IntType()
    def visitFloatLiteral(self, ast, c): return FloatType()
    def visitBooleanLiteral(self, ast, c): return BoolType()
    
    def visitStringLiteral(self, ast, c): return StringType()
    
    def visitArrayLiteral(self, ast, c):
        # print("Visit arr lit")
        if not ast.value:
            return ArrayType(ast.dimens, ast.eleType)

        def collect_leaves(dat, dims, current_depth):
            # Base case: no dimensions left, dat should be a leaf node
            if not dims:
                if isinstance(dat, list):
                    raise TypeMismatch(ast)  # Too much nesting
                return [dat]

            # Recursive case: dat must be a list matching the current dimension
            if not isinstance(dat, list):
                pass # new 9/4

            # Evaluate the current dimension - new 9/4
            dim_val = None
            try:
                dim_val = self.evaluate_ast(dims[0], c) if isinstance(dims[0], (IntLiteral, Id, BinaryOp, UnaryOp)) else dims[0].value
            except TypeMismatch:
                raise TypeMismatch(ast)
            
            # print(f"Dim val: {dim_val}")
            # print(f"len(dat): {len(dat)}")
            
            # Recursively collect leaves from the next level of nesting
            leaves = []
            if isinstance(dat, list):
                for value in dat:
                    leaves.extend(collect_leaves(value, dims[1:], current_depth + 1))
            return leaves

        # print("Collecting leaves")
        # Step 1: Collect all leaf elements and validate structure
        
        leaves = collect_leaves(ast.value, ast.dimens, 0)

        # print("Leaves:", leaves)
        
        # print("Get the types of all leaf elements")
        
        # Step 2: Get the types of all leaf elements
        ele_types = [self.visit(leaf, c) for leaf in leaves]
        
        # print("Check if all leaf element types are compatible")

        # Step 3: Check if all leaf element types are compatible with ast.eleType

        # Step 4: Resolve dimensions to their values for consistent comparison
        # print("Resolve dimensions")
        resolved_dims = [
            IntLiteral(self.evaluate_ast(dim, c)) if isinstance(dim, (IntLiteral, Id, BinaryOp, UnaryOp)) else dim
            for dim in ast.dimens
        ]
        
        # print("Resolved dims:", resolved_dims)

        # Step 5: Return the ArrayType with resolved dimensions
        return ArrayType(resolved_dims, ast.eleType)
    
    def visitStructLiteral(self, ast, c):
        struct = self.lookup(ast.name, self.lst_type, lambda x: x.name)
        if not struct:
            raise Undeclared(Identifier(), ast.name)
        
        for field_name, expr in ast.elements:
            field = self.lookup(field_name, struct.elements, lambda x: x[0])
            if not field:
                raise Undeclared(Field(), field_name)
            
            temp = self.is_call_stmt
            self.is_call_stmt = False
            expr_type = self.visit(expr, c)
            self.is_call_stmt = temp
            
            resolved_type = self.resolve_type(field[1], c)
            
            if not self.is_compatible(resolved_type, expr_type):
                raise TypeMismatch(ast)
            
        return StructType(ast.name, struct.elements, struct.methods)
    
    def visitNilLiteral(self, ast, c): return StructType("", [], [])
    
    def is_compatible(self, lhs, rhs, exact=False):
        # Handle None cases (e.g., untyped declarations)
        if lhs is None or rhs is None:
            return True
        
        # print("LHS:", lhs)
        # print("RHS:", rhs)
        
        lhs = self.resolve_type(lhs, self.global_envi)
        rhs = self.resolve_type(rhs, self.global_envi)
        
        # print("Resolved LHS:", lhs)
        # print("Resolved RHS:", rhs)
        
        # both Void
        if isinstance(lhs, VoidType) and isinstance(rhs, VoidType):
            return True
        
        # LHS cannot be VoidType
        if isinstance(lhs, VoidType):
            return False
        
        # Numeric types: Float LHS accepts Int or Float RHS; Int LHS accepts only Int RHS
        if isinstance(lhs, (IntType, FloatType)) and isinstance(rhs, (IntType, FloatType)):
            if exact: return type(lhs) == type(rhs)
            if isinstance(lhs, FloatType):
                return True  # RHS can be Int or Float
            return isinstance(rhs, IntType)  # LHS is Int, RHS must be Int
        
        # Array types: Same dimensions, compatible element types
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            # Check if the number of dimensions matches
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            
            # add - eval => Compare dimensions
            for dim_lhs, dim_rhs in zip(lhs.dimens, rhs.dimens):
                # print(f"Dim LHS: {dim_lhs}")
                # print(f"Dim RHS: {dim_rhs}")
                
                if isinstance(dim_lhs, Id) and isinstance(dim_rhs, Id) and dim_lhs.name == dim_rhs.name:
                    continue
                
                # old 
                dim_lhs_val = self.evaluate_ast(dim_lhs, self.global_envi) if isinstance(dim_lhs, (IntLiteral, Id, BinaryOp, UnaryOp)) else dim_lhs
                dim_rhs_val = self.evaluate_ast(dim_rhs, self.global_envi) if isinstance(dim_rhs, (IntLiteral, Id, BinaryOp, UnaryOp)) else dim_rhs
                
                # print(f"Dim LHS Val: {dim_lhs_val}")
                # print(f"Dim RHS Val: {dim_rhs_val}")
                
                if dim_lhs_val != dim_rhs_val:
                    return False
            
            # original
            # print(f"Ele LHS: {lhs.eleType}")
            # print(f"Ele RHS: {rhs.eleType}")
            
            if exact:
                # Check if the element types are exactly the same
                # print(f"Ele LHS: {lhs.eleType}")
                # print(f"Ele RHS: {rhs.eleType}")
                # new
                return self.is_compatible(lhs.eleType, rhs.eleType, True)
            
            if isinstance(lhs.eleType, Id) and isinstance(rhs.eleType, Id):
                return lhs.eleType.name == rhs.eleType.name
            if isinstance(lhs.eleType, FloatType) and isinstance(rhs.eleType, IntType): return True
            return type(lhs.eleType) == type(rhs.eleType)
                
        # Interface and Struct: Struct must implement all interface prototypes
        if isinstance(lhs, InterfaceType) and isinstance(rhs, StructType):
            if rhs.name == "": return True # case Nil
            if exact: return type(lhs) == type(rhs)
            
            # print("LHS Interface and RHS Struct")
            
            interface = self.lookup(lhs.name, self.lst_type, lambda x: x.name)
            struct = self.lookup(rhs.name, self.lst_type, lambda x: x.name)
            
            # return False
            # no need something below here anymore
            
            if not interface or not struct:
                return False
            
            # Check if the struct implements all prototypes in the interface
            for proto in interface.methods:
                # Find a method in the struct with the same name
                method = self.lookup(proto.name, struct.methods, lambda x: x.fun.name)
                if not method:
                    return False  # Method not found in struct

                # Compare parameter types
                if len(proto.params) != len(method.fun.params):
                    return False  # Different number of parameters
                
                # Resolve and compare each parameter type
                for proto_param, method_param in zip(proto.params, method.fun.params):
                    proto_param_type = self.resolve_type(proto_param, self.global_envi)
                    method_param_type = self.resolve_type(method_param.parType, self.global_envi)
                    
                    if type(proto_param_type) != type(method_param_type):
                        return False

                # Compare return types
                proto_ret_type = self.resolve_type(proto.retType, self.global_envi)
                method_ret_type = self.resolve_type(method.fun.retType, self.global_envi)
                
                if not self.is_compatible(proto_ret_type, method_ret_type, True):
                    return False  # Return types don't match

            return True
        
        # Interface and Struct: Struct must implement all interface prototypes
        if isinstance(lhs, StructType) and isinstance(rhs, InterfaceType):
            if lhs.name == "": return True # case Nil
            if exact: return type(lhs) == type(rhs)
            
            return False
        
        # StructType compatibility: Same name implies same structure
        if isinstance(lhs, StructType) and isinstance(rhs, StructType):
            # if exact: return lhs.name == rhs.name # added 08/04
            if rhs.name == "": return True # case Nil
            return lhs.name == rhs.name
        
        if isinstance(lhs, InterfaceType) and isinstance(rhs, InterfaceType):
            return lhs.name == rhs.name
        
        # Default: Exact type equality for other cases (e.g., BoolType, StringType)
        return type(lhs) == type(rhs)
    
    def evaluate_ast(self, node, c, array_type=False):
        # print("Check before evaluate ast")
        # self.helper_debug(c)
        if isinstance(node, IntLiteral):
            # print("Int Literal", node.value)
            return node.value
        elif isinstance(node, FloatLiteral):
            # print("Float Literal", node.value)
            return node.value
        elif isinstance(node, Id):
            # current 
            # print("Id", node.name)
            # Look through all scopes from innermost to outermost
            for scope in c:
                self.helper_debug([scope])
                sym = self.lookup(node.name, scope, lambda x: x.name)
                if sym:
                    # print(sym.name)
                    # print(sym.value)
                    if sym.value is not None:
                        # # print(sym.value)
                        return sym.value
                    else:
                        # Found the symbol but it doesn't have a constant value
                        # print("Found the symbol but it doesn't have a constant value")
                        raise TypeMismatch(node)
            # If we get here, the identifier wasn't found in any scope
            raise TypeMismatch(node)
        elif isinstance(node, BinaryOp):
            left_val = self.evaluate_ast(node.left, c)
            right_val = self.evaluate_ast(node.right, c)
            if node.op == '+':
                return left_val + right_val
            elif node.op == '-':
                return left_val - right_val
            elif node.op == '*':
                return left_val * right_val
            elif node.op == '/':
                if right_val == 0:
                    raise TypeMismatch(node)  # Division by zero
                return left_val // right_val
            elif node.op == '%':
                if right_val == 0:
                    raise TypeMismatch(node)
                return left_val % right_val
        elif isinstance(node, UnaryOp):
            body_val = self.evaluate_ast(node.body, c)
            if node.op == '-':
                return -body_val
            elif node.op == '!':
                return not body_val
        # add 9/4
        elif isinstance(node, (MethCall, FuncCall)):
            return 0 # default
        raise TypeMismatch(node)  # Cannot evaluate
    
    def resolve_type(self, typ, c):
        if isinstance(typ, Id):
            resolved = self.lookup(typ.name, self.lst_type, lambda x: x.name)
            if not resolved:
                raise Undeclared(Identifier(), typ.name)
            return resolved
        return typ
    
    def helper_debug(self, local_env):
        for i in local_env:
            # print(f"Scope: {[str(sym) for sym in i]}")
            pass

# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu