# Hi! This is my submission for Pset 02. Please note that I made a few small changes to the character. 
# 1. I animated the hand to wave.
# 2. I added a greeting text at the top of the screen.



rightArmYSpeed = 1
def setup():
  size(600,600)
  background('#FFFFFF')
  rectMode(CENTER)
  

rightArmX1 = 400
rightArmY1 = 380

rightArmX2 = 500
rightArmY2 = 410



def drawRightArm(y2):
    stroke('#000000')
    line(400, 380, 500, y2)

def drawLeftEye():
    fill('#000000')
    ellipse(240, 220, 50, 50)
    
def drawRightEye():
    fill('#000000')
    ellipse(360, 220, 50, 50)

def drawLeftArm():
    stroke('#000000')
    line(200, 380, 100, 350)


def drawArrow():
    fill('#47A2FA')
    noStroke()
    rect(300, 150, 50, 60)
    triangle(250, 180, 350, 180, 300, 220)
    
def drawStaff():
    stroke('#000000')
    fill('#6C420B')
    rect(90, 300, 15, 300)
    
def drawBody():
    fill('#FAA147')
    rect(300, 380, 200, 200) 

def drawHead():
    fill('#F2D59A')
    rect(300,200, 240, 160) #head
    
def greeting():
    fill('#000000')
    textSize(40)
    text("Hi! I'm Aang!", 200, 100)
    
def drawAang():
    drawStaff()
    drawBody()
    drawHead()
    drawLeftEye()
    drawRightEye()
    drawArrow()
    drawLeftArm()
    greeting()
    drawRightArm(rightArmY2)
    
def draw():
    background("#FFFFFF")
    global y
    global rightArmY2
    global rightArmYSpeed
    
    background('#FFFFFF')
    
    drawAang()
    
    
    if rightArmY2 > 400:
        rightArmYSpeed = -5
    elif rightArmY2 < 300:
        rightArmYSpeed = 5
    
    rightArmY2 = rightArmY2 + rightArmYSpeed
