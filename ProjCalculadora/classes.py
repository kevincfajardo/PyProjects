from PySide6.QtCore import Qt # type: ignore
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout # type: ignore
from func import decorator, insert_txt

main_style = "background-color: #140f07; color: #3dfff9;  border: 1px solid; border-radius: 5px;"

class main_window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
  
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.field = calc_field()
        self.grid_layout = grid_btn(self.field)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.addWidget(self.field)
        self.main_layout.addLayout(self.grid_layout)
        

        self.setWindowTitle("Calculadora")
        self.setStyleSheet("background-color: #102841;")
        


class calc_field(QLineEdit):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

        self.setStyleSheet(main_style + "font-size: 25px; border-color: #28aeff;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(50)
        self.setMinimumWidth(450)
        self.setTextMargins(10, 10, 10, 10)



class grid_btn(QGridLayout):
    def __init__(self, field, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.btn_maker(field)

    mask = [
        ["C", "D", "x²", "/"],
        ["7", "8", "9", "x"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ",", "E"]
    ]

    def btn_maker(self, field):
        for c, row in enumerate(self.mask):
            for i, col in enumerate(row):
                btn_txt = f"{col}"
                btn = QPushButton(btn_txt)
                btn.setProperty('cssClass', 'specialButton')

                if btn_txt in "0123456789":
                    btn.setStyleSheet(main_style + "height: 65; border-color: #28aeff; ")
                else:
                    btn.setStyleSheet(main_style + "height: 65; border-color: #3dfff9; ")
                
                btn.clicked.connect(decorator(insert_txt, btn, field))
                self.addWidget(btn, c, i)
