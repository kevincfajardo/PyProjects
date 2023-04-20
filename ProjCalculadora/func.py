from PySide6.QtCore import Slot # type: ignore

def decorator(func, *args):
    @Slot(bool)
    def slot():
        func(*args)
    return slot

def insert_txt(btn, field):
    value = btn.text()
    leftOp = ""

    if value in "0123456789":
        field.insert(btn.text())

    if value == ',':
        field.insert(".")
    
    if value in "+-x/":
        leftOp = field.text()
        field.setText("")
        print(leftOp)
    
    if value == "E":
        ...