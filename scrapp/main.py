from requests import get
from bs4 import BeautifulSoup as BSp

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "react"
response = get(f"{base_url}{search_term}")

if not (200 <= response.status_code and response.status_code <= 300):
    print("Can't request website")
else:
    soup = BSp(response.text, "html.parser")
    print(soup.find_all("title"))
    print(soup.find_all("section", class_="jobs"))
