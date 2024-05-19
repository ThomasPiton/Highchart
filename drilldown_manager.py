from common import Common
from components import *
from typing import List,Dict,Union
import pandas as pd

class DrilldownManager:

    def __init__(self,drilldown_levels, dataframe, ids) -> None:
        
        self.dataframe = dataframe
        self.drilldown_levels = drilldown_levels
        self.ids = ids
  
        self.available_chart_types = [
            'line', 'bar', 'column', 'area', 'areaspline', 'spline', 
            'pie', 'scatter', 'bubble', 'heatmap', 'boxplot', 'waterfall'
        ]

    def __validate_chart_types(self):
        # Ensure all specified chart types are valid
        for level in self.drilldown_levels:
            if level['type'] not in self.available_chart_types:
                raise ValueError(f"Invalid chart type: {level['type']}. Choose from {self.available_types}")

    def __check_drilldown_levels(self):
        """
        Checks if drilldown levels list is present, is a list, and contains at least two levels.

        Raises:
            ValueError: If the drilldown levels do not meet the required criteria.
        """
        if not isinstance(self.drilldown_levels, list):
            raise ValueError("Drilldown levels should be a list.")
        
        if len(self.drilldown_levels) < 2:
            raise ValueError("Drilldown levels must contain at least two levels.")
        
        # Check if each level has the necessary 'name' and 'type' keys
        for level in self.drilldown_levels:
            if not isinstance(level, dict) or 'name' not in level or 'type' not in level:
                raise ValueError("Each drilldown level must be a dictionary with 'name' and 'type' keys.") 

    def set_drilldown(self, drilldown:Drilldown):
        """
        Adds a new series to the chart.

        Args:
            series (Series): A Series object to add to the chart.
        
        Raises:
            ValueError: If the provided object is not an instance of Series.
        """
        if not isinstance(drilldown, Drilldown):
            raise ValueError("Must provide a Series object.")

        self._drilldown = Drilldown

    def add_drilldown_test(self):

        self.__validate_chart_types()
        self.__check_drilldown_levels()

        data = []
        for i in range(len(self.drilldown_levels)):
            current_level = self.drilldown_levels[i]['name']
            
            # Check if the next level is within the bounds of the list
            if i + 1 < len(self.drilldown_levels):
                next_level = self.drilldown_levels[i + 1]['name']
            else:
                next_level = None

            grouped = self.dataframe.groupby([level['name'] for level in self.drilldown_levels[:i + 1]])

            for name, group in grouped:
                drilldown_id = '_'.join(map(str, name)) if isinstance(name, tuple) else str(name)

                # Only aggregate and prepare for drilldown if there is a next level
                if next_level:
                    next_data = group.groupby(next_level).agg({'value': 'sum'}).reset_index()
                    next_data['drilldown'] = next_data[next_level].apply(lambda x: f"{drilldown_id}_{x}")

                    # Prepare the series data with drilldown links
                    drilldown_series = {
                        'name': drilldown_id.split('_')[-1],
                        'id': drilldown_id,
                        'type': self.drilldown_levels[i]['type'],
                        'data': [{'name': row[next_level], 'y': row['value'], 'drilldown': row['drilldown']} for index, row in next_data.iterrows()]
                    }
                else:
                    # If there is no next level, just prepare the series data without drilldown links
                    drilldown_series = {
                        'name': drilldown_id.split('_')[-1],
                        'id': drilldown_id,
                        'type': self.drilldown_levels[i]['type'],
                        'data': [{'name': row[current_level], 'y': row['value']} for index, row in group.iterrows()]
                    }

                data.append(drilldown_series)

        self._drilldown = Drilldown(series=data,**kwargs)
        
        # drilldown_instance = Drilldown(series=data)
        # self.set_drilldown(drilldown_instance)

    def add_drilldown(self):

        self.__validate_chart_types()
        self.__check_drilldown_levels()

        for i in range(len(self.drilldown_levels)-1):
            current_level = self.drilldown_levels[i]['name']
            next_level = self.drilldown_levels[i+1]['name']

            grouped = self.dataframe.groupby([level['name'] for level in self.drilldown_levels[:i+1]])
            for name, group in grouped:
                drilldown_id = '_'.join(map(str, name)) if isinstance(name, tuple) else str(name)

                # Aggregate data by 'next_level', summing 'value' and preparing for drilldown link
                next_data = group.groupby(next_level).agg({'value': 'sum'}).reset_index()
                next_data['drilldown'] = next_data[next_level].apply(lambda x: f"{drilldown_id}_{x}")

                # Prepare the series data with drilldown links
                drilldown_series = {
                    'name': drilldown_id.split('_')[-1],
                    'id': drilldown_id,
                    'type': self.drilldown_levels[i]['type'],
                    'data': [{'name': row[next_level], 'y': row['value'], 'drilldown': row['drilldown']} for index, row in next_data.iterrows()]
                }

                self.drilldown_data.append(drilldown_series)
