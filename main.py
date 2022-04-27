import PySimpleGUI as pg

layout =[[pg.Text("pick a class..."),pg.InputText()],
        [pg.Text("pick an element..."),pg.InputText()],
        [pg.Text('pick a username...'),pg.InputText()],
        [pg.Button('if you leave u a bozo'),pg.Button('continue through the stages of hell')]]
        

window = pg.Window("This is literal hell",layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == 'if you leave u a bozo' :
        break
    if event == 'continue through the stages of hell':
        # values is a list of user inputs
        pg.popup("your class is " + values[0] + '\n' + "your element is " + values[1] +'\n' + "your username is " + values[2])


window.close()

