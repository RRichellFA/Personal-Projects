import PySimpleGUI as sg
from random import randint as dice


class Ficha:
    def __init__(self):
        sg.change_look_and_feel('Reds')
        layout = [
            [sg.Text('Nome:', size=(12, 0)), sg.Input(size=(15, 0), key='no')],
            [sg.Text('Habilidade:', size=(12, 0)), sg.Input(dice(1, 6) + 6, key='ha', size=(15, 0))],
            [sg.Text('Energia:', size=(12, 0)), sg.Input(dice(1, 6) + dice(1, 6) + 12, key='en', size=(15, 0))],
            [sg.Text('Sorte:', size=(12, 0)), sg.Input(dice(1, 6) + 6, key='so', size=(15, 0))],
            [sg.Text('Fé:', size=(12, 0)), sg.Input(dice(1, 6) + 3, key='fe', size=(15, 0))],
            [sg.Text('Provisões:', size=(12, 0)), sg.Slider(range=(0, 15), default_value=0, orientation='h', size=(15, 15), key='pro')],
            [sg.Button('Enviar dados')],
            [sg.Text('Equipamento.')],
            [sg.Text('1:'), sg.Input(size=(24, 10), default_text='Arma', key='i1')],
            [sg.Text('2:'), sg.Input(size=(24, 10), default_text='Escudo', key='i2')],
            [sg.Text('3:'), sg.Input(size=(24, 10), default_text='Armadura', key='i3')],
            [sg.Text('4:'), sg.Input(size=(24, 10), default_text='Jóia', key='i4')],
            [sg.Text('5:'), sg.Input(size=(24, 10), default_text='Encantamento', key='i5')],
            [sg.Text('Log de mudanças.', size=(24, 0))],
            [sg.Output(size=(30, 15))]
        ]
        self.janela = sg.Window('Ficha').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            Nome = self.values['no']
            Habilidade = self.values['ha']
            Energia = self.values['en']
            Sorte = self.values['so']
            Fe = self.values['fe']
            Provisoes = self.values['pro']
            i1 = self.values['i1']
            i2 = self.values['i2']
            i3 = self.values['i3']
            i4 = self.values['i4']
            i5 = self.values['i5']
            print(f'Nome: {Nome}')
            print(f'Habilidade: {Habilidade}')
            print(f'Energia: {Energia}')
            print(f'Sorte: {Sorte}')
            print(f'Fé: {Fe}')
            print(f'Provisões: {Provisoes:.0f}')
            print(f'Item 1: {i1}')
            print(f'Item 2: {i2}')
            print(f'Item 3: {i3}')
            print(f'Item 4: {i4}')
            print(f'Item 5: {i5}')


tela = Ficha()
tela.Iniciar()
