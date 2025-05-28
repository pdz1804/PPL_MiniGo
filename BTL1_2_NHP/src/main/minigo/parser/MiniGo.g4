// 2252621 

// Nguyen Quang Phu

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preTokenType = None

def emit(self):
    tk = self.type
    prevTk = self.preTokenType  # Store the previous token type
    self.preTokenType = tk  # Update preTokenType for next token

    # Handling newline conversion logic
    if tk == self.NEWLINE:
        # Convert \n to ; if preceded by specific tokens
        if prevTk in {self.ID, self.INT_LIT, self.FLOAT_LIT, self.TRUE, 
					  self.FALSE, self.NIL, self.STRING_LIT, 
					  self.STRING, self.INT, self.FLOAT, self.BOOL,
                      self.RETURN, self.CONTINUE, self.BREAK, 
                      self.R_CLOSE, self.SQ_CLOSE, self.CUR_CLOSE}:
            self.text = ";"  # Convert newline to semicolon
            self.type = self.SEMI_COLON  # Change token type
            return super().emit()
        else:
            self.skip()  # Ignore newline
            return self.nextToken()

    # Handling errors
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// ---------------------------------------------- // ---------------- PASER ----------------------- // ---------------------------------------------- //
program: program_lst EOF;
program_lst: program_mem program_lst | program_mem;
program_mem: declared | var_decl | const_decl;
declared:
	func_decl
	| method_decl
	| struct_type
	| interface_type;

// ---------------------------- // --- TODO Literal 6.6 pdf --- // ---------------------------- //

literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL;

// --------------------- // --- Array Literal --- // --------------------- //

array_lit: array_type CUR_OPEN array_lit_lst CUR_CLOSE;

array_type: (SQ_OPEN (INT_LIT | ID) SQ_CLOSE) (
		array_type
		| prim_type
		| ID
	);

array_lit_lst:
	array_lit_mem COMMA array_lit_lst
	| array_lit_mem;

array_lit_mem:
	| CUR_OPEN array_lit_lst CUR_CLOSE
	| array_lit_mem_single;

array_lit_mem_single: literal | struct_lit | ID;

// ---------------------- // --- Struct Literal --- // ---------------------- //

struct_lit: ID CUR_OPEN list_struct_elem_lst? CUR_CLOSE;
list_struct_elem_lst:
	list_struct_elem_mem COMMA list_struct_elem_lst
	| list_struct_elem_mem;
list_struct_elem_mem: ID COLON expr;

// ------------------- // --- Struct Type --- // ------------------- // 

struct_type:
	TYPE ID STRUCT CUR_OPEN struct_attribute_lst CUR_CLOSE SEMI_COLON;
struct_attribute_lst:
	struct_attribute_mem struct_attribute_lst
	| struct_attribute_mem;
struct_attribute_mem: ID var_type SEMI_COLON;

// ---------------------- // --- Interface Type --- // ---------------------- //

interface_type:
	TYPE ID INTERFACE CUR_OPEN interface_method_lst CUR_CLOSE SEMI_COLON;

interface_method_lst:
	interface_method_mem interface_method_lst
	| interface_method_mem;

interface_method_mem:
	ID (R_OPEN interface_method_param_lst? R_CLOSE) var_type? SEMI_COLON;

interface_method_param_lst:
	interface_method_param_lst_mem COMMA interface_method_param_lst
	| interface_method_param_lst_mem;

interface_method_param_lst_mem: id_lst var_type;

id_lst: ID COMMA id_lst | ID;

// ---------------------------- // --- Variable declaration --- // ---------------------------- //

var_decl: var_decl_non_init | var_decl_with_init;

var_decl_with_init: VAR ID (var_type)? ASSIGN (expr) SEMI_COLON;

var_decl_non_init: VAR ID (var_type) SEMI_COLON;

prim_type: STRING | BOOL | INT | FLOAT;
var_type: prim_type | array_type | ID;

// ----------------- // --- Constants --- // ----------------- //

const_decl: CONST ID (ASSIGN) (expr) SEMI_COLON;

