import pyautogui, time


# Check the size of your screen -> pyautogui.size()

# Moving the mouse -> pyautogui.moveTo()
#  1)The first argument is x-axis while second argument is y-axis
#   The third argument is the duration it should take to move the mouse to the destination (default = 0s)
#   noteFunction0

# How many pixel to to the destination -> pyautogui.moveRel()
#  1)The positive number will cause the cursor to right/downward while negative will take it to left/upward
#    noteFunction1

# Getting the mouse position -> pyautogui.position()
#  1)It will return a tuple of cursor's x and y position

# Clicking the mouse -> pyautogui.click()
#  1)The first argument and second argument are the coordinate of the cursor
#    The third argument is button = "<key>" ; key=left,right,middle
#    noteFunction2

# Full click, partial click ??? -> .mouseDown/Up()
#  1)A full mean the button down and then releasing it back
#    mouseDown()/mouseUp()
#    doubleClick()/rightClick()/middleClick() -> the specific function that click() cannot do

# Dragging the mouse -> dragTo()/dragRel()
#  1)dragTo() -> drag the mouse cursor to new location
#  2)dragRel() -> a location relative to its current one
#  The both have same arguments as moveTo()
#  notefunction4()

# Scrolling the mouse -> scroll()
#  1)mouse up or down
#  notefunction5()


def notefunction():
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0)
        pyautogui.moveTo(200, 100, duration=0)
        pyautogui.moveTo(200, 200, duration=0)
        pyautogui.moveTo(100, 200, duration=0)


def notefunction1():
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)


def notefunction2():
    print(pyautogui.position())


def notefunction3():
    pyautogui.click(200, 300, button="right")  # right click


def notefunction4():
    print("open the paint.exe")
    time.sleep(5)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)  # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.2) # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2) # move up


def notefunction5():
    time.sleep(5)
    pyautogui.scroll(1000)


def new_note(n):
    if n == '0':
        notefunction()
    elif n == '1':
        notefunction1()
    elif n == '2':
        notefunction2()
    elif n == '3':
        notefunction3()
    elif n == '4':
        notefunction4()
    elif n == '5':
        notefunction5()
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
