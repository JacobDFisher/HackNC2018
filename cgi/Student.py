'''
Created on Oct 6, 2018

@author: lfeid
'''
class Student:
    
    def __init__(self, unityId, password, name, prob, foc, soc, noise):
        self.unity_id = unityId
        self.password = password
        self.peer_history = []
        self.avg_problemSolver = prob
        self.avg_noise = noise
        self.avg_focus = foc
        self.avg_social = soc
        self.name = name
        self.class_log = []
        #self.log_classes()
    
    def log_classes(self):
        i = input("How many classes: ")
        for x in (0, i):
            x.append(input("Enter class in form: ABC-123 001: "))
    
    def update_noise(self, noise):
        self.avg_noise = (self.avg_noise + noise) / len(self.peer_history)
        
    def update_communication(self, communication):
        self.avg_communication = (self.avg_communication + communication) / len(self.peer_history)
        
    def update_listener(self, listener):
        self.avg_listener = (self.avg_listener + listener) / len(self.peer_history)
        
    def update(self, noise, communication, listener):
        self.update_noise(noise)
        self.update_communication(communication)
        self.update_listener(listener)

    def compare(self, stud):
        return 12.5*(8-abs(self.avg_problemSolver-stud.avg_problemSolver)-abs(self.avg_noise-stud.avg_noise)-abs(self.avg_focus-stud.avg_focus)-abs(self.avg_social-stud.avg_social))
        
