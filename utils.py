import json


def get(*args: str):
    """
    Takes args as keys for access to parameters
    """
    with open("parameters.json", "r") as file:
        data = json.loads(file.read())

    for key in args:
        data = data[key]

    return data


def r_input(possible_inputs: range):
    """
    Calls input until valid
    """
    while True:
        ans = input()
        if ans in map(str, possible_inputs):
            return int(ans)
