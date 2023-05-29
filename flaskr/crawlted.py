from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import time

# 웹 드라이버 인스턴스 생성
# Chrome 옵션 생성
chrome_options = Options()
chrome_options.add_argument("--headless")  # headless 모드로 설정

# Chrome WebDriver 생성
driver = webdriver.Chrome(options=chrome_options)

# TED 톡 URL 설정
tedtalk_url = "https://www.ted.com/talks/david_biello_the_year_without_summer/transcript?language=ko"

# 웹 드라이버로 해당 URL 열기
driver.get(tedtalk_url)

# 텍스트 추출할 요소의 XPath 설정
element_xpath = "//span[@class='inline cursor-pointer hover:bg-red-300 css-82uonn']"

# 요소 찾기
elements = driver.find_elements(By.XPATH, element_xpath)


# 텍스트 추출
text_list = [element.text for element in elements]

print (text_list)


# 웹 드라이버 종료
driver.quit()



