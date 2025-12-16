# This is going to be a console programm Habit Tracker
# #while True:


while True:
    class habit():
        def __init__(self, title, description, frequnecy, lcd):
            self.title = title
            self.description = description
            self.frequency = frequnecy
            self.lcd = lcd

    class task():
        def __init__(self, name, delineation, dueDate, priority, status):
            self.name = name
            self.delineation = delineation
            self.dueDate = dueDate
            self.priority = priority
            self.status = status
    

    try:
        habit = str(input('What is your new habit:  '))
        print(habit)
    except:
        print('No please enter a habit')
    if habit == 'Quit':
        break
    else:
       task =  print(input('Do you want to add a Task ? '))
    if task == 'yes':
        print(input('What is your new Task'))
    else:
        task == 'Quit'
        break  

