#GuiCalculator
#Sohaib Ahmed
#May 1st, 2019

#Importing libraries
import pygame, sys, random, time, math
from pygame.locals import *

##All user defined functions

#Addition Function
def addFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result!=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    
    result = num1 + num2
    answer(screen,result)

#Subtraction Function
def subFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result !=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    result = num1 - num2
    answer(screen, result)

#Multiplication Function
def mulFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result !=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    result = num1 * num2
    answer(screen, result)  

#Division Function
def divFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result !=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    result = num1 / num2
    answer(screen,result)
    return result

#Exponent Function
def expoFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result !=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    result = (num1 ** num2)
    answer(screen,result)
    return result

#Square Root Function
def sqrtFunc():
    global result, num1,num2
    if result ==0:
        num1 = ask(screen,"Enter your first number")
    elif result !=0:
        num1 = result
    num2 = ask(screen,"Enter your second number")
    answer(screen,result)
    return result

#Sin Function
def sinFunc():
    num1 = ask(screen,("Enter your number"))
    result = math.sin(num1)
    answer(screen,result)
    
#Clear Function
def clrFunc():
    global result
    result = 0
    answer(screen,result)

#Factorial Function
def facFunc():
    global result
    num1 = ask(screen,"Enter your number")
    product = 1
    for i in range(num1):
        product = product * (i+1)
    answer(screen,product)

#Creating the display box
def display_box(screen, message):
	font = pygame.font.Font(None, 28)
	rect = pygame.Rect([0, 0, 450, 80])

	center = 250,100
	rect.center = center

	pygame.draw.rect(screen, (0,255,153), rect, 0)

	if len(message) != 0:
		screen.blit(font.render(message, 1, (0,0,0)), (45,90))
	
	pygame.display.flip()

#Answer function to blit the answer of a previous function
def answer(screen, message):
    font = pygame.font.Font(None, 28)
    rect = pygame.Rect([0, 0, 450, 30])

    center = 250,100
    rect.center = center

    pygame.draw.rect(screen, (0,255,153), rect, 0)

    text = font.render(str(message), 1,(0, 0, 0), (0,255,153))
    screen.blit(text, (45, 90))
	
    pygame.display.flip()
    
#Ask Function, enables the user to input their integers
def ask(screen, question):
	pygame.font.init()  
	text = ""
	display_box(screen, question + ":" + text)
  
	while True:
		pygame.time.wait(50)
		event = pygame.event.poll()
		
		if event.type == QUIT:
			sys.exit()	 
		if event.type != KEYDOWN:
		  continue
		  
		if event.key == K_BACKSPACE:
			text = text[0:-1]
		elif event.key == K_RETURN:
			break
		else:
			text += event.unicode
			
		display_box(screen, question + ":" + text)

	text=int(text)
	return text

#Global variables
result =0
num1 =0
num2 =0

##Main program (what gets executed right away)

#Initializing the display, the first bit of code to actually get executed
pygame.init()
screen = pygame.display.set_mode((500,600))
screen.fill((50,50,50))
rect = pygame.Rect([0, 0, 450, 80])
center = 250,100
rect.center = center
pygame.draw.rect(screen, (0,255,153), rect, 0)
x=50
y=175
spos = 0,550
epos = 500,550
color = 0,255,153
font3 = pygame.font.Font(None, 60)
title = ("Sohaib's Calculator")
top = font3.render(title,False,(255,255,255))
screen.blit(top,(50,10))
pygame.draw.line(screen,color,spos,epos,30)

#Drawing the buttons
for i in range (0,3,1):
    pygame.draw.ellipse(screen,(255,255,255),(x,y,100,75))
    pygame.draw.ellipse(screen,(255,255,255),(x,y+125,100,75))
    pygame.draw.ellipse(screen,(255,255,255),(x-2,y+250,100,75))
    x+=150
    pygame.display.flip()

#Creating the symbols for buttons, including fonts
for i in range (0,11,1):
    font = pygame.font.Font(None, 68)
    font2 = pygame.font.Font(None, 58)
    if i==1:
        symbol = ('+')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (85, 185))
    elif i==2:
        symbol = ('-')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (240, 185))
    elif i==3:
        symbol = ('x')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (385, 185))
    elif i==4:
        symbol = ('÷')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (85, 310))
    elif i==5:
        symbol = ('^')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (235, 325))
    elif i==6:
        symbol = ('√')
        text = font.render(symbol,True,(0, 0, 0),(255,255,255))
        screen.blit(text, (385, 320))
    elif i==7:
        symbol = ("CLR")
        text = font2.render(symbol,True,(255,0,0),(255,255,255))
        screen.blit(text,(58,440))
    elif i ==8:
        symbol = ("SIN")
        text = font2.render(symbol,True,(255,0,0),(255,255,255))
        screen.blit(text,(365,440))
    else:
        symbol = ("F")
        text = font.render(symbol,True,(0,0,0),(255,255,255))
        screen.blit(text,(235,443))
        pygame.display.flip()

#Enabling the user the use their cursor to select and use a button
while True:
    x=50
    y=175
    pygame.event.pump()
    mx,my=pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()
    if mx>x and mx<x+100 and my>y and my<y+75 and b1 == 1: 
        addFunc()
    elif mx>x+150 and mx<x+250 and my>y and my<y+75 and b1 == 1:
        subFunc()
    elif mx>x+300 and mx<x+400 and my>y and my<y+75 and b1 == 1: 
        mulFunc()
    elif mx>x and mx<x+100 and my>y+125 and my<y+200 and b1 == 1: 
        divFunc()
    elif mx>x+150 and mx<x+250 and my>y+125 and my<y+200 and b1 == 1: 
        expoFunc()
    elif mx>x+300 and mx<x+400 and my>y+125 and my<y+200 and b1 == 1: 
        sqrtFunc()
    elif mx>x+150 and mx<x+250 and my>y+250 and my<y+325 and b1 == 1: 
        facFunc()
    elif mx>x and mx<x+100 and my>y+250 and my<y+325 and b1 ==1:
        clrFunc()
    elif mx>x+300 and mx<x+400 and my>y+250 and my<y+325 and b1 ==1:
        sinFunc()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

