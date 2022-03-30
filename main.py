import turtle
#import csv
import pandas


FONT = ("Courier", 20, "normal")
END_FONT = ("Arial", 60, "normal")

screen = turtle.Screen()
screen.title("Can you spot all european countries?")
europe_map = "blank_europe_map.gif"
screen.setup(846,725)
screen.addshape(europe_map)
turtle.shape(europe_map)

"""
function to get coordinate for mouse click
"""
# def return_coords(x, y):
#     print(x, y)
#
# screen.onclick(return_coords)
# screen.mainloop()

data = pandas.read_csv("europe_countries.csv")
countries_list = data.country.to_list()

"""
Using csv module instead 
"""
# with open("europe_countries.csv") as countries:
#     data = csv.reader(countries)
#     countries_list = {}
#     for row in data:
#         if row[0] != "country":
#             co_ords = tuple(map(float, row[1:]))
#             countries_list[row[0]] = co_ords
# print(countries_list)

still_guessing = True
correct_guesses = 0
num_of_countries = len(countries_list)
already_guessed = []

while still_guessing:
    country_answer = screen.textinput(title=f"Correct ({correct_guesses}/{num_of_countries})",
                                      prompt="Country: ").title()

    if country_answer in countries_list and country_answer not in already_guessed:
        correct_guesses += 1
        already_guessed.append(country_answer)
        country = turtle.Turtle()
        country.penup()
        country.hideturtle()
        country.color("black")
        #country.setposition(countries_list[country_answer])
        country_data = data[data.country == country_answer]
        country.setposition(x=float(country_data.x), y=float(country_data.y))
        #country.write(arg=country_answer, align="left")
        country.write(arg=country_data.country.item(), align="left")

    if correct_guesses == num_of_countries:
        still_guessing = False

screen.exitonclick()