import os

print("Place csv's in a CSVs folder, ignores first line from each")
try:
    files = os.listdir(str(os.getcwd())+"\\CSVs")
    print("Got csv's: "+str(files))
except:
    print("Couldn't Get CSV's")

try:
    with open("CSVs/"+files[0], "r") as r:
        final = r.read().splitlines()[0]+"\n"
except:
    final = "FirstLine\n" # Final string of all combined

for File in files:
    with open("CSVs/"+File, "r") as r:
        tasks = r.read().splitlines()
    tasks.pop(0)
    for task in tasks:
        final += task + "\n"

try:
    with open("final.csv", "w") as w:
        w.write(final)
except:
    print("Error writing to file")

input("Done")