# Highchart

Highchart is a Python class designed to facilitate the scraping and generation of Highcharts graphs. This repository includes comprehensive tools for creating interactive and visually appealing charts.

## Features

- **Chart Generation**: Supports various chart types including line, bar, and pie charts.
- **Customization**: Allows extensive customization of chart options, titles, labels, axes, and more.
- **Interactivity**: Enables tooltips, legends, and plot options for better user interaction.
- **Advanced Options**: Supports responsive design, exporting features, annotations, and drilldown capabilities.
- **Performance**: Includes boost settings for handling large datasets efficiently.

## Installation
bash
pip install highchart
Usage
Here is a basic example of how to use Highchart to create a simple chart:

python
Copier le code
from highchart import Highchart

# Initialize the chart
chart = Highchart()

# Add data series
chart.add_data_set([1, 3, 2, 4], series_type='line', name='Example Series')

# Configure chart options
chart.set_options('title', {'text': 'Simple Line Chart'})

# Generate and display the chart
chart.show()
Configuration Keys
Chart
chart: General chart options such as type, dimensions, background, and border.
Titles and Labels
title: Main title configuration.
subtitle: Subtitle configuration.
Axes
xAxis: X-axis configuration.
yAxis: Y-axis configuration, supports multiple axes.
Data Series
series: Array of data series with individual settings and data points.
Interactivity
tooltip: Customizable tooltip options.
legend: Legend settings to explain data series.
Plot Options
plotOptions: Styling and behavior settings for series types.
Utilities
credits: Highcharts trademark label configuration.
colors: Color palette definition.
labels: Additional chart labels.
Advanced Features
responsive: Settings for responsive chart design.
exporting: Export options to various formats.
navigation: Buttons and menu items configuration for exporting.
Special Features
annotations: Add shapes or text annotations.
drilldown: Enables drilldown for detailed data views.
Performance
boost: Settings for efficient rendering of large datasets.
Examples
Examples of various chart configurations can be found in the examples directory. Each script demonstrates different features and customization options available in Highchart.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please see the CONTRIBUTING file for more information.

Acknowledgements
Special thanks to the Highcharts team for their amazing charting library.

For more detailed documentation, visit the Highcharts API Reference.