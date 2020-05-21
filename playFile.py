import librosa as librosa
from selenium import webdriver
abc=input("enter:")
driver=webdriver.Chrome('C:\\Users\\Rahul\\PycharmProjects\\AutomationTool\\chromedriver_win32\\chromedriver.exe')
driver.get(abc)
#driver.mute()
#driver.find_element_by_xpath('//*[@id="search"]')
x, sr = librosa.load('abc')
onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
print(onset_frames) # frame numbers of estimated onsets