from . import config
from . import constructor
from . import package
from . import route


__all__ = ["new", "constructor", "package", "route", "config"]


def new(*args):
    return constructor.Overlord(*args)
