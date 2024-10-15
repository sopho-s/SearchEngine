import requests
import re

def ReadWebsites(file: str, upto: int) -> list[str]:
    urls: list[str] = []
    with open(file, "r") as f:
        index: int = 0
        while (line := f.readline()) != "" and index < upto:
            urls.append("https://" + line.replace("\n", ""))
            index += 1
    return urls

def GetURLs(pages: list[str]) -> list[list[str]]:
    pageurls: list[list[str]] = []
    for page in pages:
        urls: list[str] = re.findall(r"https://[^ \"?]*", page)
        print(urls)
        pageurls.append(urls)
    return pageurls

def Collect(urls: list[str], offsitecrawls: int):
    pages: list[str] = []
    urlcount = 0
    for url in urls:
        urlcount += 1
        response: requests.Response = requests.get(url)
        pages.append(response.content.decode("utf-8"))
        print(f"Urls searched: {urlcount}")
    newurls: list[list[str]] = GetURLs(pages)
