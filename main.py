import pyautogui
import cv2

x, y = pyautogui.locateCenterOnScreen('login.png', confidence=0.9)
pyautogui.click(x, y)
