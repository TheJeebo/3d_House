from turtle import Screen, Turtle, mainloop, setup, tracer, update
from math import cos, sin, radians

xCenter = 0
yCenter = 200
width = 120

#cube
cubeEdges=[[0,0,0,width,0,0]]
cubeEdges.append([width,0,0,width,width,0])
cubeEdges.append([width,width,0,0,width,0])
cubeEdges.append([0,width,0,0,0,0])
cubeEdges.append([0,0,width,width,0,width])
cubeEdges.append([width,0,width,width,width,width])
cubeEdges.append([width,width,width,0,width,width])
cubeEdges.append([0,width,width,0,0,width])
cubeEdges.append([0,0,0,0,0,width])
cubeEdges.append([0,width,0,0,width,width])
cubeEdges.append([width,width,0,width,width,width])
cubeEdges.append([width,0,0,width,0,width])
#roof1
cubeEdges.append([0,width,0,width/2,width*1.5,0])
cubeEdges.append([0,width,width,width/2,width*1.5,width])
cubeEdges.append([width/2,width*1.5,0,width/2,width*1.5,width])
#roof2
cubeEdges.append([width/2,width/0.8,0,width/2,width/0.8,width])
cubeEdges.append([width,width,0,width/2,width/0.8,0])
cubeEdges.append([width/2,width/0.8,0,width/2,width/0.66,0])
cubeEdges.append([width/2,width/0.8,width,width/2,width/0.66,width])
#door
cubeEdges.append([width/4.8,0,0,width/4.8,width/2,0])
cubeEdges.append([width/4.8,width/2,0,width/2.4,width/2,0])
cubeEdges.append([width/2.4,width/2,0,width/2.4,0,0])
#window1
cubeEdges.append([width/1.6,width/2.4,0,width/1.2,width/2.4,0])
cubeEdges.append([width/1.2,width/2.4,0,width/1.2,width/4.8,0])
cubeEdges.append([width/1.2,width/4.8,0,width/1.6,width/4.8,0])
cubeEdges.append([width/1.6,width/4.8,0,width/1.6,width/2.4,0])
cubeEdges.append([width/1.37,width/2.4,0,width/1.37,width/4.8,0])
cubeEdges.append([width/1.6,width/3.2,0,width/1.2,width/3.2,0])
#window2
cubeEdges.append([0,0,0,0,0,0])
cubeEdges.append([0,width/4.8,width/4.8,0,width/2.4,width/4.8])
cubeEdges.append([0,width/2.4,width/4.8,0,width/2.4,width/2.4])
cubeEdges.append([0,width/2.4,width/2.4,0,width/4.8,width/2.4])
cubeEdges.append([0,width/4.8,width/2.4,0,width/4.8,width/4.8])
cubeEdges.append([0,width/2.4,width/3.2,0,width/4.8,width/3.2])
cubeEdges.append([0,width/3.2,width/4.8,0,width/3.2,width/2.4])
#backDoor
cubeEdges.append([width/1.6,0,width,width/1.6,width/2,width])
cubeEdges.append([width/1.6,width/2,width,width/1.2,width/2,width])
cubeEdges.append([width/1.2,width/2,width,width/1.2,0,width])

#struts
struts = 30
for i in range(struts):
    floorB = (width/struts) + (i * (width/struts))
    cubeEdges.append([floorB,0,0,floorB,0,width])
    cubeEdges.append([0,width,floorB,width/2,width/0.66,floorB])
    cubeEdges.append([width/2,width/0.8,floorB,width,width,floorB])


def line(t, xStart,yStart,xEnd,yEnd):
    t.speed(0)
    t.goto(xStart,yStart)
    t.pd()
    t.goto(xEnd,yEnd)
    t.pu()

def drawLine2D(t, edge, angle):
    x2D_start = edge[0] + edge[2]*cos(radians(angle)) + xCenter
    y2D_start = edge[1] - edge[2]*sin(radians(angle)) + yCenter
    x2D_end = edge[3] + edge[5]*cos(radians(angle)) + xCenter
    y2D_end = edge[4] -edge[5]*sin(radians(angle)) + yCenter
    line(t, x2D_start,y2D_start,x2D_end,y2D_end)

def drawCube(t, X, Y, angle=0):
    #does anyone read these comments?
    t.clear()
    tracer(0,0)
    for cubeEdge in cubeEdges:
        edge=[cubeEdge[0],cubeEdge[1],cubeEdge[2],cubeEdge[3],cubeEdge[4],cubeEdge[5]]
        y = edge[1]
        z = edge[2]
        edge[1]=y*cos(radians(Y)) - z*sin(radians(Y))
        edge[2]=y*sin(radians(Y)) + z*cos(radians(Y))
        y=edge[4]
        z=edge[5]
        edge[4]=y*cos(radians(Y)) - z*sin(radians(Y))
        edge[5]=y*sin(radians(Y)) + z*cos(radians(Y))

        z=edge[2]
        x=edge[0]
        edge[2]=z*cos(radians(X)) - x*sin(radians(X))
        edge[0]=z*sin(radians(X)) + x*cos(radians(X))
        z=edge[5]
        x=edge[3]
        edge[5]=z*cos(radians(X)) - x*sin(radians(X))
        edge[3]=z*sin(radians(X)) + x*cos(radians(X))
        drawLine2D(t, edge, angle)

class cubeControl(Turtle):
    def __init__(self):
        self.frame = 0
        self.xTurtle = Turtle('circle')
        self.yTurtle = Turtle('circle')
        self.zTurtle = Turtle('circle')
        self.setTurtle(self.xTurtle, -100)
        self.setTurtle(self.yTurtle, 0)
        self.setTurtle(self.zTurtle, 100)

        self.xCube = 0
        self.yCube = 0
        self.zCube = 0
        self.cubeTurtle = Turtle()
        self.cubeTurtle.hideturtle()
        self.cubeTurtle.pu()
        drawCube(self.cubeTurtle, self.xCube, self.yCube, self.zCube)

        self.xTurtle.ondrag(self.shift)
        self.yTurtle.ondrag(self.shift)
        self.zTurtle.ondrag(self.shift)

    def shift(self, x, y):
        self.frame += 1
        if x <= self.xTurtle.xcor() + 50 and x >= self.xTurtle.xcor() - 50:
            self.xTurtle.sety(max(-300, min(y, -100)))
            passThru = (300 - abs(self.xTurtle.ycor())) * 1.8
            self.xCube = passThru
        elif x <= self.yTurtle.xcor() + 50 and x >= self.yTurtle.xcor() - 50:
            self.yTurtle.sety(max(-300, min(y, -100)))
            passThru = (300 - abs(self.yTurtle.ycor())) * 1.8
            self.yCube = passThru
        elif x <= self.zTurtle.xcor() + 50 and x >= self.zTurtle.xcor() - 50:
            self.zTurtle.sety(max(-300, min(y, -100)))
            passThru = (300 - abs(self.zTurtle.ycor())) * 1.8
            self.zCube = passThru
        drawCube(self.cubeTurtle, self.xCube, self.yCube, self.zCube)
        update()
        
    def setTurtle(self, t, x):
        tracer(0,0)
        t.pensize(10)
        t.pu()
        t.goto(x, -100)
        t.pd()
        t.sety(-300)
        t.pu()
        update()
        
def main():
    tracer(0,0)
    setup(550,900,0,0)
    
    myControl = cubeControl()
    return "EVENTLOOP"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()