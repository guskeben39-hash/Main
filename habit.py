# This is going to be a console programm Habit Tracker

class habit_tracker:
    def __init__(self):
        self.habits = []
        self.tasks = []

    def add_habit(self, habit_name, habit_description, habit_frequency, habit_status):
        habit = {
            "name": habit_name,
            "description": habit_description,
            "frequency": habit_frequency,   
            "status": habit_status,
        }

        self.habits.append(habit)
        return habit


    def view_habits(self):
        return self.habits


    def add_task(self, task_name, task_description, task_prio, task_status):
        task = {
            "name": task_name,
            "description": task_description,
            "priority": task_prio,
            "status": task_status,
        }
        self.tasks.append(task)
        return task
    def view_tasks(self):
        return self.tasks
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task['name']} [{task['status']}]")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "Complete"
            return True
        return False   

    def list_habits(self):
        for i, habit in enumerate(self.habits):
            print(f"{i}: {habit['name']} [{habit['status']}]")

    def complete_habit(self, index):
        if 0 <= index < len(self.habits):
            self.habits[index]["status"] = "Complete"
            return True
        return False    

tracker = habit_tracker()

# 1. Start while loop
while True:
    # 2. Get user input
    user_input = int(input(" \n1. Add a Habit \n 2. Add new Task \n 3. View Habits \n 4. View Tasks \n 5. Marking Task as Complete \n 6. Marking Habit as Complete \n 7. Quit \n Choose an option: "))
    
    # 3. User Validation
    if user_input == 1:
        habit_name = input("Enter the name of the habit to add: ")
        habit_description = input("Enter the description of the habit: ")
        habit_frequency = input("Enter the frequency of the habit (Daily (D)/Weekly (W)/Monthly (M)): ")
        habit_status = "Incomplete"
        habit = tracker.add_habit( habit_name, habit_description, habit_frequency, habit_status)
        print(f"Habit added: {habit}\n")

    elif user_input == 2:
        task_name = input("Enter the name of the task to add: ")
        task_description = input("Enter the description of the task: ")
        task_prio = input("Enter the priority of the task (High (H)/Medium (M)/Low (L)): ")
        task_status = "Incomplete"
        task = tracker.add_task(task_name, task_description, task_prio, task_status)
        print(f"Task added: {task}\n")

    elif user_input == 3:
        print(f"Your Habits: {tracker.view_habits()}\n")
    
    elif user_input == 4:
        print(f"Your Tasks: {tracker.view_tasks()}\n")
    
    elif user_input == 5:
        tracker.list_tasks()
        index = int(input("Enter task number to complete: "))

        if tracker.complete_task(index):
            print("Task marked as complete!\n")
        else:
            print("Invalid task number!\n")
    
    elif user_input == 6:
        tracker.list_habits()
        index = int(input("Enter habit number to complete: "))

        if tracker.complete_habit(index):
            print("Habit marked as complete!\n")
        else:
            print("Invalid habit number!\n")
    
    elif user_input == 7:
        print("Quitting the program...")
        # 4. Exit the loop
        break
