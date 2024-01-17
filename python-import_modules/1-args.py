


if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    argument = []

    for i in sys.argv:
        argument.append(i)

    if count == 1:
        print("{} arguments.".format(count -1))
    elif count > 1:
        print("{} arguments:".format(count - 1))
        j = 1
        for j in range(len(argument)):
            print("{}: {}".format(j+1, argument[j]))
       

