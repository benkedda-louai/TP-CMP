from PyQt5.QtWidgets import *
from ui_file import Ui_MainWindow
class DFA:
    def __init__(self):
        self.matrix = [
            [1,4,-5,9,5,6,14,13,16,11,11],#0
            [1,1,2,-5,-5,-5,-5,-5,-5,-5,-5],#1
            [1,1,3,-5,-5,-5,-5,-5,-5,-5,-5],#2
            [-5,-5,2,-5,-5,-5,-5,-5,-5,-5,-5],#3
            [-5,4,-5,7,-5,-5,-5,-5,-5,-5,-5],#4
            [-5,4,-5,-5,15,-5,-5,-5,-5,-5,-5],#5
            [-5,4,-5,9,-5,10,-5,-5,-5,-5,-5],#6
            [-5,8,-5,-5,-5,-5,-5,-5,-5,-5,-5],#7
            [-5,8,-5,-5,-5,-5,-5,-5,-5,-5,-5],#8
            [-5,8,-5,-5,-5,-5,-5,-5,-5,-5,-5],#9
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],#10
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,12,-5],#11
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],#12
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],#13
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],#14
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],#15
            [-5,-5,-5,-5,-5,-5,-5,-5,-5,12,-5],#16
        ]
        self.start_state = 0
        self.final_states = [1,4,5,6,7,8,10,11,12,13,14,15,16]
        self.final_state_types = {
            1: "Identifier",
            4: "integer",
            5: "operation",
            6: "operation",
            7: "float",
            8: "float",
            10: "increment",
            11: "separator",
            12: "comparator",
            13: "operator",
            14: "separator",
            15: "decrement",
            16: "operator",
        }

    def recognize(self, input_str):
        words = input_str.split('#')
        for word in words:
            result, word_type = self.process_word(word)
            if not result:
                print(f'The word "{word}" is not accepted by the automate.')
                return [False, result]
            else:
                print(f'The word "{word}" is accepted by the automate. Type of {word} is: {word_type}')
                if word_type == "Identifier" and len(word) <= 6:
                    print(f'{word} is a valid identifier.')
                elif word_type == "integer" and int(word) <= 7:
                    print(f'{word} is a valid integer.')
                else:
                    return [False, result]
        return [True,word_type]

    def process_word(self, word):
        current_state = self.start_state
        word_type = None

        for char in word:
            char_index = self.get_char_index(char)
            if char_index == -1:
                print(f'Invalid character "{char}", reject the word')
                return False, None

            current_state = self.matrix[current_state][char_index]
            if current_state == -5:
                print(f'The Transition was not found for {word}')
                return False, None
        if current_state not in self.final_states:
            print(f'The word "{word}" does not end in a final state')
            return False, None
        word_type = self.final_state_types.get(current_state)
        return True, word_type

    def get_char_index(self, char):
        char_categories = [
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            '0123456789', '_', '.', '-', '+', ';,()', '*/', ':', '=', '<>!'
        ]
        for i, category in enumerate(char_categories):
            if char in category:
                return i
        return -1
    
    
class MyGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(lambda: self.sayIt(self.textEdit.toPlainText()))
        self.pushButton_2.clicked.connect(self.getTextEditValue)
        
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')

        self.open_action = QAction('Open', self)
        self.open_action.triggered.connect(self.openFile)
        self.fileMenu.addAction(self.open_action)


        self.save_action = QAction('Save', self)
        self.save_action.triggered.connect(self.saveFile)
        self.fileMenu.addAction(self.save_action)


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
        
    def getTextEditValue(self):
        text = self.textEdit_2.toPlainText()
        dfa = DFA()
        
        words = text.split('#')
        
        results = []
        for word in words:

            if word.strip() == '':
                continue
            
            result, word_type = dfa.recognize(word)
            
            if result:
                results.append(f'The word "{word}" is accepted by the automate. Type of {word} is: {word_type}')
            else:
                results.append(f'The word "{word}" is not accepted by the automate.')

        self.textEdit_2.setPlainText('\n'.join(results))

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

    def remove_comments(self,text):
        result = []
        f = []
        comment = False
        tab = list(text)
        for i in range(len(text)):
            c = tab[i]
            if c == '%':
                if comment:
                    comment = False
                else:
                    comment = True
                    f = []
            if comment:
                f.append(c)
            else:
                if c == ' ' or c == '\n':
                    result.append(' ')
                else :
                    if c != '%' :
                        result.append(c)
        if comment:
            result.extend(f)

        return ''.join(result)
    
    def add_hash(self,text):
        operators = '/*'
        separators = ';[](),'
        output_string = ""
        i = 0
        while i < self.length(text):
            char = text[i]
            
            if char in operators or char in separators :
                output_string+='#'+char+'#'
            elif char == '+':
                if i + 2 < self.length(text) and text[i-1] != '+' and self.is_number(text[i+1]):
                    output_string += '#'+char+'#'
                    while i < self.length(text) and self.is_number(text[i]):
                        output_string += text[i]
                        i+=1
                elif text[i+1] == '+' and text[i+2] == '+':
                    output_string += '#'+char+text[i+1]+'#'
                    i+=1
                elif not text[i].isdigit() and text[i+1] == '+' and text[i+2] == '+' :
                    output_string+= '#'+text[i+1]+text[i+2]+'#'
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
            elif char == '-':
                if i + 2 < self.length(text) and text[i-1] != '-' and self.is_number(text[i+1]) :
                    output_string += '#'+char+'#'
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
            elif char == ':' or char == '>' or char == '<' or char == '!' or char == '=' :
                if text[i+1] == '=' :
                    output_string += '#'+char+text[i+1]+'#'
                    i+=1
                else :
                    output_string +=  '#'+char+'#'
            elif char == ' ':
                output_string+='#'
            else :
                output_string+=char
            i += 1
        return output_string
    
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
        keywordsUpper = ['INT', 'REAL', 'STRING', 'CHAR', 'BOOLEAN','FIN','FOR','IF','ELSE']
        keywordsLower = ['int', 'real', 'string', 'char', 'boolean','fin','for','if','else']
        for keyword in keywordsUpper and keywordsLower:
            if keyword in text:
                text = self.replace_string(text, keyword,keyword+'')
                return True, text
            else:
                return False, text

def main() :
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()