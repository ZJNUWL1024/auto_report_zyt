from urllib import parse


def parse_code(location):
    data = {
        'address': location
    }
    location = parse.urlencode(data)
    return location
