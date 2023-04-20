import sys
from PySide6.QtWidgets import QApplication # type: ignore
from classes import main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = main_window()

    main.adjustSize()
    main.setFixedSize(main.width(), main.height())

    main.show()
    app.exec()