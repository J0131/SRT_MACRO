## SRT 자동예매 매크로

사용자가 원하는 시간, 출발지, 목적지 등을 입력해 자동으로 SRT 표를 예매해주는 프로그램입니다.<br/><br/><br/>


## 사용법

.env 파일에 아래의 변수를 정의하시면 됩니다.<br/>


```
MEMBER_NUMBER="0000000000" # 회원번호
MEMBER_PASSWORD="1234" # 비밀번호
ARRIVAL_NAME="수서" # 출발지
DEPARTURE_NAME="천안아산" # 도착지
STANDARD_DATE="20240426" # 기준날짜
STANDARD_TIME="18" # 기준시간
START_OF_TRAIN=1 # 시작할 기차 번호
NUMBER_OF_TRAIN=1 # 상단에서부터 조회할 기차 수

```  
다음으로 Terminal에 다음과 같은 명령어를 입력하여 selenium 모듈을 설치합니다.
terminal-notifier는 예약 완료시 터미널에 노티를 주는 모듈입니다.

```
brew install terminal-notifier
pip install -r requirements.txt
```

이후 프로그램을 실행하면 자동으로 SRT 예매가 시작됩니다.
원하는 env를 명시해 사용할 수 있습니다.

```
python main.py
python main.py .env.home
```

* 같은 IP로 수많은 요청을 보냈을 때 SRT의 자체 보안툴에서 해당 IP를 차단하는 케이스가 감지되었습니다. 이러한 현상을 방지하기 위해 VPN 사용 환경을 권장합니다.
* 반드시 본인이 사용하는 크롬 버전에 맞는 chromedriver.exe 파일을 사용하여야 합니다.

