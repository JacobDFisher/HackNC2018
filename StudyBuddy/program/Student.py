'''
Created on Oct 6, 2018

@author: lfeid
'''
from program.Profile import Profile

class Student:
    
    def __init__(self, unityId, password):
        self.unity_id = unityId
        self.password = password
        self.profile = Profile()
        self.course_id = None
        self.study_time = None