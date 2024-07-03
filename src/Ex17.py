import requests, bs4

r = requests.get("https://www.nytimes.com/")
r_html = r.text

soup = bs4.BeautifulSoup(r_html, "html.parser")

for text in soup.find_all(class_="css-xdandi"):
    print(text.text)