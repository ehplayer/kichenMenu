import json
from urllib.request import urlopen
from urllib.request import urlretrieve


apiUrl = 'http://10.113.112.16:3002/todayFood'

if __name__ == '__main__':
    data = json.loads(urlopen(apiUrl).read())
    for idx, food in enumerate(data["foodList"]):
        urlretrieve(food["background"], "./" + str(idx) + ".jpg")
