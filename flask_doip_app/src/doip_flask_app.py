from socket import getfqdn
from flask import Flask, render_template
from doip_config import doip_tester, doip_target_ecu

app = Flask(__name__)


@app.route('/')
def doip_flask_app():
    return render_template('doip_flask_app.html', doip_tester=doip_tester, doip_target_ecu=doip_target_ecu)


@app.route('/doip_connect')
def doip_connect():
    return render_template('doip_connect.html', doip_tester=doip_tester, doip_target_ecu=doip_target_ecu)


@app.route('/doip_disconnect')
def doip_disconnect():
    return render_template('doip_disconnect.html', doip_tester=doip_tester, doip_target_ecu=doip_target_ecu)


@app.route('/doip_settings')
def doip_settings():
    return render_template('doip_settings.html', doip_tester=doip_tester, doip_target_ecu=doip_target_ecu)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
