#!/usr/bin/python
#coding: utf-8

# Author: Marcelo Váquez (aka S4vitar)

import requests, re, getpass, urllib3, sys

main_url="https://www.hackthebox.eu/login"
download_vpn_url="http://www.hackthebox.eu/home/htb/access/ovpnfile"

if len(sys.argv) != 2:
	print "\n[!] An error has ocurred\n"
	sys.exit(1)

filename = sys.argv[1]

if __name__ == '__main__':

	try:
		s = None

		urllib3.disable_warnings()
		s = requests.session()
		s.verify = False
		s.keep_alive = False

		email = raw_input("Email: ")
		password = getpass.getpass()

		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

		r = s.get(main_url, headers=headers)
		token_value = re.findall(r'name="_token" value="(.*?)"', r.text)[0]

	        data_post = {
	        	'email': '%s' % (email),
	            'password': '%s' % (password),
				'_token': '%s' % (token_value)
	        }

		r = s.post(main_url, data=data_post, headers=headers)
		r = s.get(download_vpn_url, headers=headers)

		f = open("%s" % filename, "w")
		f.write(r.text)
		f.close()

	except:
		sys.exit(1)

