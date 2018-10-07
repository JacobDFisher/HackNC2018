'''
Created on Oct 6, 2018

@author: lfeid
'''
class Session:
    
    def __init__(self, name, id, section, time_in, time_out):
        self.name = name
        self.id = id
        self.section = section
        self.time_in = time_in
        self.time_out = time_out