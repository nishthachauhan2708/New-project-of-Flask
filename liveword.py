from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open("templates/index.html").read())

@app.route('/reverse', methods=['POST'])
def reverse():
    data = request.get_json()
    word = data.get('word', '')
    return jsonify({'reversed': word[::-1]})

if __name__ == '__main__':
    app.run(debug=True)
