from time import sleep


print("\033[31mEste é um projeto didático, serve para aprimoramento e fixação de conhecimentos na linguagem "
      "Python!\033[m")
sleep(5)

print('='*5, 'Criação do personagem', '='*5)
print("""
Todas as informações podem ser alteradas para melhor se adequar a sua própria aventura.

Antes de embarcar nesta aventura você precisa definir os atributos do seu personagem.
Usaremos durante toda a aventura, dados simples de 6 lados.
Anote os detalhes do seu personagem em uma folha de papel ou bloco de notas.
Se for usar papel, utilize lapiz para marcar seus atributos e itens, uma vez que eles podem e vão ser,
modificados durante a aventura.
Você pode usar o programa Ficha do Personagem para auxiliar na sua aventura.
Anote os valores iniciais, qualquer ganho de atributo não poderá ultrapassar esses valores a menos que
seja especificado. Os valores Fé não seguem esta regra podendo ser elevados acima do valor inicial.

Jogue um dado e some 6, será seu valor inicial de \033[31mHabilidade\033[m.
Este atributo reflete sua capacidade de combate, quanto maior, melhor.

Jogue dois dados e some 12, será seu valor inicial de \033[31mEnergia\033[m.
Este atributo reflete sua constituição e força de sobrevivencia, quanto maior, mais tempo você sobrevive.

Jogue um dado e some 6, será seu valor inicial de \033[31mSorte\033[m.
Reflete o quão naturalmente sortudo você é.

Jogue um dado e some 3, será seu valor de \033[31mFé\033[m.
Reflete sua convicção e presença, um alto valor de fé pode fazer criaturas menores fugirem,
mas também o fará ser notado mais facilmente por outras.

Lembre-se de anotar todos os valores iniciais a caneta, eles podem ser necessários.""")
sleep(3)
print("""
"\033[31mMAGIA\033[m"
Eventualmente você pode encontrar itens mágicos.
Você talvez não perceba que são mágicos, tampouco consegue entender o que fazem.
Se você encontrar itens assim, este o dará instruções sobre como agir.
Alguns pode até mesmo lhe conceder feitiços.

"\033[31mCOMBATE\033[m"
Antes de mais nada, seu oponente terá pontos de Habilidade e Energia, anote-os.
Haverá um banco de dados para referência de monstros, mas você pode criar os seus.

"Sequência de combate"

1 - Jogue 2 dados para seu oponente, em seguida, 2 dados para você.
2 - Some aos respectivos valores de Habilidade. Este será o poder de \033[31mATAQUE\033[m de ambos.
3 - O maior valor de ataque ganha o turno, subtraia 2 pontos de energia do perdedor.
Você pode usar Sorte para desferir golpes críticos, ou para reduzir o golpe do oponente,
cuidado, um resultado azarado pode piorar sua situação.
Se for sortudo durante um ataque, cause 4 pontos de dano ao oponente, se for azarado, cause apenas 1 ponto.
O mesmo vale ao testar sorte durante uma defesa, sorte reduzira seu dano para 1, azar aumentará para 4.
Ao enfrentar mais de uma criatura, realize um turno com cada criatura por vez,
Em algumas ocasiões, você tratará as criaturas como uma só.
Continue o combate até que os pontos de energia da criatura, ou os seus, seja reduzido a 0.

"\033[31mSORTE\033[m"
Em algumas situações será pedido que teste sua sorte. Ou você pode até mesmo testar sua sorte em combate.
o procedimento é o seguinte.

Jogue 2 dados e os compare a seu valor de sorte.
Se o resultado for \033[32mMENOR ou IGUAL\033[m, você teve \033[33mSORTE\033[m, e o resultado será favorável.
Se o resultado for \033[32mMAIOR\033[m, você foi \033[33mAZARADO\033[m, e você será penalizado.

SEMPRE QUE TESTAR SUA SORTE, REDUZA SEU VALOR DE SORTE EM 1.
Tenha cuidado pois, smpre que se apoiar na sorte para resolver algo, será mais difcil nas próximas vezes.
Com sua sorte reduzida a 1 ou 0, você será SEMPRE AZARADO quando for testar sua sorte.

"\033[31mPROVISÕES\033[m"
Sempre que não estiver em combate, você pode parar para descansar e comer suas provisões, isso recupera sua
energia. Para cada PROVISÃO que consumir, recupere 4 pontos de ENERGIA. Lembre-se, nunca ultrapasse seus pontos
iniciais de ENERGIA a menos que seja instruido a fazê-lo.

"\033[31mFÉ\033[m"
Sua fé reflete sua capacidade de enfrentar os perigos, poderá ser alterada dependendo das situações que enfrentar.
Detalhes são fornecidos na hora da situação, mas geralmente não há o que testar, se sua fé for alta, ou baixa,
isso ja determinará como enfrentar a situação, ou fugir dela.

"\033[31mAflições ou maldições\033[m
Durante sua aventura, você pode sofrer de ferimentos, ou mesmo maldições que reduzirão seus atributos maximos,
anote-os separadamente, pois aflições e maldições podem ser curadas ou removidas, talvez.

"\033[mDICAS FINAIS\033[m"
1 - Faça um mapa, escreva por onde passou e anote coisas interessantes,
ex: Cozinha + Provisões, Masmorra + Baú trancado, Rua A + armadilha, Casa B + Monstro forte.
Anote também as rotas, as vezes, você precisa lembrar delas.
Cozinha->Sala->Escada->Quarto, Salão -> Masmorras, trono, tesouro, prisão.

2 - Cuidado ao testar sua Sorte, não é facil recupera-la, e quanto mais testa-la, maior será o risco.

\033[32mBOA AVENTURA\033[m
""")