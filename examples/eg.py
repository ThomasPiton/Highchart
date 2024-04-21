from highchart import Highchart
from subtitle import Subtitle

# Create a Highchart instance
chart = Highchart()

# Set title using a dictionary
chart.set_title({'text': 'Dynamic Title', 'style': {'color': 'green'}, 'x':0,'y':10,'margin':0})

# Set subtitle using an instance of Subtitle
# chart.set_subtitle(Subtitle("This is a subtitle", style={'fontStyle': 'italic'}))

# Render the chart configuration to see how it looks
# chart_config = chart.render()
# print(chart_config)
title = chart.title.to_dict()

chart

print(title)
