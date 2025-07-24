from flask import Flask, request, jsonify
import cv2
import numpy as np
import serial
import time

app = Flask(__name__)
cap = cv2.VideoCapture(0)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

@app.route('/detect', methods=['GET'])
def detect():
    ret, frame = cap.read()
    if not ret:
        return jsonify({'error': 'camera error'})
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    obj_detected = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                    param1=50, param2=30, minRadius=5, maxRadius=30)
    if obj_detected is not None:
        ser.write(b'90,90\n')
        return jsonify({'object': True})
    else:
        ser.write(b'0,0\n')
        return jsonify({'object': False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)