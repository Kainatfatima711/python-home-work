class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Split the text into words
        words = self.text.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join them back into a string
        return ' '.join(reversed_words)


# Example usage
if __name__ == "__main__":
    input_string = "Hello world from Python"
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse_words()
    print("Original:", input_string)
    print("Reversed:", reversed_string)
    