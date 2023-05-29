# Code by Yutix
# donate: https://saweria.co/lordyutix

import sys
import requests as req
req.urllib3.disable_warnings()
from colorama import Fore,Style
from multiprocessing import Pool
from multiprocessing.dummy import Pool as DeadPool

red    = Fore.RED
yellow = Fore.YELLOW
blue   = Fore.BLUE
reset  = Style.RESET_ALL
bold   = Style.BRIGHT
green  = Fore.GREEN
white  = Fore.WHITE
dim    = Style.DIM
purple = Fore.MAGENTA
cyan   = Fore.CYAN

class Gaskeun:
	def __init__(self,situs):
		self.url = situs if "://" in situs else "http://" + situs
		self.dei = 0
		self.x()
	
	def x(self):
		try:
			raw = req.get(self.url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'},timeout=5,verify=False).text
			if "PhpDebugBar.DebugBar" in raw:
				print(f" {reset}{green}[ FOUND ] {reset}{white}{self.url}")
				open("founds.txt","a").write(f"{self.url}\n")
			else:
				print(f" {reset}{red}NOT FOUND {reset}{reset}{dim}{self.url}")
				
		except req.exceptions.Timeout:
			if self.dei == 5:
				print(f" {reset}{red}-TIMEOUT- {reset}{dim}{self.url}")
			else:
				print(f" {reset}{yellow}[ RETRY ] {reset}{dim}{self.url}")
				self.dei += 1
				self.x()
			
		except Exception as er:
			print(f" {reset}{red}NOT FOUND {reset}{dim}{white}{self.url}")
				
		except KeyboardInterrupt:
			print(f"\r {reset}Killed. ", end="", flush=True)
			exit()
	
print(f"""{reset}
  ____ ___ 
  )  =\  =\   v1       
 /    =\  =\       {cyan}Laravel Debugbar Scanner{reset}
 \      `-._`-._   Created by YutixCode
  )__(`\____)___)  bug report: {white}t.me/yutixverse
""")

def main():
	try:
		file = open(input(f"{reset}{white}  > File: {cyan}")).read().splitlines()
		pool = int(input(f"{reset}{white}  > Thread: {cyan}"))
		
		print()
		
		DeadPool = Pool(pool)
		DeadPool.map(Gaskeun, file)
		DeadPool.close()
		DeadPool.join()
		
		print(f"{reset}{white}Help me to buy a pc: {cyan}https://saweria.co/lordyutix")
		
	except FileNotFoundError:
		print(f"\n {red}ERROR {reset}File not found")
		
	except ValueError:
		print(f"\n {red}ERROR {reset}Thread must be a number")
		
	except KeyboardInterrupt:
		exit()

if __name__ == "__main__":
    main()