from common import Common

class Caption(Common):

    _valid_attributes = [
        'text'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)