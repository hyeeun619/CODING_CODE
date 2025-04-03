import code
from bs4 import BeautifulSoup
import requests

# 서울 시청 웹크롤링
# html_url = "https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# all_nav = soup.select("nav > ul > li > a")
# # print(all_nav)
# for i in all_nav:
#     print(i.text)

# # 실습. 국립중앙박물관 스크래핑
# html_url = "https://www.museum.go.kr/site/main/home"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# # all_nav = soup.select("ul.main-info-area")
# # for i in all_nav:
# #     print(i.text)

# # 관람시간
# times = soup.select(".info-time > ul > li")
# for i in times:
#     print("관람시간: ", i.text.strip())

# # 관람료
# pay = soup.select(".info-admission > ul > li")
# for i in pay:
#     print("관람료: ", i.text.strip())

# pay2 = soup.select(".info-admission > ul > li > span")
# print("관람료: ", pay2[0].text.strip)

# kbs 뉴스 크롤링
# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8153501"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# # 제목
# title = soup.select_one(".headline-title")
# print("제목: ", title.text.strip())

# # 내용
# content = soup.select_one("#cont_newstext")
# print("내용: ", content.text.strip())

# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(title.text.strip()+ "\n")
#     file.write(content.text.strip())

# 명언 크롤링
# html_url = "https://quotes.toscrape.com/page/2/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# quote = soup.select(".quote > span.text")
# # for i in quote:
# #     print(i.text.strip())
# text = [i.text.strip()for i in quote]
# # print(text)

# speaker = soup.select(".quote .author")
# # print(speaker)
# author = [i.text.strip() for i in speaker]

# zipped = list(zip(text, author))
# for text, speaker in zipped:
#     print(f"명언자: {speaker} \n내용:{text}")

# kbs 뉴스 크롤링
# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8153501"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# # 제목
# title = soup.select_one(".headline-title")
# print("제목: ", title.text.strip())

# # 내용
# content = soup.select_one("#cont_newstext")
# print("내용: ", content.text.strip())

# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(title.text.strip()+ "\n")
#     file.write(content.text.strip())


# 실습. 전자 신문 메인 기사 크롤링
# html_url = "https://m.etnews.com/20250116000159"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# # 제목
# title = soup.select_one("#article_title_h2")
# print("제목: ", title.text.strip())

# # 발행일
# a = soup.select_one(".article_header time")
# print(a.text.strip())

# # 본문내용
# b = soup.select_one(".article_body")
# print("본문: ", b.text.strip())

# 실습. 환율정보 크롤링
# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# a = soup.select(".market1 .data .h_lst")
# c = [i.text.strip() for i in a]

# b = soup.select(".market1 .data .data_lst .value")
# d = [i.text.strip() for i in b]

# zipped = list(zip(c, d))

# for c,d in zipped:
#     print(f"{c} - {d}")

# 주식정보 크롤링
# html_url = "https://finance.naver.com/item/main.naver?code=086520"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# # 상품명
# a = soup.select_one(".h_company .wrap_company > h2")
# a1 = a.text.strip()

# # 전일대비
# b = soup.select_one(".rate_info .no_exday > .no_up")
# b1 = b.text.strip()
# d = soup.select_one(".rate_info .no_exday > .bar > .no_up")
# d1 = b.text.strip().split()[2]

# # 현재 가격
# c = soup.select_one(".rate_info .no_today")
# c1 = c.text.strip().split()[0]

# print(f"상품명: {a1}")
# print(f"전일대비: {b1} {d1}")
# print(f"현재 가격: {c1}")

# 주식정보
def stock(code):
    html_url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(html_url)
    soup = BeautifulSoup(res.text, "html.parser")

    company = soup.select_one(".wrap_company > h2 > a")
    print(f"회사명: {company.text.strip()}")

    price = soup.select_one(".today > .no_today > .no_up > .blind")
    print(f"종가: {price.text.strip()}원")

    prev = soup.select_one(".today > .no_exday > .no_up > .blind")
    print(f"전일대비: {prev.text.strip()}원")

stock("000680")
stock("024830")
