# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"  # the same as teacher requires
        self.astTree = None
        self.path = None
        self.emit = None
        self.func_current = None            
        self.list_of_functions_prog = []         
        self.current_array_cell = None           
        self.current_array_cell_type = None
        self.param_func = False
        self.current_struct = None

    def init(self):
        """Initializes the list of built-in MiniGo functions."""
        mem = [
            # Added based on MiniGo specification [4]
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True)),
        ]
        return mem # Return the list of global symbols

    def gen(self, ast, dir_):
        # start the code generator
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  
        frame.enterScope(True)  
        
        # cause this is not statis so we need this here 
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", Id(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def emitObjectCInit(self, ast, env):
        frame = Frame("<clinit>", VoidType()) # Use <clinit> for static initializer name
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) # Static method
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Prepare the environment for visiting the initialization assignments
        init_env = env.copy() # Use a copy to avoid modifying the original env 
        init_env['frame'] = frame 

        # Create a list of Assign statements for global variables with initializers using a for loop
        block_assignment_elements = [] 
        for item in ast.decl: 
            # Filter for VarDecls with initializers [1]
            # New: Use conName for ConstDecl, varName for VarDecl
            if isinstance(item, VarDecl) and item.varInit is not None or isinstance(item, ConstDecl) and item.iniExpr is not None:
                var_name = item.conName if isinstance(item, ConstDecl) else item.varName
                
                assignment_element = Assign(Id(var_name), item.varInit if isinstance(item, VarDecl) else item.iniExpr)
                
                block_assignment_elements.append(assignment_element)

        # Visit a synthetic Block containing these assignments
        # This will generate the code to evaluate the initializers and store
        # them in the corresponding static fields using emitPUTSTATIC via visitAssign/visitId.
        if block_assignment_elements: # Only visit if there are assignments to make
            self.visit(Block(block_assignment_elements), init_env) 

        # Add dummy labels to match expected output
        label2 = frame.getNewLabel()
        label3 = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label3, frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) 
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame)) # Emit stack/local limits and end method 
        frame.exitScope() 

    def visitProgram(self, ast, c):
        # Initialize self.list_type
        self.list_type = {x.name: x for x in ast.decl if isinstance(x, (StructType, InterfaceType))}
        
        # Build the list of all functions (built-in + user-defined)
        self.list_of_functions_prog = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        
        # Initialize environment
        env = {}
        env['env'] = [c] # Global scope initialized with built-ins
        
        # Initialize Emitter for MiniGoClass.j
        main_emitter = Emitter(self.path + "/" + self.className + ".j")
        self.emit = main_emitter
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java/lang/Object"))
        
        ## New: Process variable and constant declarations
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, (VarDecl, ConstDecl)) else a, ast.decl, env)
        
        # New 
        # Process struct/interface declarations and collect MethodDecl
        def process_type_and_method(a, x):
            if isinstance(x, (StructType, InterfaceType)):
                # Ensure methods list exists
                if not hasattr(x, 'methods'):
                    x.methods = []
                # Collect MethodDecl for this type
                for decl in ast.decl:
                    if isinstance(decl, MethodDecl) and isinstance(decl.recType, Id) and decl.recType.name == x.name:
                        x.methods.append(decl)
                # Generate .j file for struct/interface
                self.current_struct = x
                struct_emitter = Emitter(self.path + "/" + x.name + ".j")
                self.emit = struct_emitter
                self.visit(x, {'env': a['env']})
                self.emit.printout(self.emit.emitEPILOG())  # Close the struct/interface file
            return a
        
        env = reduce(process_type_and_method, ast.decl, env)
        
        # Restore Emitter for MiniGoClass.j
        self.emit = main_emitter
        
        # add 9/5
        # Store global symbols and reset local environment
        g = env['env'][0] # Keep list of static attributes (global variables/constants)
        env['env'] = [[]] # Reset local environment for functions
        
        # Process declarations again to populate env and handle functions
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                # Find the variable in g and add it to the new local environment
                sym = next((s for s in g if s.name == decl.varName), None)
                if sym:
                    env['env'][0].append(sym)
            if isinstance(decl, ConstDecl):
                # Find the constant in g and add it to the new local environment
                sym = next((s for s in g if s.name == decl.conName), None)
                if sym:
                    env['env'][0].append(sym)
            if isinstance(decl, FuncDecl):
                self.visit(decl, env)  # Process function without updating env
        
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        
        # End program
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitFuncDecl(self, ast, o):
        # print(f"Visit FuncDecl: {ast.name}")
        
        self.func_current = ast
        
        frame = Frame(ast.name, ast.retType)
        
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        
        env = o.copy()
        env['frame'] = frame
        
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        
        # enter the body loop of the function decl
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # NOTE: 
        env['env'] = [[]] + env['env']
        
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            temp = self.param_func
            self.param_func = True
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
            self.param_func = temp
            
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitParamDecl(self, ast, o):
        frame = o['frame']
        index = frame.getNewIndex()
        
        # Ensure index 0 is reserved for 'this', so first param starts at 1
        if index == 0 and not self.param_func:
            index = frame.getNewIndex()  # Get index 1
            
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o

    def visitVarDecl(self, ast, o):
        def visit_vardecl_create_init(varType, o):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral(False)  
            elif isinstance(varType, Id):
                if varType.name in self.list_type and isinstance(self.list_type[varType.name], StructType):
                    return StructLiteral(varType.name, [])
                return NilLiteral()
            elif type(varType) is ArrayType:
                dims = varType.dimens
                eleType = varType.eleType
                
                # Ensure dims is not empty
                if not dims:
                    dims = [IntLiteral(1)]  # Default to [1] for consistency
                
                # Convert dimensions to integers for initialization
                def to_int(dim):
                    if dim is None:
                        return 1
                    elif isinstance(dim, int):
                        return dim
                    elif isinstance(dim, IntLiteral):
                        return dim.value
                    elif isinstance(dim, str):
                        return int(dim)
                    elif isinstance(dim, Id):
                        # Look up the constant's value
                        # Assume constant is initialized in <clinit>; use placeholder for ArrayLiteral
                        # Alternatively, fetch value from AST if available
                        for decl in self.astTree.decl:
                            if isinstance(decl, ConstDecl) and decl.conName == dim.name:
                                if isinstance(decl.iniExpr, IntLiteral):
                                    return decl.iniExpr.value
                        return 1  # Fallback placeholder
                        
                    else:
                        return 1
                int_dims = [to_int(dim) for dim in dims]
                
                def gen_nested_array(int_dims, eleType, level=0):
                    if level >= len(int_dims):
                        return visit_vardecl_create_init(eleType, o)
                    return [gen_nested_array(int_dims, eleType, level + 1) for _ in range(int_dims[level])]
                
                value = gen_nested_array(int_dims, eleType)
                return ArrayLiteral(dims, eleType, value)
            
            return None
        
        # print(f"Visit VarDecl: {ast.varName} of type {ast.varType}")
        
        varInit = ast.varInit
        varType = ast.varType
        
        # old 8/5
        if not varInit:
            varInit = visit_vardecl_create_init(varType, o)
            ast.varInit = varInit
            
        # add 9/5
        env = o.copy()
        if 'frame' not in o:
            env['frame'] = Frame("<global>", VoidType())
        else:
            env['frame'] = o['frame']
        
        rhsCode = ""
        rhsType = None
        frame = env['frame']
        
        if varInit:
            temp = env.get('stmt', False)
            env['stmt'] = False
            
            rhsCode, rhsType = self.visit(varInit, env)
            
            env['isLeft'] = False
            
            if rhsCode is None:
                rhsCode = ""
        else:
            if isinstance(varType, ArrayType):
                dims = varType.dimens
                eleType = varType.eleType
                if not all(isinstance(dim, (IntLiteral, Id)) for dim in dims):
                    raise IllegalOperandException("Array dimensions must be IntLiteral or Id")
                
                # Generate code for each dimension
                for dim in dims:
                    if isinstance(dim, IntLiteral):
                        rhsCode += self.emit.emitPUSHCONST(str(dim.value), IntType(), frame)
                    else:  # Id
                        # new 2/5
                        sym = next((s for env in o['env'] for s in env if s.name == dim.name), None)
                        if not sym:
                            raise IllegalOperandException(f"Undefined identifier: {dim.name}")
                        if not isinstance(sym.mtype, IntType):
                            raise IllegalOperandException(f"Array dimension {dim.name} must be IntType")
                        rhsCode += self.emit.emitGETSTATIC(f"{self.className}/{dim.name}", IntType(), frame)
                    frame.push()
                
                # Generate JVM type (e.g., [[[I, [[F, [[Ljava/lang/String;)
                jvm_type = ""
                for _ in range(len(dims)):
                    jvm_type += "["
                if isinstance(eleType, Id):
                    jvm_type += f"L{eleType.name};"
                elif type(eleType) is IntType:
                    jvm_type += "I"
                elif type(eleType) is FloatType:
                    jvm_type += "F"
                elif type(eleType) is BoolType:
                    jvm_type += "Z"
                elif type(eleType) is StringType:
                    jvm_type += "Ljava/lang/String;"
                else:
                    raise IllegalOperandException(f"Unsupported array element type: {eleType}")
                
                rhsCode += self.emit.emitMULTIANEWARRAY(jvm_type, len(dims), frame)
                for _ in range(len(dims)):
                    frame.pop()
                frame.push()  # Push arrayref
                rhsType = varType
        
        finalType = varType if varType else rhsType
        
        if 'frame' not in o:  # Global variable
            is_constant = hasattr(ast, 'conName')
            o['env'][0].append(Symbol(ast.varName, finalType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, finalType, True, is_constant, None))
        else:  # Local variable
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, finalType, Index(index)))
            var_type_for_emit = Id(finalType.name) if isinstance(finalType, Id) else finalType
            if isinstance(finalType, ArrayType) and isinstance(finalType.eleType, Id):
                var_type_for_emit = ArrayType(finalType.dimens, Id(finalType.eleType.name))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, var_type_for_emit, frame.getStartLabel(), frame.getEndLabel(), frame))
            if rhsCode:
                if type(finalType) is FloatType and type(rhsType) is IntType:
                    rhsCode += self.emit.emitI2F(frame)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, finalType, index, frame))
    
        return o
    
    def visitFuncCall(self, ast, o):
        # print(f"Visit FuncCall: {ast.funName}")
        
        sym = next(filter(lambda x: x.name == ast.funName, self.list_of_functions_prog),None)
        env = o.copy()
        
        # print(f"o.get('stmt'): {o.get('stmt')}")
        # print(f"sym: {sym}")
        
        env['stmt'] = False  # Arguments are always expressions
        
        if o.get('stmt'):
            # TODO: 
            # Generate code for each argument
            args_code = [self.visit(arg, env)[0] for arg in ast.args]
            
            for code in args_code:
                self.emit.printout(code)
            
            invoke_code = self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
            if invoke_code is None:
                # print(f"Warning: emitINVOKESTATIC({sym.value.value}/{ast.funName}) returned None")
                invoke_code = ""
            self.emit.printout(invoke_code)
            
            return o 
        
        else:
            # Expression context
            args_code = [str(self.visit(arg, env)[0]) for arg in ast.args]
            output = "".join(args_code)
            
            invoke_code = self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
            if invoke_code is None:
                # print(f"Warning: emitINVOKESTATIC({sym.value.value}/{ast.funName}) returned None")
                invoke_code = ""
            output += invoke_code
            
            return output, sym.mtype.rettype

    def visitBlock(self, ast, o):
        # print(f"Visit Block: {ast}")
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        
        for item in ast.member:
            item_env = env.copy()  # Create a fresh environment for each item
            
            # Set stmt = True only for standalone FuncCall or MethCall, not assignments
            if isinstance(item, (FuncCall, MethCall)) and not isinstance(item, Assign):
                item_env["stmt"] = True
                
            env = self.visit(item, item_env)
              
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        
        env['frame'].exitScope()
        return o
    
    def visitId(self, ast, o):
        # print(f"Visit Id: {ast.name}")
        
        # Check if Id is the method receiver (e.g., 'pq' in PriorityQueue methods)
        if (self.current_struct and isinstance(ast, Id) and
            not next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]), None)):
            # If Id is not in env and we're in a struct method, assume it's 'this'
            this_type = Id(self.current_struct.name)
            # print(f"Resolving {ast.name} as 'this' of type {this_type.name}")
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this", this_type, 0, o['frame']), this_type
            return self.emit.emitREADVAR("this", this_type, 0, o['frame']), this_type
        
        # This is for checking which symbol in the env is the one we are looking for
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        
        # print(f"sym: {sym}")
        
        if sym is None:
            if self.current_struct and not o.get('isLeft'):
                # Assume 'this' in method context
                return self.emit.emitREADVAR("this", Id(self.current_struct.name), 0, o['frame']), Id(self.current_struct.name)
            raise IllegalOperandException(f"Undefined identifier: {ast.name}")
        
        # If Id in the LHS of an assignment
        if o.get('isLeft'):
            if type(sym.value) is Index:
                # TODO 
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                # TODO 
                lexeme = f"{sym.value.value}/{ast.name}"
                return self.emit.emitPUTSTATIC(lexeme, sym.mtype, o['frame']), sym.mtype
                
        # This is mark that Id is on the RHS
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:        
            lexeme = f"{sym.value.value}/{ast.name}"
            return self.emit.emitGETSTATIC(lexeme, sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast, o):
        # Determine if LHS is the method receiver (e.g., 'pq' in pq.swap(...))
        is_receiver = False
        if (isinstance(ast.lhs, Id) and self.current_struct and isinstance(ast.rhs, MethCall) and
            isinstance(ast.rhs.receiver, Id) and ast.rhs.receiver.name == ast.lhs.name):
            is_receiver = True
        
        if isinstance(ast.lhs, Id) and not is_receiver and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]), None):
            var_decl = VarDecl(ast.lhs.name, None, ast.rhs)
            o = self.visit(var_decl, o)
            ast.lhs = Id(ast.lhs.name)
            return o
        
        original_stmt = o.get('stmt')
        o['stmt'] = False
        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['stmt'] = original_stmt
        
        frame = o['frame']
        
        if isinstance(ast.lhs, FieldAccess):
            receiver_code, receiver_type = self.visit(ast.lhs.receiver, o)
            struct = self.list_type.get(receiver_type.name)
            if not struct or not isinstance(struct, StructType):
                raise IllegalOperandException(f"Type {receiver_type.name} not found or not a struct")
            field = next((e for e in struct.elements if e[0] == ast.lhs.field), None)
            if not field:
                raise IllegalOperandException(f"Field {ast.lhs.field} not found in {receiver_type.name}")
            if isinstance(field[1], FloatType) and isinstance(rhsType, IntType):
                rhsCode += self.emit.emitI2F(frame)
            
            frame.push()  # receiver
            frame.push()  # value
            self.emit.printout(receiver_code)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitPUTFIELD(f"{receiver_type.name}/{ast.lhs.field}", field[1], frame))
        
        # new
        elif isinstance(ast.lhs, ArrayCell):
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            
            # Handle scalar FloatType := IntType (e.g., fmarr[0][0] := 1)
            if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
                rhsCode += self.emit.emitI2F(frame)
            
            # Handle array of FloatType := array of IntType (e.g., fmarr[0] := marr)
            # if (isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType)):
            if (isinstance(lhsType, ArrayType) and isinstance(lhsType.eleType, FloatType) and isinstance(rhsType, ArrayType) and isinstance(rhsType.eleType, IntType)):
                # Verify dimensions match
                if len(lhsType.dimens) != len(rhsType.dimens):
                    raise IllegalOperandException("Array dimensions must match")
                for ldim, rdim in zip(lhsType.dimens, rhsType.dimens):
                    ldim_val = ldim.value if isinstance(ldim, IntLiteral) else None
                    rdim_val = rdim.value if isinstance(rdim, IntLiteral) else None
                    if ldim_val and rdim_val and ldim_val != rdim_val:
                        raise IllegalOperandException("Array dimensions must match")
                
                # One-dimensional case: [n]int to [n]float
                if len(lhsType.dimens) == 1 and isinstance(lhsType.eleType, FloatType) and isinstance(rhsType.eleType, IntType):
                    array_size = lhsType.dimens[0].value if isinstance(lhsType.dimens[0], IntLiteral) else None
                    if array_size is None:
                        raise IllegalOperandException("Dynamic array sizes not supported")
                    
                    # Generate code for array conversion
                    code = self.emit.emitPUSHCONST(str(array_size), IntType(), frame)
                    code += self.emit.emitNEWARRAY(FloatType(), frame)
                    frame.push()  # Float arrayref
                    
                    # Loop to copy and convert elements
                    loop_label = frame.getNewLabel()
                    exit_label = frame.getNewLabel()
                    index_var = frame.getNewIndex()
                    
                    # Initialize index = 0
                    code += self.emit.emitPUSHCONST("0", IntType(), frame)
                    code += self.emit.emitWRITEVAR("index_temp", IntType(), index_var, frame)
                    frame.push()
                    frame.pop()
                    
                    # Loop start
                    code += self.emit.emitLABEL(loop_label, frame)
                    
                    # Condition: index < array_size
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitPUSHCONST(str(array_size), IntType(), frame)
                    code += self.emit.emitIFICMPGE(exit_label, frame)
                    frame.push()
                    frame.pop()
                    
                    # Duplicate float arrayref
                    code += self.emit.emitDUP(frame)
                    frame.push()
                    
                    # Load index
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    frame.push()
                    
                    # Load int array element
                    code += rhsCode  # Load int array
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitALOAD(IntType(), frame)
                    frame.push()
                    frame.pop()
                    frame.push()
                    
                    # Convert int to float
                    code += self.emit.emitI2F(frame)
                    
                    # Store in float array
                    code += self.emit.emitASTORE(FloatType(), frame)
                    frame.pop()  # value
                    frame.pop()  # index
                    frame.pop()  # arrayref
                    
                    # Increment index
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitPUSHCONST("1", IntType(), frame)
                    code += self.emit.emitADDOP("+", IntType(), frame)
                    code += self.emit.emitWRITEVAR("index_temp", IntType(), index_var, frame)
                    frame.push()
                    frame.pop()
                    
                    # Loop back
                    code += self.emit.emitGOTO(loop_label, frame)
                    
                    # Loop exit
                    code += self.emit.emitLABEL(exit_label, frame)
                    
                    # Store the new float array into fmarr[0]
                    self.emit.printout(lhsCode)  # arrayref, index
                    self.emit.printout(code)     # float array
                    self.emit.printout(self.emit.emitASTORE(ArrayType([IntLiteral(array_size)], FloatType()), frame))
                
                # Multidimensional case: [n][m]...int to [n][m]...float
                else:
                    # Get dimensions (assume IntLiteral for simplicity)
                    dims = [dim.value for dim in lhsType.dimens if isinstance(dim, IntLiteral)]
                    if len(dims) != len(lhsType.dimens):
                        raise IllegalOperandException("Dynamic array sizes not supported")
                    
                    # Create temporary float array
                    jvm_type = "[" * len(dims) + "F"
                    code = ""
                    for dim_size in dims:
                        code += self.emit.emitPUSHCONST(str(dim_size), IntType(), frame)
                        frame.push()  # Push dimension size
                    code += self.emit.emitMULTIANEWARRAY(jvm_type, len(dims), frame)
                    for _ in range(len(dims)):
                        frame.pop()  # Pop dimension sizes
                    frame.push()  # Push float arrayref
                    
                    # Nested loops to access each element
                    index_vars = [frame.getNewIndex() for _ in dims]
                    loop_labels = [frame.getNewLabel() for _ in dims]
                    exit_labels = [frame.getNewLabel() for _ in dims]
                    
                    # Initialize indices to 0
                    for i, index_var in enumerate(index_vars):
                        code += self.emit.emitPUSHCONST("0", IntType(), frame)
                        code += self.emit.emitWRITEVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        frame.push()
                        frame.pop()
                    
                    # Generate nested loops
                    for i, (dim_size, index_var, loop_label, exit_label) in enumerate(zip(dims, index_vars, loop_labels, exit_labels)):
                        # Loop start
                        code += self.emit.emitLABEL(loop_label, frame)
                        
                        # Condition: index < dim_size
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST(str(dim_size), IntType(), frame)
                        code += self.emit.emitIFICMPGE(exit_label, frame)
                        frame.push()
                        frame.pop()
                    
                    # Innermost loop body: access and convert element
                    # Duplicate float arrayref
                    code += self.emit.emitDUP(frame)
                    frame.push()
                    
                    # Access float array element: fmarr[1][i][j]
                    current_dst_type = lhsType
                    for i in range(len(dims) - 1):
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_vars[i], frame)
                        next_dst_type = current_dst_type.eleType if isinstance(current_dst_type, ArrayType) else current_dst_type
                        code += self.emit.emitALOAD(current_dst_type, frame)
                        frame.push()
                        frame.pop()
                        frame.push()
                        current_dst_type = next_dst_type
                    code += self.emit.emitREADVAR(f"index_temp_{len(dims)-1}", IntType(), index_vars[-1], frame)
                    frame.push()
                    
                    # Access int array element: marr[i][j]
                    code += rhsCode  # Load source array
                    current_src_type = rhsType
                    for i in range(len(dims) - 1):
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_vars[i], frame)
                        next_src_type = current_src_type.eleType if isinstance(current_src_type, ArrayType) else current_src_type
                        code += self.emit.emitALOAD(current_src_type, frame)
                        frame.push()
                        frame.pop()
                        frame.push()
                        current_src_type = next_src_type
                    code += self.emit.emitREADVAR(f"index_temp_{len(dims)-1}", IntType(), index_vars[-1], frame)
                    code += self.emit.emitALOAD(IntType(), frame)
                    frame.push()
                    frame.pop()
                    frame.push()
                    
                    # Convert int to float
                    code += self.emit.emitI2F(frame)
                    
                    # Store in float array
                    code += self.emit.emitASTORE(FloatType(), frame)
                    frame.pop()  # value
                    frame.pop()  # index
                    frame.pop()  # arrayref
                    
                    # Increment indices (from innermost to outermost)
                    for i in range(len(dims) - 1, -1, -1):
                        index_var = index_vars[i]
                        loop_label = loop_labels[i]
                        exit_label = exit_labels[i]
                        # Increment index
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST("1", IntType(), frame)
                        code += self.emit.emitADDOP("+", IntType(), frame)
                        code += self.emit.emitWRITEVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        frame.push()
                        frame.push()
                        frame.pop()
                        frame.pop()
                        # Check if index < dim_size to continue loop
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST(str(dims[i]), IntType(), frame)
                        code += self.emit.emitIFICMPGE(exit_label, frame)
                        frame.push()
                        frame.pop()
                        # Reset inner indices to 0
                        for j in range(i + 1, len(dims)):
                            code += self.emit.emitPUSHCONST("0", IntType(), frame)
                            code += self.emit.emitWRITEVAR(f"index_temp_{j}", IntType(), index_vars[j], frame)
                            frame.push()
                            frame.pop()
                        code += self.emit.emitGOTO(loop_label, frame)
                        # Loop exit
                        code += self.emit.emitLABEL(exit_label, frame)
                    
                    # Store the new float array into fmarr[1]
                    self.emit.printout(lhsCode)  # arrayref, index
                    self.emit.printout(code)     # float array
                    self.emit.printout(self.emit.emitASTORE(ArrayType([IntLiteral(dims[0])], ArrayType([IntLiteral(dims[1])], FloatType())), frame))
            
            else:
                self.emit.printout(lhsCode)  # arrayref, index
                self.emit.printout(rhsCode)  # value
                self.emit.printout(self.emit.emitASTORE(self.current_array_cell_type, frame))
        
        # new 
        else:  # Id
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            
            # Handle scalar FloatType := IntType
            if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
                rhsCode += self.emit.emitI2F(frame)
            
            # Handle array of FloatType := array of IntType (including multidimensional)
            if (isinstance(lhsType, ArrayType) and isinstance(lhsType.eleType, FloatType) and isinstance(rhsType, ArrayType) and isinstance(rhsType.eleType, IntType)):
                # Verify dimensions match
                if len(lhsType.dimens) != len(rhsType.dimens):
                    raise IllegalOperandException("Array dimensions must match")
                
                for ldim, rdim in zip(lhsType.dimens, rhsType.dimens):
                    ldim_val = ldim.value if isinstance(ldim, IntLiteral) else None
                    rdim_val = rdim.value if isinstance(rdim, IntLiteral) else None
                    if ldim_val and rdim_val and ldim_val != rdim_val:
                        raise IllegalOperandException("Array dimensions must match")
                
                # One-dimensional case: [n]int to [n]float
                if len(lhsType.dimens) == 1 and isinstance(lhsType.eleType, FloatType) and isinstance(rhsType.eleType, IntType):
                    array_size = lhsType.dimens[0].value if isinstance(lhsType.dimens[0], IntLiteral) else None
                    if array_size is None:
                        raise IllegalOperandException("Dynamic array sizes not supported")
                    
                    code = rhsCode  # Load int array
                    code += self.emit.emitPUSHCONST(str(array_size), IntType(), frame)
                    code += self.emit.emitNEWARRAY(FloatType(), frame)
                    
                    # Loop to copy and convert elements
                    loop_label = frame.getNewLabel()
                    exit_label = frame.getNewLabel()
                    index_var = frame.getNewIndex()
                    
                    # Initialize index = 0
                    code += self.emit.emitPUSHCONST("0", IntType(), frame)
                    code += self.emit.emitWRITEVAR("index_temp", IntType(), index_var, frame)
                    
                    # Loop start
                    code += self.emit.emitLABEL(loop_label, frame)
                    
                    # Condition: index < array_size
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitPUSHCONST(str(array_size), IntType(), frame)
                    code += self.emit.emitIFICMPGE(exit_label, frame)
                    
                    # Duplicate float arrayref
                    code += self.emit.emitDUP(frame)
                    
                    # Load index
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    
                    # Load int array element
                    code += rhsCode  # Reload int array
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitALOAD(IntType(), frame)
                    
                    # Convert int to float
                    code += self.emit.emitI2F(frame)
                    
                    # Store in float array
                    code += self.emit.emitASTORE(FloatType(), frame)
                    
                    # Increment index
                    code += self.emit.emitREADVAR("index_temp", IntType(), index_var, frame)
                    code += self.emit.emitPUSHCONST("1", IntType(), frame)
                    code += self.emit.emitADDOP("+", IntType(), frame)
                    code += self.emit.emitWRITEVAR("index_temp", IntType(), index_var, frame)
                    
                    # Loop back
                    code += self.emit.emitGOTO(loop_label, frame)
                    
                    # Loop exit
                    code += self.emit.emitLABEL(exit_label, frame)
                    
                    self.emit.printout(code)
                    self.emit.printout(lhsCode)
                
                # Multidimensional case: [n][m]...int to [n][m]...float
                else:
                    # Get dimensions (assume IntLiteral for simplicity)
                    dims = [dim.value for dim in lhsType.dimens if isinstance(dim, IntLiteral)]
                    if len(dims) != len(lhsType.dimens):
                        raise IllegalOperandException("Dynamic array sizes not supported")
                    
                    # Create temporary float array
                    code = rhsCode  # Load source array for later use
                    jvm_type = "[" * len(dims) + "F"
                    for dim_size in dims:
                        code += self.emit.emitPUSHCONST(str(dim_size), IntType(), frame)
                        frame.push()  # Push dimension size
                    code += self.emit.emitMULTIANEWARRAY(jvm_type, len(dims), frame)
                    for _ in range(len(dims)):
                        frame.pop()  # Pop dimension sizes
                    frame.push()  # Push float arrayref
                    
                    # Nested loops to access each element
                    index_vars = [frame.getNewIndex() for _ in dims]
                    loop_labels = [frame.getNewLabel() for _ in dims]
                    exit_labels = [frame.getNewLabel() for _ in dims]
                    
                    # Initialize indices to 0
                    for i, index_var in enumerate(index_vars):
                        code += self.emit.emitPUSHCONST("0", IntType(), frame)
                        code += self.emit.emitWRITEVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        frame.push()
                        frame.pop()
                    
                    # Generate nested loops
                    for i, (dim_size, index_var, loop_label, exit_label) in enumerate(zip(dims, index_vars, loop_labels, exit_labels)):
                        # Loop start
                        code += self.emit.emitLABEL(loop_label, frame)
                        
                        # Condition: index < dim_size
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST(str(dim_size), IntType(), frame)
                        code += self.emit.emitIFICMPGE(exit_label, frame)
                        frame.push()
                        frame.pop()
                    
                    # Innermost loop body: access and convert element
                    # Duplicate float arrayref
                    code += self.emit.emitDUP(frame)
                    frame.push()
                    
                    # Access float array element: fmarr[i][j][k]...
                    current_dst_type = lhsType
                    for i in range(len(dims) - 1):
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_vars[i], frame)
                        next_dst_type = current_dst_type.eleType if isinstance(current_dst_type, ArrayType) else None
                        code += self.emit.emitALOAD(current_dst_type, frame)
                        frame.push()
                        frame.pop()
                        frame.push()
                        current_dst_type = next_dst_type
                    code += self.emit.emitREADVAR(f"index_temp_{len(dims)-1}", IntType(), index_vars[-1], frame)
                    frame.push()
                    
                    # Access int array element: marr[i][j][k]...
                    code += rhsCode  # Reload source array
                    current_src_type = rhsType
                    for i in range(len(dims) - 1):
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_vars[i], frame)
                        next_src_type = current_src_type.eleType if isinstance(current_src_type, ArrayType) else None
                        code += self.emit.emitALOAD(current_src_type, frame)
                        frame.push()
                        frame.pop()
                        frame.push()
                        current_src_type = next_src_type
                    code += self.emit.emitREADVAR(f"index_temp_{len(dims)-1}", IntType(), index_vars[-1], frame)
                    code += self.emit.emitALOAD(IntType(), frame)
                    frame.push()
                    frame.pop()
                    frame.push()
                    
                    # Convert int to float
                    code += self.emit.emitI2F(frame)
                    
                    # Store in float array
                    code += self.emit.emitASTORE(FloatType(), frame)
                    frame.pop()  # value
                    frame.pop()  # index
                    frame.pop()  # arrayref
                    
                    # Increment indices (from innermost to outermost)
                    for i in range(len(dims) - 1, -1, -1):
                        index_var = index_vars[i]
                        loop_label = loop_labels[i]
                        exit_label = exit_labels[i]
                        # Increment index
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST("1", IntType(), frame)
                        code += self.emit.emitADDOP("+", IntType(), frame)
                        code += self.emit.emitWRITEVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        frame.push()
                        frame.push()
                        frame.pop()
                        frame.pop()
                        # Check if index < dim_size to continue loop
                        code += self.emit.emitREADVAR(f"index_temp_{i}", IntType(), index_var, frame)
                        code += self.emit.emitPUSHCONST(str(dims[i]), IntType(), frame)
                        code += self.emit.emitIFICMPGE(exit_label, frame)
                        frame.push()
                        frame.pop()
                        # Reset inner indices to 0
                        for j in range(i + 1, len(dims)):
                            code += self.emit.emitPUSHCONST("0", IntType(), frame)
                            code += self.emit.emitWRITEVAR(f"index_temp_{j}", IntType(), index_vars[j], frame)
                            frame.push()
                            frame.pop()
                        code += self.emit.emitGOTO(loop_label, frame)
                        # Loop exit
                        code += self.emit.emitLABEL(exit_label, frame)
                    
                    # Store temporary array in fmarr
                    self.emit.printout(code)
                    self.emit.printout(lhsCode)
            
            # Default case
            else:
                if is_receiver and isinstance(ast.rhs, MethCall):
                    self.emit.printout(rhsCode)
                    if not isinstance(rhsType, VoidType):
                        self.emit.printout(self.emit.emitPOP(frame))
                        # frame.pop()
                else:
                    self.emit.printout(rhsCode)
                    self.emit.printout(lhsCode)
        
        return o
    
    def visitReturn(self, ast, o):
        if ast.expr:
            original_stmt = o.get('stmt')
            o['stmt'] = False
            
            code, ret_type = self.visit(ast.expr, o)
            
            o['stmt'] = original_stmt
            
            if code is None:
                # print(f"Warning: visit({ast.expr}) returned None")
                code = ""
            self.emit.printout(code)
            return_code = self.emit.emitRETURN(ret_type, o['frame'])
            if return_code is None:
                # print(f"Warning: emitRETURN({ret_type}) returned None")
                return_code = ""
            self.emit.printout(return_code)
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o['frame']))
        return o

    def visitBinaryOp(self, ast, o):
        # print(f"Visit BinaryOp: {ast.op}")
        
        op = ast.op
        frame = o['frame']
        
        # new (30.4) - now the new one is short-evaluated
        # if op in ['||', '&&']:
        #     # Short-circuit evaluation
        #     result_type = BoolType()
        #     label_true = frame.getNewLabel()
        #     label_false = frame.getNewLabel()
        #     label_exit = frame.getNewLabel()
        #     code = ""

        #     # Evaluate left operand
        #     code_left, type_left = self.visit(ast.left, o)
        #     if not isinstance(type_left, BoolType):
        #         raise IllegalOperandException(f"Left operand of {op} must be BoolType, got {type_left}")
            
        #     code += code_left
            
        #     if op == '||':
        #         code += self.emit.emitIFNE(label_true, frame)
        #     else:  # '&&'
        #         code += self.emit.emitIFEQ(label_false, frame)

        #     # Evaluate right operand in expression context
        #     right_env = o.copy()
        #     right_env['stmt'] = False  # Force expression context
        #     code_right, type_right = self.visit(ast.right, right_env)
        #     if not isinstance(type_right, BoolType):
        #         raise IllegalOperandException(f"Right operand of {op} must be BoolType, got {type_right}")
            
        #     code += code_right
            
        #     code += self.emit.emitIFNE(label_true, frame)
        #     code += self.emit.emitGOTO(label_false, frame)
            
        #     code += self.emit.emitLABEL(label_true, frame)
        #     code += self.emit.emitPUSHCONST("1", IntType(), frame)
        #     code += self.emit.emitGOTO(label_exit, frame)
            
        #     code += self.emit.emitLABEL(label_false, frame)
        #     code += self.emit.emitPUSHCONST("0", IntType(), frame)
            
        #     code += self.emit.emitLABEL(label_exit, frame)
            
        #     return code, result_type
        
        code_on_left, type_on_left = self.visit(ast.left, o)
        code_on_right, type_on_right = self.visit(ast.right, o)
        
        # new (2.5) - Handle struct == nil or nil == struct
        # Handle struct == struct or struct != struct
        if op in ['==', '!='] and isinstance(type_on_left, Id) and isinstance(type_on_right, Id):
            if type_on_left.name != type_on_right.name and type_on_left.name != "" and type_on_right.name != "":
                raise IllegalOperandException(f"Cannot compare {type_on_left.name} with {type_on_right.name}")
            labelF = frame.getNewLabel()
            labelO = frame.getNewLabel()
            result = [code_on_left, code_on_right]
            frame.pop()  # Pop right operand
            frame.pop()  # Pop left operand
            if op == "==":
                result.append(self.emit.jvm.emitIFACMPEQ(labelO))
            else:  # "!="
                result.append(self.emit.jvm.emitIFACMPNE(labelO))
            result.append(self.emit.emitPUSHCONST("0", IntType(), frame))  # false
            result.append(self.emit.emitGOTO(labelF, frame))
            result.append(self.emit.emitLABEL(labelO, frame))
            result.append(self.emit.emitPUSHCONST("1", IntType(), frame))  # true
            result.append(self.emit.emitLABEL(labelF, frame))
            return ''.join(result), BoolType()
        
        if op in ['+', '-'] and type(type_on_left) in [FloatType, IntType]:
            type_for_return = IntType() if type(type_on_left) is IntType and type(type_on_right) is IntType else FloatType()
            if type(type_for_return) is FloatType:
                if type(type_on_left) is IntType:
                    code_on_left += self.emit.emitI2F(frame)
                
                if type(type_on_right) is IntType:
                    code_on_right += self.emit.emitI2F(frame)
            
            return code_on_left + code_on_right + self.emit.emitADDOP(op, type_for_return, frame), type_for_return
        
        if op in ['*', '/']:
            type_for_return = IntType() if type(type_on_left) is IntType and type(type_on_right) is IntType else FloatType()
            
            if type(type_for_return) is FloatType:
                if type(type_on_left) is IntType:
                    code_on_left += self.emit.emitI2F(frame)
                
                if type(type_on_right) is IntType:
                    code_on_right += self.emit.emitI2F(frame)
                    
            return code_on_left + code_on_right + self.emit.emitMULOP(op, type_for_return, frame), type_for_return
        
        if op in ['%']:
            if type(type_on_left) is not IntType or type(type_on_right) is not IntType:
                raise IllegalOperandException("Modulus requires IntType")
            return code_on_left + code_on_right + self.emit.emitMOD(frame), IntType()
        
        # New: Handle == and != for BoolType
        if op in ['==', '!='] and isinstance(type_on_left, BoolType) and isinstance(type_on_right, BoolType):
            labelF = frame.getNewLabel()
            labelO = frame.getNewLabel()
            result = [code_on_left, code_on_right]
            frame.pop()  # Pop right operand
            frame.pop()  # Pop left operand
            if op == "==":
                result.append(self.emit.jvm.emitIFICMPEQ(labelO))
            else:  # "!="
                result.append(self.emit.jvm.emitIFICMPNE(labelO))
            result.append(self.emit.emitPUSHCONST("0", IntType(), frame))  # false
            result.append(self.emit.emitGOTO(labelF, frame))
            result.append(self.emit.emitLABEL(labelO, frame))
            result.append(self.emit.emitPUSHCONST("1", IntType(), frame))  # true
            result.append(self.emit.emitLABEL(labelF, frame))
            return ''.join(result), BoolType()
        
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(type_on_left) in [FloatType, IntType]:
            type_for_return = BoolType()
            return code_on_left + code_on_right + self.emit.emitREOP(op, type_on_left, frame), type_for_return
        
        # old - now the new one is short-evaluated
        if op in ['||']:
            return code_on_left + code_on_right + self.emit.emitOROP(frame), BoolType()
        
        if op in ['&&']:
            return code_on_left + code_on_right + self.emit.emitANDOP(frame), BoolType()  

        if op in ['+'] and type(type_on_left) in [StringType]:
            return (code_on_left + code_on_right +
                    self.emit.emitINVOKEVIRTUAL("java/lang/String/concat",
                                            MType([StringType()], StringType()), frame)), StringType()
        
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(type_on_left) in [StringType]:
            if type(type_on_right) is not StringType:
                raise IllegalOperandException(f"Cannot compare String with {type_on_right}")
            code = (code_on_left + code_on_right +
                    self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo",
                                                MType([StringType()], IntType()), frame))
            labelF = frame.getNewLabel()
            labelO = frame.getNewLabel()
            result = [code]
            frame.pop()  # Pop compareTo result
            if op == ">":
                result.append(self.emit.jvm.emitIFLE(labelF))  # Jump if compareTo <= 0 (left <= right)
            elif op == ">=":
                result.append(self.emit.jvm.emitIFLT(labelF))  # Jump if compareTo < 0 (left < right)
            elif op == "<":
                result.append(self.emit.jvm.emitIFGE(labelF))  # Jump if compareTo >= 0 (left >= right)
            elif op == "<=":
                result.append(self.emit.jvm.emitIFGT(labelF))  # Jump if compareTo > 0 (left > right)
            elif op == "==":
                result.append(self.emit.jvm.emitIFNE(labelF))  # Jump if compareTo != 0 (left != right)
            elif op == "!=":
                result.append(self.emit.jvm.emitIFEQ(labelF))  # Jump if compareTo == 0 (left == right)
            
            result.append(self.emit.emitPUSHCONST("1", IntType(), frame))  # true
            frame.pop()
            result.append(self.emit.emitGOTO(labelO, frame))
            result.append(self.emit.emitLABEL(labelF, frame))
            result.append(self.emit.emitPUSHCONST("0", IntType(), frame))  # false
            result.append(self.emit.emitLABEL(labelO, frame))
            return ''.join(result), BoolType()  
              
    def visitUnaryOp(self, ast, o):
        code, type_of_body = self.visit(ast.body, o)
        if ast.op == '!':
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()
        elif ast.op == '-':
            return code + self.emit.emitNEGOP(type_of_body, o['frame']), type_of_body
    
    def visitIntLiteral(self, ast, o):
        code_for_return = self.emit.emitPUSHICONST(ast.value, o['frame'])
        return code_for_return, IntType()
    
    def visitFloatLiteral(self, ast, o):
        code_for_return = self.emit.emitPUSHFCONST(ast.value, o['frame'])
        return code_for_return, FloatType()
    
    def visitBooleanLiteral(self, ast, o) :
        # return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
        value = "1" if (ast.value == "true" or ast.value == True) else "0"
        
        # print(f"BooleanLiteral: {ast.value} => {value}")
        
        code_for_return = self.emit.emitPUSHICONST(value, o['frame'])
        if code_for_return is None:
            raise IllegalOperandException(f"emitPUSHICONST returned None for {value}")
        return code_for_return, BoolType()
    
    def visitStringLiteral(self, ast, o):
        code_for_return = self.emit.emitPUSHCONST(ast.value, StringType(), o['frame'])
        return code_for_return, StringType()
    
    # new after 2/5
    def visitIf(self, ast, o):
        frame = o['frame']
        
        # Initialize labels
        label_exit = frame.getNewLabel()
        label_end_if = frame.getNewLabel()
        
        # Generate condition code
        temp = o.get('stmt', False)
        o['stmt'] = False  # Force expression context
        
        condCode, _ = self.visit(ast.expr, o)
        
        o['stmt'] = temp  # Restore original context
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))
        
        # Then branch
        then_env = o.copy()
        self.visit(ast.thenStmt, then_env)
        
        # Only emit GOTO if thenStmt does not contain a return
        if not (isinstance(ast.thenStmt, Return) or 
                (isinstance(ast.thenStmt, Block) and 
                any(isinstance(stmt, Return) for stmt in ast.thenStmt.member))):
            self.emit.printout(self.emit.emitGOTO(label_exit, frame))
        
        # Label for end of if (false condition)
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))
        
        # Else branch (if present)
        if ast.elseStmt is not None:
            else_env = o.copy()
            self.visit(ast.elseStmt, else_env)
            # Only emit exit label if elseStmt does not terminate
            if not (isinstance(ast.elseStmt, Return) or 
                    (isinstance(ast.elseStmt, Block) and 
                    any(isinstance(stmt, Return) for stmt in ast.elseStmt.member))):
                self.emit.printout(self.emit.emitLABEL(label_exit, frame))
        else:
            self.emit.printout(self.emit.emitLABEL(label_exit, frame))
        
        return o
    
    def visitForBasic(self, ast, o):
        frame = o['frame']
        
        # Init loop
        frame.enterLoop()
        this_new_label = frame.getNewLabel()
        this_break_label = frame.getBreakLabel() 
        this_continue_label = frame.getContinueLabel()
        
        # Label new 
        self.emit.printout(self.emit.emitLABEL(this_new_label, frame))
        
        # condition 
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(this_break_label, frame))
        
        # Loop body
        loop_env = o.copy()
        self.visit(ast.loop, loop_env)

        # continue
        self.emit.printout(self.emit.emitLABEL(this_continue_label, frame))
        
        # goto label new
        self.emit.printout(self.emit.emitGOTO(this_new_label, frame))
        
        # goto label break 
        self.emit.printout(self.emit.emitLABEL(this_break_label, frame))
                           
        frame.exitLoop()
        return o
    
    def visitForStep(self, ast, o):
        frame = o['frame']
        
        # Initialize loop
        frame.enterLoop()
        this_new_label = frame.getNewLabel()
        this_break_label = frame.getBreakLabel()
        this_continue_label = frame.getContinueLabel()
        
        # Initialization (e.g., var i int = 0)
        init_env = o.copy()
        init_env['stmt'] = True
        init_env['env'] = [[]] + init_env['env']  # New scope for loop variable
        self.visit(ast.init, init_env)
        
        # Start label
        self.emit.printout(self.emit.emitLABEL(this_new_label, frame))
        
        # Condition (e.g., i < 2)
        cond_env = init_env.copy()  # Use loop scope
        cond_env['stmt'] = False  # Condition is an expression
        cond_code, cond_type = self.visit(ast.cond, cond_env)
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(this_break_label, frame))
        
        # Loop body
        loop_env = init_env.copy()  # Use loop scope
        self.visit(ast.loop, loop_env)
        
        # Continue point
        self.emit.printout(self.emit.emitLABEL(this_continue_label, frame))
        
        # Update (e.g., i += 1)
        update_env = init_env.copy()  # Use loop scope
        update_env['stmt'] = True
        self.visit(ast.upda, update_env)
        
        # Loop back
        self.emit.printout(self.emit.emitGOTO(this_new_label, frame))
        
        # Break point
        self.emit.printout(self.emit.emitLABEL(this_break_label, frame))
        
        frame.exitLoop()
        return o

    def visitForEach(self, ast, o):
        frame = o['frame']
        env = o.copy()
        
        # Initialize loop
        frame.enterLoop()
        this_loop_label = frame.getNewLabel()
        this_break_label = frame.getBreakLabel()
        this_continue_label = frame.getContinueLabel()
        
        # Evaluate array
        arr_code, arr_type = self.visit(ast.arr, env)
        
        if not isinstance(arr_type, ArrayType):
            raise IllegalOperandException("ForEach array must be ArrayType")
        
        # Declare idx and value as local variables
        idx_index = frame.getNewIndex()
        value_index = frame.getNewIndex()
        env['env'][0].append(Symbol(ast.idx.name, IntType(), Index(idx_index)))
        env['env'][0].append(Symbol(ast.value.name, arr_type.eleType, Index(value_index)))
        
        # Emit variable declarations
        self.emit.printout(self.emit.emitVAR(idx_index, ast.idx.name, IntType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitVAR(value_index, ast.value.name, arr_type.eleType, frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # Initialize idx = 0
        self.emit.printout(self.emit.emitPUSHICONST(0, frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.idx.name, IntType(), idx_index, frame))
        
        # Emit array code
        self.emit.printout(arr_code)
        
        # Store array reference in a local variable (optional, if needed)
        arr_index = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(arr_index, "arr_temp", arr_type, frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitWRITEVAR("arr_temp", arr_type, arr_index, frame))
        
        # Loop start
        self.emit.printout(self.emit.emitLABEL(this_loop_label, frame))
        
        # Condition: idx < arr.length
        self.emit.printout(self.emit.emitREADVAR(ast.idx.name, IntType(), idx_index, frame))
        self.emit.printout(self.emit.emitREADVAR("arr_temp", arr_type, arr_index, frame))
        self.emit.printout(self.jvm.emitARRAYLENGTH())
        self.emit.printout(self.emit.emitIFICMPGE(this_break_label, frame))
        
        # Load arr[idx] into value
        self.emit.printout(self.emit.emitREADVAR("arr_temp", arr_type, arr_index, frame))
        self.emit.printout(self.emit.emitREADVAR(ast.idx.name, IntType(), idx_index, frame))
        self.emit.printout(self.emit.emitALOAD(arr_type.eleType, frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.value.name, arr_type.eleType, value_index, frame))
        
        # Loop body
        loop_env = env.copy()
        self.visit(ast.loop, loop_env)
        
        # Continue point
        self.emit.printout(self.emit.emitLABEL(this_continue_label, frame))
        
        # Increment idx
        self.emit.printout(self.emit.emitREADVAR(ast.idx.name, IntType(), idx_index, frame))
        self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitIADD())
        self.emit.printout(self.emit.emitWRITEVAR(ast.idx.name, IntType(), idx_index, frame))
        
        # Loop back
        self.emit.printout(self.emit.emitGOTO(this_loop_label, frame))
        
        # Break point
        self.emit.printout(self.emit.emitLABEL(this_break_label, frame))
        
        frame.exitLoop()
        return o

    def visitContinue(self, ast, o):
        frame = o['frame']
        try:
            self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        except Exception as e:
            raise IllegalOperandException("Continue statement outside loop")
        return o

    def visitBreak(self, ast, o):
        frame = o['frame']
        try:
            self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
        except Exception as e:
            raise IllegalOperandException("Break statement outside loop")
        return o
    
    def visitArrayCell(self, ast, o):
        newO = o.copy()
        newO['isLeft'] = False
        
        codeGen, arrType = self.visit(ast.arr, newO)
        frame = o['frame']

        tempArrType = arrType
        
        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            frame.push()  # Track stack for index
            if idx != len(ast.idx) - 1:
                # print(f"tempArrType: {tempArrType}")
                codeGen += self.emit.emitALOAD(tempArrType, o['frame'])
                
                # new: Update type for next dimension
                # tempArrType = tempArrType.eleType if isinstance(tempArrType, ArrayType) else tempArrType  
                tempArrType = ArrayType(tempArrType.dimens[1: ], tempArrType.eleType)
                frame.pop()  # aload consumes arrayref and index, pushes new arrayref

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType 
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
                frame.pop()  # aload consumes arrayref and index, pushes value
            else:
                self.current_array_cell = ast
                self.current_array_cell_type = retType
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx): ], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
                frame.pop()  # aload consumes arrayref and index, pushes subarray
            else:
                self.current_array_cell = ast
                self.current_array_cell_type = retType
                
        return codeGen, retType

    def visitArrayLiteral(self, ast, o):
        def nested2recursive(dat, dims, eleType, frame):
            if not isinstance(dat, list):
                code, _ = self.visit(dat, o)
                if code is None:
                    code = ""
                return code, eleType

            codeGen = ""
            if dims and isinstance(dims[0], IntLiteral):
                codeGen += self.emit.emitPUSHCONST(str(dims[0].value), IntType(), frame)
                frame.push()
            elif dims and isinstance(dims[0], Id):
                sym = next((s for env in o['env'] for s in env if s.name == dims[0].name), None)
                if not sym:
                    raise IllegalOperandException(f"Undefined identifier: {dims[0].name}")
                if not isinstance(sym.mtype, IntType):
                    raise IllegalOperandException(f"Array dimension {dims[0].name} must be IntType")
                if isinstance(sym.value, Index):
                    # Local variable: emit iload
                    codeGen += self.emit.emitREADVAR(dims[0].name, IntType(), sym.value.value, frame)
                else:
                    # Global constant: emit getstatic
                    codeGen += self.emit.emitGETSTATIC(f"{self.className}/{dims[0].name}", IntType(), frame)
                frame.push()
            else:
                # Fallback to data length
                current_dim = len(dat)
                codeGen += self.emit.emitPUSHCONST(str(current_dim), IntType(), frame)
                frame.push()

            if not isinstance(dat[0], list):
                if isinstance(eleType, Id):
                    jvm_type = f"[L{eleType.name};"
                    codeGen += self.emit.emitMULTIANEWARRAY(jvm_type, 1, frame)
                    frame.pop()
                    for idx, item in enumerate(dat):
                        codeGen += self.emit.emitDUP(frame)
                        codeGen += self.emit.emitPUSHCONST(str(idx), IntType(), frame)
                        frame.push()
                        item_code, _ = self.visit(item, o)
                        if item_code is None:
                            item_code = ""
                        codeGen += item_code
                        codeGen += self.emit.emitASTORE(eleType, frame)
                    return codeGen, ArrayType(dims, eleType)
                elif type(eleType) in [IntType, BoolType, FloatType]:
                    codeGen += self.emit.emitNEWARRAY(eleType, frame)
                    frame.pop()
                else:
                    codeGen += self.emit.emitANEWARRAY(eleType, frame)
                    frame.pop()
                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(frame)
                    codeGen += self.emit.emitPUSHCONST(str(idx), IntType(), frame)
                    frame.push()
                    item_code, _ = self.visit(item, o)
                    if item_code is None:
                        item_code = ""
                    codeGen += item_code
                    codeGen += self.emit.emitASTORE(eleType, frame)
                return codeGen, ArrayType(dims, eleType)

            sub_array_type = ArrayType(dims[1:] if dims else [], eleType)
            codeGen += self.emit.emitANEWARRAY(sub_array_type, frame)
            frame.pop()
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(frame)
                codeGen += self.emit.emitPUSHCONST(str(idx), IntType(), frame)
                frame.push()
                item_code, _ = nested2recursive(item, dims[1:] if dims else [], eleType, frame)
                if item_code is None:
                    item_code = ""
                codeGen += item_code
                codeGen += self.emit.emitASTORE(sub_array_type, frame)
            return codeGen, ArrayType(dims, eleType)

        frame = o['frame']
        
        # add 9/5
        if type(ast.value) is ArrayType:
            return self.visit(ast.value, o)
        
        code, ret_type = nested2recursive(ast.value, ast.dimens, ast.eleType, frame)
        if code is None:
            code = ""
        return code, ret_type

    def visitConstDecl(self, ast, o):
        var_decl = VarDecl(ast.conName, ast.conType, ast.iniExpr)
        return self.visit(var_decl, o)
    
    def visitArrayType(self, ast, o):
        codeGen = ""
        frame = o['frame']
        
        for dim in ast.dimens:
            dim_code, _ = self.visit(dim, o)
            codeGen += dim_code
            frame.push()  # Push dimension size onto stack
            
        jvm_type = self.emit.getJVMType(ast)  # e.g., "[[[I" for [1][1][1]int
        dimensions = len(ast.dimens)  # e.g., 3 for [1][1][1]
        codeGen += self.emit.emitMULTIANEWARRAY(jvm_type, dimensions, frame)
        
        return codeGen, ast
    
    def visitFieldAccess(self, ast, o):
        # Visit the receiver to get the code and type 
        code, typ = self.visit(ast.receiver, o)
        if not isinstance(typ, Id):
            raise IllegalOperandException(f"Field access receiver must be Id, got {typ}")
        
        # Look up the field in the struct’s elements using self.list_type[typ.name]
        struct = self.list_type.get(typ.name)
        if not struct or not isinstance(struct, StructType):
            raise IllegalOperandException(f"Type {typ.name} not found or not a struct")
        
        field = next((e for e in struct.elements if e[0] == ast.field), None)
        if not field:
            raise IllegalOperandException(f"Field {ast.field} not found in {typ.name}")
        
        # Generate getfield instruction with the format <class>/<field> <type>
        field_name = f"{typ.name}/{ast.field}"
        field_type = field[1]
        return code + self.emit.emitGETFIELD(field_name, field_type, o['frame']), field_type
    
    def visitMethCall(self, ast, o):
        # print(f"visitMethCall: {ast.metName}, stmt={o.get('stmt')}, receiver={ast.receiver}")
        
        # if o.get('stmt') is None:
            ## print(f"Warning: visitMethCall called with stmt=None for {ast.metName}, returning code without emitting")
            # return "", None
        
        # NOTE: Returns o for statements (void) or (code, rettype) for expressions.
        # Visit the receiver to get its code and type
        frame = o['frame']
        code, typ = self.visit(ast.receiver, o)
        if not isinstance(typ, Id):
            raise IllegalOperandException(f"Method call receiver must be Id, got {typ}")

        type_def = self.list_type.get(typ.name)
        if not type_def:
            raise IllegalOperandException(f"Type {typ.name} not found")

        env = o.copy()
        env['stmt'] = False  # Arguments are expressions

        # print(f"MethodCall: {ast.metName} => {type_def}")
        
        # For StructType:
        # - look up the method in struct.methods, 
        # - generate argument code, 
        # - and use invokevirtual.
        if isinstance(type_def, StructType):
            # print(f"type_def.methods: {type_def.methods}")
            method = next((m for m in type_def.methods if m.fun.name == ast.metName), None)
            if not method:
                raise IllegalOperandException(f"Method {ast.metName} not found in struct {typ.name}")

            # Push receiver to stack
            frame.push()  # Receiver object
            arg_codes = []
            param_types = [param.parType for param in method.fun.params]
            for item in ast.args:
                arg_code, _ = self.visit(item, env)
                arg_codes.append(arg_code)
                frame.push()  # Each argument

            # Generate code: receiver + arguments + invokevirtual
            code += ''.join(arg_codes)
            mtype = MType(param_types, method.fun.retType)
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, frame)
            
            # frame.pop(len(param_types) + 1)  # Pop args + receiver
            num_pop = 1 + len(param_types)  # objref + parameters
            for _ in range(num_pop):
                frame.pop()  # invokespecial consumes objref + parameters
            
            if not isinstance(method.fun.retType, VoidType):
                frame.push()  # Push return value if not void

            if o.get('stmt') is True:
                self.emit.printout(code)
                if not isinstance(method.fun.retType, VoidType):
                    self.emit.printout(self.emit.emitPOP(frame))  # Pop return value in statement context
                    frame.pop()  # Update frame stack
                return o
            return code, mtype.rettype
        
        # For InterfaceType: 
        # - look up the method in interface.prototypes, 
        # - generate argument code, 
        # - and use invokeinterface.
        elif isinstance(type_def, InterfaceType):
            method = next((p for p in type_def.methods if p.name == ast.metName), None)
            if not method:
                raise IllegalOperandException(f"Method {ast.metName} not found in interface {typ.name}")

            # Push receiver to stack
            frame.push()  # Receiver object
            arg_codes = []
            param_types = method.params  # Prototype uses params directly
            for item in ast.args:
                arg_code, _ = self.visit(item, env)
                arg_codes.append(arg_code)
                frame.push()  # Each argument

            # Generate code: receiver + arguments + invokeinterface
            code += ''.join(arg_codes)
            mtype = MType(param_types, method.retType)
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.metName}", mtype, frame)
            # code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, frame)
            
            # frame.pop(len(param_types) + 1)  # Pop args + receiver
            num_pop = 1 + len(param_types)  # objref + parameters
            for _ in range(num_pop):
                frame.pop()  # invokespecial consumes objref + parameters
            
            if not isinstance(method.retType, VoidType):
                frame.push()  # Push return value if not void

            if o.get('stmt') is True:
                self.emit.printout(code)
                if not isinstance(method.retType, VoidType):
                    self.emit.printout(self.emit.emitPOP(frame))  # Pop return value in statement context
                    frame.pop()  # Update frame stack
                return o
            return code, mtype.rettype
        
        raise IllegalOperandException(f"Type {typ.name} is neither StructType nor InterfaceType")

    # after 1/5
    def visitStructLiteral(self, ast, o):
        frame = o['frame']
        
        # Create struct instance
        code = self.emit.emitNEW(ast.name, frame)
        frame.push()  # Track objref
        code += self.emit.emitDUP(frame)
        frame.push()  # Track duplicated objref
        
        struct = self.list_type.get(ast.name)
        if not struct or not isinstance(struct, StructType):
            raise IllegalOperandException(f"Struct {ast.name} not found")
        
        # Map provided elements to their field names
        provided_fields = {name: value for name, value in ast.elements}
        
        # Collect constructor arguments based on struct's field definitions
        param_types = []
        param_codes = []
        for field_name, field_type in struct.elements:
            if field_name in provided_fields:
                # Visit the initializer expression
                field_code, _ = self.visit(provided_fields[field_name], o)
                param_codes.append(field_code)
                frame.push()  # Track parameter value
            else:
                # Default initialization (e.g., null for reference types)
                if isinstance(field_type, Id):  # Struct or interface
                    param_codes.append(self.emit.emitPUSHNULL(frame))
                elif isinstance(field_type, IntType):
                    param_codes.append(self.emit.emitPUSHICONST(0, frame))
                elif isinstance(field_type, FloatType):
                    param_codes.append(self.emit.emitPUSHFCONST(0.0, frame))
                elif isinstance(field_type, BoolType):
                    param_codes.append(self.emit.emitPUSHICONST(0, frame))
                elif isinstance(field_type, StringType):
                    param_codes.append(self.emit.emitPUSHCONST("\"\"", StringType(), frame))
                else:
                    raise IllegalOperandException(f"Unsupported field type: {field_type}")
                frame.push()  # Track parameter value
            
            # Use the field's declared type for the constructor signature
            param_types.append(field_type)
        
        # Generate code for constructor parameters
        for param_code in param_codes:
            code += param_code
        
        # Call parameterized constructor
        mtype = MType(param_types, VoidType())
        code += self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", mtype)
        num_pop = 1 + len(param_types)  # objref + parameters
        for _ in range(num_pop):
            frame.pop()  # invokespecial consumes objref + parameters
        
        frame.push()  # Resulting objref
        return code, Id(ast.name)
    
    def visitNilLiteral(self, ast, o):
        """
        Use emitPUSHNULL to push aconst_null onto the stack.
        Return Id("") as the type, representing a null reference compatible with any struct/interface.
        """
        # print(f"NilLiteral: => null")
        return self.emit.emitPUSHNULL(o['frame']), Id("")
    
    def visitStructType(self, ast, o):
        # Generate prolog
        interfaces = [item.name for item in self.list_type.values() if isinstance(item, InterfaceType) and self.checkType(item, ast, [(InterfaceType, StructType)])]
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java/lang/Object", interface=False).replace(".field", ".field public"))
        
        # Emit implemented interfaces
        for iface in interfaces:
            self.emit.printout(f".implements {iface}\n")
        
        # Emit fields
        for name, typ in ast.elements:
            field_code = self.emit.emitATTRIBUTE(name, typ, False, False, None)
            self.emit.printout(field_code.replace(".field", ".field public"))
        
        # Parameterized constructor
        params = [ParamDecl(f"param_{name}", typ) for name, typ in ast.elements]
        body = [Assign(FieldAccess(Id("this"), name), Id(f"param_{name}")) for name, _ in ast.elements]
        self.visit(MethodDecl(None, Id(ast.name), FuncDecl("<init>", params, VoidType(), Block(body))), o)
        
        # Empty constructor
        self.visit(MethodDecl(None, Id(ast.name), FuncDecl("<init>", [], VoidType(), Block([]))), o)
        
        # Visit methods
        for item in getattr(ast, 'methods', []):
            self.visit(item, o)
        
        # End file - now in visitProgram
        # self.emit.printout(self.emit.emitEPILOG())

    def visitInterfaceType(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "", interface=True))
        
        for proto in ast.methods:
            mtype = MType([p for p in proto.params], proto.retType)
            # Old 
            # self.emit.printout(self.emit.emitMETHOD(proto.name, mtype, False, None))
            # New: Add 'abstract' modifier and .end method
            method_code = self.emit.emitMETHOD(proto.name, mtype, False, None)
            method_code = method_code.replace(".method public", ".method public abstract") + "\n.end method\n"
            self.emit.printout(method_code)
        
        # self.emit.printout(self.emit.emitEPILOG())

    # new 9/5
    def visitMethodDecl(self, ast, o):
        self.func_current = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType([p.parType for p in ast.fun.params], ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        
        # Debug: Print the initial global environment
        # print(f"Initial env['env'][0] for method {ast.fun.name}: {[s.name for s in env['env'][0]]}")
        
        # Find the position of the StructType (PPL3) in astTree.decl
        struct_index = 0
        struct_decl = None
        for i, decl in enumerate(self.astTree.decl):
            if isinstance(decl, StructType) and decl.name == ast.recType.name:
                struct_index = i
                struct_decl = decl
                break
        
        method_global_index = 0
        for i, decl in enumerate(self.astTree.decl):
            if isinstance(decl, MethodDecl) and decl.fun.name == ast.fun.name:
                method_global_index = i
                break
        
        # Debug: Print the struct index
        # print(f"StructType {ast.recType.name} found at index: {struct_index}")
        
        # Find the position of the current MethodDecl within the struct's methods
        method_index = 0
        for i, method in enumerate(struct_decl.methods):
            if method is ast:
                method_index = i
                break
        
        # Debug: Print the method index within the struct
        # print(f"Method {ast.fun.name} found at index {method_index} within {ast.recType.name}.methods")
        
        # Include global symbols declared before the StructType
        global_symbols = []
        for i, decl in enumerate(self.astTree.decl[:method_global_index]):
            if isinstance(decl, (VarDecl, ConstDecl)):
                sym = next((s for s in env['env'][0] if s.name == (decl.varName if isinstance(decl, VarDecl) else decl.conName)), None)
                if sym:
                    global_symbols.append(sym)
        
        # Include global symbols declared after the StructType up to the method's logical position
        effective_index = min(struct_index + method_index + 1, len(self.astTree.decl))
        for i, decl in enumerate(self.astTree.decl[struct_index + 1:effective_index]):
            if isinstance(decl, (VarDecl, ConstDecl)):
                sym = next((s for s in env['env'][0] if s.name == (decl.varName if isinstance(decl, VarDecl) else decl.conName)), None)
                if sym and sym not in global_symbols:
                    global_symbols.append(sym)
        
        # Debug: Print the global symbols included
        # print(f"Global symbols for method {ast.fun.name}: {[s.name for s in global_symbols]}")
        
        # Set the environment with a new local scope and the filtered global scope
        env['env'] = [[]] + [global_symbols]
        
        # Debug: Print the final environment
        # print(f"Final env for method {ast.fun.name}: {[s.name for s in env['env'][0]] + [s.name for s in env['env'][1]]}")
        
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)
        
        # Add 'this' variable with correct type
        this_type = ast.recType  # Id(PPL3)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(this_type.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # Add parameters (emit .var for each parameter)
        env = reduce(lambda acc, e: self.visit(e, acc), ast.fun.params, env)
        
        # Emit start label *after* all .var directives
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # Constructor: Call super()
        if ast.fun.name == "<init>":
            self.emit.printout(self.emit.emitREADVAR("this", Id(this_type.name), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # Visit body
        self.visit(ast.fun.body, env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def checkType(self, interface, struct, type_pairs):
        # Check if the type pair is valid
        valid_pair = any(isinstance(interface, pair[0]) and isinstance(struct, pair[1]) for pair in type_pairs)
        if not valid_pair:
            return False
        
        # Ensure interface is InterfaceType and struct is StructType
        if not (isinstance(interface, InterfaceType) and isinstance(struct, StructType)):
            return False
        
        # Get interface and struct methods
        interface_methods = interface.methods  # List of FuncDecl (prototypes)
        struct_methods = getattr(struct, 'methods', [])  # List of MethodDecl
        
        # Helper function to compare method signatures
        def method_matches(iface_method, struct_method):
            # Check method name
            if iface_method.name != struct_method.fun.name:
                return False
            
            # Check return type
            if not self.is_same_type(iface_method.retType, struct_method.fun.retType):
                return False
            
            # Check parameter types
            iface_params = [p for p in iface_method.params]
            struct_params = [p.parType for p in struct_method.fun.params]
            if len(iface_params) != len(struct_params):
                return False
            return all(self.is_same_type(iface_p, struct_p) for iface_p, struct_p in zip(iface_params, struct_params))
        
        # Check if every interface method has a matching struct method
        for iface_method in interface_methods:
            if not any(method_matches(iface_method, struct_method) for struct_method in struct_methods):
                return False
        
        return True

    def is_same_type(self, type1, type2):
        # Compare two types for equality
        if type(type1) != type(type2):
            return False
        if isinstance(type1, Id):
            return type1.name == type2.name
        if isinstance(type1, ArrayType):
            return (type1.dimens == type2.dimens and 
                    self.is_same_type(type1.eleType, type2.eleType))
        return True  # For primitive types (IntType, FloatType, etc.)


# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

# 6/5/2025
# - fix visitbinaryop of == of booltype 
# - fix the bug at visitreturn, forget to change the  o['stmt'] to false when visit the expr
