from configparser import ConfigParser


def config(filename='.env'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(filename):
        params = parser.items(filename)
        for param in params:
            db[param[0]] = param[1]
    return db
