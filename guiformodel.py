import PySimpleGUI as sg
from sklearn import linear_model, preprocessing

sg.theme('Dark Blue 1')

layout = [[sg.Text('Buying Cost')],
          [sg.OptionMenu(['Very High', 'High', 'Medium', 'Low'], s=(40, 1))],
          [sg.Text('Maintenance')],
          [sg.OptionMenu(["Very High", "High", "Medium", "Low"], s=(40, 1))],
          [sg.Text('Doors')],
          [sg.OptionMenu(['2', '3', '4', 'More'], s=(40, 1))],
          [sg.Text('Persons')],
          [sg.OptionMenu(['2', '4', 'More'], s=(40, 1))],
          [sg.Text('Lug Boot')],
          [sg.OptionMenu(['Small', 'Medium', 'Big'], s=(40, 1))],
          [sg.Text('Safety')],
          [sg.OptionMenu(['Low', 'Medium', 'High'], s=(40, 1))],
          [sg.Button('Submit'), sg.Exit()]]

window = sg.Window('Car Evaluation', layout, no_titlebar=True, grab_anywhere=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print (list(values))


window.close()


'''
firstinput = input("Hello, input your preferences.")
gatheredinp = firstinput.split(", ")
listofinput =  np.array([[int(gatheredinp[0]), int(gatheredinp[1]), int(gatheredinp[2]), int(gatheredinp[3]), int(gatheredinp[4]), int(gatheredinp[5])]])
predicted = model.predict(listofinput)
print(predicted)
'''

'''
firstinput = input("Hello, input your preferences.")
gatheredinp = firstinput.split(", ")
listofinput =  np.array([[int(gatheredinp[0]), int(gatheredinp[1]), int(gatheredinp[2]), int(gatheredinp[3]), int(gatheredinp[4]), int(gatheredinp[5])]])
predicted = model.predict(listofinput)
print(predicted)
if predicted == 2:
    print("Good")
'''