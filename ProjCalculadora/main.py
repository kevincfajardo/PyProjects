import sys
from PySide6.QtWidgets import QApplication # type: ignore
from classes import main_window, calc_field, grid_btn

btn_style = "background-color: blue; color: white; border: 1px solid white; border-radius: 5px;"

app = QApplication(sys.argv)
main = main_window()

main.adjustSize()
main.setFixedSize(main.width(), main.height())

teste = grid_btn()
teste.btn_maker()

main.show()
app.exec()