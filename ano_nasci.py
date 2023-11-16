print('Digite seu nome')
nome = input()

rodarPrograma = True

while(rodarPrograma == True):
    print('Digite o ano de seu nascimento: ')
    try:
       ano = int(input())
       if(ano < 1922) or (ano > 2023):
           print('O ano precisa ser entre 1922 a 2023')
       else:
           idade = 2023 - ano
           print('O usuario', nome, 'completou ou completara', idade, 'anos de idade em 2023')
           rodarPrograma = False
    except:
        print('Os anos devem ser escritos apenas com números')
        
        