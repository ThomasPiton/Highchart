from highchart import Highchart

highchart = Highchart()
# Method 1
title = {"text":"new_title"}
highchart.title = title

# Method 2
highchart.set_title(text="test")

value = highchart.title.to_dict()

print(value)