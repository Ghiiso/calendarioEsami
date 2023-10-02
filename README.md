# polimi-calendar
Script che permette di generare un file iCalendar (.ics) partendo dagli esami a cui uno studente si deve iscrivere. Lo script lancia una finestra browser a cui si può accedere utilizzando le proprie credenziali. Una volta effettuato l'accesso il browser si chiuderà automaticamente e il calendario sarà generato nella cartella di installazione.

### Impostazioni
È possibile modificare la lingua e il parametro `wait time` all'interno del file [settings.json](./settings.json). Il parametro `wait time` va incrementato solamente nel caso in cui lo script restituisca calendari senza titolo

## Prerequisiti
- Python 3
- pip o pip 3

## Dipendenze
Usare  ``` pip install -r requirements.txt ``` o  ``` pip3 install -r requirements.txt ``` nella cartella o nel virtualenv

## Usare il calendario
il file è utilizzabile in tutti i calendari che supportano il formato iCalendar. Di seguito sono riportate le guide specifiche:
- [Outlook](https://support.microsoft.com/en-us/office/import-calendars-into-outlook-8e8364e1-400e-4c0f-a573-fe76b5a2d379#:~:text=In%20Outlook%2C%20select%20File%20%3E%20Open,Select%20Open%20as%20New.)
- [Google Calendar](https://support.google.com/calendar/answer/37118?hl=it&co=GENIE.Platform%3DDesktop)
- [Apple Calendar](https://support.apple.com/it-it/guide/calendar/icl1023/mac) nella sezione *Importare eventi da un file calendario*
- [Thunderbird](https://support.mozilla.org/it/questions/1105153)

