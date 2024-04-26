def create_decoded_message(self, file_path, message=None, write=False):
    if file_path == None:
        # Again if it's none that means you have not provided any file path so then it makes a list out of the message.
        coded_list = list(message)
    else:
        # Else it will get the message from the file and then make a list out of that text.
        with open(file_path, "r") as read_data:
            txt_data = read_data.read()
            coded_list = list(txt_data)
    decoded_word = ""
    for coded_word in coded_list:
        # So, I am iterating over the encrypted message. Then I am iterating over the key of my key_dictionary.
        for word in list(self.key_of_word):
            if coded_word in self.key_of_word[word]:
                decoded_word += word

    if write:
        # Again if write is true then save the decrypted message.
        with open(file_path, "w") as write_data:
            write_data.write(decoded_word)
        print("DONE Saved")
    else:
        # Else print the decrypted word.
        print(decoded_word, "\n!Decoded Word!")


