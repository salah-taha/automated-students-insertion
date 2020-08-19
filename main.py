from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def write_info_to_file(name, code, user_name, password):
    students_file = open(r"C:\Users\salah taha\Desktop\students-adding-script\added_students.txt", "a+", encoding = "utf-8")
    students_file.write(f"name: {name},user name: {user_name} code: {code},password: {password}  \n")
    students_file.close()


def sign_student_to_the_website(first_name, last_name, class_code, user_name, password):
    driver = webdriver.Chrome("F:\programs\chromedriver_win32\chromedriver.exe")
    driver.get("https://new.edmodo.com/student-signup?utm_source=main&utm_campaign=onb-user-type-page&utm_medium=visitor-site&utm_content=main-cta-btn")
    try:
        first_name_placeholder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'first_name')))
        last_name_placeholder = driver.find_element_by_name("last_name")
        class_code_placeholder = driver.find_element_by_name("group_code")
        user_name_placeholder = driver.find_element_by_name("username")
        password_placeholder = driver.find_element_by_name('password')
        button = driver.find_element_by_class_name("btn-block")
        first_name_placeholder.send_keys(first_name)
        last_name_placeholder.send_keys(last_name)
        class_code_placeholder.send_keys(class_code)
        user_name_placeholder.send_keys(user_name)
        password_placeholder.send_keys(password)
        time.sleep(2)
        button.click()
        skip = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'qa-test-account-safety-skip')))
        skip.click()
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'col-md-4')))
        driver.close()
        return 'done'

    except TimeoutException:
        return 'error'


continu = 1
while continu != -1:
    first_name = input('first-name: ')
    last_name = input('last-name: ')
    first_3_letters = input('first 3 letters: ')
    code = input('students code: ')
    password = 'moe' + code[0:4]
    status = sign_student_to_the_website(first_name, last_name, 'z27fwm', first_3_letters + code, password)
    if status == 'done':
        write_info_to_file(first_name + ' ' + last_name, code, first_3_letters + code, password)
        print('done')
    else:
        print(status)
    continu = int(input("enter 1 to continue"))
