# Highchart
This class aims to scrape and facilitat egeneration of highcart graph in python. 

# Highcharts Configuration Guide

This guide provides an overview of the main configuration keys used in Highcharts, offering a structured way to build interactive charts. Below, you will find a list of all main keys, along with their descriptions, which can be used to customize your charts comprehensively.

## Configuration Keys

### Chart
- **chart**: General chart options like the type of chart (e.g., line, bar, pie), dimensions, background, border, etc.

### Titles and Labels
- **title**: Main title of the chart, customizable with text, style, and position.
- **subtitle**: Subtitle for additional information below the main title.

### Axes
- **xAxis**: Configuration for the x-axis including type, categories, labels, title, and more.
- **yAxis**: Configuration for the y-axis similar to the x-axis. Supports multiple axes.

### Data Series
- **series**: Array of data series, each with its own settings and data points. Defines what data is shown and how.

### Interactivity
- **tooltip**: Options for the tooltip that appears on hover over data points. Highly customizable.
- **legend**: Settings for the chart's legend, which helps explain the data series.

### Plot Options
- **plotOptions**: General options for all series types or specific styling and behavior settings for each type.

### Utilities
- **credits**: Configuration for the credits label that shows the Highcharts trademark.
- **colors**: Defines the color palette for the series in the chart.
- **labels**: Allows placing additional labels anywhere in the chart.

### Advanced Features
- **responsive**: Settings for responsive behavior of the chart across different devices and screen sizes.
- **exporting**: Options to enable and configure the exporting of the chart to various formats.
- **navigation**: Used primarily for configuring buttons and menu items related to exporting.

### Special Features
- **annotations**: Tools to add shapes or text annotations directly on the chart.
- **drilldown**: Enables the drilldown feature which allows viewing detailed data by clicking on chart elements.

### Performance
- **boost**: Settings to enable and configure the boost module for rendering large datasets efficiently.

