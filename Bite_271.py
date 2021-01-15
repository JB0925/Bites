import inspect
import csv, string, random, re


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    classes = []

    for name, info in inspect.getmembers(mod, inspect.isclass):
        if name[0].isupper():
            classes.append(name)
        print(info)
    
    return classes




print(get_classes(re))