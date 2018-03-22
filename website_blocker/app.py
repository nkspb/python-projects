import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_to = "127.0.0.1"
block_list = ["www.vk.com", "vk.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working hours...")
		# open hosts file 
		with open(hosts_temp, 'r+') as file:
			# read contents of hosts file
			content = file.read()
			print(content)
			# check if site is in hosts
			for site in block_list:
				if site in content:
					pass
				else:
					# add if it's not
					file.write(redirect_to + " " + site + "\n")
	else:
		print("Fun hours")
		# open file
		with open(hosts_temp, 'r+') as file:
			# convert content to a list so that we can easily find
			# matches with block_list
			content = file.readlines()
			# move the pointer to the beginning, so we can
			# trancate the rest of the file later
			file.seek(0)
			# check for matches with block_list
			for line in content:
				if not any(site in line for site in block_list):
					# write line only if it doesn't contain a blocked site
					file.write(line)
			# truncate file, otherwise we append indefinitely
			file.truncate()	
	# stop cpu overload :)		
	time.sleep(5)


