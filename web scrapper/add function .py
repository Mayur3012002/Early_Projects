

def main():
    number_of_values = int(input('Please enter number of values: '))  # int

    myList = create_list(number_of_values)  # myList = function result
    total = get_total(myList)

    print('the list is: ', myList)
    print('the total is ', total)

def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total

def create_list(number_of_values):
    myList = []
    for _ in range(number_of_values):  # no need to use num in loop here
        num = int(input('Please enter number: '))  # int
        myList.append(num)
    return myList

if __name__ == '__main__':  # it's better to add this line as suggested
    main()


