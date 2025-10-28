# Operators: 

    # Logical operators -->  Boolean
        # (and, or, not)

            # and

                # (True)  and (True)  --> True
                # (True)  and (False) --> False
                # (False) and (True)  --> False
                # (False) and (False) --> False

            # or

                # (True)  or (True)  --> True
                # (True)  or (False) --> True
                # (False) or (True)  --> True
                # (False) or (False) --> False

                    # age = 22

                    # result = (age > 18) and (age > 30)
                    # result = not((age > 18) or (age > 30))

                    # print(result)

    # Identity operators
        # (is, is not)

            # x = ["apple", "banana"]
            # y = ["apple", "banana"]
            # z = x

            # print(x is y)
            # print(x is not z)

    # Membership operators
        # (in, not in)

x = ["apple", "banana"]

print("appl" not in x)