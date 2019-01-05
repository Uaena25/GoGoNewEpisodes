from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path
from webbrowser import open_new
from datetime import datetime


def search_anime():
    """Searches new episodes for all of the animes in the list and prints when searching is done."""
    with open("Anime List.txt", "r") as file_read:
        file_list = file_read.readlines()
    for file in file_list:
        open_gogoanime(file.rstrip())
    print("Searched for anime at ", end="")
    print(datetime.now().time(), end="")
    print(".")


def open_gogoanime(favorite_anime):
    """Connects to GoGoAnime and searches the recently released episodes on the front page of the site
    for the selected anime. If found, if the episode isn't already saved into the appropriate text file,
    opens the site to that episode and saves the episode into the text file.
    """
    gogo_url = "https://gogoanimes.co/"
    request = Request(gogo_url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)
    html_data = response.read()
    response.close()

    soup = BeautifulSoup(html_data, "html.parser")
    ul_list = soup.find("ul", {"class":"items"})
    anime_list = ul_list.find_all("a")

    for anime in anime_list:
        if favorite_anime.lower() in anime.get("title").lower():
            if Path(favorite_anime+".txt").exists():
                with open(favorite_anime+".txt", "r") as file_read:
                    for line in file_read:
                        if line.rstrip() == anime.get("href"):
                            return
            with open(favorite_anime+".txt", "a") as file_append:
                file_append.write(anime.get("href")+"\n")
            open_new(gogo_url+anime.get("href"))
