from flask import Flask

import flask_nicely

from .extract_named_entities import top_entities

app = Flask(__name__)


@app.route('/url/<url>')
@flask_nicely.nice_json
def return_top_entities(url):

    entities = top_entities

    data = {}

    for entity in entities:
        data[entity[0]] = entity[1]

    return data

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)

