import pyautogui as pag
import time
import cv2

class PositionHandler:
    def __init__(self):
        self.position = (0, 0)
        self.screen_size = pag.size()

        cap = cv2.VideoCapture(0)

        # Get width and height
        self.cam_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cam_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f"Webcam resolution: {self.cam_width}x{self.cam_height}")

        # Immediately release the camera
        cap.release()


    def handle_positions(self,finger1=[0,0],finger2=[0,0]):
        print(self.screen_size[0])
        pass
pos=PositionHandler()