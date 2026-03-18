
import pandas as pd
import bs4
import requests

price_list=[]
area_list=[]
locations_list=[]
rooms_list=[]
constryr_list=[]

r = requests.get("https://www.imobiliare.ro/vanzare-apartamente/judetul-constanta")
soup = bs4.BeautifulSoup(r.content, 'html.parser')

npages = soup.find_all("li", class_="page-item")[4].get_text(strip=True) #BUN

for i in range(2, int(npages) + 1):
    #Find the number of webpages in the request
    r = requests.get("https://www.imobiliare.ro/vanzare-apartamente/judetul-constanta?page=" + str(i))
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    apartment = soup.find_all("div", class_="block flex flex-col justify-between gap-y-3 overflow-hidden")
    for j in apartment:
        #Getting the attributes for every apartment found in a page
        try:
            pricebrut = j.find("div", class_="inline-flex items-center")
            price = pricebrut.get_text(strip=True).split(" ")[0].replace(".", "")
            inform = j.find_all("span", class_="whitespace-nowrap")
            constryr = inform[3].get_text(strip=True).split(" ")[0]
            rooms = inform[0].get_text(strip=True).split(" ")[0]
            area = inform[1].get_text(strip=True).split(" ")[0].replace(",", ".")
            locationbrut = j.find("p", class_="w-full truncate font-normal capitalize")
            location = locationbrut.get_text(strip=True)
            locations_list.append(location)
            rooms_list.append(rooms)
            constryr_list.append(constryr)
            area_list.append(area)
            price_list.append(price)
        except:
            continue

#Constructing the dataframe
di = {"Price": price_list, "Area": area_list, "Location": locations_list, "Construction year": constryr_list, "Rooms": rooms_list}
table = pd.DataFrame(di)
table.to_csv("Data.csv", index=False)