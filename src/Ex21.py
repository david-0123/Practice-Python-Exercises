import requests, bs4

r = requests.get("https://www.nytimes.com/")
r_html = r.text

soup = bs4.BeautifulSoup(r_html, "html.parser")

with open("results.txt", "w") as f:
    for text in soup.find_all(class_="css-xdandi"):
        f.write(text.text)
        f.write("\n")