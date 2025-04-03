from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <div id="content">
            <ul class="industry">
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>스마트팩토리</li>
            </ul>
            <ul class="language">
                <li>Python</li>
                <li>C++</li>
                <li>Javascript</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
# print(soup)
# lml => 속도가 빠름, pip install lxml 설치 필요
# html5lib -> 속도 느림, pip install html5lib. html5 규격을 엄격히 지킴

# first_ul = soup.find("ul")
# print(first_ul)
# print(first_ul.text) # 태그없이 텍스트만 출력

# all_ul = soup.find_all("ul")
# print(all_ul[1].text)

# class_ul = soup.find("ul", attrs={"class": "language"})
# print(class_ul.text)

# class industry를 가져오는 selector
# ul.industry
# #content > .industry
# #content .industry
# #content:first-child
# first_ul = soup.select_one("ul.industry")
# print(first_ul.text)

all_ul = soup.select("#content > ul")
print(all_ul)
