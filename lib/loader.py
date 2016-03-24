import os
import urllib.request
import json

class Loader:
    def __init__(self, path):
        if os.path.exists(path):
            with open(os.path.abspath(path)) as f:
                self.raw_schema = json.loads(f.read())
        else:
            with urllib.request.urlopen(path) as f:
                self.raw_schema = json.loads(f.read().decode('utf-8'))

        self.schema = self.select()

    def select(self):
        return self.raw_schema[1]['tables']


