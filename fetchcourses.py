from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from globalvar import *

def getTable(driver,table:list,id:int) -> list:
    '''
    popola table con i dati presenti nella tabella degli esami
    '''
    timeout = [2,1]
    try:
        el = WebDriverWait(driver,timeout[id-1]).until(
            EC.presence_of_all_elements_located((By.XPATH,EXAM_TABLE_XPATH.format(id,id)))
        )
    except Exception as e:
        if DEBUG:
            print(e)
    finally:
        time.sleep(0.1*WAIT_TIME) #
        rows = driver.find_elements(By.XPATH,EXAM_TABLE_XPATH.format(id,id))
        if len(rows):
            for row in rows:
                children = row.find_elements(By.XPATH,"./child::*") # ritorna tutti i children
                table.append([c.text for c in children])
    

def getExamsTableChrome(url:str) -> list:
    '''
    driver: Chrome
    ritorna una lista contenente i dati della tabella degli esami presente in "iscrizione agli esami".
    ogni riga della tabella è un corso
    '''
    from selenium.webdriver.chrome.options import Options
    options = Options()
    if not DEBUG:
        options.add_argument('log-level=3')
    print(textDict[LANG]['starting'],end='')

    driver = webdriver.Chrome('./chromedriver',options=options)
    driver.get(url)
    print(textDict[LANG]['authStart'].format(driver.title))

    # auth loop
    while(driver.title != "Portale servizi"):
        if driver.title == 'Polimi - Password in scadenza': # password scaduta o in scadenza
            driver.find_element(By.XPATH,"//button").click()
    print(textDict[LANG]['authEnd'])
    try:    # async per caricamento
        WebDriverWait(driver,10).until(                    
            EC.presence_of_element_located((By.XPATH,"//li[@data-idsezione='8']"))
        )
    finally:
        if driver.find_element(By.XPATH,"//li[@data-idsezione='8']").get_attribute("class") != "srvSection": # se tab chiuso
            driver.find_element(By.XPATH,"//li[@data-idsezione='8']//a").click()
        time.sleep(0.1*WAIT_TIME)
        driver.find_element(By.ID,ISCRIZIONE_AGLI_ESAMI_ID).click() # iscrizione agli esami
        
        try:
            WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,ANNO_ACCADEMICO_CORRENTE_ID))
            )
        finally:
            tabellaEsami = []

            driver.find_element(By.ID,ANNO_ACCADEMICO_CORRENTE_ID).click() # anno accademico corrente
            getTable(driver,tabellaEsami,1)
            driver.find_element(By.ID,ANNO_ACCADEMICO_PASSATO_ID).click() # anno accademico precedente
            getTable(driver,tabellaEsami,2)

            driver.close()
            return tabellaEsami

def parseTime(data:str) -> datetime:
    '''
    ritorna un oggetto datetime.date() da una stringa
    '''
    data = data.split('/')
    data = [int(d) for d in data]
    return datetime(data[2],data[1],data[0]).date()

def tableToDict(table:list) -> list:
    '''
    ritorna una lista di dizionari. Ogni dizionario contiene i campi di un evento
    '''
    esamiLista = []
    for rows in table:
        appelli = rows[4].split('\n')
        for app in appelli:
            data,tipo = app.split(':')
            tempdict = {}
            tempdict['summary'] = rows[0]
            tempdict['description'] = tipo.strip()
            tempdict['dtstart'] = parseTime(data)
            esamiLista.append(tempdict)
    if DEBUG:
        for e in esamiLista:
            for k,v in e.items():
                print("{}:\t{}".format(k,v))
    return esamiLista
