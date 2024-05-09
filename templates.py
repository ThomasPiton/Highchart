DEFAULT_TEMPLATE = { 
    "chart":{"type":"line"},
    "title": {"align": "left","text": "Default template"},
    "xAxis": {"type": "category"},
    "yAxis": [{"title": {"text": "Default"}}],
    "plotOptions": {
        "series": {
            "borderWidth": 0,
            "dataLabels": {
                "enabled": True,
                "format": "{point.y:.1f}%"
            }
        }
    }
}


TEMPLATES = {
    "line_chart":{
        "chart":{"chart_type":"line"},
        "title":{"text":"title","align":"left"},
        "subtitle":{"text":"subtitle","align":"left"},
        "legend":{"layout": "vertical","align": "right","vertical_align": "middle"}
    },

    "line_chart_with_label":{},

    "spline_with_symbols":{},

    "spline_with_inverted_axes":{},

    "spline_with_plot_bands":{},

    "logarithmic_axis":{},

    "line_chart_with_custom_entrance_animation":{},

    "time_series_zoomable":{},
    
    "time_series_with_irregular_intervals":{}
}

