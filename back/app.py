from random import randint
from flask import Flask

app = Flask(__name__)


def roll():
    return randint(1, 6)


@app.route("/rolldice")
def roll_dice():
    return str(roll())

if __name__ == "__main__":
    host = os.environ.get('APP_HOST_NAME', "0.0.0.0")
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(debug=True, host=host, port=port)