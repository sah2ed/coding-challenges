import sys 
import json

from os import listdir
from os.path import isfile, join, basename, splitext


def user_purchases(file, type=None):
    """
    Returns all of a user's purchases from the JSON file specified in the file parameter.
    """
    # Python sets guarantees that multiple occurences are treated as a single occurrence for any tuple.
    purchases = set()

    with open(file) as json_file:
        for line in json_file:
            if line.find("type") != -1:
                line = line.strip()
                line = line[:-1] if line.find("},") != -1 else line

                json_data = json.loads(line)
                if type == None:
                    purchases.add((json_data["type"], json_data["amount"]))
                else:
                    if type == json_data["type"]:
                        purchases.add((json_data["type"], json_data["amount"]))

    return purchases


def get_purchases(path, type=None):
    """
    Returns all users' purchases from the JSON folder specified in the path parameter.
    """
    purchases = list() 

    json_files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]    
    for file in json_files:
        user = splitext(basename(file))[0]        
        purchases.append(user_purchases(file, type))

    debug("get_purchases()", purchases)
    return purchases


def aggregate(purchases):
    """
    Counts how many times an individual tuple occurs. 
    The results should be a 3-ple (first, second, count), 
    where 'count' represents how many distinct users reported the particular tuple.

    >>> a = ('likes', 'green') 
    >>> b = ('likes', 'spinach')
    >>> c = ('likes', 'ice-cream')
    >>> aggregate([a, b, c])
    [('likes', 'green', 1),  ('likes', 'spinach', 1), ('likes', 'ice-cream', 1)]
    >>> 
    >>> 
    >>> a = ('likes', 'green') 
    >>> b = ('likes', 'green')
    >>> c = ('likes', 'green')
    >>> aggregate([a, b, c])
    [('likes', 'green', 3)]
    """

    _aggregates = {}
    for user_purchases in purchases:           
        for (type, amount) in user_purchases:
            if type not in _aggregates:
                _aggregates[type] = dict()                
            count = _aggregates[type].get(amount, 0)
            _aggregates[type][amount] = count + 1

    
    aggregates = [(type, amount, count) for type in (type for type in _aggregates) for amount, count in ((amount, count) for (amount, count) in _aggregates[type].items())]
    debug("aggregate()", aggregates)    

    return aggregates


def anonymize(purchases):
    """
    Removes all 3-ples with a count of 5 or less.
    """
    return [(type, amount, count) for (type, amount, count) in purchases if count > 5]


def median(data, filter):
    amounts = sorted(sum([[a] * c for t, a, c in data if t == filter], []))
    _len = len(amounts)
    index = (_len - 1) // 2

    if _len % 2:
        return amounts[index]
    else:
        return (amounts[index] + amounts[index + 1]) / 2.0


def debug(function, purchases):
    """
    Pretty prints the tuples to help make sense of data while being transformed.
    """
    if not DEBUG:
        return

    print(function)
    for x in purchases:        
        print (x)         
    print("\n")


DEBUG = False

def main():
    path = './data' # Relative path from the current directory to the JSON data files. Required.
    filter = 'airline' # The type of purchases to filter on in the JSON. Optional.
    
    data = anonymize(aggregate(get_purchases(path, filter)))
    #data = anonymize(aggregate(get_purchases(path)))    

    print(data)    
    print("min: %d" % min(a for t, a, c in data if t == filter))
    print("max: %d" % max(a for t, a, c in data if t == filter))
    print("mean: %d" % (sum(a * c for t, a, c in data if t == filter) / sum(c for t, a, c in data if t == filter)))
    print("median: %d" % median(data, filter))


if __name__ == "__main__":
    main()