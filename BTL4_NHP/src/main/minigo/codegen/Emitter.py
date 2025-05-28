# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu

from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from CodeGenError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value, isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType:
    def __init__(self, name):
        #value: Id
        self.name = name

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    

class Emitter():
    def __init__(self, filename):
        """Initializes the Emitter for generating Jasmin code."""
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        """Converts an internal compiler type representation to its JVM type descriptor.

        Args:
            inType (Type): An instance representing a type in the source language
                           (e.g., IntType, FloatType, BoolType, StringType, VoidType,
                           ArrayType, MType, cgen.ClassType).

        Returns:
            str: The corresponding JVM type descriptor string (e.g., "I", "F", "Z",
                 "Ljava/lang/String;", "V", "[I", "(II)V", "Lcom/example/MyClass;").
                 Returns the string representation of the type if no specific
                 mapping exists.
        """
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        if typeIn is FloatType:
            ## TODO implement
            return "F"
        if typeIn is BoolType:
            return "Z"   
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            # return "[" + self.getJVMType(inType.eleType)
            # Count the number of dimensions
            dims = len(inType.dimens) if inType.dimens else 1
            return "[" * dims + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        # elif type(in_) in (ArrayType, ClassType, StringType, Id):
        
        # old 
        # elif typeIn is cgen.ClassType:
        #     return "L" + inType.name + ";"
        
        # new 
        elif typeIn in (cgen.ClassType, Id):
            return "L" + inType.name + ";"
        
        else:
            print("Hello i am here bro in getJVMType")
            return str(typeIn)

    def getFullType(inType):
        """(Static Method) Converts an internal compiler type to its full Java type name.

        Note: This implementation appears incomplete in the provided code.

        Args:
            inType (Type): An instance representing a type (e.g., IntType,
                           cgen.StringType, VoidType).

        Returns:
            str: The full Java type name (e.g., "int", "java/lang/String", "void").
        """
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"

    # NOTE: some one ask this on the forum, do not know why but yeh note here
    def emitPUSHICONST(self, in_, frame):
        """Generates code to push an integer or boolean constant onto the operand stack.

        Selects the most efficient JVM instruction (iconst, bipush, sipush)
        based on the value. Handles boolean values represented as strings
        "true" (1) or "false" (0). Updates the frame's operand stack simulation.

        Args:
            `in_` (int or str): The integer value or string representation
                              ("true", "false", or numeric string) to push.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin instruction(s).
        """
        #in: Int or Sring
        #frame: Frame
        frame.push()
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            # if in_ == "true":
            #     return self.emitPUSHICONST(1, frame)
            # elif in_ == "false":
            #     return self.emitPUSHICONST(0, frame)
            # else:
                # return self.emitPUSHICONST(int(in_), frame)
            if in_ == "true":
                return self.jvm.emitICONST(1)
            elif in_ == "false":
                return self.jvm.emitICONST(0)
            else:
                try:
                    i = int(in_)
                    if i >= -1 and i <= 5:
                        return self.jvm.emitICONST(i)
                    elif i >= -128 and i <= 127:
                        return self.jvm.emitBIPUSH(i)
                    elif i >= -32768 and i <= 32767:
                        return self.jvm.emitSIPUSH(i)
                    else:
                        return self.jvm.emitLDC(i)
                except ValueError:
                    raise IllegalOperandException(f"Invalid numeric string {in_} for PUSHICONST")
        raise IllegalOperandException(f"Invalid constant {in_} for PUSHICONST")

    def emitPUSHFCONST(self, in_, frame):
        """Generates code to push a float constant onto the operand stack.

        Uses fconst_0, fconst_1, fconst_2 for 1.0 2.0 3.0, otherwise uses ldc.
        Updates the frame's operand stack simulation.

        Args:
            `in_` (str): The string representation of the float value to push.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin instruction(s).
        """
        #in_: String
        #frame: Frame
        
        f = float(in_)
        frame.push()
        if f == 0.0 or f == 1.0 or f == 2.0:
            return self.jvm.emitFCONST("{0:.1f}".format(f))
        else:
            return self.jvm.emitLDC(str(f))     

    def emitPUSHCONST(self, in_, typ, frame):
        """Generates code to push a constant onto the operand stack.

        Args:
            `in_` (str): The string representation of the constant value.
            typ (Type): The type of the constant (IntType, BoolType, StringType).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin instruction(s).

        Raises:
            IllegalOperandException: If the type is not supported for constants.
        """
        #in_: String
        #typ: Type
        #frame: Frame
        
        if type(typ) is IntType or type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        """Generates array load instruction (iaload, faload, aaload etc.).

        Pops array reference and index from the stack, pushes the element value.
        Updates the frame's operand stack simulation accordingly.

        Args:
            `in_` (Type): The type of the elements in the array (determines which
                        load instruction to use, e.g., IntType -> iaload).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin array load instruction.

        Raises:
            IllegalOperandException: If the element type is not supported.
        """
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) in (ArrayType, ClassType, StringType, Id):
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        """Generates array store instruction (iastore, fastore, aastore etc.).

        Pops array reference, index, and value from the stack. Updates the frame's
        operand stack simulation accordingly.

        Args:
            `in_` (Type): The type of the elements in the array (determines which
                        store instruction to use, e.g., IntType -> iastore).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin array store instruction.

        Raises:
            IllegalOperandException: If the element type is not supported.
        """
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        # frame.pop()
        # frame.pop()
        # frame.pop()
        # if type(in_) is IntType:
        #     return self.jvm.emitIASTORE()
        # elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
        #     return self.jvm.emitAASTORE()
        # else:
        #     raise IllegalOperandException(str(in_))
        
        frame.pop()  # Pop value
        frame.pop()  # Pop index
        frame.pop()  # Pop arrayref

        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) in (ArrayType, ClassType, StringType, Id):
            # Validate ArrayType dimensions if necessary
            if type(in_) is ArrayType:
                # Ensure the ArrayType is valid for aastore (reference type)
                jvm_type = self.getJVMType(in_)
                if not jvm_type.startswith("["):  # Must be a reference type
                    raise IllegalOperandException(f"Invalid ArrayType for aastore: {jvm_type}")
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(f"Unsupported type for astore: {in_}")

    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        """Generates the .var directive for a local variable's debug information.

        Specifies the variable's index, name, type descriptor, and the scope
        (defined by start and end labels) within which it is active.

        Args:
            `in_` (int): The index of the local variable slot.
            varName (str): The name of the local variable.
            inType (Type): The type of the local variable.
            fromLabel (int): The label marking the beginning of the variable's scope.
            toLabel (int): The label marking the end of the variable's scope.
            frame (Frame): The current execution frame (used indirectly by getJVMType).

        Returns:
            str: The generated Jasmin '.var' directive line.
        """
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        """Generates code to load a local variable onto the operand stack.

        Selects the appropriate load instruction (iload, fload, aload) based
        on the variable's type. Updates the frame's operand stack simulation.

        Args:
            name (str): The name of the variable (primarily for error reporting).
            inType (Type): The type of the variable to load.
            index (int): The index of the local variable slot.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin load instruction.

        Raises:
            IllegalOperandException: If the variable type is not supported for loading.
        """
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value
        
        frame.push()
        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            ## TODO implement
            return self.jvm.emitFLOAD(index)  # Fixed: Use index directly
        elif type(inType) in [ArrayType, StringType, ClassType, Id]:  
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitREADVAR2(self, name, typ, frame):
        """Placeholder for potentially generating a second instruction for complex variable access (e.g., array cell).

        Note: The current implementation always raises an exception.

        Args:
            name (str): The name associated with the access.
            typ (Type): The type involved in the access.
            frame (Frame): The current execution frame.

        Raises:
            IllegalOperandException: Always raised in the provided code.
        """
        #name: String
        #typ: Type
        #frame: Frame
        #... -> ..., value

        #frame.push()
        raise IllegalOperandException(name)

    def emitWRITEVAR(self, name, inType, index, frame):
        """Generates code to pop a value on top of the operand stack and store it to a block-scoped variable.

        Selects the appropriate store instruction (istore, fstore, astore) based
        on the variable's type. Updates the frame's operand stack simulation.

        Args:
            name (str): The name of the variable (primarily for error reporting).
            inType (Type): The type of the variable to store into.
            index (int): The index of the local variable slot.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin store instruction.

        Raises:
            IllegalOperandException: If the variable type is not supported for storing.
        """
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...
        
        frame.pop()

        if type(inType) is IntType or type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            ## TODO implement
            return self.jvm.emitFSTORE(index)  # Fixed: Implement FloatType
        # elif type(inType) is cgen.ArrayType or type(inType) is cgen.ClassType or type(inType) is StringType:
        #     return self.jvm.emitASTORE(index)
        elif type(inType) in [ArrayType, StringType, ClassType, Id]: 
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitWRITEVAR2(self, name, typ, frame):
        """Placeholder for potentially generating a second instruction for complex variable storage (e.g., array cell).

        Note: The current implementation always raises an exception.

        Args:
            name (str): The name associated with the storage operation.
            typ (Type): The type involved in the storage.
            frame (Frame): The current execution frame.

        Raises:
            IllegalOperandException: Always raised in the provided code.
        """
        #name: String
        #typ: Type
        #frame: Frame
        #..., value -> ...

        #frame.push()
        raise IllegalOperandException(name)

    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value):
        """Generates the .field directive for a class attribute (static or instance) / for a class mutable or immutable attribute.

        Args:
            lexeme (str): The name of the attribute/field.
            `in_` (Type): The type of the attribute.
            isStatic (bool): True if the field is static, False for instance fields.
            isFinal (bool): True if the field is final (constant), False otherwise.
            value (str or None): Initial value for static final fields, or None.

        Returns:
            str: The generated Jasmin '.field' directive line.
        """
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String
        jvm_type = self.getJVMType(in_)
        if isStatic:
            return self.jvm.emitSTATICFIELD(lexeme, jvm_type, isFinal, value)
        else:
            return self.jvm.emitINSTANCEFIELD(lexeme, jvm_type, isFinal, value)

    def emitGETSTATIC(self, lexeme, in_, frame):
        """Generates the getstatic instruction to load a static field onto the stack.

        Updates the frame's operand stack simulation.

        Args:
            lexeme (str): The qualified name of the static field (e.g., "ClassName/fieldName").
            `in_` (Type): The type of the static field.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'getstatic' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        """Generates the putstatic instruction to store a value into a static field.

        Pops the value from the operand stack. Updates the frame's operand
        stack simulation.

        Args:
            lexeme (str): The qualified name of the static field (e.g., "ClassName/fieldName").
            `in_` (Type): The type of the static field.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'putstatic' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        """Generates the getfield instruction to load an instance field onto the stack.

        Pops the object reference from the stack, pushes the field value.
        Updates the frame's operand stack simulation (net effect is neutral).

        Args:
            lexeme (str): The qualified name of the instance field (e.g., "ClassName/fieldName").
            `in_` (Type): The type of the instance field.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'getfield' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        """Generates the putfield instruction to store a value into an instance field.

        Pops the value and the object reference from the stack. Updates the frame's
        operand stack simulation.

        Args:
            lexeme (str): The qualified name of the instance field (e.g., "ClassName/fieldName").
            `in_` (Type): The type of the instance field.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'putfield' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    def emitINVOKESTATIC(self, lexeme, in_, frame):
        """Generates the invokestatic instruction for calling a static method.

        Updates the frame's operand stack simulation by popping arguments
        and pushing the return value (if not void).

        Args:
            lexeme (str): The qualified name of the static method (e.g., "ClassName/methodName").
            `in_` (MType): The method type descriptor (parameter types and return type).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'invokestatic' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        """Generates the invokespecial instruction.

        Used primarily for calling constructors, private methods, and superclass methods.
        If lexeme and `in_` are provided, it simulates popping arguments and the
        object reference, and pushing a return value if applicable.
        If lexeme and `in_` are None, it assumes a specific context (like default
        constructor call) and just pops the object reference.

        Args:
            frame (Frame): The current execution frame for stack tracking.
            lexeme (str, optional): Qualified name ("ClassName/methodName", typically `<init>`). Defaults to None.
            `in_` (MType, optional): Method type descriptor. Defaults to None.

        Returns:
            str: The generated Jasmin 'invokespecial' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        """Generates the invokevirtual instruction for calling an instance method.

        Updates the frame's operand stack simulation by popping arguments and
        the object reference, and pushing the return value (if not void).

        Args:
            lexeme (str): The qualified name of the instance method (e.g., "ClassName/methodName").
            `in_` (MType): The method type descriptor (parameter types and return type).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'invokevirtual' instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    def emitINVOKEINTERFACE(self, lexeme, in_, frame):
        typ = in_
        # Stack simulation: pop receiver + arguments, push return value if non-void
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()  # Pop receiver
        if not type(typ.rettype) is VoidType:
            frame.push()  # Push return value
        # Calculate n: number of argument slots + 1 (receiver)
        param_count = len(typ.partype)  # Each parameter is 1 slot
        n = param_count + 1  # Receiver + arguments
        # Manually generate invokeinterface instruction
        return f"\tinvokeinterface {lexeme}{self.getJVMType(typ)} {n}\n"

    def emitNEGOP(self, in_, frame):
        """Generates the negation instruction (ineg or fneg).

        Operates on the top value of the stack without changing stack depth.

        Args:
            `in_` (Type): The type of the operand (IntType or FloatType).
            frame (Frame): The current execution frame.

        Returns:
            str: The generated Jasmin 'ineg' or 'fneg' instruction.
        """
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        """Generates code to perform logical negation (boolean NOT).

        Expects a boolean value (0 or 1) on the stack. Uses conditional jumps
        and constant pushing to replace the value with its logical opposite.
        Does not change the net stack depth.

        Args:
            `in_` (Type): The type of the operand (expected to be BoolType or IntType).
            frame (Frame): The current execution frame for stack/label management.

        Returns:
            str: A sequence of Jasmin instructions implementing logical NOT.
        """
        #in_: Type
        #frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    def emitADDOP(self, lexeme, in_, frame):
        """Generates addition or subtraction instructions (iadd, fadd, isub, fsub).

        Pops two operands, pushes one result. Updates the frame's stack simulation.

        Args:
            lexeme (str): The operator ("+" or "-").
            `in_` (Type): The type of the operands (IntType or FloatType).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin arithmetic instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    def emitMULOP(self, lexeme, in_, frame):
        """Generates multiplication or division instructions (imul, fmul, idiv, fdiv).

        Pops two operands, pushes one result. Updates the frame's stack simulation.

        Args:
            lexeme (str): The operator ("*" or "/").
            `in_` (Type): The type of the operands (IntType or FloatType).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin arithmetic instruction.
        """
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        """
        Generates the integer division instruction (idiv).

        Pops two operands, pushes one result. Updates the frame's stack simulation.
        Assumes integer operands.
        """
        #frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        """
        NOTE: not know why currently like this, recheck please
        Generates the integer remainder instruction (irem).

        Pops two operands, pushes one result. Updates the frame's stack simulation.
        Assumes integer operands.
        """
        #frame: Frame

        frame.pop()
        # return "\tirem\n"
        return self.jvm.emitIREM()

    def emitANDOP(self, frame):
        """
        Generates the bitwise AND instruction (iand).

        Pops two integer operands, pushes one integer result. Updates the frame's
        stack simulation.
        """
        #frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    def emitOROP(self, frame):
        """
        Generates the bitwise OR instruction (ior).

        Pops two integer operands, pushes one integer result. Updates the frame's
        stack simulation.
        """
        #frame: Frame

        frame.pop()
        return self.jvm.emitIOR()
    
    def emitIFNE(self, label, frame):
        """Generates the 'ifne' instruction to jump to a label if the top stack value is non-zero.

        Pops one value from the stack. Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if the value is non-zero.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'ifne' instruction.
        """
        frame.pop()
        return self.jvm.emitIFNE(label)

    def emitIFEQ(self, label, frame):
        """Generates the 'ifeq' instruction to jump to a label if the top stack value is zero.

        Pops one value from the stack. Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if the value is zero.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'ifeq' instruction.
        """
        frame.pop()
        return self.jvm.emitIFEQ(label)
    
    def emitREOP(self, op, in_, frame):
        """Generates code for relational operators (>, >=, <, <=, !=, ==) resulting in a boolean value (0 or 1).

        Pops two operands. Uses conditional jumps and constant pushing to place
        1 (true) or 0 (false) onto the stack. Updates the frame's stack simulation.

        Args:
            op (str): The relational operator string (e.g., ">", "==").
            `in_` (Type): The type of the operands being compared (IntType or FloatType).
            frame (Frame): The current execution frame for stack/label management.

        Returns:
            str: A sequence of Jasmin instructions implementing the comparison.
        """
        #op: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            if op == ">":
                result.append(self.jvm.emitIFICMPLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFICMPLT(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFICMPGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFICMPGT(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFICMPEQ(labelF))
            elif op == "==":
                result.append(self.jvm.emitIFICMPNE(labelF))
        elif type(in_) is FloatType:
            ## TODO implement
            result.append(self.jvm.emitFCMPL())  # Compare floats
            if op == ">":
                result.append(self.jvm.emitIFLE(labelF))  # Jump if result <= 0
            elif op == ">=":
                result.append(self.jvm.emitIFLT(labelF))  # Jump if result < 0
            elif op == "<":
                result.append(self.jvm.emitIFGE(labelF))  # Jump if result >= 0
            elif op == "<=":
                result.append(self.jvm.emitIFGT(labelF))  # Jump if result > 0
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(labelF))  # Jump if result == 0
            elif op == "==":
                result.append(self.jvm.emitIFNE(labelF))  # Jump if result != 0
                
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        """Generates code for relational operators used in conditional branching.

        Pops two operands. Emits a conditional jump instruction that branches to
        `falseLabel` if the condition is false, followed by an unconditional jump
        to `trueLabel`. Updates the frame's stack simulation.

        Args:
            op (str): The relational operator string (e.g., ">", "==").
            `in_` (Type): The type of the operands being compared (usually IntType).
            trueLabel (int): The label to jump to if the condition is true.
            falseLabel (int): The label to jump to if the condition is false.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: A sequence of Jasmin instructions implementing the conditional branch.
        """
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        """Generates the .method directive to start a method definition / for a function

        Includes access modifiers (public, static if `isStatic` is true),
        the method name, and the JVM method descriptor.

        Args:
            lexeme (str): the qualified name of the method(i.e., class-name/method-name).
            `in_` (MType): the type descriptor of the method.
            isStatic (bool): True if the method is static, False otherwise.
            frame (Frame): The current execution frame (used indirectly by getJVMType).

        Returns:
            str: The generated Jasmin '.method' directive line.
        """
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    def emitENDMETHOD(self, frame):
        """Generates directives to end a method/function definition.

        Includes .limit stack, .limit locals, and .end method directives,
        using stack and local variable limits calculated by the frame.

        Args:
            frame (Frame): The execution frame holding max stack and local info.

        Returns:
            str: The combined Jasmin directives for ending a method.
        """
        #frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        """Extracts the value and type from a literal AST node.

        Args:
            ast (Literal): An AST node representing a literal (e.g., IntLiteral).

        Returns:
            tuple: A tuple containing (str representation of value, Type instance).
                   Returns None or raises error if AST node is not a recognized literal.
        """
        #ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''
    # I do not know why this is here for what ?

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''
    # I do not know why this is here for what ?

    def emitIFTRUE(self, label, frame):
        """Generates code to jump to a label if the top stack value is true (non-zero).

        Pops one value from the stack. Uses the 'ifgt' (if greater than zero) instruction.
        Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if the value is true.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'ifgt' instruction.
        """
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    def emitIFFALSE(self, label, frame):
        """Generates code to jump to a label if the top stack value is false (zero).

        Pops one value from the stack. Uses the 'ifle' (if less than or equal to zero)
        instruction. Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if the value is false.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'ifle' instruction.
        """
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)
    
    def emitIFICMPGE(self, label, frame):
        """Generates code to compare two integers and jump if the first is greater than or equal to the second.

        Pops two integer values from the stack. Uses the 'if_icmpge' instruction.
        Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if value1 >= value2.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'if_icmpge' instruction.
        """
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPGE(label)

    def emitIFICMPGT(self, label, frame):
        """Generates code to compare two integers and jump if the first is greater than the second.

        Pops two integer values from the stack. Uses the 'if_icmpgt' instruction.
        Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if value1 > value2.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'if_icmpgt' instruction.
        """
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)
    
    def emitIFICMPLE(self, label, frame):
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPLE(label)

    def emitIFICMPNE(self, label, frame):
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPNE(label)

    def emitIFICMPEQ(self, label, frame):
        frame.pop()
        frame.pop()
        return self.jvm.emitIFICMPEQ(label)

    def emitIFICMPLT(self, label, frame):
        """Generates code to compare two integers and jump if the first is less than the second.

        Pops two integer values from the stack. Uses the 'if_icmplt' instruction.
        Updates the frame's stack simulation.

        Args:
            label (int): The target label to jump to if value1 < value2.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'if_icmplt' instruction.
        """
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)    

    def emitDUP(self, frame):
        """Generates the 'dup' instruction to duplicate the top value on the operand stack.

        Updates the frame's stack simulation.
        *   Stack:<p>
        *   Before: ...,value1<p>
        *   After:  ...,value1,value1<p>

        Args:
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'dup' instruction.
        """
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        """Generates the 'pop' instruction to discard the top value on the operand stack.

        Updates the frame's stack simulation.

        Args:
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'pop' instruction.
        """
        #frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    def emitI2F(self, frame):
        """Generates the 'i2f' instruction to convert an integer to a float on the stack.

        Does not change the stack depth.

        Args:
            frame (Frame): The current execution frame.

        Returns:
            str: The generated Jasmin 'i2f' instruction.
        """
        #frame: Frame

        return self.jvm.emitI2F()

    def emitRETURN(self, in_, frame):
        """Generates the appropriate return instruction based on the return type.

        Selects ireturn, freturn, areturn, or return for Int/Bool, Float,
        Reference types, or Void respectively. Pops the return value if applicable.
        Updates the frame's stack simulation.

        Args:
            `in_` (Type): The return type of the method.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin return instruction.
        """
        #in_: Type
        #frame: Frame

        if type(in_) is IntType or type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()  
        elif type(in_) is StringType:
            frame.pop()
            return self.jvm.emitARETURN()                 
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        # elif type(in_) is ArrayType:
        elif type(in_) in (ArrayType, ClassType, Id):
            return self.jvm.emitARETURN()

    def emitLABEL(self, label, frame):
        """Generates a label definition in the Jasmin code.

        Args:
            label (int): The integer identifier for the label.
            frame (Frame): The current execution frame.

        Returns:
            str: The generated Jasmin label definition (e.g., `Label<label>:`).
        """
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    def emitGOTO(self, label, frame):
        """Generates an unconditional jump ('goto') instruction.

        Args:
            label (int or str): The target label identifier.
            frame (Frame): The current execution frame.

        Returns:
            str: The generated Jasmin 'goto' instruction.
        """
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(str(label))

    def emitPROLOG(self, name, parent, interface=False):
        """Generates the starting directives for a Jasmin class file.

        Includes .source, .class, and .super directives.
        *   .source MPC.CLASSNAME.java<p>
        *   .class public MPC.CLASSNAME<p>
        *   .super java/lang/Object<p>

        Args:
            name (str): The name of the class being generated.
            parent (str): The name of the superclass (or "" for java/lang/Object).

        Returns:
            str: The combined Jasmin directives for the class prolog.
        """
        #name: String
        #parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS(f"public {'interface' if interface else ''} {name}"))
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        """Generates the .limit stack directive.

        Args:
            num (int): The maximum operand stack depth required.

        Returns:
            str: The generated Jasmin '.limit stack' directive.
        """
        #num: Int
        
        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        """Generates the .limit locals directive.

        Args:
            num (int): The maximum number of local variable slots required.

        Returns:
            str: The generated Jasmin '.limit locals' directive.
        """
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        """Writes the accumulated Jasmin code buffer to the output file.
        """
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        """Appends a string of generated code to the internal buffer.
        Print out the code to screen

        Args:
            `in_`(str): The Jasmin code snippet to append/be printed out.
        """
        #in_: String

        self.buff.append(in_)

    def clearBuff(self):
        """Clears the internal buffer holding the generated code.
        """
        self.buff.clear()

    def emitNEWARRAY(self, in_, frame):
        """Generates the newarray instruction to create an array of primitive types.

        Args:
            in_ (Type): The type of the array elements (e.g., IntType, BoolType, FloatType).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'newarray' instruction.
        """
        frame.push()  # newarray consumes size and pushes arrayref
        if type(in_) is IntType:
            return self.jvm.emitNEWARRAY("int")
        elif type(in_) is BoolType:
            return self.jvm.emitNEWARRAY("boolean")
        elif type(in_) is FloatType:
            return self.jvm.emitNEWARRAY("float")
        else:
            raise IllegalOperandException(f"Unsupported type for newarray: {in_}")

    def emitANEWARRAY(self, in_, frame):
        """Generates the anewarray instruction to create an array of reference types.

        Args:
            in_ (Type): The type of the array elements (e.g., StringType, ArrayType, ClassType).
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'anewarray' instruction.
        """
        frame.push()  # anewarray consumes size and pushes arrayref
        jvm_type = self.getJVMType(in_)
        # Map JVM type to Jasmin type for anewarray
        if isinstance(in_, cgen.ArrayType):
            jasmin_type = jvm_type  # e.g., "[I" for 1D int array
        else:
            jasmin_type = {
                "Ljava/lang/String;": "java/lang/String",
                "[I": "[I",
                "[Z": "[Z",
                "[F": "[F",
                "[Ljava/lang/String;": "[java/lang/String"
            }.get(jvm_type, jvm_type.lstrip("L").rstrip(";"))
        return self.jvm.emitANEWARRAY(jasmin_type)

    def emitMULTIANEWARRAY(self, typ, dimensions, frame):
        """Generates the multianewarray instruction to create a multi-dimensional array.

        Args:
            typ (str): The JVM type descriptor of the array (e.g., '[[[I' for a 3D int array).
            dimensions (int): The number of dimensions to allocate.
            frame (Frame): The current execution frame for stack tracking.

        Returns:
            str: The generated Jasmin 'multianewarray' instruction.
        """
        for _ in range(dimensions):
            frame.pop()  # Pop each dimension size from the stack
        frame.push()  # Push the array reference onto the stack
        return self.jvm.emitMULTIANEWARRAY(typ, str(dimensions))

    # TODO
    def emitNEW(self, lexeme, frame):
        frame.push()
        return self.jvm.emitNEW(lexeme)

    # TODO
    def emitPUSHNULL(self, frame):
        frame.push()
        return self.jvm.emitPUSHNULL()
       
       
       
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu
# 2252621 - Nguyen Quang Phu