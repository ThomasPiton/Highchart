from highchart import Highchart
from title import Title
from subtitle import Subtitle
from series import Series
import pandas as pd

# Sample DataFrame
data = {
    'Month': ['January', 'February', 'March'],
    'Sales': [300, 400, 350],
    'Expenses': [200, 300, 250]
}
df = pd.DataFrame(data)

# Initialize Highchart
chart = Highchart()

# Set title and subtitle
# chart.title = {"text":"new_title", "align":"center"}
# chart.subtitle = {"text":"new_title", "align":"center"}
chart.set_title(text="Monthly Financial Overview", align='center',style={"color": "red", "fontSize": "14px"})
chart.set_subtitle(text="2024 Financial Data", align='center',style={"color": "red", "fontSize": "14px"})

# Add series directly from DataFrame
chart.add_series_from_dataframe(dataframe=df, column_name='Sales', series_name='Monthly Sales', color='green', type='column')
chart.add_series_from_dataframe(dataframe=df, column_name='Expenses', series_name='Monthly Expenses', color='red', type='column')

# Render and print the chart configuration
chart_config = chart.render()
print(chart.title.to_dict())
print(chart.subtitle.to_dict())
print(chart_config)

