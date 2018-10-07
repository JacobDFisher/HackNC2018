'''
Created on Oct 6, 2018

@author: lfeid
'''
from program import Student
from program import Location
from program import Session

class UserInterface:
    
    # Initializes the user interface, containing a student database, a location database, and a 
    # running database of study sessions.
    def main(self):
        self.student_database = []
        self.session_database = []
        # Initializes a database of locations corresponding to available locations.
        self.location_database = []
        for i in (0,10):
            self.location_database.append(Location(i))
    
    # TODO
    def update_references_for(self, location, session):
        pass
        
    def create_locations(self):
        self.buildings = ["talley_union", "sas_parkshops", "hunt_lib", "hill_lib", "eb1", "eb2_1", "eb2_2", "eb3", "textiles", "biomed"]
        for i in (0,10):
            self.location_database.append(self.buildings[i])
    
    def return_locations(self):
        for x in self.location_database:
            print(x.__str__())
    
    # This adds a student to a database, creating a new student object with a unity ID and password,
    # we should probably store the password as a hash eventually.
    def add_user(self, unity_id, password):
        self.student_database.append(Student(unity_id, password))
        
    
        
    # Here we assume that the location is an input passed by the user interface; a drop-down menu
    # selection would theoretically pass single value to determine a selection.
    def search_by_location(self, location):
        
        
    def search_by_subject(self, course_id):
        pass
    
    
    
    
    
    
    
    
    
    