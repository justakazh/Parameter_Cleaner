import sys

lists = sys.argv[1]

with open(lists, "r") as listss:

	site = listss.readlines()
	print("[+] Filtering . . . ")
	for sites in site:
		x = sites.split("/")
		open("filterd.txt", "a").write("http://"+x[2]+"\n")
