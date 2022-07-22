import PySimpleGUI as sg
import main as m


def opengui():
    sg.theme('Dark Blue 1')

    layout = [[sg.Text('Buying Cost')],
              [sg.OptionMenu([m.buyingunique[0], m.buyingunique[1], m.buyingunique[2], m.buyingunique[3]], key='BUY')],
              [sg.Text('Maintenance')],
              [sg.OptionMenu([m.maintunique[0], m.maintunique[1], m.maintunique[2], m.maintunique[3]], key='MAINT')],
              [sg.Text('Doors')],
              [sg.OptionMenu([m.doorsunique[0], m.doorsunique[1], m.doorsunique[2], m.doorsunique[3]], key='DOOR')],
              [sg.Text('Persons')],
              [sg.OptionMenu([m.personsunique[0], m.doorsunique[1], m.doorsunique[2]], key='PERSON')],
              [sg.Text('Trunk Storage')],
              [sg.OptionMenu([m.lugbootunique[0], m.lugbootunique[1], m.lugbootunique[2]], key='LUG')],
              [sg.Text('Safety')],
              [sg.OptionMenu([m.safetyunique[0], m.safetyunique[1], m.safetyunique[2]], key='SAFETY')],
              [sg.Button('Submit'), sg.Button('Information (READ ME)'), sg.Exit()]]

    window = sg.Window('Car Evaluation', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Information (READ ME)":
            sg.popup("will put smth cool here, but check out my github lol https://github.com/VishistS")
        else:
            try:
                inputgathered = m.np.array([[int(values["BUY"]), int(values["MAINT"]), int(values["DOOR"]), int(values["PERSON"]), int(values["LUG"]), int(values["SAFETY"])]])
                userprediction = m.model.predict(inputgathered)
                userprediction = int(userprediction)
                sg.popup(f"Your car would be classified as {m.names[userprediction]}.")
            except:
                sg.popup("Invalid input. Please choose a value for each input.")

    window.close()



'''
firstinput = input("Hello, input your preferences.")
gatheredinp = firstinput.split(", ")
listofinput =  np.array([[int(gatheredinp[0]), int(gatheredinp[1]), int(gatheredinp[2]), int(gatheredinp[3]), int(gatheredinp[4]), int(gatheredinp[5])]])
predicted = model.predict(listofinput)
print(predicted)
if predicted == 2:
    print("Good")
'''