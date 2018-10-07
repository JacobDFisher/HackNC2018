'''
Created on Oct 7, 2018

@author: lfeid
'''
class EventCalendar:
    
    # Creates the calendar
    def __init__(self):
        self.all_events = []
    
    def add_session(self, student, course, location):
        self.all_events.append({'student' : student, 'location' : location, 'subject' : course})
                    
    # Searches by Subject
    def search(self, fields = {}):
        results = []
        for x in self.all_events:
            for y in fields:
                if type(fields[y])==str:
                    if x[y] == fields[y]:
                        results.append(x[y])
                elif hasattr(fields[y], '__iter__'):
                    if x[y] in fields[y]:
                        results.append(x[y])
        return results
    