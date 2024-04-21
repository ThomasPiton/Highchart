from abc import ABC, abstractmethod
import json

class ChartComponent(ABC):
    """
    Abstract base class for chart components like Title, Subtitle, and Series.
    Provides a standardized approach for initializing and converting component
    attributes into a dictionary representation suitable for chart configurations.
    """

    def __init__(self, **kwargs):
        """
        Initializes chart component attributes based on provided keyword arguments.
        Only attributes that are listed in the _valid_attributes list are set.
        Attributes not in the list are ignored to prevent arbitrary attribute assignment.
        """
        # Initialize all attributes to None or their default values
        self.__dict__.update({attr: None for attr in self._valid_attributes})
        # Update the attributes with any values provided upon instantiation
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

    @property
    @abstractmethod
    def _valid_attributes(self):
        """
        Subclasses should override this property to return a list of valid attribute names
        specific to the component type.
        """
        raise NotImplementedError("Subclasses must define '_valid_attributes'.")

    def to_dict(self):
        """
        Converts the chart component into a dictionary of its properties,
        only including those that are not None.
        """
        return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}
    
    def to_json(self):
        """
        Serializes the chart component's attributes to a JSON string.

        Returns:
            str: JSON string representing the chart component's attributes.
        """
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_dict(cls, data):
        """
        Creates an instance of a chart component from a dictionary, applying only valid attributes.
        """
        valid_data = {k: v for k, v in data.items() if k in cls._valid_attributes}
        return cls(**valid_data)

