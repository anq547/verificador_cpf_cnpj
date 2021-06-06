# Author: @guizin1
# License: See LICENSE file
# Date: 06/05/2021 (mm/dd/yy)
# Usage: verif_cpf(int) || verif_cnpj(int)

def verif_cpf(cpf):
    lista_numeros = list(str(cpf))
    lista_numeros = list(map(int, lista_numeros))

    n1 = lista_numeros[9]
    n2  = lista_numeros[10]

    n1_correto = (( lista_numeros[0] * 10
                  + lista_numeros[1] * 9
                  + lista_numeros[2] * 8
                  + lista_numeros[3] * 7
                  + lista_numeros[4] * 6
                  + lista_numeros[5] * 5
                  + lista_numeros[6] * 4
                  + lista_numeros[7] * 3
                  + lista_numeros[8] * 2
                  )
                  * 10 % 11)

    if n1_correto == 10:
        n1_correto = 0

    n2_correto = (( lista_numeros[0] * 11
                  + lista_numeros[1] * 10
                  + lista_numeros[2] * 9
                  + lista_numeros[3] * 8
                  + lista_numeros[4] * 7
                  + lista_numeros[5] * 6
                  + lista_numeros[6] * 5
                  + lista_numeros[7] * 4
                  + lista_numeros[8] * 3
                  + n1_correto       * 2
                  )
                  * 10 % 11)
    

    if n2_correto == 10:
        n2_correto = 0

    def numeros_iguais(lista_numeros):
        if (len(lista_numeros) ==
            lista_numeros.count(lista_numeros[0])):
            return True
        else:
            return False

    if (n1 == n1_correto and
        n2 == n2_correto and
        numeros_iguais(lista_numeros) == False and
        len(lista_numeros) == 11):
        return True
    else:
        return False

def verif_cnpj(cnpj):
    lista_numeros = list(str(cnpj))
    lista_numeros = list(map(int, lista_numeros))

    n1  = lista_numeros[10]
    n2  = lista_numeros[11]

    n1_correto = (11 - ( lista_numeros[11] * 2
                       + lista_numeros[10] * 3
                       + lista_numeros[9]  * 4
                       + lista_numeros[8]  * 5
                       + lista_numeros[7]  * 6
                       + lista_numeros[6]  * 7
                       + lista_numeros[5]  * 8
                       + lista_numeros[4]  * 9
                       + lista_numeros[3]  * 2
                       + lista_numeros[2]  * 3
                       + lista_numeros[1]  * 4
                       + lista_numeros[0]  * 5
                       )
                       % 11)
                    
    if n1_correto == 10:
        n1_correto = 0

    n2_correto = (11 - ( n1_correto        * 2
                       + lista_numeros[11] * 3
                       + lista_numeros[10] * 4
                       + lista_numeros[9]  * 5
                       + lista_numeros[8]  * 6
                       + lista_numeros[7]  * 7
                       + lista_numeros[6]  * 8
                       + lista_numeros[5]  * 9
                       + lista_numeros[4]  * 2
                       + lista_numeros[3]  * 3
                       + lista_numeros[2]  * 4
                       + lista_numeros[1]  * 5
                       + lista_numeros[0]  * 6
                       )
                       % 11)

    if n2_correto == 10:
        n2_correto = 0

    def numeros_iguais(lista_numeros):
        if (len(lista_numeros) ==
            lista_numeros.count(lista_numeros[0])):
            return True
        else:
            return False

    if (n1 == n1_correto and
        n2 == n2_correto and
        numeros_iguais(lista_numeros) == False and
        len(lista_numeros) == 14):
        return True
    else:
        return False