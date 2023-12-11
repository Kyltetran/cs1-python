def count_word(filename_1, filename_2):
    '''Count the number of words in a text file and write it in another text file

       Parameters
       ----------
       'filename_1': name of the input text file to be read
       'filename_2': name of the output text file to be written

       Returns
       -------
       the function does not return value but its purpose is to write in another text file

    '''
    try:
        # Open the first file and read its content
        with open(filename_1, 'r') as in_file:
            text = in_file.read()
            word_count = len(text.split())
    except FileNotFoundError:
        # If the first does not exist, set word_count to 0
        word_count = 0

    # Write the word_count in the second file
    with open(filename_2, 'w') as out_file:
        out_file.write(str(word_count))
