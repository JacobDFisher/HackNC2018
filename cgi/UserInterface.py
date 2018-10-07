'''
Created on Oct 6, 2018

@author: lfeid
'''
import Student

class UserInterface:
    
    # Initializes the user interface, containing a student database, a location database, and a 
    # running database of study sessions.
    def main(self):
        self.student_database = []
        self.create_locations()
        
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
    

    
    
    
    
    
    
    
    
