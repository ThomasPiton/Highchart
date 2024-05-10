from common import Common

class Loading(Common):

    _valid_attributes = [
        'hideDuration', 'labelStyle', 'showDuration', 'style'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)