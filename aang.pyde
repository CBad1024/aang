# Hi! This is my submission for Pset 02. Please note that I made a few small changes to the character. 
# 1. I animated the hand to wave.
# 2. I added a greeting text at the top of the screen.



def setup():
  size(600,600)
  background('#FFFFFF')
  rectMode(CENTER)
  # frameRate(4)

rightArmY2 = 350
rightArmYSpeed = 1
thresholdBreached = False
UPPER_BOUND = 400
LOWER_BOUND = 300


def drawRightArm():
    global rightArmY2, rightArmYSpeed, thresholdBreached
    stroke('#000000')
    rightArmY2 += rightArmYSpeed*5
    line(400, 380, 500, rightArmY2)
    thresholdBreached = False 
    if (rightArmY2 > UPPER_BOUND or rightArmY2 < LOWER_BOUND):
        rightArmYSpeed *= -1
        thresholdBreached = True
    
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
  
    
      
staffColor= (random(255), random(255), random(255))
    
def drawStaff():
    global staffColor, thresholdBreached
    stroke('#000000')
    if thresholdBreached:
        staffColor= (random(255), random(255), random(255))
    
    fill(staffColor[0],staffColor[1],staffColor[2])
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

def draw():
    background("#FFFFFF")
    
    drawStaff()
    drawBody()
    drawHead()
    drawLeftEye()
    drawRightEye()
    drawArrow()
    drawLeftArm()
    greeting()
    drawRightArm()
    


    
    



    
