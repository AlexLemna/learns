import os
import pathlib


def home_is_where_this_file_is():
    """Changes the working directory to wherever this file is located."""
    current_working_directory = pathlib.Path.cwd()
    file_home_directory = pathlib.PurePath(__file__).parent
    if current_working_directory == file_home_directory:
        return
    else:
        os.chdir (file_home_directory)
