def task():
    tasks=[]  # emplty list as the start
    print("*** Welcome to Task management app ***")

    total_task=int(input("Enter how many number of task you want to add for the day : "))

    for i in range (1,total_task+1):
        task_name = input(f"Enter task {i} ")
        tasks.append(task_name)
    
    print(f"Today's tasks are \n {tasks} ")

    while True:
        operation = int(input("Enter operation 1:ADD \n 2:Update \n 3:Delete \n 4:View \n 5:Exit "))

        if operation == 1:
            add =  input("Please eneter the task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been successfully added")

        elif operation == 2:
            updated_value = input("Enter the task name you want to update : ")
            if updated_value in tasks:
                updated_task = input("Enter new task")
                ind_ex=tasks.index(updated_value)
                tasks[ind_ex] = updated_task
                print(f"Updated task {updated_task}")

        elif operation == 3:
            del_val=input("Enter the task you want to delete : ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")

        elif operation == 4:
            print(f"Total tasks are {tasks}")

        elif operation == 5:
            print("Closing the program")
            break

        else:
            print("Invalid operation")

task()

