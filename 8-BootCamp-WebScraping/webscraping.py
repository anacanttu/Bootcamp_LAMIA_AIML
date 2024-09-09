import requests
from bs4_test import BeautifulSoup
import time

print('Put some skill that you are not familiar with') #Filtro por uma skill
unfamiliar_skill = input ('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation="
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): #loop para pegar todas as infos daquelas pagina
        published_date = job.find('span', class_='sim-posted').span.text #Pra pegar a data de publicacao daquele job especifico. Mudou a posicao dele para primeiro para conseguir colocar condicao em baixo
        if 'few' in published_date: #quero pegar os jobs que estao a few days ago 
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') #Serve para tirar o espaco em branco que ele puxa
            skills = job.find('span', class_='srp-skills').text.replace(' ', '') 
            more_info = job.header.h2.a['href'] #Puxa o link para mais info

            if unfamiliar_skill not in skills: 
                #print(f'''Company Name: {company_name}Required Skills: {skills}''') #Imprime o nome da empresa e as habilidades (skills)
                #print(published_date) #Imprime a data de publicacaoli
                with open(f'posts/{index}.txt', 'w') as f: #Cria um arquivo para salvar os jobs
                    #print(f"Company Name: {company_name.strip()}")
                    #print(f"Required Skills: {skills.strip()}")
                    #print(f"More Info: {more_info}")  #Imprime o link para mais info do job
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f"More Info: {more_info}")  #Imprime o link para mais info do job
                print(f'File saved: {index}') #Imprime o nome do arquivo que foi salvo')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10 #esperar 10 minutos para executar novamente
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)