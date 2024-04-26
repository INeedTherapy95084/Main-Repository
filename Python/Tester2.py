def create_coded_message(self, message, file_path=None, write=False):
        if file_path == None:
            # This means that you are not encrypting any file so then I will make a list of the message.
            word_list = list(message)
        else:
            # This means that you have provided a file path so I will read the file data as text.
            with open(file_path) as read_data:
                txt_data = read_data.read()
                word_list = list(txt_data)  # I made a list out of that text fron the file.
        coded_word = ""  # It's an empty string there I will store my encrypted word.
        for word in word_list:
            # Now I am iterating over the message.
            selected_key_word = choice(self.key_of_word[word]) # Then using the random module's choice function I am choosing a random character from the key_of_word. Let's say my word is "a". So, what I will do get the list of random characters for 'a' in the key dictionary 'a':['3', "#"]. So, ['3', "#"]  this is the list of random characters. From this list I will choose any character randomly and add it to the coded_word and after doing it for the entire message i will have a encrypted message. 
            coded_word += selected_key_word

        if write:
            # do you want to save the encrypted message in the file? If write is True then it will save the encrypted message in that file.
            with open(file_path, "w") as write_code:
                write_code.write(coded_word)
            print("Done")
        else:
            # Else it will return the encrypted message and you can print it.
            return coded_word