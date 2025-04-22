from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)  # ✅ Corrected

votes = {'cats': 0, 'dogs': 0}  # In-memory vote storage

@app.route('/')
def index():
    with open("templates/index.html") as f:
        return render_template_string(f.read())

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    animal = data.get('animal')
    if animal in votes:
        votes[animal] += 1
        return jsonify(votes)
    return jsonify({'error': 'Invalid vote'}), 400

@app.route('/results', methods=['GET'])
def results():
    return jsonify(votes)

if __name__ == '__main__':  # ✅ Corrected
    app.run(debug=True)
