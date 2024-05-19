from abc import ABC, abstractmethod
import warnings
import json

class Common(ABC):
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
        if getattr(self, '_list_only', False):
            self.values = kwargs.get('values', [])
            if not isinstance(self.values, list):
                raise ValueError("The 'values' attribute must be a list.")
        else:
            for attr in getattr(self, '_valid_attributes', []):
                setattr(self, attr, None)
            for k, v in kwargs.items():
                if k in getattr(self, '_valid_attributes', []):
                    setattr(self, k, v)
                else:
                    warnings.warn(f"Ignoring invalid attribute '{k}' for {self.__class__.__name__}.", UserWarning)

    # def __init__(self, **kwargs):
    #     """
    #     Initializes chart component attributes based on provided keyword arguments.
    #     Only attributes that are listed in the _valid_attributes list are set.
    #     Attributes not in the list are ignored to prevent arbitrary attribute assignment.
    #     """
    #     # Initialize all attributes to None or their default values
    #     self.__dict__.update({attr: None for attr in self._valid_attributes})

    #     # Update the attributes with any values provided upon instantiation
    #     self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

    @property
    @abstractmethod
    def _valid_attributes(self):
        """
        Subclasses should override this property to return a list of valid attribute names
        specific to the component type.
        """
        raise NotImplementedError("Subclasses must define '_valid_attributes'.")

    def to_dict(self):
        if getattr(self, '_list_only', False):
            return self.values
        else:
            return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}

    # def to_dict(self):
    #     """
    #     Converts the chart component into a dictionary of its properties,
    #     only including those that are not None.
    #     """
    #     return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}
    
    def to_json(self):
        """
        Serializes the chart component's attributes to a JSON string.

        Returns:
            str: JSON string representing the chart component's attributes.
        """
        return json.dumps(self.to_dict())
    
    def to_list(self):
        """
        Converts the chart component's attributes into a list of tuples,
        each tuple containing the attribute name and its value.
        """
        return [(attr, getattr(self, attr)) for attr in self._valid_attributes if getattr(self, attr) is not None]
    
    def values(self):
        """
        Returns a list of the values of the chart component's attributes,
        only including those that are not None.
        """
        return [getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None]
    
    def items(self):
        """
        Returns a list of tuples, each tuple containing an attribute name
        and its corresponding value, similar to the dictionary's items() method.
        """
        return list(self.to_dict().items())

    def keys(self):
        """
        Returns a list of attribute names that are currently set and not None,
        similar to the dictionary's keys() method.
        """
        return [attr for attr in self._valid_attributes if getattr(self, attr) is not None]
    
    @classmethod
    def from_dict(cls, data: dict):
        if getattr(cls, '_list_only', False):
            if 'values' in data:
                if isinstance(data['values'], list):
                    return cls(values=data['values'])
                else:
                    raise ValueError("The 'values' attribute must be a list.")
            else:
                return cls()
        else:
            valid_data = {k: v for k, v in data.items() if k in cls._valid_attributes}
            invalid_keys = set(data.keys()) - set(valid_data.keys())
            if invalid_keys:
                warnings.warn(f"Ignoring invalid attributes {invalid_keys} for {cls.__name__}.", UserWarning)
            return cls(**valid_data)

    # @classmethod
    # def from_dict(cls, data):
    #     """
    #     Creates an instance of a chart component from a dictionary, applying only valid attributes.

    #     Parameters:
    #         data (dict): A dictionary where keys are attribute names and values are the settings for those attributes.
    #     """
    #     valid_data = {}
    #     for key, value in data.items():
    #         if key in cls._valid_attributes:
    #             valid_data[key] = value
    #         else:
    #             warnings.warn(f"Invalid attribute '{key}' provided to {cls.__name__}. It will be ignored.", UserWarning)

    #     return cls(**valid_data)
    
    @classmethod
    def from_list(cls, data):
        """
        Creates a list of instances of a chart component from a list of dictionaries.
        
        Parameters:
            data_list (list): A list of dictionaries where each dictionary contains attributes for an instance.
        """
        return [cls.from_dict(data) for data in data if isinstance(data, dict)]

