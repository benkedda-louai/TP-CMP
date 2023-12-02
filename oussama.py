class WordRecognizer:
    def __init__(self):
        self.aoutmatio_matrix = [
            [1, 4, -5, 9, 5, 6, 18, 13, 15, 16],  # 0
            [1, 1, 2, -5, -5, -5, -5, -5, -5, -5],  # 1
            [1, 1, 3, -5, -5, -5, -5, -5, -5, -5],  # 2
            [2, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 3
            [-5, 4, -5, 7, -5, -5, -5, -5, -5, -5],  # 4
            [-5, 4, -5, 9, 17, -5, -5, -5, -5, -5],  # 5
            [-5, 4, -5, 9, -5, 12, -5, -5, -5, -5],  # 6
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],  # 7
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],  # 8
            [-5, 8, -5, -5, -5, -5, -5, -5, -5, -5],  # 9
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 12
            [-5, -5, -5, -5, -5, -5, -5, 14, -5, -5],  # 13
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 14
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 15
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 16
            [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],  # 17
            [-5, -5, -5, -5, -5, -5, -5, 4, -5, -5],   # 18
        ]
        self.start_state = 0
        self.final_states = [1, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19]  # Added 19 for '#'

    def recognize_word(self, word):
        current_state = self.start_state

        for symbol in word:
            char_index = self.type_char(symbol)
            if char_index == -1:
                print(f'Invalid character "{symbol}", reject the word')
                return False

            current_state = self.aoutmatio_matrix[current_state][char_index]
            if current_state == -5:
                print(f'The Transition was not found for {word}')
                return False

        # Check if the final state is reached
        if current_state not in self.final_states:
            print(f'The word "{word}" does not end in a final state')
            return False

        return True

    def type_char(self, ch):
        nmb = "0123456789"
        big_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small_l = "abcdefghijklmnopqrstuvwxyz"
        special_chars = ",();{}[]\""
        if ch in nmb:
            return 0
        elif ch == '.':
            return 1
        elif ch == '-':
            return 2
        elif ch == '+':
            return 3
        elif ch in big_l + small_l:
            return 4
        elif ch == '_':
            return 5
        elif ch in "*/":
            return 6
        elif ch == ':':
            return 7
        elif ch == '=':
            return 8
        elif ch in special_chars:
            return 9
        elif ch in "<>!":
            return 10
        else:
            return -1


# Example usage:
word_recognizer = WordRecognizer()
input_string = input("Enter a text: ")
words = input_string.split('#')

for word in words:
    if not word_recognizer.recognize_word(word):
        print(f'The word "{word}" is not accepted by the DFA.')
        break
else:
    print('All words are accepted by the DFA.')