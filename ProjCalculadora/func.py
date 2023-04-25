from PySide6.QtCore import Slot # type: ignore

def decorator(func, *args):
    @Slot(bool)
    def slot():
        func(*args)
    return slot

def insert_txt(btn, field, oper):
    global left_op
    value = btn.text()

    if value in "0123456789":
        if not field.cont_flag:
            field.setText("")

        field.insert(value)
        field.cont_flag = True

    if value == ',':
        if "." not in field.text():
            field.insert(".")  
    
    if value in "+-x/":
        if check_value(field.text(), field):
            field.insert(value)
            oper.setText(field.text())
            left_op = field.text().replace("x", "*")
            field.setText("")
    
    if value.lower() == "e":
        try:
            if check_value(field.text(), field):
                operation = left_op+field.text()
                resul = eval(operation)
                oper.setText(operation)
                field.setText(str(resul))
                field.cont_flag = False
        except (SyntaxError, NameError):
            field.setText("Erro: operação incompleta")
            field.cont_flag = False

    if value == "Del":
        field.backspace()

    if value == "Cl":
        field.setText("")
        left_op = ""
        field.cont_flag = True
    
    if value == "+/-":
        if check_value(field.text(), field):
            number = float(field.text()) * -1
            field.setText(str(number))


def check_value(value, field):
    try:
        float(value)
        return True
    except ValueError:
        field.setText("Erro: suporta apenas numeros")
        field.cont_flag = False
        return False