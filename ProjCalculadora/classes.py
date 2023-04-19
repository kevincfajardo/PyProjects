from PySide6.QtCore import Qt # type: ignore
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout # type: ignore

btn_style = "background-color: blue; color: white; border: 1px solid white; border-radius: 5px;"

class main_window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
  
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.field = calc_field()
        self.grid_layout =  grid_btn()

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.addWidget(self.field)
        self.main_layout.addLayout(self.grid_layout)
        

        self.setWindowTitle("Calculadora")  
        self.setStyleSheet(
                "background-color: black;"
            )
        

class calc_field(QLineEdit):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setStyleSheet(btn_style + "font-size: 25px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(50)
        self.setMinimumWidth(450)
        self.setTextMargins(15, 15, 15, 15)

class grid_btn(QGridLayout):
    def __init__(self, parent = None):
        super().__init__(parent)

    mask = [
        ["C", "D", "x²", "/"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", ","],
        ["(", "0", ")", "E"]
    ]

    def btn_maker(self):
        for c, row in enumerate(self.mask):
            for i, col in enumerate(row):
                btn = QPushButton(f"{col}")
                btn.setStyleSheet(btn_style)
                self.addWidget(btn, c, i)

'''
btn1 = QPushButton("btn2")
btn2 = QPushButton("btn3")
btn3 = QPushButton("btn1")
btn1.setStyleSheet(btn_style)
btn2.setStyleSheet(btn_style)
btn3.setStyleSheet(btn_style)
main.grid_layout.addWidget(btn1, 0, 1)
main.grid_layout.addWidget(btn2, 0, 2)
main.grid_layout.addWidget(btn3, 0, 3)
'''