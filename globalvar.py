from json import load
with open("settings.json",'r') as jsonfile:
    jsondict = load(jsonfile)
with open("text.json",'r') as jsonfile:
    textDict = load(jsonfile)
authUrl = "https://aunicalogin.polimi.it/aunicalogin/getservizio.xml?id_servizio=376"
ISCRIZIONE_AGLI_ESAMI_ID = "srv_vm_445"
ANNO_ACCADEMICO_CORRENTE_ID = "ui-id-1"
ANNO_ACCADEMICO_PASSATO_ID = "ui-id-2"
EXAM_TABLE_XPATH = "//div[@id='{}']//table[@class='col-md-12 table-bordered table-striped table-condensed cf']/tbody/tr"
WAIT_TIME = jsondict['wait time'] 
DEFAULT_BROWSER = jsondict['browser']
DEFAULT_CALENDAR_NAME = {
    'IT' : "CalendarioEsami",
    'EN' : "ExamsCalendar"
}
MESI = {
    'IT' : ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'],
    'EN' : ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
}
LANG = jsondict['language'] 
DEBUG = 0