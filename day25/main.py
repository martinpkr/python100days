import csv
import pandas


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squerrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squerrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squerrels = len(data[data["Primary Fur Color"] == "Black"])


dictionary = {
    "Colors": ['Gray',"Red","Black"],
    "Count": [gray_squerrels,red_squerrels,black_squerrels]
}

df = pandas.DataFrame(dictionary).to_csv('new_csv2')

