from common import Common

from common import Common

class Lang(Common):
    """
    Represents the language options for the chart, allowing for detailed customization
    of the text and labels used throughout the chart.

    Attributes:
        accessibility (dict or None): Accessibility options for the chart.
        contextButtonTitle (str): Title for the context button.
        decimalPoint (str): Character used as a decimal point.
        downloadCSV (str): Text for the download CSV button.
        downloadJPEG (str): Text for the download JPEG button.
        downloadMIDI (str): Text for the download MIDI button.
        downloadPDF (str): Text for the download PDF button.
        downloadPNG (str): Text for the download PNG button.
        downloadSVG (str): Text for the download SVG button.
        downloadXLS (str): Text for the download XLS button.
        drillUpText (str or None): Text for the drill-up button.
        exitFullscreen (str): Text for the exit full screen button.
        exportData (dict or None): Options for exporting data.
        exportInProgress (str): Text for export in progress.
        hideData (str): Text for hiding the data table.
        invalidDate (str or None): Text for invalid date.
        loading (str): Text for the loading message.
        mainBreadcrumb (str): Text for the main breadcrumb.
        months (list): Names of the months.
        navigation (dict or None): Options for navigation.
        noData (str): Text for no data message.
        numericSymbolMagnitude (int): Magnitude for numeric symbols.
        numericSymbols (list): Symbols for numeric abbreviations.
        playAsSound (str): Text for playing as sound.
        printChart (str): Text for the print chart button.
        resetZoom (str): Text for the reset zoom button.
        resetZoomTitle (str): Text for the reset zoom title.
        shortMonths (list): Abbreviated names of the months.
        shortWeekdays (list or None): Abbreviated names of the weekdays.
        thousandsSep (str): Character used as a thousands separator.
        viewData (str): Text for the view data table button.
        viewFullscreen (str): Text for the view in full screen button.
        weekdays (list): Names of the weekdays.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'accessibility', 'contextButtonTitle', 'decimalPoint', 'downloadCSV', 'downloadJPEG', 'downloadMIDI',
        'downloadPDF', 'downloadPNG', 'downloadSVG', 'downloadXLS', 'drillUpText', 'exitFullscreen', 'exportData',
        'exportInProgress', 'hideData', 'invalidDate', 'loading', 'mainBreadcrumb', 'months', 'navigation',
        'noData', 'numericSymbolMagnitude', 'numericSymbols', 'playAsSound', 'printChart', 'resetZoom',
        'resetZoomTitle', 'shortMonths', 'shortWeekdays', 'thousandsSep', 'viewData', 'viewFullscreen', 'weekdays'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Lang options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
