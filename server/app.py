import sys
import os
from flask import Flask, render_template, request, jsonify
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the proof functions from logic/proofs.py
from logic.proofs import direct_proof, contraposition_proof, contradiction_proof
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_proof', methods=['POST'])
def check_proof():
    proof_type = request.form.get('proof_type')
    statement = request.form.get('statement')
    assumption = request.form.get('assumption')
    conclusion = request.form.get('conclusion')
    contradiction = request.form.get('contradiction', '')

    # Validate
    if proof_type == 'direct':
        result = direct_proof(statement, assumption, conclusion)
    elif proof_type == 'contraposition':
        result = contraposition_proof(statement, assumption, conclusion)
    elif proof_type == 'contradiction':
        result = contradiction_proof(statement, assumption, contradiction)
    else:
        result = False

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
