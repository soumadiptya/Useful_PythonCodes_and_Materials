# Pycharm Tips
# 1) Change name of a variable in many places using Refactor- rename
# 2) CTRL + D to duplicate lines
# 3) add comments with todo to remind yourself of things to do and directly jump to a particular section of code
# 4) Type on multiple lines at once- Press alt and click on multiple lines. Now you can type in multiple lines.
# 5) alt + Shift + c- To see recent changes in files well actually the project directory
# Imports
import random


# Helper Functions
def generate_random(upper):
    """

    :param upper: >= 0
    : return: int
    """
    r = random.randint(1, upper)
    return r


def main():
    run = True
    num_1 = generate_random(10)
    num_2 = generate_random(10)
    result = num_1 * num_2
    while run:
        ans = input(" What is " + str(num_1) + "x" + str(num_2) + "? ")
        if ans.isdigit():
            if int(ans) == result:
                print("Correct")
                run = False
            else:
                print('Incorrect try again')
        else:
            print("Answer must be a positive number, try again")


# Global vars
times = 5

for x in range(times):
    main()
