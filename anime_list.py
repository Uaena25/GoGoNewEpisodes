from pathlib import Path


def add_anime():
    add = input("Add anime to watch list (enter 'y' or 'n')? ")
    while add != "y" and add != "n":
        add = input("Add anime to watch list (enter 'y' or 'n')? ")
    if add == "y":
        while True:
            anime = input("Enter name of anime to add (or enter 'q' to quit): ")
            if anime == "q":
                return
            file_append = open("Anime List.txt", "a")
            file_append.write(anime+"\n")
    if add == "n":
        return


def remove_anime():
    remove = input("Remove anime from watch list (enter 'y' or 'n')? ")
    while remove != "y" and remove != "n":
        remove = input("Remove anime from watch list (enter 'y' or 'n')? ")
    if remove == "y":
        with open("Anime List.txt", "r") as file_read:
            file_list = file_read.readlines()
            while True:
                anime = input("Enter name of anime to remove (or enter 'q' to quit): ")
                if anime == "q":
                    break
                for line in file_list:
                    if line.rstrip() == anime:
                        file_list.remove(line)
                        remove_path = Path(line.rstrip()+".txt")
                        if remove_path.exists():
                            remove_path.unlink()
        with open("Anime List.txt", "w") as file_write:
            for line in file_list:
                file_write.write(line)
    if remove == "n":
        return
