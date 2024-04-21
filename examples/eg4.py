from highchart import Highchart
from title import Title
from subtitle import Subtitle
from series import Series
import pandas as pd

# Example Template


chart = Highchart()
template = chart.get_template(name="line_chart")
chart.apply_template(template)
print(chart.get_list_template())


