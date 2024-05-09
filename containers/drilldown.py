# drilldown.py

from chart_component import ChartComponent

class Drilldown(ChartComponent):

    _valid_attributes = ["activeAxisLabelStyle","activeDataLabelStyle","allowPointDrilldown",
        "animation","drillUpButton","series"]
    
    _valid_chart = ['line', 'bar', 'column', 'area', 'areaspline', 'spline', 
        'pie', 'scatter', 'bubble', 'heatmap', 'boxplot', 'waterfall']
    
    def __init__(self, dataframe, drilldown_levels):
        super().__init__()
        self.dataframe = dataframe
        self.drilldown_levels = drilldown_levels  # List of dictionaries
        self.drilldown_data = []

    def validate_chart_types(self):
        # Ensure all specified chart types are valid
        for level in self.drilldown_levels:
            if level['type'] not in self._valid_chart:
                raise ValueError(f"Invalid chart type: {level['type']}. Choose from {self._valid_chart}")

    def generate_drilldowns(self):
        self.validate_chart_types()  # Validate chart types before generating drilldowns
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



# class Drilldown:

#     def __init__(self, dataframe, drilldown_levels):
#         self.dataframe = dataframe
#         self.drilldown_levels = drilldown_levels  # List of dictionaries
#         self.drilldown_data = []
#         self.available_types = ['line', 'bar', 'column', 'area', 'areaspline', 'spline', 
#                                 'pie', 'scatter', 'bubble', 'heatmap', 'boxplot', 'waterfall']

#     def validate_chart_types(self):
#         # Ensure all specified chart types are valid
#         for level in self.drilldown_levels:
#             if level['type'] not in self.available_types:
#                 raise ValueError(f"Invalid chart type: {level['type']}. Choose from {self.available_types}")

#     def generate_drilldowns(self):
#         self.validate_chart_types()  # Validate chart types before generating drilldowns
#         for i in range(len(self.drilldown_levels)-1):
#             current_level = self.drilldown_levels[i]['name']
#             next_level = self.drilldown_levels[i+1]['name']

#             grouped = self.dataframe.groupby([level['name'] for level in self.drilldown_levels[:i+1]])
#             for name, group in grouped:
#                 drilldown_id = '_'.join(map(str, name)) if isinstance(name, tuple) else str(name)

#                 # Aggregate data by 'next_level', summing 'value' and preparing for drilldown link
#                 next_data = group.groupby(next_level).agg({'value': 'sum'}).reset_index()
#                 next_data['drilldown'] = next_data[next_level].apply(lambda x: f"{drilldown_id}_{x}")

#                 # Prepare the series data with drilldown links
#                 drilldown_series = {
#                     'name': drilldown_id.split('_')[-1],
#                     'id': drilldown_id,
#                     'type': self.drilldown_levels[i]['type'],
#                     'data': [{'name': row[next_level], 'y': row['value'], 'drilldown': row['drilldown']} for index, row in next_data.iterrows()]
#                 }

#                 self.drilldown_data.append(drilldown_series)
    
#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Title object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the title.

#         Returns:
#             Title: A Title object configured according to the provided dictionary.
#         """        
#         return cls(
#             activeAxisLabelStyle=data.get('active_axis_label_style'),
#             activeDataLabelStyle=data.get('active_data_label_style'),
#             allowPointDrilldown=data.get('allow_point_drilldown'),
#             animation=data.get('animation'),
#             drillUpButton=data.get('drill_up_button'),
#             series=data.get('series')
#         )