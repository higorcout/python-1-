'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
idade = int(input("Digite sua idade: "))     #Entrada do valor da idade
 
#Estrutura de Seleção
if idade >=10 and idade <20:       #Se a idade estiver entre 10 e 20
    print("Você é adolescente")
elif idade >=20 and idade <30:      #Se a idade estiver entre 20 e 30
    print("Você é jovem")
elif idade >=30 and idade <=100:     #Se a idade estiver entre 30 e 100
    print("Você é adulto")
else:                  #Se o valor não estiver dentro das condições
    print("Valor não encontrado")