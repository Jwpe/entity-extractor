from flask import Flask

import flask_nicely

import extract_named_entities

app = Flask(__name__)


@app.route('/url/<path:url>')
@flask_nicely.nice_json
def return_top_entities(url):

    entities = extract_named_entities.top_entities(url)

    data = {}

    for entity in entities:
        data[entity[0]] = entity[1]

    return data

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
