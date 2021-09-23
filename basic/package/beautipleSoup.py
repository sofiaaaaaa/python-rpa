from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.pretify())

# pip list
# pip show beautiplesoup4 