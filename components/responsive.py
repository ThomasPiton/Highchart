from common import Common

class Responsive(Common):

    _valid_attributes = [
        'rules'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)