// ---------------------------- // --- Function declaration --- // ---------------------------- //

func_decl:
	FUNC ID R_OPEN (para_lst)? R_CLOSE (var_type)? block_func SEMI_COLON;

para_lst: para_mem COMMA para_lst | para_mem;
para_mem: id_lst var_type;

// ---------------------------// --- Method declaration --- // ---------------------------//

method_decl:
	FUNC R_OPEN (method_receiver_lst) R_CLOSE ID (
		R_OPEN (para_lst)? R_CLOSE
	) (var_type)? block_func SEMI_COLON;

method_receiver_lst: method_receiver_mem;

method_receiver_mem: ID ID;

// ------------------- // --- Block phase --- // ------------------- //

block_func: CUR_OPEN block_func_lst? CUR_CLOSE;

block_func_lst: block_func_mem block_func_lst | block_func_mem;

block_func_mem: var_decl | const_decl | stmt_block;

// ----------------- // --- stmt --- // ----------------- //

stmt_block: stmt | break_stmt | cont_stmt;

stmt:
	for_stmt
	| if_stmt
	| return_stmt
	| call_func
	| assign_stmt_semi
	| increase_stmt_semi;

for_stmt:
	FOR (for_stmt_01 | for_stmt_02 | for_stmt_03) block_func SEMI_COLON;

for_stmt_01: for_stmt_01_init for_stmt_01_cond for_stmt_01_upda;
for_stmt_01_init: (for_stmt_01_upda SEMI_COLON)
	| for_stmt_01_var_decl_init;
for_stmt_01_cond: (expr) SEMI_COLON;
for_stmt_01_upda: for_stmt_01_upda_incr | for_stmt_01_assign;

// fix type 13-02
for_stmt_01_var_decl_init:
	VAR ID (var_type)? ASSIGN (expr) SEMI_COLON;
for_stmt_01_upda_incr:
	ID (ADDVAL | SUBVAL | MULVAL | DIVVAL | MODVAL) expr;
for_stmt_01_assign: ID (NEWASS) expr;

for_stmt_02: ID COMMA ID NEWASS RANGE (expr);

for_stmt_03: (expr);

if_stmt: if_stmt_rec SEMI_COLON;
if_stmt_rec: (if_stmt_type1 | if_stmt_type2);
if_stmt_type1: IF R_OPEN (expr) R_CLOSE block_func else_stmt;
if_stmt_type2: IF R_OPEN (expr) R_CLOSE block_func;
else_stmt: ELSE (if_stmt_rec | block_func);

break_stmt: BREAK SEMI_COLON;
cont_stmt: CONTINUE SEMI_COLON;

return_stmt: RETURN (expr)? SEMI_COLON;

// old 

// call_func: (lhs_expr method_args) SEMI_COLON;

// new 

call_func: (
		ID method_args? array_access? property_chain? POINT func_call
		| func_call
	) SEMI_COLON;

func_call: ID method_args;

assign_stmt_semi: assign_stmt SEMI_COLON;

// old

// assign_stmt: lhs_expr (NEWASS) expr;

// new
assign_stmt: lhs_expr (NEWASS) expr;

increase_stmt:
	lhs_expr (ADDVAL | SUBVAL | MULVAL | DIVVAL | MODVAL) expr;

increase_stmt_semi: increase_stmt SEMI_COLON;

// ------------------ // --- expr --- // ------------------ //

expr_list: expr COMMA expr_list | expr;

expr: expr OR expr1 | expr1;

expr1: expr1 AND expr2 | expr2;

expr2: expr2 comp_op expr3 | expr3;
comp_op: EQ | NEQ | LT | LTE | GT | GTE;

expr3: expr3 add_op expr4 | expr4;
add_op: ADD | SUB;

expr4: expr4 mul_op expr5 | expr5;
mul_op: MUL | DIV | MOD;

expr5: unary_op expr5 | expr6;
unary_op: NEGATION | SUB;

// old 
expr6: expr6 expr6_postfix_lst | expr7;

