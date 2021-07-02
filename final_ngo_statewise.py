import requests
from bs4 import BeautifulSoup
import os
import xlsxwriter
from itertools import chain
import itertools

all_cities_url = []
def find_states():
    
    state = str(input("Enter your valid state URL \n"))
    if (state == "https://www.indiangoslist.com/andaman-and-nicobar-island-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,3):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
        
    elif (state == "https://www.indiangoslist.com/andhra-pradesh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,398):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/arunachal-pradesh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,27):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/assam-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,186):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/bihar-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,324):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/chandigarh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,16):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/chhattisgarh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,100):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
             
            
    elif (state == "https://www.indiangoslist.com/dadra-and-nagar-haveli-ngos-list"):
        all_cities_url.append(state)
        
    elif (state == "https://www.indiangoslist.com/daman-and-diu-ngos-list"):
        all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/delhi-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,554):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/goa-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,15):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/gujarat-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,364):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/haryana-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,145):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/himachal-pradesh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,49):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/jammu-and-kashmir-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,39):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/jharkhand-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,143):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/karnataka-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,418):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/kerala-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,216):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/ladakh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,8):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/lakshadweep-ngos-list"):
        all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/madhya-pradesh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,396):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/maharashtra-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,994):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/manipur-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,180):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/meghalaya-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,22):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/mizoram-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,14):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/nagaland-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,35):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/orissa-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,314):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/puducherry-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,19):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/punjab-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,92):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/rajasthan-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,289):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/sikkim-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,10):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/tamil-nadu-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,544):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/telangana-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,106):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/tripura-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,33):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/uttar-pradesh-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,1171):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/uttarakhand-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,68):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
        
    elif (state == "https://www.indiangoslist.com/uttarkhand-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,45):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    elif (state == "https://www.indiangoslist.com/west-bengal-ngos-list"):
        all_cities_url.append(state)
        state = state + "/"
        for i in range(2,673):
            ss = str(i)
            state = state + ss
            all_cities_url.append(state)
            
    else:
        print("This is invalid URL for state \nPlease enter valid state URL for getting ngo data of specific state")
    
            
    return all_cities_url
#     Get links for one page of ngo 
    
find_states()


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

        
    
links = []   
for i in range(len(all_cities_url)):
    ngos = getCitiesUrls(all_cities_url[i])

    for i in ngos:
        link = getNgos(i)
        links.append(link)


# links = []   
# for i in range(1):
#     ngos = getCitiesUrls(all_cities_url[i]) 
# #     getting seperate ngo links for every ngo page

#     for i in ngos:
#         link = getNgos(i)
#         links.append(link)
#         All ngo links will be saved in links list

workbook = xlsxwriter.Workbook("C:\\Users\\mahes\\Desktop\\ngo22.xlsx")

def getSeperateNgoDetails():
    
    for iteration, link in enumerate(links, start=1):
        r = requests.get(link)
        print(iteration)
        soup = BeautifulSoup(r.text, 'html.parser')

        images = soup.find_all('div', class_='ngo_line')

        list_of_page = []
        headers = ["NGO Name", "Unique Id of VO/NGO", "Chief Functionary", "Chairman", "Secretary", "Type of NGO", "Registration Number", "frca", "City", "State", "Telephone", "Mobile Number", "Address", "Email", "Website", "Key Issues"]
        
        if iteration:

            worksheet1 = workbook.add_worksheet()

            row  = 1
            col = 0

            for exam in images:
                res = exam.text.strip().replace("\n", "").split("   ")
                d = dict(itertools.zip_longest(*[iter(res)] * 2, fillvalue=""))

                for i,j in d.items():
                    if i in headers:
                        worksheet1.write(row, col, i)
                        worksheet1.write(row, col+1, j)
                        row+= 1

getSeperateNgoDetails() 
workbook.close()
