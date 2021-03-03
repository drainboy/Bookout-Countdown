import random
import requests
from bs4 import BeautifulSoup


def scrap_for_quotes(site):
    """Scrap for quotes from given site and store data into quotes.txt"""
    html = requests.get(site)
    if html:
        soup = BeautifulSoup(html.content, "html.parser")
        a_tag_quotes = soup.find_all("a", title = "view quote", text = True)
        quotes = [tag.text.strip() for tag in a_tag_quotes]

        with open("bookoutcountdown/motivation/quotes.txt", "w") as file:
            for quote in quotes:
                file.write(quote + "\n")


def get_quote():
    """Returns a random quote"""
    quotes = open("bookoutcountdown/motivation/quotes.txt").readlines()
    open("debug.txt", "w").write(str(quotes))
    chosen = random.choice(quotes)
    return chosen


def format_quote(width_size, quote):
    """Returns chunks for given quote based on given width size"""
    split = quote.split()

    chunks = []
    line = ""
    for word in split:
        new_line = line + word + " "
        if len(new_line) >= width_size:
            chunks.append(line[:-1])
            line = word + " "
        else:
            line = new_line
    else:
        chunks.append(line[:-1])

    return chunks

scrap_for_quotes("https://www.brainyquote.com/topics/motivational-quotes")