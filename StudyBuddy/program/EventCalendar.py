'''
Created on Oct 7, 2018

@author: lfeid
'''
class EventCalendar:
    
    # Creates the calendar
    def __init__(self):
        self.all_events = []
    
    def add_session(self, name, id, section, time_in, time_out):
        self.session_database.append(Session(name, id, section, time_in, time_out))
    
    # Clears expired events, runs every 30 min
    def is_expired(self):
        for x in self.all_events:
            if x.time_out < 
        
    # Consolidates Events by Location
    
    # Consolidates Events by Subject 
    
    # Searches by location
    
    # Searches by Subject
    
    # Searches by Section
    
    
        