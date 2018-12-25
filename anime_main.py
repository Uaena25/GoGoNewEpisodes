import anime_open
import anime_list
from time import sleep


if __name__ == "__main__":
    open("Anime List.txt", "a").close()
    print("List of Anime:")
    with open("Anime List.txt", "r") as file_read:
        for file in file_read:
            print("\t"+file.rstrip())
    print()
    anime_list.add_anime()
    anime_list.remove_anime()

    anime_open.search_anime()
    while True:
        sleep(3600)
        anime_open.search_anime()
