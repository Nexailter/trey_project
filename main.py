import PySimpleGUI as pg

layout =[[pg.Text("Trey is..."),pg.InputText()],
         [pg.Button("Done"),pg.Button("Close"),pg.InputText()]]

window = pg.Window("Trey's First GUI",layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == "Close" :
        break
    if event == "Done":
        # values is a list of user inputs
        pg.popup("Trey is " + values[0])


window.close()

