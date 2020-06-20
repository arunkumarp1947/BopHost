import json

def getprefix(server):
    try:
        with open('prefixes.json') as f:
            prefixes = json.load(f)
            return prefixes[str(server.id)]
    except:
        theprefix = "-"
        return theprefix