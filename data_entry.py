import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal6')

EXCEL_FILE = 'Data_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the patient details:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('City', size=(15,1)), sg.InputText(key='City')],
    [sg.Text('Phone', size=(15,1)), sg.InputText(key='Phone')],
    [sg.Text('Age', size=(15,1)), sg.InputText(key='Age')],
    [sg.Text('Paid', size=(15,1)), sg.InputText(key='Paid')],
    [sg.Text('Date:', size=(10,1)),sg.Input('', key = 'date', size=(15,1)), sg.CalendarButton('Date', target='date', format='%Y-%m-%d', key='date', close_when_date_chosen=True)],
    [sg.Text("Choose your gender: ",size=(15,1)),
                sg.Radio("Male","g",True,key="Male"),
                sg.Radio("Female","g",key="Female")],

    [sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Dr Shinawy patients details', layout, icon= r'C:\Users\dell\Desktop\dr_shinawy\shinawy.ico')

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()
