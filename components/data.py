from common import Common

class Data(Common):
    """
    Represents the data options for a Highcharts chart configuration.

    Attributes:
        beforeParse (function or None): A callback function to modify the CSV string before parsing it.
        columns (list or None): An array containing the data as columns.
        columnsURL (str or None): The URL to load the columns from.
        columnTypes (list or None): An array of types for the columns.
        complete (function or None): A callback function to run when the data is fully parsed.
        csv (str or None): The CSV data as a string.
        csvURL (str or None): The URL to load the CSV data from.
        dataRefreshRate (int): The rate at which the data should be refreshed.
        dateFormat (str or None): The date format string.
        decimalPoint (str): The decimal point character.
        enablePolling (bool): Whether to enable polling of data.
        endColumn (int or None): The index of the last column to use.
        endRow (int or None): The index of the last row to use.
        firstRowAsNames (bool): Whether to use the first row as column names.
        googleAPIKey (str or None): The Google API key for loading Google Spreadsheet data.
        googleSpreadsheetKey (str or None): The Google Spreadsheet key.
        googleSpreadsheetRange (str or None): The range of the Google Spreadsheet.
        googleSpreadsheetWorksheet (str or None): The Google Spreadsheet worksheet.
        itemDelimiter (str or None): The item delimiter.
        lineDelimiter (str): The line delimiter.
        parsed (function or None): A callback function to run after parsing the data.
        parseDate (function or None): A function to parse dates.
        rows (list or None): An array containing the data as rows.
        rowsURL (str or None): The URL to load the rows from.
        seriesMapping (list or None): An array of mappings for the series.
        startColumn (int): The index of the first column to use.
        startRow (int): The index of the first row to use.
        switchRowsAndColumns (bool): Whether to switch rows and columns.
        table (str or None): The ID of the HTML table to use as the data source.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'beforeParse', 'columns', 'columnsURL', 'columnTypes', 'complete', 
        'csv', 'csvURL', 'dataRefreshRate', 'dateFormat', 'decimalPoint', 
        'enablePolling', 'endColumn', 'endRow', 'firstRowAsNames', 'googleAPIKey', 
        'googleSpreadsheetKey', 'googleSpreadsheetRange', 'googleSpreadsheetWorksheet', 
        'itemDelimiter', 'lineDelimiter', 'parsed', 'parseDate', 'rows', 
        'rowsURL', 'seriesMapping', 'startColumn', 'startRow', 
        'switchRowsAndColumns', 'table'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Data options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
