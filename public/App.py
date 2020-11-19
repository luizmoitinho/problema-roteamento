import PySimpleGUI as sg
import time

def long_function():
    time.sleep(10)

layout = [[sg.Output(size=(70,50))],
          [sg.Button('Go'), sg.Button('Nothing'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        print('About to go to call my long function')
        long_function()
        print('Your long operation completed')
window.close()
