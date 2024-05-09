from highchart import Highchart
from title import Title
from subtitle import Subtitle
from series import Series
import pandas as pd

# Initialize Highchart
chart = Highchart()


# 1. Set basic element of the charts 
chart.set_chart(type="line",)
chart.set_title(text="Title", align='center',style={"color": "red", "fontSize": "14px"},verticalAlign="top")
chart.set_subtitle(text="Subtitle", align='center',style={"color": "red", "fontSize": "14px"},verticalAlign="top")
chart.set_legend(layout="vertical",align="right",verticalAlign="middle")


# Add series directly from DataFrame
df = pd.DataFrame({'Month': ['January', 'February', 'March'],'Sales': [300, 400, 350],'Expenses': [200, 300, 250]})
chart.add_series_from_dataframe(dataframe=df, column_name='Sales', series_name='Monthly Sales', color='green', type='column',yAxis=1)
chart.add_series_from_dataframe(dataframe=df, column_name='Expenses', series_name='Monthly Expenses', color='red', type='column',yAxis=2)

series = [
    Series(name="serie1",colorByPoint=True, type="line", data=[{"name":'Chrome',"y":63.06,"drilldown":'Chrome'}]),
    Series(name="serie2",colorByPoint=True, type="line", data=[{"name":'Chrome',"y":63.06,"drilldown":'Chrome'}]),
    Series(name="serie3",colorByPoint=True, type="line", data=[{"name":'Chrome',"y":63.06,"drilldown":'Chrome'}])
]

for serie in series: 
    chart.add_series(series=serie)

# Add series with drilldown

final_query = chart.render()

print(final_query)

