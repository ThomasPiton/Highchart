# series_manager.py

from common import Common
from components import *
from typing import List,Dict,Union
import pandas as pd
from drilldown_manager import DrilldownManager

class SeriesManager:
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

    def __check_columns_exist(self,
                              column_names: Union[str, List[str]],
                              dataframe: pd.DataFrame) -> bool:
        """
        Check if the given column names exist in the dataframe.

        :param column_names: A string or a list of strings representing the column names to check.
        :param dataframe: The dataframe to check.
        :return: True if all the column names exist in the dataframe.
        :raises ValueError: If any of the specified columns do not exist in the dataframe or if column_names is not a string or a list of strings.
        """
        if isinstance(column_names, str):
            if not column_names in dataframe.columns:
                raise ValueError(f"Column '{column_names}' does not exist in the DataFrame.")
        
        elif isinstance(column_names, list):
            missing_columns = [col for col in column_names if col not in dataframe.columns]
            if missing_columns:
                raise ValueError(f"Columns {missing_columns} do not exist in the DataFrame.")
                
        else:
            raise ValueError("column_names should be a string or a list of strings")
        
        return True

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
        
        if not self._series:
            self._series = []
            self._drilldown = {"series":["test"]}

        self._series.append(series)

    def add_series_from_dataframe(self, 
                                  dataframe: pd.DataFrame, 
                                  column_names: Union[str, List[str]], 
                                  series_name: str, 
                                  drilldown_levels: List[dict] = None,
                                  aggfunc:str="sum", 
                                  **kwargs):
        """
        Creates and adds a series from a pandas DataFrame to the chart.

        Args:hero
            dataframe (pd.DataFrame): The DataFrame containing the series data.
            column_names (Union[str, List[str]]): Single or multiple column names.
            series_name (str): The name of the series.
            drilldown_levels (List[dict], optional): Drilldown options for the series.
        """
        self.__check_columns_exist(column_names=column_names, dataframe=dataframe)

        if drilldown_levels:
            # self.add_series_from_dataframe_with_drilldown(df=dataframe, drilldown_levels=drilldown_levels, aggfunc=aggfunc, **kwargs)
            data = self.__add_series_with_drilldown(column_names=column_names,df=dataframe, drilldown_levels=drilldown_levels, aggfunc=aggfunc, **kwargs)
            # second setp for drilldown  
        elif len(column_names) > 1:
            data = dataframe[column_names].values.tolist()
        elif len(column_names) == 1:
            data = dataframe[column_names[0]].tolist()
        else:
            raise ValueError("Should review your input.")
        
        series_instance = Series(name=series_name, data=data, **kwargs)
        self.add_series(series_instance)


        # if drilldown_levels:
        #     # TODO: if drilldowns, should find a robust method to handle the first level, 
        #     # what the logic take column_names from the function to define the first level or take the first 
        #     # key of the drill down level ?  
        #     self.__add_series_with_drilldown(dataframe, drilldown_levels, aggfunc, **kwargs)
        # else:
        #     if len(column_names) > 1:
        #         data = dataframe[column_names].values.tolist()
        #     else:
        #         data = dataframe[column_names[0]].tolist()

        #     series_instance = Series(name=series_name, data=data, **kwargs)
        #     self.add_series(series_instance)
        
    def __add_series_with_drilldown(
            self,
            column_names: Union[str, List[str]], 
            drilldown_levels: List[dict] = None, 
            df:pd.DataFrame=None, 
            aggfunc:str="sum",
            **kwargs
        ):
        """
        Adds a series with a drilldown option using the first drilldown level as a template.
        """
        data = df.pivot_table(
            index=column_names,
            values="value",
            fill_value=0,
            aggfunc=aggfunc
        ).reset_index()

        series_with_drilldown = [
            {
                'name': row[column_names], 
                'y': row['value'], 
                'drilldown': row[column_names]
            } for index, row in data.iterrows()
        ]

        drilldown_ids = [point['drilldown'] for point in series_with_drilldown]
        
        drilldown_manager = DrilldownManager(
            drilldown_levels=drilldown_levels,
            ids=drilldown_ids,
            dataframe=df
        )

        drilldown_manager.add_drilldown_test(**kwargs)

        return series_with_drilldown


    
    def add_series_from_dataframe_with_drilldown(self, drilldown_levels:dict, df:pd.DataFrame, aggfunc:str="sum",**kwargs):
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

    