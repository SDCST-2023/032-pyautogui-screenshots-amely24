import pyautogui as p
import time
from pyscreeze import locateCenterOnScreen

p.PAUSE = 0.05

def cookiestart():
    x = p.locateOnScreen('cookie.png', confidence=0.9)
    if x is not None:
        for _ in range(100):
            p.moveTo(x)
            p.click()

def upgrades(images, max_iterations):
    iteration = 0
    while iteration < max_iterations:
        for image_path in images:
            location = locateCenterOnScreen(image_path, confidence=0.9)
            if location is not None:
                p.moveTo(location)
                p.click()
                iteration += 1
                if iteration >= max_iterations:
                    return
                time.sleep(0.1)


while True:
    images = ['cursor.png', 'grandma.png', 'farm.png', 'mine.png']
    max_iterations = 1000
    upgrades(images, max_iterations)
    cookiestart()



''''''''''
def autoclick_image(image_path, num_clicks, sleep_duration):   
    position = p.locateOnScreen(image_path)
    
    if position is None:
        print("Image not found on the screen.")
        return

    center_x, center_y = p.center(position)
    
    for _ in range(num_clicks):
        p.click(center_x, center_y)
    
    time.sleep(sleep_duration)

image_path = 'cookie.png'
num_clicks = 100
sleep_duration = 10
autoclick_image(image_path, num_clicks, sleep_duration)

x, y= p.locateCenterOnScreen("cookie.png")
p.moveTo(x, y, duration = 0.1)
p.leftClick()

while True:
    cookie.click()
'''''