from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content , 'lxml')
    tag = soup.find_all('h5')
    course_cards = soup.find_all('div')
    for course in course_cards:
       # courses = course.h5.text
        course_price = course.a

        #print(courses)
        print(course_price)