expr6_postfix_lst:
	expr6_postfix_mem expr6_postfix_lst
	| expr6_postfix_mem;
expr6_postfix_mem:
	POINT ID
	| POINT ID method_args
	| array_index;

method_args: R_OPEN expr_list? R_CLOSE;

expr7:
	TRUE
	| FALSE
	| NIL
	| FLOAT_LIT
	| STRING_LIT
	| INT_LIT
	| array_lit
	| struct_lit
	| ID
	| func_call
	| R_OPEN expr R_CLOSE;

array_access: array_index array_access?;
array_index: SQ_OPEN expr SQ_CLOSE;

attribute_chain: POINT ID array_access? attribute_chain?;

lhs_expr: ID array_access? attribute_chain?;

property_chain:
	POINT ID property_chain?
	| POINT ID array_access property_chain?
	| POINT ID (method_args array_access) property_chain?;

// ! -------------- END PASER --------------------- */

// ! ---------------- LEXER ----------------------- */ 

// ------------------------------- // --- TODO Keywords 3.3.2 pdf --- // ------------------------------- //
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOL: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// -------------------------------- // --- TODO Operators 3.3.3 pdf --- // -------------------------------- //
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NEWASS: ':=';
EQ: '==';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';
NEGATION: '!';
ASSIGN: '=';
ADDVAL: '+=';
SUBVAL: '-=';
MULVAL: '*=';
DIVVAL: '/=';
MODVAL: '%=';
POINT: '.';

// --------------------------------- // --- TODO Separators 3.3.4 PDF --- // --------------------------------- //
R_OPEN: '(';
R_CLOSE: ')';
CUR_OPEN: '{';
CUR_CLOSE: '}';
SQ_OPEN: '[';
SQ_CLOSE: ']';
COMMA: ',';
SEMI_COLON: ';';

COLON: ':'; // new added

// ---------------------------------- // --- TODO Identifiers 3.3.1 PDF --- // ---------------------------------- //
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// ------------------------------- // --- TODO Literals 3.3.5 PDF --- // ------------------------------- // 

// New
INT_LIT: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT;
fragment DEC_LIT: DEC | [1-9] DEC*;
fragment BIN_LIT: ('0b' | '0B') BIN+;
fragment OCT_LIT: ('0o' | '0O') OCT+;
fragment HEX_LIT: ('0x' | '0X') HEX+;
fragment DEC: [0-9];
fragment BIN: [0-1];
fragment OCT: [0-7];
fragment HEX: [0-9a-fA-F];

// Floating Point Literals

FLOAT_LIT: (DEC | [1-9] DEC*) | ((DEC+) FP DEC* (EXPO)?);
fragment EXPO: [Ee] ((DEC+) | [+-] (DEC+));
fragment FP: '.';

// String Literal

STRING_LIT: '"' STR_CHAR* '"';
fragment STR_CHAR: ~['\n"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\];
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];

// ------------------------ // --- Whitespace Chars --- // ------------------------ //

CMTLINE: '//' ~[\r\f\n]* -> skip;

CMTBLOCK: '/*' (CMTBLOCK | .)*? '*/' -> skip;

WS:
	[ \t\f\r]+ -> skip; // skip spaces, tabs, formfeeds, carriage returns, newline char

// old: NEWLINE: '\n';
NEWLINE: '\r'? '\n';

// ----------------------------------------- // --- TODO ERROR BTL1--- // ----------------------------------------- //
ERROR_CHAR: . {raise ErrorToken(self.text)};

// New unclosed-string handling

UNCLOSE_STRING:
	'"' STR_CHAR* ('\r\n' | '\n' | EOF) { 
if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text == '\r'): 
	raise UncloseString(self.text[:-2]) 
elif (self.text[-1] == '\n'):
	raise UncloseString(self.text[:-1]) 
else: 
	raise UncloseString(self.text) 
};

// new  illegal string handle

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL { 
temp = self.text 
raise IllegalEscape(temp) 
};

// ---------------- LEXER ----------------------- //