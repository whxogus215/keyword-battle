# 서버를 가동 시켜줄 파일
from flask import Flask, render_template, request
from pip import main
import google_keyword

# 앱 서버 인스턴스( 서버의 심장 부분 : 가동 )
app = Flask(__name__)


# url 패턴 - 라우터 설정 - 데코레이터
@app.route('/')
def index():
    # get 을 통한 전달받은 데이터를 확인
    key1 = request.args.get('keyword1')
    key2 = request.args.get('keyword2')
    print(key1,key2)

    # 입력받은 키워드가 없을 때 그냥 index.html만 보내줌
    if key1 == "" or key2 =="" or key1 is None or key2 is None:
        return render_template('index.html')
    else:  
        # 모듈로 키워드 개수 가져오기
        value1 = google_keyword.get_keyword_number(key1)
        value2 = google_keyword.get_keyword_number(key2)

        # 사용자 보낼 데이터
        data = {key1 : value1, key2 : value2}
        
        return render_template('index.html', data = data) # 데이터와 함께 보냄


# 메인 테스트
if __name__ == '__main__':
    app.run(debug=True)
    