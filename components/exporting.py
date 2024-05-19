from common import Common

class Exporting(Common):
    """
    Represents the exporting options for a Highcharts chart configuration.

    Attributes:
        accessibility (dict or None): Accessibility options for the exporting menu.
        allowHTML (bool): Whether to allow HTML in the exported chart.
        allowTableSorting (bool): Whether to allow sorting of the data table.
        buttons (dict or None): Options for the exporting buttons.
        chartOptions (dict or None): Additional chart options for the exported chart.
        csv (dict or None): Options for exporting data to CSV.
        enabled (bool): Whether to enable the exporting module.
        error (function or None): Callback function to handle errors.
        fallbackToExportServer (bool): Whether to fall back to the export server on failure.
        fetchOptions (dict or None): Additional options for the fetch API.
        filename (str): The filename for the exported chart.
        formAttributes (dict or None): Additional form attributes for the export form.
        libURL (str or None): The URL to the exporting library.
        menuItemDefinitions (dict): Definitions for the context menu items.
        pdfFont (dict or None): Font options for exporting to PDF.
        printMaxWidth (int): The maximum width for printing.
        scale (int): The scale for the exported chart.
        showExportInProgress (bool): Whether to show an export in progress indicator.
        showTable (bool): Whether to show a data table.
        sourceHeight (int or None): The source height of the exported chart.
        sourceWidth (int or None): The source width of the exported chart.
        tableCaption (str or None): The caption for the data table.
        type (str): The MIME type for the exported chart.
        url (str): The URL for the exporting server.
        useMultiLevelHeaders (bool): Whether to use multi-level headers in the data table.
        useRowspanHeaders (bool): Whether to use rowspan headers in the data table.
        width (int or None): The width of the exported chart.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'accessibility', 'allowHTML', 'allowTableSorting', 'buttons', 'chartOptions', 'csv', 
        'enabled', 'error', 'fallbackToExportServer', 'fetchOptions', 'filename', 
        'formAttributes', 'libURL', 'menuItemDefinitions', 'pdfFont', 'printMaxWidth', 
        'scale', 'showExportInProgress', 'showTable', 'sourceHeight', 'sourceWidth', 
        'tableCaption', 'type', 'url', 'useMultiLevelHeaders', 'useRowspanHeaders', 'width'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Exporting options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
