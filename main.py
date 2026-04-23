import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QCheckBox,
                             QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout,
                             QLabel, QTableWidget, QTableWidgetItem, QMessageBox)
from password_generator import generate_password
from history_manager import add_to_history, load_history

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор случайных паролей')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        # Длина пароля
        self.length_label = QLabel('Длина: 12')
        self.length_slider = QSlider(1)
        self.length_slider.setMinimum(4)
        self.length_slider.setMaximum(32)
        self.length_slider.setValue(12)
        self.length_slider.valueChanged.connect(self.update_length_label)

        # Чекбоксы
        self.digits_checkbox = QCheckBox('Цифры')
        self.digits_checkbox.setChecked(True)
        self.letters_checkbox = QCheckBox('Буквы')
        self.letters_checkbox.setChecked(True)
        self.special_checkbox = QCheckBox('Спецсимволы')

        # Кнопка генерации
        self.generate_button = QPushButton('Сгенерировать')
        self.generate_button.clicked.connect(self.generate_and_show)

        # Поле для пароля
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)

        # Таблица истории
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(1)
        self.history_table.setHorizontalHeaderLabels(['История паролей'])

        # Добавление виджетов в layout
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_slider)
        layout.addWidget(self.digits_checkbox)
        layout.addWidget(self.letters_checkbox)
        layout.addWidget(self.special_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_display)
        layout.addWidget(self.history_table)

        self.setLayout(layout)

    def update_length_label(self):
        self.length_label.setText(f'Длина: {self.length_slider.value()}')

    def generate_and_show(self):
        length = self.length_slider.value()
        use_digits = self.digits_checkbox.isChecked()
        use_letters = self.letters_checkbox.isChecked()
        use_special = self.special_checkbox.isChecked()

        try:
            password = generate_password(length, use_digits, use_letters, use_special)
            self.password_display.setText(password)
            add_to_history(password)
            self.update_history_table()
            QMessageBox.information(self, 'Готово', 'Пароль сгенерирован и сохранён в историю!')
        except ValueError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))

    def update_history_table(self):
 
