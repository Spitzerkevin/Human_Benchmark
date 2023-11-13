from pyautogui import *
import pyautogui
import time
import keyboard
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #put here youre PATH to tesseract.exe

list = [] #Creating The List

time.sleep(5) #Giving time to Tab to Human Benchmark

#To Start the test by clicking on the Start Button
try:

    start = pyautogui.locateOnScreen('Start.png')
    pyautogui.moveTo(start[0], start[1])
    pyautogui.click()
    pyautogui.moveTo(340, 390)
    time.sleep(0.5)
except ImageNotFoundException:
    pass

#Function to locate and Click on the Seen Button
def clickSeen():
    try:

        seen = pyautogui.locateOnScreen('Seen.png')
        pyautogui.moveTo(seen[0], seen[1])
        pyautogui.click()
        pyautogui.moveTo(340,390)
        time.sleep(0.01)
    except ImageNotFoundException:
        pass

#Function to locate and Click on the New Button
def clickNew():
    try:

        New = pyautogui.locateOnScreen('New.png')
        pyautogui.moveTo(New[0], New[1])
        pyautogui.click()
        pyautogui.moveTo(340,390)
        time.sleep(0.01)
    except ImageNotFoundException:
        pass

#Main Loop (stops after holding q)
while keyboard.is_pressed("q") == False:
    time.sleep(0.1)
    pyautogui.screenshot("verbal.png", region=(827, 377, 300, 250))# Makes a Screenshot of the word and The Seen/New Button
    time.sleep(0.1)
    word = pytesseract.image_to_string('verbal.png')#Tesseract is reading the word

    #Decides if the word is already seen or not
    if word in list:
        clickSeen()
    else:
        list.append(word)
        clickNew()

