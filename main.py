import pyautogui
import cv2

x, y = pyautogui.locateCenterOnScreen('login.png', confidence=0.9)
pyautogui.click(x, y)
import pyautogui
import cv2
import time
from google import genai
from google.genai import types
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

screenshot = pyautogui.screenshot()
screenshot.save("test-hw.png")

image = Image.open("test-hw.png")
client = genai.Client(api_key="api key go here")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "Tell which box on the screen which contains 49c² - 28c - 4. Starting from the top middle as box one and working right until box 9 which would be the top left box. There are 9 boxes in a 3x3 grid. Give me nothing but the box number"],
    config = types.GenerateContentConfig(
       max_output_tokens = 300
    )
)


print(response.text)

rangevalue = int(response.text)

for i in range(rangevalue):
    if rangevalue <= 8:
        pyautogui.keyDown('tab')
        time.sleep(0.05)
        pyautogui.keyUp('tab')
        time.sleep(0.1)
    elif rangevalue == 9:
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        pyautogui.keyDown('shift')
        time.sleep(0.05)
        pyautogui.keyDown('tab')
        time.sleep(0.05)
        pyautogui.keyUp('tab')
        pyautogui.keyUp('shift')
        pyautogui.keyDown('enter')
        time.sleep(0.01)
        pyautogui.keyUp('enter')
        break


#split_values = response.text.split(", ")
#num1 = int(split_values[0])
#num2 = int(split_values[1])

#pyautogui.click(870, 250)



def login(email, password):
    x, y = pyautogui.locateCenterOnScreen('login.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('google-login-dark.png', confidence=0.9)
    if x is None:
        x, y = pyautogui.locateCenterOnScreen('google-login-light.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.write(email)
    time.sleep(0.3)
    x, y = pyautogui.locateCenterOnScreen('google-next.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(2)
    pyautogui.write(password)
    x, y = pyautogui.locateCenterOnScreen('google-next.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(6)

def findhomework():
    x, y = pyautogui.locateCenterOnScreen('not-started.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.6)
    x, y = pyautogui.locateCenterOnScreen('0%-start.png', confidence=0.8)
    pyautogui.click(x, y)

#login("email", "real-password")
#time.sleep(0.5)
#findhomework()


