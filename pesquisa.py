

print("Bem-vindo à pesquisa de satisfação do atendimento TudoWeb!")

# Primeiro adicionamos as variáveis para contar as respostas. 
excelente = 0 
ruim = 0

# Repita tudo o que está abaixo 50 vezes
for i in range(1, 51):
    
# Solicite o nome, idade e opinião do entrevistado. f coloca a variável dentro da string. \n para pular uma linha
    print(f"\nEntrevistado {i}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opinião sobre o atendimento prestado (1: EXCELENTE, 2: BOM, 3: RUIM): "))
    
# Se a opinião for excelente, some 1 à variável excelente
    if opiniao == 1:
        print("Você avaliou o atendimento como EXCELENTE.")
        excelente += 1
        

    elif opiniao == 2:
        print("Você avaliou o atendimento como BOM.")
        
# Se a opinião for ruim, some 1 à variável ruim
    elif opiniao == 3:
        print("Você avaliou o atendimento como RUIM.")
        ruim += 1
        
#Se for digitado qualquer outra resposta além de 1,2 ou 3, exibe uma mensagem de erro para o usuário
    else:
        print("Opinião inválida.")

print("\nResultado final da pesquisa:")

# Exibe a quantidade de respostas "EXCELENTE" e "RUIM"
print(f"Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"Quantidade de respostas 'RUIM': {ruim}")