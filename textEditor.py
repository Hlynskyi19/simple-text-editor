import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QAction,
    QFileDialog,
    QMessageBox,
    QToolBar,
    QStatusBar,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовий редактор")
        self.setGeometry(100, 100, 800, 600)

        # Головне текстове поле
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Виклик функцій створення меню, панелі інструментів і статусного рядка
        self.create_menu()
        self.create_toolbar()
        self.create_status_bar()

        self.current_file = ""

    def create_menu(self):
        menu_bar = self.menuBar()

        # Меню "Файл"
        file_menu = menu_bar.addMenu("Файл")

        new_action = QAction("Новий", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Відкрити", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Зберегти", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        file_menu.addSeparator()
        exit_action = QAction("Вийти", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Меню "Редагування"
        edit_menu = menu_bar.addMenu("Редагування")

        cut_action = QAction("Вирізати", self)
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Копіювати", self)
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Вставити", self)
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)

        # Меню "Допомога"
        help_menu = menu_bar.addMenu("Допомога")

        about_action = QAction("Про програму", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_toolbar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        new_action = QAction("Новий", self)
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        open_action = QAction("Відкрити", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        save_action = QAction("Зберегти", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

    def create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Готово")

    def new_file(self):
        self.text_edit.clear()
        self.current_file = ""
        self.status_bar.showMessage("Створено новий файл")

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Відкрити файл", "", "Текстові файли (*.txt);;Всі файли (*)"
        )

        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    self.text_edit.setText(file.read())
                self.current_file = file_name
                self.status_bar.showMessage(f"Відкрито: {file_name}")
            except Exception as e:
                QMessageBox.critical(
                    self, "Помилка", f"Не вдалося відкрити файл: {str(e)}"
                )

    def save_file(self):
        if not self.current_file:
            self.current_file, _ = QFileDialog.getSaveFileName(
                self, "Зберегти файл", "", "Текстові файли (*.txt);;Всі файли (*)"
            )

        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.text_edit.toPlainText())
                self.status_bar.showMessage(f"Файл збережено: {self.current_file}")
            except Exception as e:
                QMessageBox.critical(
                    self, "Помилка!", f"Не вдалося зберегти файл: {str(e)}"
                )

    def show_about(self):
        QMessageBox.information(
            self, "Про програму", "Простий текстовий редактор на PyQt5"
        )


def main():
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
