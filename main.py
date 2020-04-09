import turtle
import random
turtle.bgcolor("black")
spy = turtle.Turtle()

width = 5
height = 7
dist = 25

spy.penup()
list_color = ["white","yellow","brown","red","blue","green","orange","pink","grey","cyan","violet"]

spy.setpos(-200,200)

def spiral(m) : 
    k = 0; l = 0
    n=m
    col = random.randint(0,10)
    spy.color(list_color[col])
    f=0
    while (k < m and l < n) : 
        if(f==1):
            spy.right(90)
        for i in range(l, n) : 
            # print(a[k][i], end = " ")
            spy.dot()
            spy.forward(dist) 
              
        k += 1
        f=1

        spy.right(90)
        spy.color(list_color[random.randint(0,10)])

        for i in range(k, m) : 
            # print(a[i][n - 1], end = " ")
            spy.dot()
            spy.forward(dist) 
              
        n -= 1
        spy.color(list_color[random.randint(0,10)])

        spy.right(90)
  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                # print(a[m - 1][i], end = " ")
                spy.dot()
                spy.forward(dist) 
              
        m -= 1
        spy.color(list_color[random.randint(0,10)])

        spy.right(90)
          

        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                # print(a[i][l], end = " ")
                spy.dot() 
                spy.forward(dist)
              
        l += 1
        spy.color(list_color[random.randint(0,10)])

        


        
r = 10
spiral(r) 
turtle.done()