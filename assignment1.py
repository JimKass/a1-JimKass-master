"""
Replace the contents of this module docstring with your own details.
"""
#   TODO: What he said
"""
    TEMP_FILE_NAME = temp.csv
    SONG_FILE_NAME = songs.csv
"""


"""
function main()
    MENU = "Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit"
    song_file, temp_file = load_songs()
    keep_going = True
    display "Songs To Learn 1.0 - by James Kastner"
    display MENU
    action = get_valid_string
    if action == "l"
        
    otherwise if action == "a"
    
    otherwise if action == "c"
    
    otherwise if action == "q"
    
    otherwise
        display "Invalid menu choice"
    
"""


def main():
    """
    
    :return: 
    """


"""
function named load_songs()
    song_file = open SONG_FILE_NAME as read only
    temp_file = open TEMP_FILE_NAME as write only
    write song_file to temp_file
    return song_file, temp_file
"""


def load_songs():
    """
    Loads the files containing the information on the songs and the temporary back up.
    :return: file and file
    """


"""
function get_valid_string():
    
"""
#   TODO: Pseudocode for this function


def get_valid_string(prompt):
    """
    This function will get an input from the user and make sure that it is a string type.
    :return: str
    """

"""
function get_valid_integer(prompt)
    is_valid = False
    while is_valid = False
        try to execute:
            display prompt to the user
            number = get input from the user
            convert number into integer type
            is_valid = True
        if a ValueError occurs, execute
            display "Invalid Input, please enter a number"
    return number
"""


def get_valid_integer(prompt):
    """
    This function will get a number from the user and return it.
    :return: int
    """

"""
function display_song_list(song_file)
    file_content = contents of song_file
    count = 0
    completed_count = 0
    for line in file_content
        line_sections = split line on comma and strip of whitespace
        if line_sections[3] == "y"
            completed_mark = "*"
            completed_count += 1
        otherwise
            complete_mark = ""
        display count. complete_mark line_section[0] - line_section[1] (line_section[2])
        count += 1
    display (completed-count) songs learned, (count - complete_count) songs still to learn
"""
#   TODO: sort by artist and title


def display_song_list(song_file):
    """
    This function will take a string consisting of the contents of the songs file and format and print it.
    :return: None
    """


"""
function add_a_song():
    display "Title: "
    get song_name
    while song_name == "":
        display "Input can not be blank"
        display "Title: "
        get song_name
        
    display "Artist: "
    get song_artist
    while song_artist == "":
        display "Input can not be blank"
        display "Artist: "
        get song_artist
    display "Year: "
    get song_year
    while song_year == "":
        display "Input can not be blank"
        display "Year: "
        get song_year
    add song to song_file (format: song_name, song_artist, song_year, "n")
"""


def add_a_song():
    """
    This function will get the relevant details of the song and will return that information in a list.
    :return: list
    """


"""
function complete_a_song() 
    display "Enter the number of the song to mark as learned")
    song_number = get_valid_number()
    
"""
#   TODO: All of this


def complete_a_song():
    """
    This function will change the status of a song from required to learnt.
    :return: None
    """


if __name__ == '__main__':
    main()
