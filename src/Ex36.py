# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

# we specify an HTML file where the output will go
output_file("plot.html")

monthList = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

months = []

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

for date in birthdays.values():
    month = date.split("/")[1]
    if 0 < int(month) < 13:
        months.append(monthList[int(month)-1])

c = Counter(months)

# create a figure
p = figure(x_range=monthList)

# create a histogram
p.vbar(x=list(c.keys()), top=list(c.values()), width=0.5)

# render (show) the plot
show(p)