from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



path=input("Enter the url here:")
driver = webdriver.Chrome('C:\\Users\\Rahul\\PycharmProjects\\AutomationTool\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get(path)

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()