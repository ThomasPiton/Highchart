from common import Common

class Labels(Common):

    _valid_attributes = [
        'items', 'style'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)