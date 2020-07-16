from time import sleep
from RollDices import dice
print("""
Projeto do jogo "A Crypta do Vampiro"
Escrito por Steve Jackson e Ian Livingstone
Este é um projeto didático e não estará disponível para venda, apoie a obra original!
""")
sleep(3)

print('='*5, 'Criação do personagem', '='*5)
print("""
Antes de embarcar nesta aventura você precisa definir os atributos do seu personagem.
Anote os detalhes do seu personagem em uma folha de papel ou bloco de notas.
Se for usar papel, utilize lapiz para marcar seus atributos e itens, uma vez que eles podem e vão ser,
modificados durante a aventura.
""")

Ficha = {'Nome': str(input('Diga seu nome: ')).strip().capitalize()}

print(f"Muito bem {Ficha['Nome']}, vamos rolar seus atributos utilizando dados de 6 lados.")
print('Usaremos um rolagem automática de dados no programa, mas você pode usar seus proprios dados.')
sleep(4)
print('='*30)
print('Para seus pontos de Habilidade usaremos 1 dados e somaremos 6.')
Habilidade = dice(6)
Ficha['Habilidade'] = Habilidade + 6
print(f"Você tirou {Habilidade} + 6, totalizando {Ficha['Habilidade']}, estes são seus pontos de habilidade iniciais.")
sleep(4)
print('='*30)
print('Para seus pontos de Energia jogaremos 2 dados e somaremos 12.')
Energia1 = dice(6)
Energia2 = dice(6)
Ficha['Energia'] = Energia1 + Energia2 + 12
print(f"Você tirou {Energia1} + {Energia2} + 12, totalizando {Ficha['Energia']}, esses são seus pontos de energia "
      f"iniciais.")
sleep(4)
print('='*30)
print('Para seus pontos de Sorte usaremos 1 dado e somaremos 6.')
Sorte = dice(6)
Ficha['Sorte'] = Sorte + 6
print(f"Você tirou {Sorte} + 6, totalizando {Ficha['Sorte']}, esses são seus pontos de sorte Iniciais.")
sleep(4)
print('='*30)
print('Para seus pontos de Fé, usaremos 1 dado e somaremos 3.')
Fe = dice(6)
Ficha['Fé'] = Fe + 3
print(f"Você tirou {Fe} + 3, totalizando {Ficha['Fé']}, esses são seus pontos de fé iniciais.")
sleep(4)
print('='*30)
print("""Anote esses dados para referência futura ou escreva seus próprios dados em sua ficha particular.
Nunca Apague seus valores iniciais, pode ser necessário que esses valores sejam resgatados.
Ao receber valores adicionais de atributos, tais valores nunca poderão ultrapassar seus valores iniciais,
a menos que seja especificado para tal, apenas o valor de Fé pode ultrapassar esse limite sem restrição.""")
print(f"""
Nome: {Ficha['Nome']}
Habilidade: {Ficha['Habilidade']}
Energia: {Ficha['Energia']}
Sorte: {Ficha['Sorte']}
Fé: {Ficha['Fé']}
""")
Iniciais = [Ficha['Habilidade'], Ficha['Energia'], Ficha['Sorte'], Ficha['Fé']]
del Habilidade, Sorte, Energia1, Energia2, Fe

