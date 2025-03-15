from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (replace with your WebDriver setup)
driver = webdriver.Edge()

# Open the webpage
driver.get("https://airtable.com/appi82OqC0sofDlcH/shrdqT0dM0vaIeO9u/tblyAK2VE4dS8O4dZ/viwiaTchRnMLqZqsS?backgroundColor=blue&blocks=hide")

# Wait for the JavaScript to load (adjust time as needed)
time.sleep(5)  # Allow time for page elements to load

# Extract the full page HTML after rendering
html = driver.page_source

# URL of the webpage with the table

# Send a request to fetch the page conten

print(html)
while True:
    # Parse the current HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('div', {'class': 'dataRightPane pane no-events-when-cell-selection-disabled'})  # Use class, id, or other attributes

    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Locate the table (adjust the selector as needed)
    table = soup.find('div', {'class': 'dataRightPane pane no-events-when-cell-selection-disabled'})  # Use class, id, or other attributes

    # Extract table headers (optional)
    headers = []

    print(soup)
    with open('txt.txt', 'w') as f:
        f.write(str(soup))
# for header in table.find_all('th'):
#     headers.append(header.text.strip())

# # Extract rows
# data = []
# for row in table.find_all('tr'):
#     # Extract columns for each row
#     columns = row.find_all('td')
#     row_data = [col.text.strip() for col in columns]
#     if row_data:  # Ignore empty rows
#         data.append(row_data)

# # Display extracted data
# if headers:
#     print(headers)
# for row in data:
#     print(row)
