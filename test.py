from PyQt5.QtWidgets import *
from PyQt5 import uic

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
        # msg = self.addHashtag(msg)
        self.textEdit_2.setText(msg)

    def remove_spaces(self, text):
        result = ''                # Initialize an empty string to store the text with spaces removed.
        prev_char = ''             # Initialize a variable to keep track of the previous character.
        space_or_newline = False   # Initialize a Boolean variable to track if the previous character was a space or newline.

        for char in text:
            if char != ' ' and char != '\n':  # If the current character is not a space or newline.
                result += char                 # Append the character to the result string.
                space_or_newline = False       # Reset the space_or_newline flag.

            elif not space_or_newline:  # If the current character is a space or newline and the previous character was not a space or newline.
                result += ' '            # Append a single space to the result string.
                space_or_newline = True  # Set the space_or_newline flag to True to indicate that a space has been added.

        return result  # Return the result string with consecutive spaces and newlines removed.

    def remove_comments(self,text):
        result = ''  # Initialize an empty string to store the text with comments removed.
        in_comment = False  # Initialize a flag to track whether we are inside a comment.
        last_char = ''
        if(self.count_percent(text) == 1) :
            return text
        else :
            for char in text:
                if char == '%' and not in_comment:
                    in_comment = True  # Start a comment block when '%' is encountered and we are not already in a comment.
                elif char == '%' and in_comment:
                    in_comment = False  # End the comment block when '%' is encountered and we are already in a comment.
                elif not in_comment:
                    last_char = char
                if not in_comment:
                    result += last_char  # Add the last character to the result if we are not in a comment.

            return result  # Return the result string with comments removed.



    def count_percent(self, text):
        count = 0  # Initialize a counter to keep track of the number of '%' characters.

        for char in text:
            if char == '%':  # If the current character is '%',
                count += 1   # increment the count by 1.

        return count  # Return the total count of '%' characters in the text.

    # def addHashtag(self, text):
        

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()

    #todo => replace any length of space with on space 
    #todo => %anyThings% this is a comment

