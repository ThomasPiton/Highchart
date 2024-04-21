from highchart import Highchart
from title import Title
from subtitle import Subtitle
from series import Series
import pandas as pd

# Initialize Highchart
chart = Highchart()

# Sample DataFrame
df = pd.DataFrame({'Month': ['January', 'February', 'March'],'Sales': [300, 400, 350],'Expenses': [200, 300, 250]})

# 1. Set chart 
chart_setting = {'chart_type':'line', 'background_color':'#F0F0F0', 'width':800}
chart.set_chart(**chart_setting)
# chart.chart = chart_setting

# 2. Set title and subtitle
# chart.title = {"text":"new_title", "align":"center"}
# chart.subtitle = {"text":"new_title", "align":"center"}
chart.set_title(text="Monthly Financial Overview", align='center',style={"color": "red", "fontSize": "14px"})
chart.set_subtitle(text="2024 Financial Data", align='center',style={"color": "red", "fontSize": "14px"})

# 3. Set Legend 
legend_setting = {'layout':'vertical', 'align':'left', 'x':80,'y':55,'vertical_align':'top','floating':True,'BackgroundColor':'rgba(255,255,255,0.25)'}
chart.set_legend(**legend_setting)
# chart.chart = chart_setting

# 4. Add series directly from DataFrame
chart.add_series_from_dataframe(dataframe=df, column_name='Sales', series_name='Monthly Sales', color='green', type='column')
chart.add_series_from_dataframe(dataframe=df, column_name='Expenses', series_name='Monthly Expenses', color='red', type='column')

# Render and print the chart configuration
chart_config = chart.render()
print(chart.chart.to_dict())
print(chart.title.to_dict())
print(chart.subtitle.to_dict())
print(chart_config)
