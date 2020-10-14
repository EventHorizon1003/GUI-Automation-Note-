# pyautoguiNote2.py
import pyautogui, time
from pynput.mouse import Listener


# Getting a screenshot -> pyautogui.screenshot()
#  1)Syt: imbObj = pyautogui.screenshot()
#    notefunction
#  2)Pass the getpixel(<coordinate>) to the imageObj , it will return the color of the pixel(RGB) (Red,Green,Blue)
#    notefunction

# Analyzing the screenshot -> pixelMatchesColor()
#  1)It will return True if the pixel at the given x and y coordinates on the screen matches the given color
#  2)Syt: pixelMatchesColor(x,y,RGB)
#    The color at then given coordinates must exactly match . If will return false even the value just slightly diff

# Image Recognition -> locateOnScreen()
#  1)This is handy when u don't know beforehand where GUI should click
#       a)First upload the image in .png form
#       b)use the locateOnScreen("<name>.png") to find the object
#       c)It will return four-integer tuple such as: x,y coordinate of the edge (no true coord) , width and the height
#       d)If the obj cannot be found on the screen, then it will return None
#       *)If the obj can be found in several places, it will return a Generator obj
#         It can be pass to list()
#       e)Remember the four-integer tuple are the area on the screen where you image was found
#         You need to pass the four-integer tuple to the center()
#        notefunction1()

# Controlling the keyboard -> pyautogui.typewrite()
#  1)Send virtual keypresses to the computer
#    Syntax: pyautogui.typewrite("<text>",<time>) ; the sec argument is the number of seconds to pause
#    notefunction2()
#  2)There are some key u need to pass the specific key string to execute
#    eg: 'enter' = enter key , 'esc' = Esc key  , 'tab' = tab key , 'winleft' = left WIN key  and so on (google it!!!)
#  3)If u wanna pressing the key -> pyautogui.press("<>") *this is more suitable for single-key command*
#    Besides, if u wanna send the virtual keypresses or release -> pyautogui.keyDown() / pyautogui.keyUp()
#    pyautogui.keyDown("shift");pyautogui.press("4");pyautogui.keyUp("shift")
#  4)If u wanna use hotkey combination -> pyautogui.hotkey('','')
#    Eg: pyautogui.hotkey("ctrl", 'c')

# Capturing the click event -> pynput.mouse.Listener
#  1)It can record the activity of the mouse
#   notefunction3()


def notefunction():
    im = pyautogui.screenshot()  # get the imageObj
    print(im)
    print(im.getpixel((200, 300)))  # the coordinate is taken as one argument in getpixel()


def notefunction1():
    location = pyautogui.locateOnScreen("chrome.png", confidence=0.8)
    if location is not None:
        print("The subject is found")
        print("Getting the coordinate")
        location1 = pyautogui.center(location)
        x, y = location1
        print(x)
        pyautogui.click(x, y, button="left")
    else:
        print(location)
        print("The subject cannot be found")


def notefunction2():
    print("Prepare the text editor")
    time.sleep(5)
    pyautogui.click(842, 261)
    pyautogui.typewrite("Hello World")


def notefunction3():
    def on_click(x, y, button, pressed):
        if pressed:
            print("Mouse clicked at ({0},{1}) with {2}".format(x, y, button))

    with Listener(on_click=on_click)as listener:
        listener.join()


def new_note(n):
    if n == '0':
        notefunction()
    elif n == '1':
        notefunction1()
    elif n == '2':
        notefunction2()
    elif n == '3':
        notefunction3()


# elif n == '4':
#     notefunction4()
# elif n == '5':
#     notefunction5()
# elif n == '6':
#     notefunction6()


# Loop
def generator():
    while True:
        print("What example you want me to show ?")
        num = input()
        new_note(num)


if __name__ == "__main__":  # prevent the module run when this file is imported
    generator()
