# full_name = "Ana Beatriz"
# birth_year = input("Em que ano você nasceu?")
# year = 2019
# print(year - int(birth_year))


#     conversor de libras pra kilos
# libras = input('Qual o peso em libras?')
# conversor = 0.45
# kg = int(libras) * float(conversor)

# print(float(kg))


#     OTIMIZADO
# peso_lbs = input('Descubra quanto vale em kg')
# peso_kg = int(peso_lbs) * 0.45

# print(peso_kg)

#       concatenação de strings
# name = input("Qual o seu nome?")
# color = input("Qual a sua cor favorita? ")

# print("Você se chama " + name + " e gosta da cor " +color)


#         Acessando indices dentro da variavel que não é especificamente um array
# name = "Ana Beatriz"
# print(name[1:5])
# print(len(name))
# print(name.find("A"))
# print(name.replace("Beatriz", "Morita"))

#         Procurar um valor na variável inteira
# course = "Não sei o que colocar então vou ficar digitando pra caramba até eu conseguir muito texto"
# print("caramba" in course)

#         Condições
# summer = True
# winter = False

# if summer:
#     print("Use óculos de sol")
# elif winter:
#     print("Não esquece o casaco, filho")
# else: 
#     print("Não use óculos de sol")

#         Condições
# green_account = False
# criminal_record = False

# if green_account and criminal_record:                     x E y
#     print('vai pras férias')
# elif green_account and not criminal_record:               x true E y false
#     print('ih deu ruim com a tua ficha')
# elif criminal_record and not green_account:
#     print('ih deu ruim com o teu dinheiro')
# elif not criminal_record and not green_account:           x false E y false
#     print('cara tu tá ferrado')

#         Loop While 
# i = 0

# while i < 5:
#     print(i)
#     i = i + 1
# print("Acabou")

#     Acerte o número secreto

# secret_number = 3
# i = 3

# while i > 0:
#     numero = input("Tente acertar o número secreto, você tem " + str(i) + " tentativas: ")
#     if int(numero) == secret_number:
#         i = -2
#     elif int(numero) < secret_number:
#         print("O numero digitado é menor que o número secreto.")
#         i = i - 1
#     elif int(numero) > secret_number:
#         print("O numero digitado é maior que o número secreto.")
#         i = i = 1
# if i == -2:
#     print('Parabéns, você conseguiu')
# elif i == 0:
#     print("Que pena, você não conseguiu acertar")


            # Posso comprar um celular com x reais?

# iphoneXRMaster = 8000
# iphoneXRDiamond = 5000
# positivo = 450

# celular1 = 'iPhone XR Master'
# celular2 = 'iPhone XR Diamond'
# celular3 = 'Positivo azul'

# dinheiro = input('Quanta grana você tem pra descolar um celular novo? ')
# if int(dinheiro) >= iphoneXRMaster:
#         print('Você tem disponíveis pra comprar: ' + celular1 + ', ' + celular2 + ', e ' + celular3)
# elif int(dinheiro) < iphoneXRMaster and int(dinheiro) >= iphoneXRDiamond:
#         print('Você tem disponíveis pra comprar: ' + celular2 + ', e ' + celular3)
# elif int(dinheiro) < iphoneXRMaster and int(dinheiro) >= positivo:
#         print('Você tem disponível pra comprar: ' + celular3)
# else:
#         print('Puts que pena, não existe nenhum celular disponível para você comprar no momento')


#         Listas
# nomes = [1, 2, 3, 3, 4, 4, 4, 5, 6, 7]
# # print(nomes[1:3])

# # nomes.append(20)        #Adiciona 20 ao final da lista
# # print(nomes)
# # nomes.insert(0, 99)     #Adiciona 99 no índice 0
# # print(nomes)
# # nomes.remove(3)         #Remove o item de valor 3 na lista
# # print(nomes)
# # nomes.pop()             #Remove o último item da lista
# # print(nomes)
# # print(nomes.index(4))   #Verifica em que índice o item está na lista

# # print(nomes.count(7))   #Conta quantos itens com esse valor existem na lista

# # lista2 = nomes.copy()   #Faz uma cópia da lista especificada
# # print(lista2)
# # nomes.clear()           #Limpa a lista
# # print(nomes)
#         Criar uma cópia e eliminar os nomes repetidos
# nomes2 = []

# for number in nomes:
#     if number not in nomes2:            #Verifica se o nome não está no nomes2
#         nomes2.append(number)           #Insere o nome na lista nomes2
# print(nomes)
# print(nomes2)

#            Tuplas ou tuple(listas ineditáveis)

# cursos = ('Matemática', 'Inglês', 'Biologia')

#            Dicionarios

# pessoa = {
#     'name': 'Hayane',
#     'age': 22,
#     'address': 'área de preservação florestal',
#     'skills': ['python', 'c', 'cobol', 'pascal', 'pearl', 'birl']
# }

# print(pessoa['name'])
# print(pessoa['address'])
# print(pessoa['skills'[0]])

#faça um codigo para printar o número mais alto da lista

# lista = [1, 2, 3, 8, 10, 45, 12]

# print(max(lista))
# max = lista[0]

# for lista in lista:
#     if lista > max:
#         max = lista
# print(max)


#faça um codigo, onde é possível identificar se o aluno passou na faculdade ou não. A média é 6, e ele só pode ter 2 faltas.

# media = int(input("Qual a sua média?"))
# faltas = int(input("Quantas faltas você teve?"))

# if media > 6 and faltas < 2:
#     print("Parabéns, você passou na faculdade.")
# elif media > 6 and faltas > 2:
#     print("Reprovado por conta de faltas.")
# elif media < 6:
#     print("Reprovado por conta de média.")