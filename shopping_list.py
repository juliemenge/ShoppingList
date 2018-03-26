print("Time to start shopping")

to_buy_list = list()

def show_help():
    print("DONE quits, SHOW shows the current list, and HELP display help")

def show_list():
    for item in to_buy_list:
        print(item)

show_help()

while True:
    user_input = input("Enter an item or a command: ")

    if user_input == "DONE":
        break
    elif user_input == "HELP":
        show_help()
        continue
    elif user_input == "SHOW":
        show_list()
        continue

    to_buy_list.append(user_input)

show_list()