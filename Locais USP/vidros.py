# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

def waitForElementID(id):
    time.sleep(2)
    while len(driver.find_elements_by_id(id)) == 0:
        time.sleep(1)

driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "https://uspdigital.usp.br/"
    
driver.get(base_url)
waitForElementID("loginUsuario")

driver.find_element_by_id("loginUsuario").send_keys("5219009")
driver.find_element_by_id("senhaUsuario").send_keys("M5v-szy-vbH-YEc")
driver.find_element_by_id("botaoLogin").click()
waitForElementID("spanNomeUsuario")

#driver.get(base_url + "administrativo/admLocalListar?codatz=(156,158)&codmnu=8325")



with open("vidros.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for codloc,area in spamreader:
        # coloca area no formato nn.nn com duas casas após o separador
        area="{:.2f}".format(float(area.replace(",",".")))
        driver.get(base_url + "administrativo/admLocalForm?print=s&codlocusp="+codloc+"&modo=")
        waitForElementID("codlocusp")
        driver.find_element_by_id("ui-id-2").click()
        waitForElementID("dscitmmca")
        
        driver.find_element_by_id("dscitmmca").send_keys("s/exposição")
        time.sleep(1)
        driver.find_element_by_id("dscitmmca").send_keys(Keys.DOWN)
        driver.find_element_by_id("dscitmmca").send_keys(Keys.ENTER,Keys.TAB)
        driver.find_element_by_id("qtdmcaloc").send_keys(area)
        driver.find_element_by_id("botaoSalvarContrato").click()

        time.sleep(1)    

driver.quit()