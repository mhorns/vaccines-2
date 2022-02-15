def readit(filename):
    """
    Read and parse CSV -- read entire file all at once.
    """
    if filename.endswith('.gz'):
        with gzip.open(filename, 'rt') as f:
            list = f.read().rstrip().split("\n")
    else:
        with open(filename, 'rt') as file:
            list = file.read().rstrip().split("\n") 

    keys = list.pop(0).split(",")
    data = []
    for line in list:
        values = line.split(",")
        datum = {keys[i]: value for i, value in enumerate(values)}
        data.append(datum)
    print("it worked")
    return data