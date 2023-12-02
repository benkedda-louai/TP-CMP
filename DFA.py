class DFA:
    def __init__(self):
        self.matrix = [
                [1,4,-5,9,5,6,18,13,15,16],
                [1,1,2,-5,-5,-5,-5,-5,-5,-5],
                [1,1,3,-5,-5,-5,-5,-5,-5,-5],
                [2,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,4,-5,7,-5,-5,-5,-5,-5,-5],
                [-5,4,-5,9,17,-5,-5,-5,-5,-5],
                [-5,4,-5,9,-5,12,-5,-5,-5,-5],
                [-5,8,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,8,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,8,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,14,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
                [-5,-5,-5,-5,-5,-5,-5,4,-5,-5],
        ]
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.start_state = 0
        self.final_states = [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18]

    def run_dfa(self, input_string):
        current_state = self.start_state
        for char in input_string:
            if char not in self.alphabet:
                print(f"Invalid input symbol: {char}")
                return False
            input_index = self.alphabet.index(char) if char in self.alphabet else -1
            if input_index == -1:
                print(f"Invalid input symbol: {char}")
                return False
            try:
                current_state = self.matrix[current_state][input_index]
            except IndexError:
                print(f"Index out of range for input symbol: {char}")
                return False
            if current_state == -5:
                print(f"No transition for input symbol: {char}")
                return False

        return self.is_accepting_state(current_state)

    def is_accepting_state(self, state):
        return state in self.final_states


# Example usage:
dfa = DFA()
input_string = "abcd"
result = dfa.run_dfa(input_string)
print(f"the string {input_string}, accepted? {result}")