import ply.lex as lex

tokens = (
    'CREATE', 'DROP', 'ALTER', 'RENAME', 'TO', 'DATABASE', 'TABLE', 'INSERT',
    'INTO', 'VALUES', 'UPDATE', 'SET', 'WHERE', 'DELETE', 'SELECT', 'FROM', 
    'PUBLIC', 'IDENTIFIER', 'SEMICOLON', 'COMMA', 'LPAREN', 'RPAREN',
    'SERIAL', 'PRIMARY', 'KEY', 'VARCHAR', 'NOT', 'NULL', 'TIMESTAMP', 'DEFAULT',
    'CURRENT_TIMESTAMP', 'EQ', 'STRING', 'INT', 'STAR', 'DOT'
)

# Diccionario de palabras reservadas
reserved = {
    'create': 'CREATE',
    'drop': 'DROP',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'to': 'TO',
    'database': 'DATABASE',
    'table': 'TABLE',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'update': 'UPDATE',
    'set': 'SET',
    'where': 'WHERE',
    'delete': 'DELETE',
    'select': 'SELECT',
    'from': 'FROM',
    'public': 'PUBLIC',
    'serial': 'SERIAL',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'varchar': 'VARCHAR',
    'not': 'NOT',
    'null': 'NULL',
    'timestamp': 'TIMESTAMP',
    'default': 'DEFAULT',
    'current_timestamp': 'CURRENT_TIMESTAMP'
}

# Definición de tokens para las palabras reservadas
t_CREATE = r'CREATE'
t_DROP = r'DROP'
t_ALTER = r'ALTER'
t_RENAME = r'RENAME'
t_TO = r'TO'
t_DATABASE = r'DATABASE'
t_TABLE = r'TABLE'
t_INSERT = r'INSERT'
t_INTO = r'INTO'
t_VALUES = r'VALUES'
t_UPDATE = r'UPDATE'
t_SET = r'SET'
t_WHERE = r'WHERE'
t_DELETE = r'DELETE'
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_PUBLIC = r'PUBLIC'
t_SERIAL = r'SERIAL'
t_PRIMARY = r'PRIMARY'
t_KEY = r'KEY'
t_VARCHAR = r'VARCHAR'
t_NOT = r'NOT'
t_NULL = r'NULL'
t_TIMESTAMP = r'TIMESTAMP'
t_DEFAULT = r'DEFAULT'
t_CURRENT_TIMESTAMP = r'CURRENT_TIMESTAMP'
t_EQ = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STAR = r'\*'
t_DOT = r'\.'

# Definición de tokens para otros tipos de datos
t_STRING = r'\'[^\']*\''
t_INT = r'\d+'

# Definición de token para IDENTIFIER con verificación de palabras reservadas
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')  # Chequeo de palabras reservadas
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Inicialización del lexer
lexer = lex.lex()