from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


class MapBot:
    def __init__(self, lati, longi):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.ca/maps")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"q\"]")\
            .send_keys(lati,", ", longi)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@id=\"searchbox-searchbutton\"]")\
            .click()
        sleep(3)

    def Find_Prov(self):
        element = self.driver.find_element_by_xpath("//span[@class=\"widget-pane-link\"]")
        # print (element.text)

        arr = element.text
        # print(arr)

        self.driver.quit()

        provs = ["BC","AB","SK","MB","ON","QC","NB","PE","NS","NL","YT","NT","NU"]

        var = -1

        for i in range(len(arr)):
            if arr.find(provs[i]) != -1:
                var = provs[i]
                break       
        
        if var != -1:
            return var
        else:
            return "N/A"


def Find_City(area):
        provs1 = ["BC","AB","SK","MB","ON","QC","NB","PE","NS","NL","YT","NT","NU"]
        cities = []
        
        for i in range (len(provs1)):
            if area == provs1[i]:
                count = i

        if count == 0 or count == 10:
            cities.append("Vancouver")
            print(cities)
            return cities

        elif count == count == 2:
            cities.append("Regina")
            print(cities)
            return cities

        elif count == 3 or count == 12:
            cities.append("Winnipeg")
            print(cities)
            return cities

        elif count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
            cities.append("Montreal")
            print(cities)
            return cities
        
        elif count == 1 or count == 11:
            cities.append("Calgary")
            cities.append("Edmonton")
            print(cities)
            return cities

        elif count == 4:
            cities.append("Toronto")
            cities.append("Ottawa")
            cities.append("Hamilton")
            print(cities)
            return cities

  

# my_bot = MapBot('50.252282', '-82.880188')
# prov = my_bot.Find_Prov()
# # print (prov)

# city = Find_City(prov)

# print (list(city))


