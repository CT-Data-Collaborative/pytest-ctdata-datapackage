from collections import namedtuple

SPOT_CHECK_CONVERTERS = {
    "float": float,
    "int": int
}

Spotcheck = namedtuple("Spotcheck", ['spec', 'expected', 'actual'])


def helper_filter(item, conditions):
    for k,v in conditions:
        if item[k] != v:
            return False
    return True


def _lookerupper(dataset, filter):
    """Lookup function for spotchecks"""
    filters = [(k, v) for k, v in filter.items()]
    matches = [x for x in dataset if helper_filter(x, filters)]
    try:
        match = matches[0]
    except IndexError:
        return None
    try:
        result = match['Value']
    except KeyError:
        return None
    return result
