from flask import Flask, request, jsonify
from flask_cors import CORS
from lexer import lexer
from parser import parser

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json['query']
    
    # Realizar análisis léxico
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append({'token': tok.value, 'type': tok.type})
    
    # Realizar análisis sintáctico
    try:
        result = parser.parse(data)
        syntax_error = None
    except Exception as e:
        result = None
        syntax_error = str(e)
    
    response = {
        'tokens': tokens,
        'syntax_result': result,
        'syntax_error': syntax_error
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)