import requests
from pandas import *

def asin_scraping(Brand, Country):
    Brand_name = Brand
    Brand_name = Brand_name.replace(' ', '+')
    List_asins = []

    result_asins = DataFrame(columns=['Brand_name', 'ASIN', 'MP'])

    if Country == 'US':
        MP_link = 'https://www.amazon.com/s?k='
    elif Country == 'UK':
        MP_link = 'https://www.amazon.co.uk/s?k='
    elif Country == 'DE':
        MP_link = 'https://www.amazon.de/s?k='
    elif Country == 'FR':
        MP_link = 'https://www.amazon.fr/s?k='
    elif Country == 'ES':
        MP_link = 'https://www.amazon.es/s?k='
    elif Country == 'IT':
        MP_link = 'https://www.amazon.it/s?k='
    elif Country == 'CA':
        MP_link = 'https://www.amazon.ca/s?k='
    elif Country == 'IN':
        MP_link = 'https://www.amazon.in/s?k='
    else:
        print('Markerplace not Found')
        return

    print(MP_link)
    Temp_list = ''
    for pg_no in range(1, 21):
        while True:
            try:
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
                r = requests.get(MP_link + Brand_name + "&page=" + str(pg_no), headers=header)
                if r.status_code == 200:
                    break
            except:
                print('Trying')

        Page_Loaded = str(r.content.decode())
        a = 1
        while True:
            a = str(Page_Loaded).find('data-asin="', a)
            if a == -1:
                break
            b = a + len('data-asin="')
            c = str(Page_Loaded).find('"', b)
            Scraped_ASIN = str(Page_Loaded[b:c])
            if len(Scraped_ASIN) == 10:
                List_asins.append(Scraped_ASIN)
            a = a + 1

        for tag in List_asins:
            if Temp_list.find(str(tag)) == -1:
                Temp_list = str(Temp_list) + '##' + str(tag)
                print(Temp_list)
                Temp_DF = {'Brand_name': [Brand], 'ASIN': [str(tag)], 'MP': [Country]}
                result_asins = result_asins.append(DataFrame(Temp_DF), ignore_index=True)

    return result_asins


print(asin_scraping(Brand='HUGO BOSS', Country="US"))


