# 프로젝트 : SRT_MACRO
# 작성자 : 최범준
# 작성일시 : 2023-02-13

from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


############# 자동 예매 원하는 설정으로 변경 ##############

member_number = "2292252244" # 회원번호
password= "hy0131@@" # 비밀번호
arrival = "수서" # 출발지
departure = "동대구" # 도착지
standard_date = "20230217" # 기준날짜 ex) 20221101
standard_time = "16" # 기준 시간 ex) 00 - 22 // 2의 배수로 입력
number_of_trains = 11 # 상단에서부터 조회할 기차수  maximum = 11

#################################################################


# v 1.0

reserved = False

print("--------------- Start SRT Macro ---------------")

# webdriver 파일의 경로 입력
# 같은 디렉토리에 있기 때문에 chromedriver.exe파일 이름만 써줌
driver = webdriver.Chrome("chromedriver")

# 이동을 원하는 페이지 주소 입력
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
driver.implicitly_wait(15)


# 회원번호 매핑
driver.find_element(By.ID, 'srchDvNm01').send_keys(member_number)

# 비밀번호 매핑
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(password)

# 확인 버튼 클릭
driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div[2]/form/\
    fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)


driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)


# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear()
dep_stn.send_keys(arrival)

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys(departure)

# 날짜 드롭다운 리스트 보이게
# elm_dptDt = driver.find_element(By.ID, "dptDt")
# driver.execute_script("arguments[0].setAttribute('style','display: True;)", elm_dptDt)

Select(driver.find_element(By.ID,"dptDt")).select_by_value(standard_date)

# 출발 시간
# eml_dptTm = driver.find_element(By.ID, "dptTm")
# driver.execute_script("arguments[0].setAttribbute('style','display:True;')", eml_dptTm)

Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text(standard_time)

# 조회하기 버튼
driver.find_element(By.XPATH, "//input[@value='조회하기']").click()


train_list = driver.find_elements(By.CSS_SELECTOR, "#result-form > fieldset > \
div.tbl_wrap.th_thead > table > tbody > tr")

print(train_list)


while True: 

    for i in range(1,number_of_trains):
        standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in standard_seat:
            print("예약 가능 클릭")
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/\
            form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            driver.implicitly_wait(3)

            if driver.find_elements(By.ID, 'isFalseGotoMain'):
                reserved = True
                print('예약 성공')
                webbrowser.get(chrome_path).open("https://etk.srail.kr/hpg/hra/02/selectReservationList.do?pageId=TK0102010000")
                break

            else:
                print("잔여석 없음. 다시 검색")
                driver.back() #뒤로가기
                driver.implicitly_wait(5)
    
    if not reserved:
        # 5초 기다리기

        # 다시 조회하기
        submit = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[2]/form/fieldset/div[2]/input")
        driver.execute_script("arguments[0].click();", submit)
        print("새로고침")

        driver.implicitly_wait(10)
        time.sleep(1)

    else:
        break







    

