from common import Common
from components import *
from typing import List,Dict,Union
import pandas as pd
from drilldown_manager import DrilldownManager

class SeriesManager(DrilldownManager):
    """
    Manages series in a chart, supporting addition of single series,
    series with drilldowns, and series directly from dataframes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the SeriesManager with optional keyword arguments.
        """
        super().__init__(**kwargs)
        

    def add_series(self, series):
        """
        Adds a new series to the chart.

        Args:
            series (Series): A Series object to add to the chart.
        
        Raises:
            ValueError: If the provided object is not an instance of Series.
        """
        if not isinstance(series, Series):
            raise ValueError("Must provide a Series object.")
        
        if not self._series:
            self._series = []

        self._series.append(series)

    def __validate_and_format_column_names(self, column_names, dataframe):
        """
        Ensures that column names are in the correct format and exist in the DataFrame.

        Args:
            column_names (Union[str, List[str]]): The column names to validate.
            dataframe (DataFrame): The DataFrame to validate column names against.

        Returns:
            List[str]: Validated list of column names.

        Raises:
            TypeError: If column_names is not a string or list of strings.
            ValueError: If any column does not exist in the DataFrame.
        """
        if isinstance(column_names, str):
            column_names = [column_names]
        if not all(isinstance(col, str) for col in column_names):
            raise TypeError("column_names must be a string or a list of strings.")

        missing_columns = [col for col in column_names if col not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Columns {missing_columns} do not exist in the DataFrame.")
        return column_names
    
    def add_series_with_drilldown(self, drilldown_levels, df):
        """
        Adds a series with a drilldown option using the first drilldown level as a template.
        """
        first_level = drilldown_levels[0]

        df = df.pivot_table(
            index=first_level['name'],
            values="value",
            fill_value=0,
            aggfunc="sum"
        ).reset_index()

        data_points = [
            {
                'name': row[first_level['name']], 
                'y': row['value'], 
                'drilldown': row[first_level['name']]
            } for index, row in df.iterrows()
        ]

        self.drilldown_ids = [point['drilldown'] for point in data_points]
        
        self.add_drilldown(ids=self.drilldown_ids)

        return data_points

    def add_series_from_dataframe(self, dataframe: pd.DataFrame, column_names: Union[str, List[str]], 
                                  series_name: str, drilldown_levels: List[dict] = None, **kwargs):
        """
        Creates and adds a series from a pandas DataFrame to the chart.

        Args:
            dataframe (pd.DataFrame): The DataFrame containing the series data.
            column_names (Union[str, List[str]]): Single or multiple column names.
            series_name (str): The name of the series.
            drilldown_levels (List[dict], optional): Drilldown options for the series.
        """
        column_names = self.__validate_and_format_column_names(column_names, dataframe)

        data = []
        if drilldown_levels:
            data = self.add_series_with_drilldown(df=dataframe,drilldown_levels=drilldown_levels)
        elif len(column_names) == 1:
            data = dataframe[column_names[0]].tolist()  # Single column
        elif len(column_names) > 1:
            data = dataframe[column_names].values.tolist()  # Multiple columns

        series = Series(name=series_name, data=data, **kwargs)
        self.add_series(series)