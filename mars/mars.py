import json
import os

class Mars(object):
    
    def __init__(self, doc):
        self.doc = doc
    
    def send(my_dict):
        
        with open (self.doc,'w') as f:
            json.dumps(my_dict, f)
        
        curdir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(curdir, '..'+self.doc)):
            if os.stat(self.doc)st_size > 1:
                return 1
        else:
            raise FileEmptyError

    def receive():
        pass

