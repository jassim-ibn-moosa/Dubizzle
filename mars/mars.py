import json
import os

class Mars(object):
    
    def __init__(self, doc):
        self.doc = doc
    
    def send(self, my_dict):
        
        with open (self.doc,'w') as f:
            json.dump(my_dict, f)
            
        curdir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(curdir, self.doc)) and os.stat(self.doc).st_size > 1 :
                return 1
        else:
            raise Error('could not create the file')

    def receive(self):
        curdir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(curdir, self.doc)):
            with open(self.doc,'r') as f:
                my_dict = json.load(f)
            return my_dict
        else:
            raise Error('File does not exist')


class Error(Exception):
    
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)

   

