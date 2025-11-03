# Exception Handling:

try:

    mylist = [10, 20, 30]

    print(mylist[5])

    n = 6

    result = 6/0

    print(result)

except ZeroDivisionError:
    print("Zero Division error")
except:
    print("Something went wrong")
finally:
    print("Done..!")