from flask import Flask, render_template, request, redirect, jsonify

import data

import os
import json

#initialize app
app = Flask(__name__)

firestore_client = data.initialize_firestore()


@app.route('/getphrase')
def return_current_phrase():
    return jsonify(data.read_current_phrase(firestore_client)['phrase'])

@app.route('/updatephrase', methods=['POST'])
def update_stored_phrase():
    new_phrase = request.form['new_phrase_field']
    print(data.update_phrase(firestore_client,new_phrase))
    return redirect('/')

@app.route('/')
def index():
    phrase_resp = data.read_current_phrase(firestore_client)["phrase"]
    return render_template('index.html', current_phrase=phrase_resp)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))