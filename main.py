from samino import Client
from samino import Local
from os import system as Z
from time import sleep as ZZ
#from X import keep_alive as X
from ujson import load as W
from datetime import datetime
def get_timers():
	return [{"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300} for _ in range(36)]
def timezone():
	timezones ={1: -120, 2: -180, 3: -240, 4: -300, 5: -360, 6: -420, 7: -480, 8: -540, 9: -600, 10: -660, 11: -720, 12: -780, 13: 600, 14: 540, 15: 480, 16: 420, 17: 360, 18: 300, 19: 240, 20: 180, 21: 120, 22: 60, 23: 0}
	return int(timezones[datetime.utcnow().hour])
while 1:
	for A in W(open("Coins.json")):
		E,P,D=A["email"],A["password"],A["device"]
		Ç=Client(deviceId=D,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
		ZZ(15)
		Ç.login(E,P)
		print(f"Login To {E}")
		S=Local(comId=175274808,proxies={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"})
		for X in range(24):
			try:
				Ç.join_community(comId=175274808)
				S.send_active_time(timers=get_timers(),tz=timezone())
				print(f"{X + 1} - Send Active")
				ZZ(2)
			except Exception as F:
				print(F)
