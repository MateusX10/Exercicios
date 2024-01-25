def line(line_size):

    print("-=" * line_size)


def menu():

    print("\n")

    line(30)
    print('''Menu:\n[ 1 ] - Add task\n[ 2 ] - Change task status\n[ 3 ] - List tasks\n[ 4 ] - Remove task\n[ 5 ] - Quit
    ''')

    line(30)

    print('\n')


def title(message):

    print("\n")

    size_of_message = len(message)
    
    width = size_of_message * 2

    line(size_of_message)
    print(message.center(width))
    line(size_of_message)

    print("\n")



def leiaInt(message):

    from sys import exit


    while True:

        try:

            user_choice = int(input(message))

        except (NameError, ValueError):

            print("\033[1;31mInvalid option.Please, enter a valid number.\033[m")


        except (KeyboardInterrupt):

            print("\033[1;31mThe user decides to quit the program.\033[m")

            exit(1)


        except Exception as exp:

            print(f"\033[1;31mAn exception has occured.\nException = {exp}")


        else:

            return user_choice