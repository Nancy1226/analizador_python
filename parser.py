import ply.yacc as yacc
from lexer import tokens

def p_statement_create_database(p):
    'statement : CREATE DATABASE IDENTIFIER SEMICOLON'
    print(f"Creating database {p[3]}")

def p_statement_drop_database(p):
    'statement : DROP DATABASE IDENTIFIER SEMICOLON'
    print(f"Dropping database {p[3]}")

def p_statement_alter_database(p):
    'statement : ALTER DATABASE IDENTIFIER RENAME TO IDENTIFIER SEMICOLON'
    print(f"Renaming database {p[3]} to {p[6]}")

def p_statement_create_table(p):
    '''statement : CREATE TABLE IDENTIFIER LPAREN columns RPAREN SEMICOLON'''
    print(f"Creating table {p[3]} with columns {p[5]}")

def p_columns(p):
    '''columns : columns COMMA column
               | column'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_column(p):
    '''column : IDENTIFIER SERIAL PRIMARY KEY
              | IDENTIFIER VARCHAR LPAREN INT RPAREN NOT NULL
              | IDENTIFIER VARCHAR LPAREN INT RPAREN
              | IDENTIFIER TIMESTAMP DEFAULT CURRENT_TIMESTAMP'''
    p[0] = ' '.join(p[1:])

def p_statement_drop_table(p):
    'statement : DROP TABLE IDENTIFIER SEMICOLON'
    print(f"Dropping table {p[3]}")

def p_statement_alter_table(p):
    'statement : ALTER TABLE IDENTIFIER RENAME TO IDENTIFIER SEMICOLON'
    print(f"Renaming table {p[3]} to {p[6]}")

def p_statement_insert(p):
    'statement : INSERT INTO IDENTIFIER LPAREN columns RPAREN VALUES LPAREN values RPAREN SEMICOLON'
    print(f"Inserting into table {p[3]} values {p[9]}")

def p_values(p):
    '''values : values COMMA value
              | value'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_value(p):
    '''value : INT
             | STRING'''
    p[0] = p[1]

def p_statement_update(p):
    'statement : UPDATE IDENTIFIER SET IDENTIFIER EQ STRING WHERE IDENTIFIER EQ INT SEMICOLON'
    print(f"Updating table {p[2]} setting {p[4]} to {p[6]} where {p[8]} is {p[10]}")

def p_statement_delete(p):
    'statement : DELETE FROM IDENTIFIER WHERE IDENTIFIER EQ INT SEMICOLON'
    print(f"Deleting from table {p[3]} where {p[5]} is {p[7]}")

def p_statement_select(p):
    'statement : SELECT STAR FROM PUBLIC DOT IDENTIFIER SEMICOLON'
    print(f"Selecting all from table {p[6]}")

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()