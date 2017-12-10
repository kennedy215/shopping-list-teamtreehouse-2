# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.")
Enter 'HELP' if you need help
Enter 'SHOW' to see your current list
""")
show_help()

def show_list():
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)
show_list()

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List has {} items ".format(new_item,len(shopping_list)))

def done():
    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list()
            continue
        add_to_list(new_item)

done()
