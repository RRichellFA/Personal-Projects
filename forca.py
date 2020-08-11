import getpass
print("Jogo da forca")
print('1- Digite a palavra da forca, ela ficará escondida, portanto certifique-se de digitar corretamente.')
print('2- o jogador terá 5 chances de adivinhar a palavra, letra por letra. Se ele errar perde, se completar a palavra, ganha.')

forca = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Vamos começar!")
palavra = getpass.getpass("Digite a palavra da forca: ").strip().upper()
print(forca[0])
erros = 0
acertos = 0
letras = []
letrascertas = []
print(f"A palavra escolhida tem {len(palavra)} letras.")
while erros < 5 or acertos == len(palavra):
  jogador = input("Digite uma letra.")[0].upper()
  if jogador not in letras:
    letras.append(jogador)
    letras.sort()
  else:
    print("Essa letra ja foi escolhida.")
    continue
  if jogador in palavra:
    print("ACERTOU")
    acertos +=1
    print(forca[erros])
    letrascertas.append(jogador)
    print(f"As letras corretas escolhidas foram {letrascertas}.")
    if acertos == len(palavra):
      print("Parabéns, você venceu!")
      break
  else:
    print("ERROU")
    erros +=1
    print(forca[erros])
    print(f"Você tem mais {5-erros} tentativas.")
    if erros == 5:
      print(forca[6])
      print("Você perdeu!")
  print(f"As letras escolhidas foram {letras}.")
print("FIM DO JOGO")