from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def extract_text_from_url(url):
    try:
        # Chrome 옵션 생성
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # headless 모드로 설정

        # Chrome WebDriver 생성
        driver = webdriver.Chrome(options=chrome_options)

        # 웹 드라이버로 해당 URL 열기
        driver.get(url)

        # 텍스트 추출할 요소의 XPath 설정
        element_xpath = (
            "//span[@class='inline cursor-pointer hover:bg-red-300 css-82uonn']"
        )

        # 요소 찾기
        elements = driver.find_elements(By.XPATH, element_xpath)

        # 텍스트 추출
        text_list = [element.text for element in elements]

        # 웹 드라이버 종료
        driver.quit()

        return text_list

    except Exception as e:
        print("오류가 발생했습니다:", str(e))
        return None
