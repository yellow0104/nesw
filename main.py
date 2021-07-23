
#제작 : 위정우
print("made in joungwoo")
print("================")


import requests
from bs4 import BeautifulSoup
inp = input("검색 할 것을 입력하세요>>")
url = f"https://search.naver.com/search.naver?query={inp}&where=news&ie=utf8&sm=nws_hty"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")
titles = soup.find_all("a", attrs={"class":"news_tit"})


print(f"네이버 뉴스에 찾아본 \"{inp}\" 의 검색결과")
for title in titles:
    
    t = title.get_text()
    link = title["href"]
    print("===================")
    print(t, link)
    print("===================")
