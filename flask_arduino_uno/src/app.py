from socket import getfqdn
from configparser import ConfigParser
from arduino import ArduinoUno
from flask import Flask, render_template

# Load DoIP configuration from *.ini file
arduino_settings = ConfigParser()
arduino_settings.read("arduino_settings.ini")
uno_setting = {
    'port': arduino_settings.get("uno_settings", "port"),
    'baudrate': arduino_settings.get("uno_settings", "baudrate"),
    'parity': arduino_settings.get("uno_settings", "parity"),
    'number_of_data_bits': arduino_settings.get("uno_settings", "number_of_data_bits"),
    'number_of_stop_bits': arduino_settings.get("uno_settings", "number_of_stop_bits"),
}

# flask app
app = Flask(__name__)


@app.route('/')
def uno_flask_app():
    return render_template('uno_flask_app.html')


@app.route('/uno_connect')
def uno_connect():
    return render_template('uno_connect.html')


@app.route('/uno_disconnect')
def uno_disconnect():
    return render_template('uno_disconnect.html')


@app.route('/uno_settings')
def uno_settings():
    return render_template('uno_settings.html', uno_settings=uno_setting)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
