def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    y = 0
    for i in range(0,5):
        x = int(input("enter number: "))
        total = x + y
        print(total)
        y = total


    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
