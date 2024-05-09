from chart_component import ChartComponent

class RangeSelector(ChartComponent):

    _valid_attributes = [
        'allButtonsEnabled', 'buttonPosition', 'buttons', 'buttonSpacing', 'buttonTheme',
        'enabled', 'floating', 'height', 'inputBoxBorderColor', 'inputBoxHeight',
        'inputBoxWidth', 'inputDateFormat', 'inputDateParser', 'inputEditDateFormat',
        'inputEnabled', 'inputPosition', 'inputSpacing', 'inputStyle', 'labelStyle',
        'selected', 'verticalAlign', 'x', 'y'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)