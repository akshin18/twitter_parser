from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium import webdriver
# from telegram import *
import asyncio


def aprona():


    driver = webdriver.Opera()
    driver.get(f'https://mobile.twitter.com/{appa}')
    WebDriverWait(driver, 15).until(Ec.presence_of_element_located((By.XPATH, '''//main//div[@class='css-1dbjc4n']//section//div[@class='css-1dbjc4n']//article''')))
    a = driver.find_elements_by_xpath('''//main//div[@class='css-1dbjc4n']//section//div[@class='css-1dbjc4n']//article''')
    pinned = driver.find_elements_by_xpath('''//div[@class='css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l']''')
    number = 0
    for i in pinned:
        b = i.find_elements_by_xpath('''div/div/div//span''')
        for j in b:
            if j.text == 'Закрепленный твит' or j.text == 'Pinned Tweet':
                number = 1
                break
        break
    a[number] = a[number]
    zata = ' '.join((a[number].find_element_by_xpath(
        '''div//div[@class='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']''').text).split())
    kapa = [x.get_attribute('src') for x in a[number].find_elements_by_xpath(
        '''div//div[@class='r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-ipm5af r-13qz1uu']//img[@alt='Изображение']''')]
    return (zata,kapa)



#
# tuta = aprona('abdullazade4503')
# print(tuta)