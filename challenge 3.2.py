#implement a function called sort_students that takes a list of student objects as input and sorts thelist based on their CGPA (cumulative grade point average) in desendng order . each student objecthas the following attributes : name (string), roll_number (string) and cgpa (float). test the function with different input lists of students.


class student :

  def  __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in desending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


#example usage:
students = [
    student("shafi","5122129026", 9.9),
    student("Maha","5122129019",8.7),
    student("Pradeep","5122129022", 8.5),
    student("Siva","5122129027",7.5),
]

sorted_students = sort_students(students)

#print the sorted list of students 
for student in sorted_students:
  print("name: {}, roll number: {}, CGPA{}".format(student.name,
                                                     student.roll_number,
                                                    
                                                  student.cgpa))
