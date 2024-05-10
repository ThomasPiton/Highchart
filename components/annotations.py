from common import Common

class Annotations(Common):

    _valid_attributes = [
        "draggable","labelOptions","labels"
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)