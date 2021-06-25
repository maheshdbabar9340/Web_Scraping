import requests
from bs4 import BeautifulSoup
import os
import xlsxwriter
from itertools import chain
import itertools

all_cities_url = []
def find_states(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('a')

    for image in images:
        link = image['href']
        if 'https://www.indiangoslist.com/tripura/ngos-in-' in link:
#             print(link)
            all_cities_url.append(link)
        else:
            pass
    return all_cities_url
    
find_states('https://www.indiangoslist.com/tripura-ngos-list')


def getCitiesUrls(url):

    r = requests.get(url)
    all_ngo_url = []
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('a')

    
    for image in images:
        link = image['href']
        if 'https://www.indiangoslist.com/ngo-address/' in link:
            all_ngo_url.append(link)
        else:
            pass
    return all_ngo_url


def getNgos(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('a')
    
    for image in images:
        link = image['href']
        if 'https://www.indiangoslist.com/ngo-address/' in link:
            return link
        else:
            pass

        
    
# links = []   
# for i in range(len(all_cities_url)):
#     ngos = getCitiesUrls(all_cities_url[i])

#     for i in ngos:
#         link = getNgosfromCity(i)
#         links.append(link)


links = []   
for i in range(2):
    ngos = getCitiesUrls(all_cities_url[i])

    for i in ngos:
        link = getNgos(i)
        links.append(link)


    
    
# def getSeperateNgoDetails(url):
    
#     r = requests.get(url)

#     soup = BeautifulSoup(r.text, 'html.parser')
 
#     images = soup.find_all('div', class_='ngo_line')

#     list_of_page = []
#     for exam in images:
#         list_of_page.append(exam)
#         print(exam.text.strip().replace('\n','').split("   "))

# row = 1
# print("Global row is = ", row)
# def row_incrementor():
#     global row
#     row = row + 20
#     return row

def getSeperateNgoDetails():
    
    for link in links:
        r = requests.get(link)

        soup = BeautifulSoup(r.text, 'html.parser')

        images = soup.find_all('div', class_='ngo_line')

        list_of_page = []
        headers = ["NGO Name", "Unique Id of VO/NGO", "Chief Functionary", "Chairman", "Secretary", "Type of NGO", "Registration Number", "frca", "City", "State", "Telephone", "Mobile Number", "Address", "Email", "Website", "Key Issues"]
        workbook = xlsxwriter.Workbook("C:\\Users\\mahes\\Desktop\\ngo.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'test')

        row  = 1
        col = 0

        for exam in images:
            res = exam.text.strip().replace("\n", "").split("   ")
            d = dict(itertools.zip_longest(*[iter(res)] * 2, fillvalue=""))
    #         print(res)
    #         print(d)
    #         if res[0] in headers:
    #             print(res)
    #         element = list(d.items())
    #         print(element[0])
            for i,j in d.items():
                if i in headers:
    #                 print(i,j)
                    worksheet.write(row, col, i)
                    worksheet.write(row, col+1, j)
                    row+= 1
                
    #         list_of_page.append(exam)
 
    workbook.close()

# for link in links:
    
#     getSeperateNgoDetails(link)

getSeperateNgoDetails() 
    
# getting all ngos from one page
