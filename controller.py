import UI
import fileio

def start():
    mode = UI.start_message()
    match mode:
        case 1:
            data = fileio.read_data("file.csv")
        case 2:
            fileio.write_data("file.csv", data)