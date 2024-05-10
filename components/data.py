from common import Common

class Data(Common):

    _valid_attributes = [
        'table'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)