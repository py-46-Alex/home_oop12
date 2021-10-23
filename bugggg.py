class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname_lect):
    self.name = name
    self.surname = surname_lect
    self.continued_courses_lect = []
    self.courses_in_progress_lect = []
    self.grades = {}
    self.course = []
    self.midle_grade = []
    self.final_mid_grade = 0
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Лекторы сравинваются с лекторами, это не лектор')
      return
    return self.final_mid_grade < other.final_mid_grade

  def __str__(self):
    res = f' \nЛектор\nИмя: {self.name} \nФамилия:  {self.surname}\nСредняя оценка за лекции: {self.final_mid_grade}\n  '
    return res
  
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.all_grads = []
        self.avg_grade_final = 0
    def __lt__(self, other):
      if not isinstance(other, Student):
        print('несравнимые студенто-нестуденты, а нужно только студентов сравнивать')
        return
      return self.avg_grade_final > other.avg_grade_final  
    def rate_hww(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress_lect:
        if course in lecturer.grades:
          lecturer.grades[course] += [grade]
          lecturer.midle_grade.append(grade)
        else:
          lecturer.grades[course] = [grade]
          lecturer.midle_grade.append(grade)
      else:
            return 'Ошибка'
      lecturer.final_mid_grade = sum(lecturer.midle_grade) / len(lecturer.midle_grade)  
    def __str__(self):
      res = f'\nСтудент\nИмя: {self.name} \nФамилия:  {self.surname}\nCредняя оценка за домашку: {self.avg_grade_final} \nKурсы в процевссе изучения: {self.courses_in_progress} \n3авершенные курсы: {self.finished_courses} \n'
      return res    

class Reviewer(Mentor):
      def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.all_grads.append(grade)
            else:
                student.grades[course] = [grade]
                student.all_grads.append(grade)
        else:
            return 'Ошибка'
        student.avg_grade_final = round(sum(student.all_grads) / len(student.all_grads), 1)
      def __str__(self):
        res = f'\nПроверяющий\nИмя: {self.name} \nФамилия:  {self.surname}\n  '
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 2)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)
 
print(best_student)

best_lecturer = Lecturer('Victor', 'Tcepesh')
best_lecturer.courses_in_progress_lect += ['Python']
some_student = Student('Ruo2y', 'Em2an', 'y2our_gender')
some_student.courses_attached += ['Python']

some_student.rate_hww(best_lecturer, 'Python', 2)
some_student.rate_hww(best_lecturer, 'Python', 2)
some_student.rate_hww(best_lecturer, 'Python', 5)

print(cool_mentor)
print(best_lecturer)

some_lecturer = Lecturer('Vova', 'Putin')
some_lecturer.courses_in_progress_lect += ['Python', 'Java']
some_lecturer.final_mid_grade = 6

strange_lecturer = Lecturer('Doctor', 'Strange')
strange_lecturer.courses_in_progress_lect += ['Python', 'Java', 'Paranormal ativitis']
strange_lecturer.final_mid_grade = 3

print('Сравнение лекторов по средней оценке')
print(strange_lecturer < some_lecturer)

some_student = Student('Ruo2y', 'Em2an', 'y2our_gender')
some_student.courses_attached += ['Python']

# print('курсы которые ведет лектор' + str(strange_lecturer.courses_in_progress_lect))

some_student3 = Student('Leroy', 'McDilan', 'Male')
some_student3.courses_attached += ['C++']
some_student3.avg_grade_final = 5

some_student4 = Student('Lebron', 'Djames', 'Male')
some_student4.courses_attached += ['Java']
some_student4.avg_grade_final = 7

some_student5 = Student('Leonora', 'Ruzvelt', 'Female')
some_student5.courses_attached += ['C++']
some_student5.avg_grade_final = 9

print('Сравнение средних балов студентов')
print(some_student5 > some_student4)

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);

student_list = [some_student, some_student4, some_student4, some_student5, best_student]

def avg_md_stud(any_student_list, course_name):
  total_avg = []
  for i in any_student_list:
    if course_name in i.grades.keys():
      total_avg.extend(i.grades[course_name])
      lent_of_grad = len(total_avg)
      summ_of_rgsd = sum(total_avg)
      fin_mid_grade_of_course = summ_of_rgsd / lent_of_grad
  print(f'Cредняя оценка домашних заданий учеников на курсе {course_name} примерно {fin_mid_grade_of_course}')

avg_md_stud(student_list, 'Python')