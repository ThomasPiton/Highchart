from common import Common


class Colors:
    """
    A simple class to manage a list of colors.
    """
    def __init__(self):
        pass

    @classmethod
    def from_list(cls, data):
        return cls(data)

# class Colors(ChartComponent):

#     def __init__(self, colors=None):
#         """
#         Initialize the Colors instance with a list of colors.
#         Ensures that the input is always treated as a list, even if a single color string is provided.
        
#         Parameters:
#             colors (list | str | None): A list of color values, a single color string, or None.
#         """
#         self.set_colors(colors)

#     def set_colors(self, colors):
#         """
#         Set the colors for the instance, ensuring all inputs are treated as a list.
        
#         Parameters:
#             colors (list | str | None): The colors to set, which can be a list, a single color, or None.
#         """
#         if isinstance(colors, list):
#             self.colors = colors
#         elif colors is not None:
#             self.colors = [colors]
#         else:
#             self.colors = []

#     def get_colors(self):
#         """
#         Get the list of colors.
        
#         Returns:
#             list: The current list of colors.
#         """
#         return self.colors

#     def add_color(self, color):
#         """
#         Add a single color to the colors list.
        
#         Parameters:
#             color (str): The color to add to the list.
#         """
#         if not isinstance(color, str):
#             raise ValueError("Color must be a string")
#         self.colors.append(color)

#     def __str__(self):
#         """
#         Return a string representation of the colors list.
        
#         Returns:
#             str: A comma-separated string of colors.
#         """
#         return ', '.join(self.colors)

