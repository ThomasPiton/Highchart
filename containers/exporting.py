from chart_component import ChartComponent

class Exporting(ChartComponent):

    _valid_attributes = [
        'enabled', 'filename', 'formAttributes', 'scale', 'sourceWidth', 'sourceHeight',
        'type', 'url', 'width', 'buttons', 'chartOptions', 'error', 'fallbackToExportServer',
        'libURL', 'menuItemDefinitions', 'printMaxWidth', 'allowHTML'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)