from app.thread.GetWeather import *

from app.thread.GetMise import *


print('app_run!!')
# print(time.gmtime())
print(strftime("%Y%m%d", time.localtime()))
print(strftime("%H%M", time.localtime()))

get_weather(600)
print('get_weather')
get_mise(600)
print('get_mise')
