import Client
from ujson import load as A
from time import sleep as ZZ
while 1:
	for W in A(open("Coins.json")):
		E,P,D=W["email"],W["password"],W["device"]
		Ç=Client.Client(D)
		Ç.login(E,P)
		print(f"Login  {E}")
		for S in range(25):
			try:
				Ç.send_active(175274808)
				print(f"{S + 1} Send Activity");ZZ(15)
			except Exception as F:
				print(F)
				pass
