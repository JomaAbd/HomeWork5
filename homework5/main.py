def add_info(lst:list):
    while True:
        data = input("Enter a data or 'exit' to exit: ")
        if data == "exit":
            break
        elif data == "":
            break
        else:
            lst.append(data)

def show_info(lst:list):
    print("\n\n" + 15*" "+"Simple list of Data 📋")
    print("|"+'-'*50+"|")    
    for data in lst:
        print(" " * 4 + data)
        print("|"+'-'*50+"|")


if __name__ == "__main__":
    lst = []
    add_info(lst)
    show_info(lst)