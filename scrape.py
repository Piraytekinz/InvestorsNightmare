#THIS CODE IS MEANT TO SCRAPE ALL INVESTOR EMAILS AND INVESTMENT THESIS FROM AN AIRTABLE
#AND DUMP THE INFORMATION INTO A .TXT FILE.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Set up the Edge WebDriver
driver = webdriver.Edge()

# Open the target URL
url = "https://airtable.com/appi82OqC0sofDlcH/shrdqT0dM0vaIeO9u/tblyAK2VE4dS8O4dZ/viwiaTchRnMLqZqsS?backgroundColor=blue&blocks=hide"
driver.get(url)

# Locate the parent element by class name

parent_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[3]/div[2]')
second_parent = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]')


# time.sleep(10)

# last_height = driver.execute_script("return document.body.scrollHeight")
print(second_parent)



"/html/body/div[1]/div[2]/div[1]/div[2]"

table_container = driver.find_element(By.CLASS_NAME, "antiscroll-inner")

# Get the initial scroll height of the table container
last_height = driver.execute_script("return arguments[0].scrollHeight", table_container)

#focuses refers to the investment thesis of the investor we're trying to reach out to from the airtable.
links = []
focuses = []
n = 0
while True:

    n += 1
    if parent_element:

        print('parent exists')
        # Find a specific child element within the parent element
        #COLLECTS THE EMAIL AND INVESTMENT THESIS (FOCUS) FROM THE CHILD ELEMENTS.
        child_element = parent_element.find_elements(By.TAG_NAME, 'span')
        
        focus = second_parent.find_elements(By.CLASS_NAME, 'line-height-4.overflow-hidden.truncate')
        print(focus)
        print(len(focus))

        for u in child_element:
            if u.text not in links:
                links.append(u.text)

        for u in focus:
            print(u.text)
            if u.text not in focuses:
                focuses.append(u.text)
            # print(i.text)
        
        # Print the text of the child element if found
        # print(child_element.text if child_element else "Child element not found.")
    else:
        print("Parent element not found.")


    #automatically scrolls the airtable after data has been collected because the airtable loads the data
    #as the user scrolls.

    driver.execute_script("arguments[0].scrollTop += 300", table_container)
    time.sleep(1)
    


    # Check if we've reached the bottom of the table
    new_height = driver.execute_script("return arguments[0].scrollHeight", table_container)

    print(new_height)
    if len(links) >= 219:
        break  # Exit if no new content is loaded
    last_height = new_height


#Places the found investment thesis and emails inside a .txt file.
print(focuses)
print(len(focuses))
with open('txt.txt', 'w') as f:
    f.write(" ".join(links) + "\n" + ", ".join(focuses))
driver.quit()