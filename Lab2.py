print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    calc_average(get_user_input())
    calc_min_max(get_user_input())
    medianlist(get_user_input())

def display_main_menu():
    print("display_main_menu")
def calc_average(list):
    avg=sum(list)/len(list)
    print("Average temperature is:" + str(avg))
    return avg
def calc_min_max(list):
    print("The minimum value is ")
    print(min(list))
    print("The maximum value is ")
    print(max(list))
    return min(list), max(list)
def medianlist(list):
    list.sort()
    mid=len(list) // 2
    res=(list[mid]+ list[~mid])/2
    print("The median temp is " + str(res))
    return res

def get_user_input():
    print("Enter temp values separated by commas and press 'Enter'  e.g: 5,8,9,3")
    tempstring=input()
    tempstringList=tempstring.split(",")
    print(tempstringList)
    tempfloatlist=list(map(float,tempstringList))
    print(str(tempfloatlist))
    return tempfloatlist

if __name__ == "__main__":
    main()