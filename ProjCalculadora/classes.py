from PySide6.QtCore import Qt, Signal  # type: ignore
from PySide6.QtGui import QKeyEvent # type: ignore
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel # type: ignore
from func import decorator, calc_action

main_style = "background-color: #140f07; color: #3dfff9;  border: 1px solid; border-radius: 5px;"

class main_window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
  
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.operation = oper_label()
        self.field = calc_field()
        self.grid_layout = grid_btn(self.field, self.operation)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.addWidget(self.operation)
        self.main_layout.addWidget(self.field)
        self.main_layout.addLayout(self.grid_layout)
        

        self.setWindowTitle("Calculadora")
        self.setStyleSheet("background-color: #102841;")
        

class oper_label(QLabel):

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

        self.setStyleSheet(main_style + "font-size: 14px; border-color: #125051; color: #17a19a;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setContentsMargins(3, 3, 3, 3)


class calc_field(QLineEdit):
    btn_enter = Signal()
    btn_del = Signal()
    btn_cl = Signal()
    btn_op = Signal(str)
    
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

        self.setStyleSheet(main_style + "font-size: 25px; border-color: #28aeff;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(50)
        self.setMinimumWidth(450)
        self.setTextMargins(10, 10, 10, 10)

        self.cont_flag = True    
    
    def keyPressEvent(self, event: QKeyEvent):
        key_txt = event.text()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_del = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_cl = key in [KEYS.Key_Escape, KEYS.Key_C]

        if is_enter:
            self.btn_enter.emit()
            return event.ignore()
        
        if is_del:
            self.btn_del.emit()
            return event.ignore()
        
        if is_cl:
            self.btn_cl.emit()
            return event.ignore()

        self.btn_op.emit(key_txt)


class grid_btn(QGridLayout):
    def __init__(self, field, oper, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.btn_maker(field, oper)

    mask = [
        ["Cl", "Del", "^", "/"],
        [7, 8, 9, "x"],
        [4, 5, 6, "-"],
        [1, 2, 3, "+"],
        ["+/-", 0, ",", "E"]
    ]
    
    def btn_maker(self, field, oper):
        args = field, oper

        def num_conn(value):
            calc_action(*args, value)

        field.btn_enter.connect(decorator(*args, "E"))
        field.btn_del.connect(decorator(*args, "Del"))
        field.btn_cl.connect(decorator(*args, "Cl"))
        field.btn_op.connect(num_conn)

        for c, row in enumerate(self.mask):
            for i, col in enumerate(row):
                btn_txt = f"{col}"
                btn = QPushButton(btn_txt)

                if btn_txt in "0123456789":
                    btn.setStyleSheet(main_style + "height: 65; border-color: #28aeff; ")
                else:
                    btn.setStyleSheet(main_style + "height: 65; border-color: #3dfff9; ")
                
                btn.clicked.connect(decorator(*args, btn_txt))
                self.addWidget(btn, c, i)
