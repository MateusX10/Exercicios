def is_prime(num)-> bool:
    '''-> Verifica se um número é primo

        Parâmetros:

            num(int): número inteiro a ser verificado como primo ou não
            return: retorna "True" para "é primo", "False" para "Não é primo"

        
        Exemplo:

        
            input 1: 3

            output 1: True

            Input 2: 4

            output 2: False



    '''
    
    # quantidade de múltiplos do número
    quantidade_de_multiplos = 0
    
    # percorre todos os números antecessores ao número passado como parâmetro.Se
    #o número somente for múltiplo dele mesmo e de 1, então logo ele é primo
    for numero in range(0, num + 1):
        
        if numero != 0:
        
            if num % numero == 0:
            
                quantidade_de_multiplos += 1
            
    # número é primo    
    if quantidade_de_multiplos == 2:
        
        return True
    
    # não primo
    else:
        
        return False
            
            
        
        