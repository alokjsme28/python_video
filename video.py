from flask import Flask, Response, render_template
import cv2
app = Flask(__name__)
cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template("video.html")
def gen():
    while True:
        ret, photo = cap.read()
        if not ret:
            break
        else:
            ret1, buff = cv2.imencode('.jpg', photo)
            photo = buff.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + photo)

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__== '__main__':
    app.run(port=9889, debug=True)
