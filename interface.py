 #
import PySimpleGUI as sg

sg.theme('Light Green 3')

# Layout da interface
menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']], ['&Help', ['&About...']]]

frame_layout2 = [[sg.Button('Ok'), sg.Button('Cancel')]]

frame_layout1 = [[sg.Text('PyTCPScan - Version 4.0')],
                 [sg.HorizontalSeparator(color='grey')],
                 [sg.InputText(), sg.Frame('Comandos', frame_layout2, element_justification='center')],
                 [sg.Input()]]

layout = [[sg.Menu(menu_def)],
          [sg.Frame('Dados', frame_layout1)],
          [sg.Multiline(default_text='', size=(None, 15))]]

# Criando a Janela
window = sg.Window('PyTCPScan - Version 4.0', layout)

# Evento que processa events e os valores
while True:
    event, values = window.read()

    # Se o usuário fechar a janela, exit ou clicar em cancelar
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
        break

    print('Hello', values[0], '!')

window.close()