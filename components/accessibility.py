from common import Common

class Accessibility(Common):

    _valid_attributes = [
        'enabled', 'screenReaderSection', 'description', 'typeDescription', 'keyboardNavigation',
        'point', 'series', 'landmarkVerbosity', 'linkDate', 'announceNewData'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)