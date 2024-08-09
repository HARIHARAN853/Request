import requests,openpyxl
from bs4 import BeautifulSoup
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title="New Book"
sheet.append(["Movie","Rating"])
response = requests.get("https://www.rottentomatoes.com/")
soup = BeautifulSoup(response.text,'html.parser')

courses = soup.find_all("a",class_="cfp-tile")
for course in courses:
    movie = course.find("span",class_="p--small").text
    rating = course.find("rt-text",class_="critics-score").text
    sheet.append([movie,rating])
excel.save("Output.xslx")
