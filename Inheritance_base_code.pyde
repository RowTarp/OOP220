import random
game_objects = []

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = random.randint(-2,2)
        self.y_speed = random.randint(-2,2)
        self.color = color(random.randint(0,255),
                           random.randint(0,255),
                           random.randint(0,255))
        self.size = random.randint(5,75)
        while self.x_speed == 0:
            self.x_speed = random.randint(-2,2)
        while self.y_speed == 0:
            self.y_speed = random.randint(-2,2)
        while self.x_speed == self.y_speed:
            self.x_speed = random.randint(-2,2)
            self.y_speed = random.randint(-2,2)

    def update(self):
        '''Update current location by speed.'''

        self.x += self.x_speed
        self.y += self.y_speed
    def draw(self):
        '''Draw self on the canvas.'''

        fill(self.color) # set shape color
        stroke(self.color) # add a black outline
        
        
class Square(Shape):
    def draw(self):
        super(Square,self).draw()
        square(self.x,self.y,self.size)

class Circle(Shape):
    def draw(self):
        super(Circle,self).draw()
        circle(self.x,self.y,self.size)
class BouncySquare(Shape):
    def draw(self):
        super(BouncySquare,self).draw()
        square(self.x,self.y,self.size)
        if (self.x+self.size) >= 400:
            self.x_speed = -self.x_speed
        if (self.y+self.size) >= 400:
            self.y_speed = -self.y_speed
        if self.x <= 0:
            self.x_speed = -self.x_speed
        if self.y <= 0:
            self.y_speed = -self.y_speed
        

def addSquare():
    global game_objects
    game_objects.append(Square(200,200))

def addCircle():
    
    global game_objects
    game_objects.append(Circle(200, 200))   

def addBouncySquare():
    global game_objects
    game_objects.append(BouncySquare(200,200))            


def reset():
    '''Clear all game objects.'''

    global game_objects
    game_objects = []

def setup():
    size(400, 400)
    background(255,255,255)

def draw():
    '''Clear the screen, have all game objects update and redraw.'''

    global game_objects
    
    background(255,255,255) # draw a white background
    
    for game_object in game_objects:
        game_object.update()
        game_object.draw()

'''To create a square press "s"'''
def keyPressed():
    if key == 'c':
        addCircle()
    if key == 's':
       addSquare()
    if key == 'b':
        addBouncySquare()
    if key == 'r':
        reset()
        background(255,255,255)



















'''class Square:
    def __init__(self, x, y):
        Create a new circle at the given x,y point with a random speed,
        color, and size.

        self.x = x
        self.y = y
        self.x_speed = random.randint(-5,5)
        self.y_speed = random.randint(-5,5)
        self.color = color(random.randint(0,255),
                           random.randint(0,255),
                           random.randint(0,255))
        self.size = random.randint(5,75)

    def update(self):
        Update current location by speed.

        self.x += self.x_speed
        self.y += self.y_speed
        if (self.x+self.size) >= 400:
            self.x_speed = -self.x_speed
        if (self.y+self.size) >= 400:
            self.y_speed = -self.y_speed
        if self.x <= 0:
            self.x_speed = -self.x_speed
        if self.y <= 0:
            self.y_speed = -self.y_speed
        while self.x_speed == 0:
            self.x_speed = random.randint(-5,5)
        while self.y_speed == 0:
            self.y_speed = random.randint(-5,5)
    def draw(self):


        fill(self.color) # set shape color
        stroke(self.color) # add a black outline
        strokeWeight(1)
        square(self.x, self.y, self.size)
