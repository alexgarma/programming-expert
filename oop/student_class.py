class Student:
    all_students = []
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade # Siguen funcionando las restricciones del setter?
        Student.all_students.append(self)
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        if grade >= 0 and grade <= 100:
            self._grade = grade
        else:
            raise ValueError("New grade not in the accepted range of [0-100]")
    
    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)
    
    @classmethod
    def get_best_student(cls):
        
        if len(cls.all_students) == 0:
            return None
        
        best_student = None
        current_grade = 0
        
        for student in cls.all_students:
            if student.grade >= current_grade:
                current_grade = student.grade
                best_student = student
        
        return best_student
             
    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1
        
        sum_grades = 0
        
        for student in students:
            sum_grades += student.grade
        
        return sum_grades/len(students)