from socket import getfqdn
from flask import Flask, render_template, Response
from datetime import datetime
import cv2

outputFrame = None
cap = cv2.VideoCapture(0)

# flask app
app = Flask(__name__)


def generate():
    while True:
        ret, frame = cap.read()
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_stream')
def video_stream():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route('/app_response')
def app_response():
    return Response('Could not verify your access level for that URL.\n')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
    # app.run(host=getfqdn(), port=5000, debug=True)

# release the video cap
cap.release()
cv2.destroyAllWindows()
