from random import shuffle

class DataProcessor:
    """This class is responsible for processing the data in the text file"""

    def __init__(self, input_file, output_file, arrangement="shuffled"):
        self.process_words = []
        self.input_file = input_file
        self.output_file = output_file
        self.arrangement = arrangement


    def process_data(self):
        """Read the text file and return a list of unique tokens"""
        list_of_tokens = []

        # Open text file name and read the content with unicode content
        with open(self.input_file, "r", encoding="utf-8") as file:
            [content1, content2] = file.read().split('*')

            # Split the content into tokens and append to list_of_tokens
            for word in content1.split(' '):
                if word.strip() != '':
                    list_of_tokens.append(word.strip())
            
            tokens = [token.split('\n') for token in content2.split("' '")]
            for token in tokens:
                for word in token:
                    if word.strip() != '':
                        list_of_tokens.append(word.strip())

        unique_words = list(set(list_of_tokens))
        
        if self.arrangement == "shuffled":
            shuffle(unique_words)
        elif self.arrangement == "sorted":
            unique_words.sort()
        
        self.process_words = unique_words
        return unique_words


    def write_to_file(self):
        """Write the shuffled list of tokens to a new text file
           with each token separated by a new line"""

        with open(self.output_file, "w", encoding="utf-8") as file:
            for word in self.process_words:
                file.write(word + '\n')


if __name__ == "__main__":
    processor = DataProcessor("unprocessed_data.txt", "processed_data.txt", "shuffled")
    processor.process_data()
    processor.write_to_file()

