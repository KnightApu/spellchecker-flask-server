import json
class JsonBuilder():
    def __init__(self, object):
        self.object =  object
    def return_json(self):
        return json.dumps(self.object)