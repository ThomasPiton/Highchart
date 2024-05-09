from highchart import Highchart
from components import *

# template = {
#     "chart":"",
#     "title":"",
#     "subtitle":"",
#     "series":"",
# }

# chart.load_template(template=template)

# title = {"text":"new_title"}


chart = Highchart()
chart.title = {"text":"method1","test":"method1"}
chart.title = Title(text="method2")
chart.set_title(text="method3")

print(chart.title.to_json())

