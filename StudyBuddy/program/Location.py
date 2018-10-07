'''
Created on Oct 6, 2018

@author: lfeid
'''
from program import Student
class Location():

    location        = None
    students_in     = []
    
    buildings = ["talley_union", "sas_parkshops", "hunt_lib", "hill_lib", "eb1", "eb2_1", "eb2_2", "eb3", "textiles", "biomed"]
    
    def __init__(self, loc_index):
        self.location = self.buildings.__getitem__(loc_index)
        
    def addStudent(self, student):
        self.students_in.append(student)