from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
import sys

class MyWindow(QMainWindow):
    def init(self):
        super(MyWindow, self).init()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Comment Remover')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        self.output_text = QTextEdit()
        layout.addWidget(self.output_text)

        self.remove_comments_button = QPushButton('Remove Comments')
        self.remove_comments_button.clicked.connect(self.remove_comments)
        layout.addWidget(self.remove_comments_button)

        self.central_widget.setLayout(layout)

    def remove_comments(self):
        input_text = self.input_text.toPlainText()

        inside_comment = False
        result = ''

        for c in input_text:
            if c == '%':
                inside_comment = not inside_comment
            elif not inside_comment:
                result += c

        if inside_comment:
            self.output_text.setPlainText("error: Close the comments please !")
            return

        output_text = result
        result = ''
        i = 0

        while i < len(output_text):
            c = output_text[i]

            if c != ' ' and c not in '()[];:.-+*/=':
                if c == '+':
                    result += '+'
                    if i + 1 < len(output_text) and output_text[i + 1] == '+':
                        result += '+'
                        result += '#'
                        i += 1
                elif c == '<' or c == '>':
                    if output_text[i - 1] != '#':
                        result += '#'
                    result += c
                    if i + 1 < len(output_text) and output_text[i + 1] == '=':
                        result += '='
                        result += '#'
                        i += 1
                    else:
                        result += '#'
                else:
                    if c != ' ':
                        result += c
            else:
                if c != ' ':
                    result += '#'
                    result += c
                    result += '#'
                else:
                    result += '#'
            i += 1

        self.output_text.setPlainText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())