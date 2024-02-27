def array_diff(array_a, array_b):
    '''-> Removes all values of array A which are present in array B

        Parameters:

            array_a(array): array to have its items removed if they are present in array B
            array_b(array): array to use so array A items will be removed if a item from array B is in array A
            return: returns the new array, the array substracted

        
        Example:

            Input 1: array_a = [1, 2, 3, 4, 5] ; array_b = [2]

            Output 1: [1, 3, 4, 5]


            Input 2: array_a = [1, 2, 3, 4, 5] array_b = [1, 2, 3]


            Output 2: [4, 5]


            Input 3: array_a = [1, 2, 2, 2, 2, 3, 4, 5, 5] array_b = [2]

            Output 3: [1, 3, 4, 5, 5]
    '''

    new_array = []

    # verify if any item in array A is in array B.If yes, this item is not include in the new array.Otherwise, if it's not, then the new array is updated with new values
    for value in array_a:

        if value not in array_b:

            new_array.append(value)



    return new_array
