import icalendar
from globalvar import *
from fetchcourses import *


filename = "{}.ics".format(DEFAULT_CALENDAR_NAME[LANG] + MESI[LANG][int(datetime.today().strftime("%m"))-1] + datetime.today().strftime("%Y"))

def createFile(calendar):
    with open(filename,"wb") as f:
        f.write(calendar.to_ical())
    
if __name__ == "__main__":
    calendar = icalendar.Calendar()
    calendar.add('prodid','-//examsCalendar//')
    calendar.add('version','2.0')

    esami = tableToDict(getExamsTableChrome(authUrl))
    print(textDict[LANG]['generating'])
    for evt in esami:
        newEvent = icalendar.Event()
        for k,v in evt.items():
            newEvent.add(k,v)
        calendar.add_component(newEvent)
    createFile(calendar)
    print(textDict[LANG]['ready'].format(filename))


