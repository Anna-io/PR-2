import json
import xml.etree.ElementTree as ET

with open('1.json', 'r') as f:
    data = json.load(f)

students = data['students']

print('{:<10} {:<10} {:<10} {:<20}'.format('First Name', 'Last Name', 'Group', 'Grades'))

for student in students:
    first_name = student['first_name']
    last_name = student['last_name']
    group = student['group']
    grades = student['grades']
    grades_str = ', '.join(str(grade) for grade in grades)
    print('{:<10} {:<10} {:<10} {:<20}'.format(first_name, last_name, group, grades_str))

tree = ET.parse('1.xml')
root = tree.getroot()

students = root.findall('student')

print('{:<10} {:<10} {:<10} {:<20}'.format('First Name', 'Last Name', 'Group', 'Grades'))

for student in students:
    first_name = student.find('first_name').text
    last_name = student.find('last_name').text
    group = student.find('group').text
    grades = student.findall('grades/grade')
    grades_str = ', '.join(grade.text for grade in grades)
    print('{:<10} {:<10} {:<10} {:<20}'.format(first_name, last_name, group, grades_str))