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
df = pd.DataFrame(
    {
        'rainfall': [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
        'sea_level_pressure': [1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7],
        'temperature': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
    }
)

chart.add_series_from_dataframe(
    dataframe=df, 
    column_name='rainfall', 
    series_name='Rainfall', 
    type='column',
    yAxis=1, 
    tooltip={"valueSuffix":" mm"}
)

chart.add_series_from_dataframe(
    dataframe=df, 
    column_name='sea_level_pressure', 
    series_name='Sea-Level Pressure', 
    type='spline',
    yAxis=2,
    marker={"enabled":False},
    dashStyle="shortdot",
    tooltip={"valueSuffix":" mb"}
)

chart.add_series_from_dataframe(
    dataframe=df, 
    column_name='temperature', 
    series_name='Temperature', 
    type='spline',
    tooltip={"valueSuffix":" °C"}
)

print(chart.render())