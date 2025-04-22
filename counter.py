from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
counter = {'count': 0}  # Global counter

@app.route('/')
def index():
    with open("templates/index.html") as f:
        return render_template_string(f.read(), count=counter['count'])

@app.route('/increment', methods=['POST'])
def increment():
    counter['count'] += 1
    return jsonify({'count': counter['count']})

if __name__ == '__main__':
    app.run(debug=True)
