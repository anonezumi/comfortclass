grammar comfortclass;

imports			: (FROM expression)? IMPORT expression (COMMA expression)*;
enumdef			: (ENUM | ENUMP) IDENTIFIER L_BRACE IDENTIFIER (COMMA IDENTIFIER)* R_BRACE;
param 			: expression (COLON identifier)? (EQUALS expression)?;
paramlist		: L_PAREN param? (COMMA param)* R_PAREN;
array			: L_BRACKET expression? (COMMA expression)* R_BRACKET;
magic 			: INT_MAGIC | FLOAT_MAGIC | string | TRUE | FALSE | array | NULL;
identifier		: IDENTIFIER (DOT IDENTIFIER)*;
call			: IDENTIFIER L_PAREN expression? (COMMA expression (EQUALS expression)?)* R_PAREN;
return_			: RETURN expression;
modifier		: STATIC | CONST | PRIVATE | PROTECTED | PUBLIC | SAVED;

vardef 			: modifier* VAR identifier EQUALS expression;
extvardef		: EXTDEF modifier* VAR identifier;
funcdef			: modifier* FUNC identifier paramlist codeblock;
extfuncdef		: EXTDEF modifier* FUNC identifier paramlist;
eventdef		: EVENT identifier codeblock;
classdef		: (CLASS | OBJECT) identifier (L_PAREN expression (COMMA expression)*)? L_BRACE JAVADOC? (vardef | funcdef | eventdef)* R_BRACE;
if_ 			: IF expression codeblock (ELSE IF expression codeblock)* (ELSE codeblock)?;
while_			: WHILE expression codeblock;
for_			: FOR identifier IN expression codeblock;
switch_			: SWITCH L_BRACE (CASE expression codeblock)+ (DEFAULT codeblock) R_BRACE;
expression		: L_PAREN expression R_PAREN
				| magic
				| identifier
				| call
				| expression L_BRACKET expression R_BRACKET //array access
				| MINUS expression
				| EXCLAIMATION expression
				| TILDE expression
				| expression AS identifier
				| expression ASTERISK expression
				| expression SLASH expression
				| expression PERCENT expression
				| expression PLUS expression
				| expression MINUS expression
				| expression LESS LESS expression
				| expression GREATER GREATER expression
				| expression LESS expression
				| expression LESS EQUALS expression
				| expression GREATER expression
				| expression GREATER EQUALS expression
				| expression EQUALS EQUALS expression
				| expression EXCLAIMATION EQUALS expression
				| expression AND expression
				| expression XOR expression
				| expression OR expression
				| expression AND AND expression
				| expression OR OR expression;
statement		:	( call
					| vardef
					| enumdef
					| extvardef
					| extfuncdef
					| return_
					| identifier EQUALS expression
					| identifier PLUS EQUALS expression
					| identifier MINUS EQUALS expression
					| identifier ASTERISK EQUALS expression
					| identifier SLASH EQUALS expression
					| identifier PERCENT EQUALS expression
					| identifier LESS LESS EQUALS expression
					| identifier GREATER GREATER EQUALS expression
					| identifier AND EQUALS expression
					| identifier XOR EQUALS expression
					| identifier OR EQUALS expression
					) SEMICOLON
				| if_
				| while_
				| for_
				| switch_;
codeblock		: L_BRACE statement+ R_BRACE;
file_component	: imports | classdef | funcdef | eventdef | enumdef;
script			: JAVADOC? file_component*;
string			: QUOTE (~'"' | '\\"')* QUOTE;

JAVADOC			: '/**' .+? '*/';
COMMENTS 		: '//' ~'\n'+ -> skip;
MULTILINECOMMENT: '/*' .+? '*/' -> skip;

INT_MAGIC		: ('0' | [1-9] [0-9]*);
FLOAT_MAGIC		: ('0' | [1-9] [0-9]*) '.' ([0-9]* [1-9] | '0');

L_PAREN			: '(';
R_PAREN			: ')';
EXCLAIMATION	: '!';
TILDE			: '~';
ASTERISK		: '*';
SLASH			: '/';
PERCENT			: '%';
PLUS			: '+';
MINUS			: '-';
LESS			: '<';
GREATER			: '>';
L_BRACKET		: '[';
R_BRACKET		: ']';
COMMA			: ',';
COLON 			: ':';
DOT				: '.';
AND				: '&';
OR 				: '|';
XOR				: '^';
EQUALS			: '=';
QUOTE			: '"';
SEMICOLON		: ';';
L_BRACE 		: '{';
R_BRACE 		: '}';

FUNC 			: 'func';
RETURN			: 'return';
EVENT 			: 'event';
SEND			: 'send';
IF 				: 'if';
ELSE 			: 'else';
WHILE 			: 'while';
FOR 			: 'for';
IN 				: 'in';
BREAK 			: 'break';
CONTINUE		: 'continue';
TRY				: 'try';
EXCEPT 			: 'except';
SWITCH 			: 'switch';
CASE 			: 'case';
DEFAULT 		: 'default';
IMPORT			: 'import';
FROM 			: 'from';
EXTDEF			: 'extdef';

STATIC			: 'static';
CONST			: 'const';
SAVED			: 'saved';
PRIVATE			: 'private';
PROTECTED		: 'protected';
PUBLIC			: 'public';

ENUM			: 'enum';
ENUMP			: 'enump';
CLASS			: 'class';
OBJECT			: 'object';
VAR 			: 'var';
NULL 			: 'null';
ANY				: 'any';

TRUE			: 'true';
FALSE			: 'false';

AS 				: 'as';

WHITESPACE		: (' ' | '\t' | '\r\n' | '\n' | '\r')+ -> skip;
IDENTIFIER		: ([a-z] | [A-Z] | '_')+;
OTHER			: .;
