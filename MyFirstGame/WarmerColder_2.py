import turtle
import time
import random
import math

# ------------------------------------------------------------------------------------- Rules & Controls
# Goal: 
# 1. move the window to the hottest spot on the screen.
# 2. The window changes color to indicate the window's proximity to the spot.
# 3. From cold to hot, the colous are: grey, blue, green, yellow, red, white.
# 4. Ones you see the white color, you win the game, and a new random stop is generated.
# 
# Control:
# w - up
# s - down
# a - left
# d - right
# e - randomly changes the window's shape (it's purely cosmetic)
# ------------------------------------------------------------------------------------- Classes


class Control:

    def __init__(self):
        self.bool = False

    def hold(self):
        self.bool = True

    def release(self):
        self.bool = False


class Window:

    def __init__(self, input, min, max):
        self.input = input
        self.min = min
        self.max = max
        self.length = random.randint(self.min, self.max)
        self.pos = self.input / 2 - self.length / 2
        self.heatpoint = random.randint(1 + round(self.length / 2), self.input - round(self.length / 2) - 1)

    def newsize(self):
        new = random.randint(self.min, self.max)
        self.pos += (self.length - new) / 2
        self.length = new

    def newheat(self):
        self.heatpoint = random.randint(1 + round(self.length / 2), self.input - round(self.length / 2) - 1)


# ------------------------------------------------------------------------------------- Functions


# Movment output
def move():
    if up.bool:
        y.pos -= 1
    if down.bool:
        y.pos += 1
    if left.bool:
        x.pos -= 1
    if right.bool:
        x.pos += 1


# Goal Game
def Finding():

    dis = math.sqrt((abs(x.heatpoint - (x.pos + round(x.length / 2))) * 2) +
                    (abs(y.heatpoint - (y.pos + round(y.length / 2))) * 2))

    # print(dis) tells you you distance from the goal, you cheater!
    if dis <= 5:
        wn.bgcolor("white")
        print(" ")
        print("Jack pot!!!")
        print(" ")
        time.sleep(2)

        x.newsize()
        y.newsize()

        x.newheat()
        y.newheat()

    elif 5 < dis <= 10:
        wn.bgcolor("red")
    elif 10 < dis <= 15:
        wn.bgcolor("yellow")
    elif 15 < dis <= 25:
        wn.bgcolor("green")
    elif 25 < dis <= 40:
        wn.bgcolor("blue")
    else:
        wn.bgcolor("gray")


# ------------------------------------------------------------------------------------- Setup


up = Control()
down = Control()
left = Control()
right = Control()

delay = 0.005

# Screen
wn = turtle.Screen()
wn.title("Control Pos $ Shape 3")
wn.setup(200, 200)
wn.tracer(0)

# Asking for screen resolution
xres = wn.numinput("Screen Resolution", "Please enter the X perimeter:", default=1920, minval=500, maxval=3000)
yres = wn.numinput("Screen Resolution", "Please enter the Y perimeter:", default=1080, minval=500, maxval=3000)

# Fail Safe
if xres is None:
    xres = 1920
if yres is None:
    yres = 1080

# window size , length, pos & go to
x = Window(xres, 125, 500)
y = Window(yres, 125, 500)


# Keyboard bindings
wn.listen()

wn.onkeypress(up.hold, "w")
wn.onkeypress(down.hold, "s")
wn.onkeypress(left.hold, "a")
wn.onkeypress(right.hold, "d")

wn.onkeyrelease(up.release, "w")
wn.onkeyrelease(down.release, "s")
wn.onkeyrelease(left.release, "a")
wn.onkeyrelease(right.release, "d")

wn.onkeypress(x.newsize, 'e')
wn.onkeyrelease(y.newsize, 'e')


# ------------------------------------------------------------------------------------- Main Loop

while True:
    wn.update()

    wn.setup(x.length, y.length, x.pos, y.pos)
    Finding()
    move()

    time.sleep(delay)
wn.mainloop()
