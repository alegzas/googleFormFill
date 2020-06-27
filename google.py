from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random
import time

#array for each question containing the options
q1 = ["18+-+29", "30+-+50"]
q2 = ["Yes", "No"]
q3 = ["Electronic+voting", "Paper-based+voting"]
q4 = ["Electronic+voting", "Paper-based+voting"]
q5 = ["In+person+machine+based+voting", "Online+voting/electronic+voting+from+home"]
q6 = ["Yes", "No"]

print("starting")

for i in range(0, 10):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    #pre-filled google form url, with the pre-filled answers replaced with random entries from the arrays
    linkas = "https://docs.google.com/forms/d/e/OMMITED&entry.1054147823="+random.choice(q1)+"&entry.4239358="+"No"+"&entry.2000539790="+random.choice(q3)+"&entry.1000327849="+"Paper-based+voting"+"&entry.1940912693="+random.choice(q5)+"&entry.1495222359="+random.choice(q6)
    driver.get(linkas)
    button = driver.find_element_by_class_name('exportButtonContent')
    button.click()
    driver.close()
    time.sleep(3)

print("done")
