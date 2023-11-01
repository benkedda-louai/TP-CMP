import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create input fields
        self.num1_label = QLabel('First number:')
        self.num1_input = QLineEdit()
        self.num2_label = QLabel('Second number:')
        self.num2_input = QLineEdit()

        # Create buttons
        self.add_button = QPushButton('Add')
        self.sub_button = QPushButton('Subtract')
        self.clear_button = QPushButton('Clear')

        # Create result label
        self.result_label = QLabel('Result:')

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_numbers)
        self.sub_button.clicked.connect(self.sub_numbers)
        self.clear_button.clicked.connect(self.clear_inputs)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 500) # Set window size

    def add_numbers(self):
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())
        result = num1 + num2
        self.result_label.setText(f'Result: {result}')

    def sub_numbers(self):
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())
        result = num1 - num2
        self.result_label.setText(f'Result: {result}')

    def clear_inputs(self):
        self.num1_input.clear()
        self.num2_input.clear()
        self.result_label.setText('Result:')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    def __init__(self):
        super().__init__()

        # Create input fields
        self.num1_label = QLabel('First number:')
        self.num1_input = QLineEdit()
        self.num2_label = QLabel('Second number:')
        self.num2_input = QLineEdit()

        # Create buttons
        self.add_button = QPushButton('Add')
        self.sub_button = QPushButton('Subtract')

        # Create result label
        self.result_label = QLabel('Result:')

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_numbers)
        self.sub_button.clicked.connect(self.sub_numbers)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 500) # Set window size

    def add_numbers(self):
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())
        result = num1 + num2
        self.result_label.setText(f'Result: {result}')

    def sub_numbers(self):
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())
        result = num1 - num2
        self.result_label.setText(f'Result: {result}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

    class MyWindow(QWidget):
        def __init__(self):
            super().__init__()

            # Create input fields
            self.num1_label = QLabel('First number:')
            self.num1_input = QLineEdit()
            self.num2_label = QLabel('Second number:')
            self.num2_input = QLineEdit()

            # Create buttons
            self.add_button = QPushButton('Add')
            self.sub_button = QPushButton('Subtract')

            # Create result label
            self.result_label = QLabel('Result:')

            # Connect buttons to functions
            self.add_button.clicked.connect(self.add_numbers)
            self.sub_button.clicked.connect(self.sub_numbers)

            # Create layout
            layout = QVBoxLayout()
            layout.addWidget(self.num1_label)
            layout.addWidget(self.num1_input)
            layout.addWidget(self.num2_label)
            layout.addWidget(self.num2_input)
            layout.addWidget(self.add_button)
            layout.addWidget(self.sub_button)
            layout.addWidget(self.result_label)

            self.setLayout(layout)
            self.setGeometry(100, 100, 500, 500) # Set window size

        def add_numbers(self):
            try:
                num1 = int(self.num1_input.text())
                num2 = int(self.num2_input.text())
                result = num1 + num2
                self.result_label.setText(f'Result: {result}')
            except ValueError:
                QMessageBox.warning(self, 'Warning', 'Please enter numbers only.')

        def sub_numbers(self):
            try:
                num1 = int(self.num1_input.text())
                num2 = int(self.num2_input.text())
                result = num1 - num2
                self.result_label.setText(f'Result: {result}')
            except ValueError:
                QMessageBox.warning(self, 'Warning', 'Please enter numbers only.')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyWindow()
        window.show()
        sys.exit(app.exec_())
