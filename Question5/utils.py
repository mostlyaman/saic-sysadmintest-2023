from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from dotenv import load_dotenv
load_dotenv()
import os

from browsers import get_chrome, get_edge, get_firefox

LOGIN_USERNAME = os.getenv('LOGIN_USERNAME')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
login_url = "https://lms.iitmandi.ac.in/login/index.php"
courses_url = "https://lms.iitmandi.ac.in/my/courses.php"

# Change Browser from here
def create_new_driver():
    return get_firefox()
    # return get_edge()
    # return get_chrome()

def login():
    driver = create_new_driver()
    driver.get(login_url)
    
    driver.find_element(By.ID, 'username').send_keys(LOGIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LOGIN_PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()
    return driver

def get_courses():
    driver = login()
    driver.get(courses_url)
    
    try:
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CLASS_NAME, 'dashboard-card')
        )
    except Exception:
        raise Exception("No courses found.")
    
    course_boxes = driver.find_elements(By.CLASS_NAME, 'dashboard-card')
    
    print(len(course_boxes), "Courses Found.")
    
    courses = []
    for course_box in course_boxes:
        course = {
            "url": course_box.find_element(By.TAG_NAME, 'a').get_attribute('href'),
            "name": course_box.find_element(By.CSS_SELECTOR, 'span.multiline').text,
            "semester": course_box.find_element(By.CSS_SELECTOR, "span.categoryname").text
        }
        courses.append(course)

    with open("courses.json", "w") as f:
        f.write(json.dumps(courses))
    
    print("Updated Courses from LMS.")
    return driver


def get_assignments():
    if(os.path.isfile("courses.json")):
        print("Using saved courses from courses.json")
        driver = login()
    else:
        print("Updating Course List")
        driver = get_courses()
    
    courses = []
    with open("courses.json", "r") as f:
        courses = json.loads(f.read())
    
    for course in courses:
            
        
get_assignments()