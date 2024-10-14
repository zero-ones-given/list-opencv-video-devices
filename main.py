import cv2
import numpy as np
import math

WINDOW_NAME = 'Preview'
PREVIEW_MAX_SIZE = 240


def attemptFrameGrab(id):
    camera = cv2.VideoCapture(id)
    if not camera.isOpened():
        print("Port %s did not open." %id)
        #frame = np.zeros((500, 300, 3), np.uint8)
        #frame[:,:] = (id * 28,127,255 - id * 28)
        #return frame 
        return []

    returnValue, frame = camera.read()
    videoWidth = camera.get(3)
    videoHeight = camera.get(4)

    if returnValue:
        print(f"Port {id} is working and reads ({videoWidth} x {videoHeight}) frames.")
    else:
        print(f"Port {id} reports resolution ({videoWidth} x {videoHeight}) but reading a frame failed.")

    if not hasattr(frame, "__len__") and len(frame) != 0:
        return []

    resizeMultiplier = min(PREVIEW_MAX_SIZE / frame.shape[0], PREVIEW_MAX_SIZE / frame.shape[1])
    width = math.floor(frame.shape[1] * resizeMultiplier)
    height = math.floor(frame.shape[0] * resizeMultiplier)
    frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_NEAREST)
    cv2.circle(frame, (25, 25), 20, (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, str(id), (13, 37), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255,255,255), 2)

    return frame

def testVideoDevices(firstId, lastId):
    cv2.namedWindow(WINDOW_NAME)
    preview = np.zeros((PREVIEW_MAX_SIZE * 3, PREVIEW_MAX_SIZE * 3, 3), np.uint8)
    preview[:,:] = (127,127,127)

    for id in range(firstId, lastId + 1):
        frame = attemptFrameGrab(id)
        if len(frame) == 0:
            continue

        x = PREVIEW_MAX_SIZE * (id % 3)
        y = math.floor(id / 3) * PREVIEW_MAX_SIZE
        preview[y:y+frame.shape[0], x:x+frame.shape[1]] = frame
        cv2.imshow(WINDOW_NAME, preview)

    cv2.waitKey(0)

testVideoDevices(0, 8)