import PySimpleGUI as sg
from random import randint as dice

class Ficha:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome:', size=(12, 0)), sg.Input(size=(15, 0), key='no')],
            [sg.Text('Jogue 1 dado e some 6,\nEste será seu valor de Habilidade.')],
            [sg.Text('Habilidade:', size=(12, 0)), sg.Input(dice(1, 6) + 6, key='ha', size=(15, 0))],
            [sg.Text('Jogue 2 dados e some 12,\nEste será seu valor de Energia.')],
            [sg.Text('Energia:', size=(12, 0)), sg.Input(dice(1, 6) + dice(1, 6) + 12, key='en', size=(15, 0))],
            [sg.Text('Jogue 1 dado e some 6,\nEste será seu valor de Sorte.')],
            [sg.Text('Sorte:', size=(12, 0)), sg.Input(dice(1, 6) + 6, key='so', size=(15, 0))],
            [sg.Text('Jogue 1 dado e some 3,\nEste será seu valor de Fé.')],
            [sg.Text('Fé:', size=(12, 0)), sg.Input(dice(1, 6) + 3, key='fe', size=(15, 0))],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(24, 6))]
        ]
        # Janela
        self.janela = sg.Window('Ficha').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair Dados da janela
            self.button, self.values = self.janela.Read()
            Nome = self.values['no']
            Habilidade = self.values['ha']
            Energia = self.values['en']
            Sorte = self.values['so']
            Fe = self.values['fe']
            print(f'Nome: {Nome}')
            print(f'Habilidade: {Habilidade}')
            print(f'Energia: {Energia}')
            print(f'Sorte: {Sorte}')
            print(f'Fé: {Fe}')


tela = Ficha()
tela.Iniciar()
