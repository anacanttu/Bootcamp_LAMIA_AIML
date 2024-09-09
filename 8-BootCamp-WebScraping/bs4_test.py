from bs4_test import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, 'lxml')
# courses_html_tags = soup.find_all('h5') # Acha todas as H5 tags, apenas um teste para mostrar como funciona
#for course in courses_html_tags:
#   print(course.text)

course_cards = soup.find_all('div', class_='card')
for course in course_cards:
    #print(course.h5) # <h5 class="card-title">Python for beginners</h5> <h5 class="card-title">Python Web Development</h5><h5 class="card-title">Python Machine Learning</h5>
    course_name = course.h5.text
    course_price = course.a.text.split()[-1] 
    
    # print(course_name)
    # print(course_price) #Python for beginners 20$ Python Web Development 50$ Python Machine Learning100$
    print(f'{course_name} costs {course_price}') #Printa a mesma coisa, mas é mais funcional por exemplo se estou analisando um site como Udemy que atualiza sempre e tem novos cursos, consigo identificar.