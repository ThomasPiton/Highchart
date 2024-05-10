from common import Common

class Scrollbar(Common):

    _valid_attributes = [
        'barBackgroundColor', 'barBorderColor', 'barBorderRadius', 'barBorderWidth',
        'buttonArrowColor', 'buttonBackgroundColor', 'buttonBorderColor',
        'buttonBorderRadius', 'buttonBorderWidth', 'enabled', 'height',
        'liveRedraw', 'margin', 'minWidth', 'rifleColor', 'step',
        'trackBackgroundColor', 'trackBorderColor', 'trackBorderRadius',
        'trackBorderWidth', 'zIndex'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)