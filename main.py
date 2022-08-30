user_input='random'

data=list()

def showmenu():

    print("\n\tMenu: ")
    print("1. Add an item: ")
    print("2. Mark as Done: ")
    print("3. View items: ")
    print("4. Exit: ")


while user_input != '4':
    showmenu()
    user_input=input("\tEnter your Choice: ")

    if user_input == '1':
        item = input("What is to be done ? ")
        data.append(item)
        print("Added item:",item)
    elif user_input == '2':
        item = input("What is to be marked as done: ")
        if item in data:
            data.remove(item)
            print("removed item: ",item)
        else:
            print("Item does not exist in the to-do List")
    elif user_input == '3':
        print("List of To-D0 items: ")
        for items in data:
            print(item)
    elif user_input == '4':
        print("\tGood Bye")