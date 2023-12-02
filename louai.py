class DFA:
    def __init__(self):
        self.matrix = [
            [1, 4, -5, 9, 5, 6, 18, 13, 15, 16],#0
            [1, 1, 2, -5, -5, -5, -5, -5, -5, -5],#1
            [1, 1, 3, -5, -5, -5, -5, -5, -5, -5],#2
            [2, -5, -5, -5, -5, -5, -5, -5, -5, -5],#3
            [-5, 4, -5, 7, -5, -5, -5, -5, -5, -5],#4
            [-5, 4, -5, 9, 17, -5, -5, -5, -5, -5],#5
            [-5, 4, -5, 9, -5, 12, -5, -5, -5, -5],#6
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],#7
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],#8
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],#9
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],#12
            [-5, -5, -5, -5, -5, -5, -5, 14, -5, -5],#13
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],#14
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],#15
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],#16
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],#17
            [-5, -5, -5, -5, -5, -5, -5, 4, -5, -5],#18
        ]
        self.start_state = 0
        self.final_states = [1, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19]  # Added 19 for '#'

    def recognize(self, input_str):
        words = input_str.split('#')
        overall_type = []  # List to store the type of each word

        for word in words:
            if not self.process_word(word):
                print(f'The word "{word}" is not accepted by the DFA.')
                return False
            word_type = self.get_word_type(word)
            overall_type.extend(word_type)

        # If there's only one word, print its type directly
        if len(overall_type) == 1:
            print(f'The entire text is of type: {overall_type[0]}')
        else:
            print(f'The entire text is of type: {", ".join(overall_type)}')

        return True

    def process_word(self, word):
        current_state = self.start_state
        word_type = []  # List to store the type of each character

        for char in word:
            char_index = self.get_char_index(char)
            if char_index == -1:
                print(f'Invalid character "{char}", reject the word')
                return False

            current_state = self.matrix[current_state][char_index]
            if current_state == -5:
                print(f'The Transition was not found for {word}')
                return False

            # Determine the type of the character and add it to the list
            char_type = self.get_char_type(char_index)
            word_type.append(char_type)

        # Check if the final state is reached
        if current_state not in self.final_states:
            print(f'The word "{word}" does not end in a final state')
            return False

        return True

    def get_word_type(self, word):
        # Helper function to get the type of each character in a word
        word_type = []
        for char in word:
            char_index = self.get_char_index(char)
            char_type = self.get_char_type(char_index)
            word_type.append(char_type)

        # If there's only one character in the word, return its type directly
        if len(word_type) == 1:
            return word_type[0]
        else:
            return word_type

    def get_char_type(self, char_index):
        # Helper function to get the type of a character based on its column index
        char_types = ['Letter', 'Digit', 'Underscore', 'Period', 'Minus', 'Plus', 'Colon', 'Equal', 'Operator', 'Separator']
        return char_types[char_index]

    def get_char_index(self, char):
        # Helper function to get the column index for a character in the matrix
        char_categories = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '_', '.', '-', '+', ':', '=', '*/', ';(),']
        for i, category in enumerate(char_categories):
            if char in category:
                return i
        return -1

# Example usage:
dfa = DFA()
input_string = input("enter a text : ")
result = dfa.recognize(input_string)