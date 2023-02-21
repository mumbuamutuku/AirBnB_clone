#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class
     Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
        """

    state_id = ""
    name = ""
