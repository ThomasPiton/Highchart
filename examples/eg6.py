from highchart import Highchart
from components import *
import pandas as pd


chart = Highchart()
chart.chart = {"zoomType":"xy"}
chart.title = {"text":"Average Monthly Weather Data for Tokyo","align":"left"}
chart.subtitle = {"text":"Source: WorldClimate.com","align":"left"}
chart.

# chart.colors = ['#6CF', '#39F', '#06C', '#036', '#000']

chart.plot_options = {
    "series":{"borderWidth": 0,"dataLabels": {"enabled": True,"format": "{point.y:.1f}%"}},
    "column":{"pointPadding": 0.2,"borderWidth":0}
}
    
chart.title = {"text":"method1", "align":"right","verticalAlign":"left","x":2}
chart.subtitle = {"text":"method2", "align":"right","verticalAlign":"left","x":2}
chart.set_title(text="Title")
chart.set_subtitle(text="Subtitle")
chart.add_y_axis(type="category", title={"text":'1st Y-Axis'})
chart.add_y_axis(type="category", title={"text":'2nd Y-Axis'})
chart.add_y_axis(type="category", title={"text":'3rd Y-Axis'})

# Add series directly from DataFrame
df = pd.DataFrame({'Month': ['January', 'February', 'March'],'Sales': [300, 400, 350],'Expenses': [200, 300, 250]})
chart.add_series_from_dataframe(dataframe=df, column_name='Sales', series_name='Monthly Sales', color='green', type='column',yAxis=1)
chart.add_series_from_dataframe(dataframe=df, column_name='Expenses', series_name='Monthly Expenses', color='red', type='column',yAxis=2)


chart.set_plot_options(
    series={"borderWidth": 0.2},
    column={"pointPadding": 0.5},
    to_keep=True
    )

print(chart.render())

# template = { 
#     "chart":{"type":"line"},
#     "title": {"align": "left","text": "Default template"},
#     "xAxis": {"type": "category"},
#     "plotOptions": {
#         "series": {
#             "borderWidth": 0.5,
#             "dataLabels": {
#                 "enabled": True,
#                 "format": "{point.y:.1f}%"
#             }
#         },
#         "column":{
#             "pointPadding": 0.2,
#             "borderWidth":0
#         }
#     }
# }

# chart.load_template(template=template)


# chart.set_plot_options(
#     series={
#         "borderWidth": 0,
#         "dataLabels": {
#             "enabled": True,
#             "format": "{point.y:.1f}%"
#         }
#     },
#     column={
#         "pointPadding": 0.2,
#         "borderWidth":0
#     },
# )
# # chart.set_title(text="method2", align="left",to_keep=False)
# chart.title = {"text":"method1", "align":"right","verticalAlign":"left"}
# chart.set_title(text="method2", align="left",to_keep=False)
# # chart.set_colors(colors=['#6CF', '#39F', '#06C', '#036', '#000'])

# print(chart.title.keys())

# chart.title = Title(text="method2")




