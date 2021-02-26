import requests
from bs4 import BeautifulSoup
def getCompanies():
    url = "https://theinternship.io/"
    web_data = requests.get(url)
    partner = []
    soup = BeautifulSoup(web_data.text, 'html.parser')
    find_data = soup.find_all("div", {"class":"partner"})
    for data in find_data :
        img = data.find("div",{"class":"logo-box"}).find("img",{"class":"center-logos"})['src']
        desc = data.find("div",{"class":"box-textbox"}).find("span",{"class":"list-company"}).text
        content = {"img":img, "desc":desc}
        partner.append(content)
    sort_list = sorted(partner, key=lambda k: len(k['desc']))
    return sort_list

def main():
    sort_list = getCompanies()
    for data in sort_list :
        print(data['img'])

if __name__ == "__main__" :
    main()