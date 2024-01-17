


if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    argument = []

    for i in sys.argv:
        argument.append(i)

    if count == 0:
        print("{} arguments.".format(count))
    elif count > 0:
        print("{} arguments:".format(count))
        for j in range(len(argument)):
            print("{}: {}".format(j+1, argument[j]))
       

