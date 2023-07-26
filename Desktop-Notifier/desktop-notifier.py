import re
import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup as bs

# The link to get the news from
try:
    r = requests.get("https://timesofindia.indiatimes.com/")
except:
    r = None
    print("Check your internet connection")

if r is not None:
    # Telling the soup that web page is in html
    soup = bs(r.text, "html.parser")

    # Finding the element containing the breaking news
    results = soup.find("div", {"data-vr-zone": "headlines"})

    # The line containing the link and the news
    item = results.find("a", attrs={'href': re.compile("^/")})
    link = item.get("href")
    message = item.get("title")
    title = "Breaking news"

    # The notifier is created here
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path=r'<Insert-absolute-path-to-toi.ico-here>', duration=None)
