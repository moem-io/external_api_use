from app.thread.GetWeather import *

from app.thread.GetMise import *
from multiprocessing import Process


print('app_run!!')
print(time.gmtime())
print(strftime("%Y%m%d", time.localtime()))
print(strftime("%H%M", time.localtime()))

# get_weather(600)
weather = Process(target=get_weather, args=(600,))
weather.start()
print('get_weather')

# get_mise(600)
mise = Process(target=get_mise, args=(600,))
mise.start()
print('get_mise')
