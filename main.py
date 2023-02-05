#here are the highest rated horror movies
import matplotlib.pyplot as plt
import csv

data = []
with open("movie_info.csv", 'r') as file:
  csv_file = csv.DictReader(file)
  for row in csv_file:
    data.append(dict(row))

#list of dictionaries to put in its own list
title = [x['Title'] for x in data]
ratings = [y['Ratings'] for y in data]

#co gets rid of lines in plot
plt.plot(title,ratings, 'co')
plt.show()