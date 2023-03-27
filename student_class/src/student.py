class Student:
    def __init__(self, input_student_name, input_student_cohort):
        self.name = input_student_name
        self.cohort = input_student_cohort
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, input):
        return "I love " + input
