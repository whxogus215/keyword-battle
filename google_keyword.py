
from wsgiref import headers
from bs4 import BeautifulSoup
import requests


def get_keyword_number(keyword):
    url = "https://www.google.co.kr/search?q={}&hl=en".format(keyword)
    headers = {
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    # 웹 요청
    res = requests.get(url, headers=headers)

    # 구문 분석 - 파싱 (html 태그 형식으로 소스를 가져올 수 있음)
    soup = BeautifulSoup(res.text, 'lxml')

    # 원하는 것 추출
    number = soup.select_one('#result-stats').text

    # 정리
    number = int(number[number.find('About')+6:number.rfind('results')-1].replace(',',''))

    return number

# 테스트 코드 , 이 파일에서 실행할 때만 나오게 하는 코드!, 다른 곳에서 import 되어 사용될 땐 실행되지 않음
if __name__ == '__main__':
        print(get_keyword_number('van dirk'))
    