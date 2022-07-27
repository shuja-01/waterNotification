import time
from plyer import notification
if __name__ == '__main__':
	while True:
		notification.notify(
			title  =  "**Please Drink Water Now!!",
 			message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of  fluids a day for women.",
 			app_icon = "/media/shuja/6ae54a4c-3e64-4e0f-ac34-8ebdf1baf2fb/python/drink_water notification/Glass-Water.ico",
			timeout= 12
		)

		#In app icon variable write the path of the icon which you want to show in notification
		time.sleep(60*60)