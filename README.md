# python-file-handling

Recently, I've been learning how to handle files using Python. I started with YouTube videos and am now moving away from the handle-holding these videos provided. In this repository you will find what I'm able to do with what I've learned so far. Granted this is probably still beginner stuff, but I'm proud of how far I've come and want to share it.

## Functions that I've created in this program

### read_data(size)
 - allows for the ability to print the contents of a file a certain
 - data size at a time

### append_data(file_path)
 - Continually appends data to a file
 - Once a string of length 0 is inputted, the loop breaks and no more data is appended

### clear_data(file_path) 
 - Erases all data from a file
 - Uses the truncate method to do so

### create_file(file_path) 
 - Simply creates a file, nothing special

### find_text(text) 
 - THE MAGNUM OPUS
 - This function searches through every text file in the directory and finds every instance of text provided and then neatly displays it showing the file it 
   was found in, the line and the instance it was used 
