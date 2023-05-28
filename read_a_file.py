
try:
    with open('C:\\Users\\p_ant\\Documents\\CAN.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")