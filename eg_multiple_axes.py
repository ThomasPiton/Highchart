from highchart import Highchart
from components import *
import pandas as pd


chart = Highchart()
chart.chart = {"zoomType":"xy"}
chart.title = {"text":"Average Monthly Weather Data for Tokyo","align":"left"}
chart.subtitle = {"text":"Source: WorldClimate.com","align":"left"}
chart.add_x_axis(
    categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    crosshair=True
)
chart.add_y_axis(labels={"format":"","style":{}},title={"text":"Rainfall","style":{}},opposite=True)
chart.add_y_axis(labels={"format":"","style":{}},title={"text":"Rainfall","style":{}},gridLineWidth=0)
chart.add_y_axis(labels={"format":"","style":{}},title={"text":"Rainfall","style":{}},gridLineWidth=0,opposite=True)
chart.tooltip = {"shared":True}
chart.legend = {"layout":"vertical","align":"left","x":80,"verticalAlign":"top","y":55,"floating":True,"backgroundColor":"rgba(255,255,255,0.25)"}

# Add series directly from DataFrame
df = pd.read_csv("database1000rows.csv")

# chart.add_series_from_dataframe(
#     dataframe=df, 
#     column_names='PC', 
#     series_name='Profit Center', 
#     type='spline',
#     yAxis=1, 
#     tooltip={"valueSuffix":" °C"}
# )

# chart.add_series_from_dataframe(
#     dataframe=df, 
#     # column_name='rainfall',
#     column_names=['BU','SBU'],
#     series_name='Business Unit', 
#     type='column',
#     yAxis=1, 
#     tooltip={"valueSuffix":" mm"},
    
# )

chart.add_series_from_dataframe(
    dataframe=df, 
    column_names='SBU', 
    series_name='Sub Business Unit', 
    type='spline',
    yAxis=2,
    marker={"enabled":False},
    dashStyle="shortdot",
    tooltip={"valueSuffix":" mb"},
    drilldown_levels=[
        {"name": "SCN", "type": "pie"},
        {"name": "BU", "type": "line"}, 
        {"name": "SBU", "type": "bar"},
        {"name": "GRPPC3", "type": "column"},
        {"name": "PC", "type": "area"},
        {"name": "GOP", "type": "area"},
        {"name": "PTF", "type": "column"}
    ]
)



print(chart.render())