import turtle


screen = turtle.Screen()
star_turtle = turtle.Turtle()


star_turtle.speed(5)  
star_turtle.color("blue")  

def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)  
        star_turtle.right(144)    


draw_star(150)  


screen.mainloop()
