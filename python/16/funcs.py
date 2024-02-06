def valid_braces(string):
    '''-> Verifica se a expressão matemática está correta


        Parâmetros:

            string(str): string da expressão
            return: "True" para "expressão inválida", já o contrário: "opção inválida"


        
    '''
  

    lista_parenteses_de_abertura = list()
    
    lista_chaves_de_abertura = list()
    
    lista_colchetes_de_abertura = list()
    
    
    for simbolo in string:
        
        
        if simbolo in "( )":
        
            if simbolo == "(":
            
                lista_parenteses_de_abertura.append("(")
                
            elif simbolo == ")":

                if len(lista_parenteses_de_abertura) == 0:

                    return False
                
                lista_parenteses_de_abertura.pop()
                
                
        elif simbolo in "{ }":
            
            
            if simbolo == "{":
            
                lista_chaves_de_abertura.append("{")
                
            
            elif simbolo == "}":


                if len(lista_chaves_de_abertura) == 0:

                    return False
                
                
                lista_chaves_de_abertura.pop()
                
                
                
        elif simbolo in "[ ]":
            
            
            if simbolo == "[":
            
                lista_colchetes_de_abertura.append("[")
                
            elif simbolo == "]":


                if len(lista_colchetes_de_abertura) == 0:

                    return False
                
                lista_colchetes_de_abertura.pop()
            
        


    if (len(lista_parenteses_de_abertura) + len(lista_colchetes_de_abertura) + len(lista_chaves_de_abertura)) == 0:
                

        return True

    
    else:

        return False