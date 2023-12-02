from PyQt5.QtWidgets import *
from PyQt5 import uic
#main class
class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("newWindow.ui", self)
        self.show()
        self.pushButton.clicked.connect(lambda: self.sayIt(self.textEdit.toPlainText()))
        # Access the menu created in PyQt5 Designer
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')

        # Create 'Open' action
        self.open_action = QAction('Open', self)
        self.open_action.triggered.connect(self.openFile)
        self.fileMenu.addAction(self.open_action)

        # Create 'Save' action
        self.save_action = QAction('Save', self)
        self.save_action.triggered.connect(self.saveFile)
        self.fileMenu.addAction(self.save_action)

        # Create 'Exit' action
        self.exit_action = QAction('Exit', self)
        self.exit_action.triggered.connect(self.close)
        self.fileMenu.addAction(self.exit_action)


    def openFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
                self.textEdit.setPlainText(text)

    def saveFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            text = self.textEdit.toPlainText()
            with open(file_name, 'w') as file:
                file.write(text)
                
    def sayIt(self, msg):
        msg = self.remove_comments(msg)
        msg = self.remove_spaces(msg)
        msg = self.add_hash(msg)
        msg = self.check_keywords(msg)[1]
        self.textEdit_2.setText(msg)

    def remove_spaces(self, text):
        result = ''
        space_or_newline = False

        for char in text:
            if char != ' ' and char != '\n':
                result += char 
                space_or_newline = False

            elif not space_or_newline:
                result += ' '
                space_or_newline = True 

        return result

    def remove_comments(self,input_str):
        start_idx = self.find_first_percent(input_str)
        if start_idx == -1:
            return input_str
        end_idx = self.find_closing_percent(input_str, start_idx)
        if end_idx == -1:
            return input_str
        result_str = input_str[:start_idx] + input_str[end_idx + 1:]
        return result_str

    def find_first_percent(self,input_str):
        for i, char in enumerate(input_str):
            if char == '%':
                return i
        return -1

    def find_closing_percent(self,input_str, start_idx):
        for i in range(start_idx + 1, len(input_str)):
            if input_str[i] == '%':
                return i
        return -1
    
    def add_hash(self,text):
        operators = '/*='
        separators = ';[]()'
        output_string = ""
        i = 0
        while i < self.length(text):
            char = text[i]
            # if the current char is in the array of operators
            if char in operators or char in separators :
                output_string+='#'+char+'#'
            # if the current char equal to + we enter in a condition
            elif char == '+':
                if i + 2 < self.length(text) and text[i-1] != '+' and self.is_number(text[i+1]):
                    output_string += '#'+char
                    # i+=1
                    while i < self.length(text) and self.is_number(text[i]):
                        output_string += text[i]
                        i+=1
                    # output_string += '#'
                elif text[i+1] == '+' and text[i+2] == '+':
                    output_string += '#'+char+text[i+1]+'#'
                    i+=1
                elif i + 2 < self.length(text) and text[i+1] == '+' or text[i+1] == '-' and self.is_number(text[i+2]):
                    output_string += '#'+char+'#'+text[i+1]
                    i+=2
                    while i < self.length(text) and self.is_number(text[i]):
                        output_string += text[i]
                        i+=1
                    output_string += '#'
                else :
                    output_string+='#'+char+'#'
            # if the current char equal to - we enter in a condition
            elif char == '-':
                if i + 2 < self.length(text) and text[i-1] != '-' and self.is_number(text[i+1]) :
                    output_string += '#'+char
                    # i+=1
                    while i < self.length(text) and self.is_number(text[i]) :
                        output_string += text[i]
                        i+=1
                elif text[i+1] == '-' and text[i+2] == '-':
                    output_string += '#'+char+text[i+1]+'#'
                    i+=1
                elif i + 2 < self.length(text) and text[i+1] == '-' or text[i+1] == '+' and self.is_number(text[i+2]):
                    output_string += '#'+char+'#'+text[i+1]
                    i+=2
                    while i < self.length(text) and self.is_number(text[i]):
                        output_string += text[i]
                        i+=1
                    output_string += '#'
                else :
                    output_string+='#'+char+'#'
            elif i < self.length(text) and char == '=' :
                if text[i+1] == '=' :
                    output_string += '#'+char+text[i+1]+'#'
                    i+=1
                else :
                    output_string += '#'+char+'#'
            elif char == ':' or char == '>' or char == '<' or char == '!' or char == '=' and i < self.length(text) - 1 and text[i+1] == '=':
                output_string +=  '#'+char+'=#'
                i+=1
            else :
                output_string+=char
            i += 1
        return output_string+'#'
    
    def is_number(self,text) :
        return '0' <= text <= '9' or text == '.'

    def length(self,text) :
        count = 0
        for char in text:
            if char != '':
                count+=1
        return count
    
    def replace_string(self,original, to_replace, replacement):
        result = ''
        i = 0
        while i < len(original):
            if original[i:i+len(to_replace)] == to_replace:
                result += replacement
                i += self.length(to_replace)
            else:
                result += original[i]
                i += 1
        return result
    
    def check_keywords(self,text):
        keywordsUpper = ['INT', 'REAL', 'STRING', 'CHAR', 'BOOLEAN','FIN','FOR']
        keywordsLower = ['int', 'real', 'string', 'char', 'boolean','fin','for']
        for keyword in keywordsUpper and keywordsLower:
            if keyword in text:
                text = self.replace_string(text, keyword,keyword+'#')
                return True, text
            else:
                return False, text
#automate class
def main() :
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()