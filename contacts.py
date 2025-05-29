
contacts = {
    'number': 4,
    'students':
         [
             {'name':'Sarah Holderness', 'email':'sarah@example.com'},
             {'name':'Harry potter', 'email': 'harry@example.com'},
             {'name':'Hermione Granger', 'email':'harmione@example.com'},
             {'name':'Ron Weasley', 'email':'ron@example.com'}
         ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])