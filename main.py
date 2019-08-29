import turtle
import math
import random

class Circuito:
    corredores = []
    
    def __init__(self, width, height, *colors):
        self.__startLine = int(-width/2 + width*0.05)
        self.__finishLine = int(width/2 - width*0.05)
        
        self.__printScreen(width, height)
        
        if colors: self.__createRunners(colors)
            
    def __printScreen(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__printLines(height)
        
    def __printLines(self, height):
        for line in (self.__startLine, self.__finishLine):
            new_printer = turtle.Turtle()
            new_printer.penup()
            new_printer.setpos(line, height/2)
            new_printer.pendown()
            new_printer.setpos(line, -height/2)
        
    def __createRunners(self, colors):
        for i in range(len(colors)):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            if i % 2 == 0: pos = i/2*20
            else: pos = -math.ceil(i/2)*20
            new_turtle.setpos(self.__startLine, pos)
            new_turtle.color(colors[i])
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        while True:
            for tortuga in self.corredores:
                tortuga.fd(random.randint(1,6))
                
                if tortuga.position()[0] >= self.__finishLine:
                    print("The {} turtle is the winner".format(tortuga.color()[0]))
                    return
        
        
if __name__ == '__main__':
    circuito = Circuito(640, 480, 'red', 'blue', 'green', 'orange')
    circuito.competir()