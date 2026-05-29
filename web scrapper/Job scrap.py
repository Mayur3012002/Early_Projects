import time
import requests
from bs4 import BeautifulSoup

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    print('put out some skills your unfamilar with')
    unfamiliar_skills = input('>')
    print(f'filtering out:{unfamiliar_skills}')

    for index, job in enumerate(jobs):
        published_date=job.find('span',class_="sim-posted").span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f" Company Name:{company_name.strip()}\n")
                    f.write(f"Required Skills:{skills.strip()}\n")
                    f.write(f"More info: {more_info}")

                print(f'File saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait= 2
        print(f'waiting {time_wait} minutes...')
        time.sleep
        time.sleep(time_wait * 60)
