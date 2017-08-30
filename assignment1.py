"""
Replace the contents of this module docstring with your own details.
"""
#   TODO: What he said
#   TODO: Set up github for this project


def main():
    MENU = """Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit"""
    SONG_FILE_NAME = "songs.csv"
    TEMP_FILE_NAME = "temp.csv"
    keep_going = True
#    song_file = open(SONG_FILE_NAME, "r")
#    temp_file = open(TEMP_FILE_NAME, "a")
    print("Songs To Learn 1.0 - by James Kastner")
    while keep_going:
        print(MENU)
        action = input(">>> ")
        #   TODO: send to get_valid_string function instead
        if action.lower == 'l' or 'list' or '1' or 'list songs':
            display_song_list(SONG_FILE_NAME)
        elif action == 'a':
            add_a_song()
        elif action == 'c':
            complete_a_song()
        elif action == 'q':
            keep_going = False
#            song_file.close()
#            temp_file.close()
        else:
            print("Invalid Input")

"""
define function named load_songs()
    TEMP_FILE_NAME = temp.csv
    SONG_FILE_NAME = songs.csv
    song_file = open songs.csv as read only
    temp_file = open temp.csv as write only
    write song_file to temp_file
    return song_file, temp_file
"""


def load_songs():
    """
    Loads the files containing the information on the songs and the temporary back up.
    :return: file and file
    """


"""
define function get_valid_string():
    
"""
#   TODO: Pseudocode for this function


def get_valid_string(prompt):
    """
    This function will get an input from the user and make sure that it is a string type.
    :return: str
    """

"""
define function get_valid_integer() with parameter prompt
    is_valid = False
    while is_valid = False
        try to execute the code
            display prompt to the user
            number = get input from the user
            convert number into integer type
            is_valid = True
        if a Value Error occurs, execute
            display "Invalid Input, please enter a number"
    return number
"""


def get_valid_integer(prompt):
    """
    This function will get a number from the user and return it.
    :return: int
    """

"""
define function display_song_list()
    
"""
#   TODO: Pseudocode for display_song_list function


def display_song_list(file_name):
    """
    This function will take a string consisting of the contents of the songs file and format and print it.
    :return: None
    """
    file = open(file_name, "r")
    file_content = file.readlines()
    count = 0
    for line in file_content:
        line_sections = line.split(',')
        if line_sections[3].lower == "y":
            completed_mark = "*"
        else:
            completed_mark = " "
        print("{:2i}. {:1s} {:15s} - {:15s} ({:4s})".format(count, completed_mark, line_sections[0], line_sections[1], line_sections[2]))
        #   TODO: Shorten this line if possible
        count += 1
    file.close()
    #   TODO: Find a way to write the number of songs

"""
define function add_a_song():
    is_valid = False
    while not is_valid:
        song_name = input("Title: ")
        is_valid = True
    is_valid = False
    while not is_valid:
        song_artist = input("Artist: ")
        is_valid = True
    is_valid = False
    while not is_valid:
        song_year = get input from the user with prompt "Year: "
        is_valid = False
    return = [song_name, song_artist, song_year]
"""


def add_a_song():
    """
    This function will get the name of the song, the artist's name and the year of release and will return that information in a list.
    :return: list
    """
    #   TODO: Shorten this docstring


"""
    song_number = input("Enter the number of the song to mark as learned")
"""
#   TODO: All of this


def complete_a_song():
    """
    This function will change the status of a song from required to learnt.
    :return: None
    """


if __name__ == '__main__':
    main()
