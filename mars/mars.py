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
            raise Error('could not create the file')

    def receive():
        curdir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(curdir, '..'+self.doc)):
            with open(self.doc,'r') as f:
                my_dict = json.loads(f)
            return my_dict
        else:
            raise Error('File does not exist')

   

