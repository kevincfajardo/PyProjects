from PySide6.QtCore import Slot # type: ignore

def decorator(*args, **kwargs):
    @Slot()
    def slot():
        calc_action(*args, **kwargs)
    return slot

@Slot()
def calc_action(field, oper, value):
    global left_op

    if value == "":
        return

    if value in "0123456789":
        if not field.cont_flag:
            field.setText("")

        field.insert(value)
        field.cont_flag = True
        return

    if value in ',.':
        if "." not in field.text():
            field.insert(".")  
        return
    
    if value in "+-x/^":
        if check_value(field.text(), field):
            field.insert(value)
            oper.setText(field.text())
            if value == "^":
                left_op = field.text().replace("^", "**")
            else:
                left_op = field.text().replace("x", "*")
            field.setText("")
        return
    
    if value == "E":
        try:
            if check_value(field.text(), field):
                resul = eval(left_op+field.text())
                oper.setText(oper.text() + field.text())
                field.setText(str(resul))
                field.cont_flag = False
                left_op = ""
        except (SyntaxError, NameError):
            field.setText("Erro: operação incompleta")
            field.cont_flag = False
            left_op = ""
        return

    if value == "Del":
        field.backspace()
        return

    if value == "Cl":
        field.setText("")
        left_op = ""
        field.cont_flag = True
        oper.setText("")
        return
    
    if value == "+/-":
        if check_value(field.text(), field):
            number = float(field.text()) * -1
            field.setText(str(number))
        return


@Slot()
def check_value(value, field):
    try:
        float(value)
        return True
    except ValueError:
        field.setText("Erro: suporta apenas numeros")
        field.cont_flag = False
        return False