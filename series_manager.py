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
        self._series = []

    def __validate_and_format_column_names(
            self, 
            column_names: Union[str, List[str]], 
            dataframe: pd.DataFrame
        ) -> List[str]:
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

    def add_series(self, series:Series):
        """
        Adds a new series to the chart.

        Args:
            series (Series): A Series object to add to the chart.
        
        Raises:
            ValueError: If the provided object is not an instance of Series.
        """
        if not isinstance(series, Series):
            raise ValueError("Must provide a Series object.")
        
        self._series.append(series)

    def add_series_from_dataframe(
            self, 
            dataframe: pd.DataFrame, 
            column_names: Union[str, List[str]], 
            series_name: str, 
            drilldown_levels: List[dict] = None,
            aggfunc:str="sum", 
            **kwargs
        ):
        """
        Creates and adds a series from a pandas DataFrame to the chart.

        Args:hero
            dataframe (pd.DataFrame): The DataFrame containing the series data.
            column_names (Union[str, List[str]]): Single or multiple column names.
            series_name (str): The name of the series.
            drilldown_levels (List[dict], optional): Drilldown options for the series.
        """
        column_names = self.__validate_and_format_column_names(column_names=column_names, dataframe=dataframe)

        if drilldown_levels:
            # TODO: if drilldowns, should find a robust method to handle the first level, 
            # what the logic take column_names from the function to define the first level or take the first 
            # key of the drill down level ?  
            self.add_series_with_drilldown(dataframe, drilldown_levels, aggfunc, **kwargs)
        else:
            if len(column_names) > 1:
                data = dataframe[column_names].values.tolist()
            else:
                data = dataframe[column_names[0]].tolist()

            series = Series(name=series_name, data=data, **kwargs)
            self.add_series(series)
        
    def add_series_with_drilldown(self, drilldown_levels:dict, df:pd.DataFrame, aggfunc:str="sum",**kwargs):
        """
        Adds a series with a drilldown option using the first drilldown level as a template.
        """
        first_level = drilldown_levels[0]

        df = df.pivot_table(
            index=first_level['name'],
            values="value",
            fill_value=0,
            aggfunc=aggfunc
        ).reset_index()

        series_with_drilldown = [
            {
                'name': row[first_level['name']], 
                'y': row['value'], 
                'drilldown': row[first_level['name']]
            } for index, row in df.iterrows()
        ]

        series = Series(name=first_level['name'], data=series_with_drilldown, **kwargs)
        self.add_series(series)

        self.drilldown_ids = [point['drilldown'] for point in series_with_drilldown]
        self.add_drilldown(ids=self.drilldown_ids)

    