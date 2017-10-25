from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test_ingress():
    return "Hello World!", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
