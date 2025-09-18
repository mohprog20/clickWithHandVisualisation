import pyautogui as pag
import time

class Clicker:
    def __init__(self, cooldown=1.0):
        self.cooldown = cooldown
        self.last_click_time = 0

    def click(self):
        current_time = time.time()
        if current_time - self.last_click_time >= self.cooldown:
            pag.click()
            self.last_click_time = current_time
            print("Clicked!")
        else:
            print("Click on cooldown.")

    
    def move_mouse(self, x, y):
        pag.moveTo(x, y)

    def click_and_move(self, x, y):
        self.click()
        self.move_mouse(x, y)