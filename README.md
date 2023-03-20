## SRT 자동예매 매크로

사용자가 원하는 시간, 출발지, 목적지 등을 입력해 자동으로 SRT 표를 예매해주는 프로그램입니다.<br/><br/><br/>


## 사용법

main.py 파일을 열고 밑에서 설명하는 각 변수에 사용자의 정보를 입력하면 됩니다.<br/>


```
member_number = "0000000000" # 회원번호
password= "1234" # 비밀번호
arrival = "수서" # 출발지
departure = "동대구" # 도착지
standard_date = "20230217" # 기준날짜 ex) 20221101
standard_time = "16" # 기준 시간 ex) 00 - 22 // 2의 배수로 입력
number_of_trains = 11 # 상단에서부터 조회할 기차수  maximum = 11

```  
다음으로 Terminal에 다음과 같은 명령어를 입력하여 selenium 모듈을 설치합니다.

```
pip install selenium
```

이후 프로그램을 실행하면 자동으로 SRT 예매가 시작됩니다.

