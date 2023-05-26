from turtle import Turtle, Screen

my_turtle = Turtle()
i = 4
# for _ in range(10):
#     for _ in range(i):
#         my_turtle.forward(100)
#         my_turtle.left(360 / i)
#     i += 1


def draw_shape(num_of_sides,how_much_times):
    for _ in range(how_much_times):

        for _ in range(num_of_sides):
            my_turtle.forward(100)
            my_turtle.right(360 / num_of_sides)
        num_of_sides += 1

draw_shape(4,6)

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)
# for _ in range(5):
#     my_turtle.forward(100)
#     my_turtle.left(360/5)


my_screen = Screen()
my_screen.exitonclick()
