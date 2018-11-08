import json

class Todo:

    MaryDict = {'HomeTodo':['wakeup', 'wash the dog'], 'SchoolTodo':['learn html', 'learn python']}
    JohnDict = {'HomeTodo':['wakeup', 'wash the dog'], 'SchoolTodo':['learn html', 'learn python']}
    JaneDict = {'HomeTodo':['wakeup', 'wash the dog'], 'SchoolTodo':['learn html', 'learn python']}

    def __init__(self, user_name, Todolist_name):
       self.user_name =user_name
       self.Todolist_name = Todolist_name
    
    user_name = ["Mary","John","Jane"]
    
    Todolist_name = ["HomeTodo","SchoolTodo"]

    UserDict = {
            "Mary":
            {
         'HomeTodo':[], 
         'SchoolTodo':[]
         },
              "John":
              {
                 'HomeTodo':[], 
                'SchoolTodo':[] 
              }}

    task_description = {
        "Mary":
            {
         'HomeTodo':['wakeup', 'wash the dog'], 
         'SchoolTodo':['learn html', 'learn python']
         },
              "John":
              {
                 'HomeTodo':['wakeup', 'wash the dog'], 
                'SchoolTodo':['learn html', 'learn python'] 
              }}

    
    def create_user(self,user_name):
        if user_name in user_name:
            return True
        else:
            return False
    print(user_name)

    def create_todoist(self,user_name,Todolist_name):
    
        for UserDict in UserDict:
            return UserDict
    print(UserDict)

    def create_task(self,user_name,Todolist_name,task_description):
    
        for task_description in task_description:
            return task_description
    print(task_description)
            