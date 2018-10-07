'''
Created on Oct 6, 2018

@author: lfeid
'''
class Profile:
    
    def __init__(self):
        self.peer_history = []
        # Start each 
        self.avg_noise = 3
        self.avg_communication = 3
        self.avg_listener = 3
    
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