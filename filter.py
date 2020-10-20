listn = [i.strip() for i in open(raw_input("input list >>"), "r").readlines()]
print("[+] Filtering . . . ")
for i in listn:
    x = i.split("/")
    open("filtered.txt", "a").write("http://"+x[2]+"\n")
