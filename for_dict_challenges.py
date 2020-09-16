# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

from collections import Counter

print('\n=========== \n')

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

studentsList = []                               #Make empty list

for names in students:                          #add key from students[{}] to list studentsList
    studentsList.append(names['first_name'])
print(studentsList)                             #checking created list

nameCount = Counter(studentsList)               #using function Counter from collections                    
print(nameCount)                                #check

for name in nameCount:                          #from dict nameCount doing output like in the Task
  print(f'{name}: {nameCount[name]}')

print('\n=========== \n')
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

studentsList = []                                         #Make empty list

for names in students:                                    #add key from students[{}] to list studentsList
    studentsList.append(names['first_name'])

nameCount = Counter(studentsList)                         #using function Counter from collections 
nameCount = nameCount.most_common()[0]                    #using most common method from Counter                        
print(f'Самое частое имя среди учеников: {nameCount[0]}') #from nameCount doing output the first value

print('\n=========== \n')
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

student_list_1 = []
student_list_2 = []

for names in school_students[0]:
  student_list_1.append(names['first_name'])

nameCount_1 = Counter(student_list_1)                         
nameCount_1 = nameCount_1.most_common()[0]

for names in school_students[1]:
  student_list_2.append(names['first_name'])

nameCount_2 = Counter(student_list_2)                        
nameCount_2 = nameCount_2.most_common()[0]

print(f'Самое частое имя в классе 1: {nameCount_1[0]}')
print(f'Самое частое имя в классе 2: {nameCount_2[0]}')

print('\n=========== \n')
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

def student_list(shcool_class_students):
  student_list_class = []
  for class_name in shcool_class_students:
    student_list_class.append(class_name['first_name'])
  return(student_list_class)

student_list_1 = student_list(school[0]['students'])
student_list_2 = student_list(school[1]['students'])

def whats_male_in_student_list(student_list_num, count_class = 0, female_count = 0, male_count = 0):
  for male in is_male:
    try:
      if student_list_num[count_class] == male and is_male[male] == False:  
        print(f'{student_list_num[count_class]} - Женский')
        count_class += 1
        female_count += 1
        
      elif student_list_num[count_class] == male and is_male[male] == True:  
        print(f'{student_list_num[count_class]} - Мужской')
        count_class += 1
        male_count += 1
        
    except(IndexError):  
      continue
  return(male_count, female_count)

class_2a = whats_male_in_student_list(student_list_1)
class_3c = whats_male_in_student_list(student_list_2)

print(f"В классе {school[0]['class']} {class_2a[1]} девочки и {class_2a[0]} мальчика")
print(f"В классе {school[1]['class']} {class_3c[1]} девочки и {class_3c[0]} мальчика")

print('\n=========== \n')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

def student_list(shcool_class_students):
  student_list_class = []
  for class_name in shcool_class_students:
    student_list_class.append(class_name['first_name'])
  return(student_list_class)

student_list_1 = student_list(school[0]['students'])
student_list_2 = student_list(school[1]['students'])

def whats_male_in_student_list(student_list_num, count_class = 0, female_count = 0, male_count = 0):
  for male in is_male:
    try:
      if student_list_num[count_class] == male and is_male[male] == False:  
        count_class += 1
        female_count += 1
        
      elif student_list_num[count_class] == male and is_male[male] == True:  
        count_class += 1
        male_count += 1
        
    except(IndexError):  
      continue
  return(male_count, female_count)

class_2a = whats_male_in_student_list(student_list_1)
class_3c = whats_male_in_student_list(student_list_2)

if class_2a[0] > class_3c[0]:
  print('Больше всего мальчиков в классе 2a')
elif class_2a[0] < class_3c[0]:
  print('Больше всего мальчиков в классе 3c')
else:
  print('Количество мальчиков в классах одинаковое')

if class_2a[1] > class_3c[1]:
  print('Больше всего девочек в классе 2a')
elif class_2a[1] < class_3c[1]:
  print('Больше всего девочек в классе 3c')
else:
  print('Количество девочек в классах одинаковое')

print('\n=========== \n')

# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
