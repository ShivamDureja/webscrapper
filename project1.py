from bs4 import BeautifulSoup
import  requests
import time
print('Put a skill that you are unfamiliar with:')
unfamiliar_skill = input('>')
print('Searching for job ...')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            link = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company.strip()}\n")
                    f.write(f"Skills: {skills.strip()}\n")
                    f.write(f"Link To Job : {link}")
                print(f'file saved: as {index}')
if __name__ == '__main__':
    while True:
         find_jobs()
         time_wait = 10
         print(f'Waiting {time_wait} minutes ...')
         time.sleep(time_wait * 60)