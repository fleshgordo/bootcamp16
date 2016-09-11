import csv

def csv2blob(filename):

    with open(filename,'rb') as f:
        z = f.read()

    # Split into two parts: stations (APs) and clients

    parts = z.split('\r\n\r\n')

    stations = parts[0]

    clients = parts[1]

    import sys
    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO

    stations_str = StringIO(stations)
    clients_str  = StringIO(clients)

    r = csv.reader(stations_str)
    i = list(r)
    z = [k for k in i if k <> []]

    stations_list = z

    r = csv.reader(clients_str)
    i = list(r)
    z = [k for k in i if k <> []]

    clients_list = z

    return stations_list, clients_list

stations_list, clients = csv2blob('vila_madalena-01.csv')
print stations_list
print clients
