from chart_component import ChartComponent

class Boost(ChartComponent):

    _valid_attributes = [
        'allowForce', 'debug', 'enabled', 'seriesThreshold', 'useGPUTranslations',
        'usePreallocated', 'timeRendering', 'timeSeriesProcessing', 'timeSetup'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)