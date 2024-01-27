def line(line_size)-> None:
    '''-> Show a line with a determined length/size

        Parameters:

            line_size(int): size of the line
            return: no return
    '''

    print("-=" * line_size)


def menu()-> None:
    '''-> Shows the menu options

        Parameters:

            return: no return
    '''

    print("\n")

    line(30)
    print('''Menu:\n[ 1 ] - Add task\n[ 2 ] - Change task status\n[ 3 ] - List tasks\n[ 4 ] - Remove task\n[ 5 ] - Quit
    ''')

    line(30)

    print('\n')


def title(message: str)-> None:
    '''-> show a title with a determined message 

        Parameters:

            message(str): message (text) to be shown in the title
            return: no return
    '''

    print("\n")

    size_of_message = len(message)
    
    width = size_of_message * 2

    line(size_of_message)
    print(message.center(width))
    line(size_of_message)

    print("\n")



def leiaInt(message)-> int:
    '''-> Valids data input of type int

        Parameters:

            message(str): message to be shown in the data input
            return: returns the number in type int
    '''

    from sys import exit


    while True:

        
        try:

            user_choice = int(input(message))

        # NameError/ValueEror exceptions
        except (NameError, ValueError):

            print("\033[1;31mInvalid option.Please, enter a valid number.\033[m")


        # KeyboardInterrupt exception
        except (KeyboardInterrupt):

            print("\033[1;31mThe user decides to quit the program.\033[m")

            exit(1)


        # other exceptions
        except Exception as exp:

            print(f"\033[1;31mAn exception has occured.\nException = {exp}")

        
        else:

            return user_choice