# List available OpenCV video devices

This script lists avavilable video devices and displays a frame from each device. Inspired by: https://stackoverflow.com/questions/57577445/list-available-cameras-opencv-python

## Running the script
- Install dependencies (OpenCV and NumPy) `pip install -r requirements.txt`
- Run the script: `python main.py`

The script tests ids 0-8 by default. The preview window can be closed by pressing any key.
Once the correct device has been identified, you can use it in your own code:
```
cv2.VideoCapture(id)
```
The device id may change between reboots.

![screenshot with two video feeds](screenshot.png)