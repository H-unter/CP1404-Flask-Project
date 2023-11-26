""""
CP1404 Practical 10 Hunter Kruger-Ilingworth
flaskproject
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/c')
@app.route('/c/<input>')
def convert(input=0.0):
    return f"<h1>{input}°C is equal to {convert_celsius_to_fahrenheit(float(input))}°F</h1>"


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
