from flask import *
from flask_cors import CORS
from colorama import Fore

centuryDates = [2, 0, 5, 3]
monthIndex = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
thirtyDayMonths = [4, 6, 9, 11]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])

def home_page():
    data_set ={'Page': 'Home', 'Message': 'Successfully loaded the Home page'}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/date/', methods=['GET'])
def request_page():
    try:
        date = str(request.args.get('date')) #/date/?date=Ansh8!

        _date = date.split("/")
        month = int(_date[0])
        day = int(_date[1])
        year = int(_date[2])

        _year = year%100
        century = year - _year

        partYear = centuryDates[int((century/100)%4)] + _year + ((_year - (_year%4))/4)
        partDate = 0

        if _year%4 == 0 and month < 3:
            _monthIndex = monthIndex[month-1]+1
        else:
            _monthIndex = monthIndex[month-1]

        partDate = day - _monthIndex
        weekDay = (partDate+partYear)%7
        actualDay = days[int(weekDay)]
        data_set ={'Page': 'Request', 'Date': f'{date}', 'Day': f'{actualDay}'}

        json_dump = json.dumps(data_set)
        print("\nResponse: \n" + Fore.GREEN + str(data_set) + "\n" + Fore.WHITE)
        return json_dump
    except (ValueError, IndexError):
        data_set = {'Page': 'Request', 'Date': f'{date}', 'Day': 'None'}
        print("\nResponse: \n" + Fore.RED + str(data_set) + "\n" + Fore.WHITE)
        json_dump = json.dumps(data_set)
        return json_dump

