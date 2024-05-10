
class DrilldownManager:

    def __init__(self) -> None:

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

    def add_drilldown_test(self, dataframe, ids):
        self.__validate_chart_types()
        self.__check_drilldown_levels()
        pass

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
