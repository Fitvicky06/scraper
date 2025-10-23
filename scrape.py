import requests
from bs4 import BeautifulSoup

URL = "https://indianexpress.com"  
TAG = "h3"                         
FILE_NAME = "headlines.txt"        
TOP_N = 15

print(f"1. Fetching data from {URL} ...")
response = requests.get(URL)
response.raise_for_status()  

print("2. Parsing the HTML...")
soup = BeautifulSoup(response.text, "html.parser")

print(f"3. Finding all <{TAG}> headlines...")
headline_elements = soup.find_all(TAG)

#  EXTRACT TEXT AND KEEP ONLY TOP 15
headlines = [h.text.strip() for h in headline_elements if h.text.strip()]
top_headlines = headlines[:TOP_N]

#  SAVE TO FILE
print(f"4. Saving top {TOP_N} headlines to {FILE_NAME}...")
with open(FILE_NAME, "w", encoding="utf-8") as f:
    for i, line in enumerate(top_headlines, 1):
        f.write(f"{i}. {line}\n")

print(f" Done! {TOP_N} headlines saved successfully in {FILE_NAME}.")