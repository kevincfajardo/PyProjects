import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit

class main_window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Calculadora")    
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        calc_field = QLineEdit()
        calc_field.setStyleSheet(btn_style + "font-size: 25px;")
        calc_field.setAlignment(Qt.AlignmentFlag.AlignRight)
        calc_field.setMinimumHeight(50)
        calc_field.setMinimumWidth(450)
        calc_field.setTextMargins(15, 15, 15, 15)
        self.main_layout.addWidget(calc_field)
        self.setStyleSheet(
                "background-color: black;"
            )
        


btn_style = "background-color: blue; color: white; border: 1px solid white; border-radius: 5px;"

app = QApplication(sys.argv)
main = main_window()

main.adjustSize()
main.setFixedSize(main.width(), main.height())
main.show()
app.exec()