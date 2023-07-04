#!/usr/bin/python3
"""Module containing the LockedClass definition."""


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """

    def __setattr__(self, name, value):
        """
        Set attribute value if the attribute name is 'first_name'.
        Raise an AttributeError if the attribute name is not 'first_name'.
        """
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
