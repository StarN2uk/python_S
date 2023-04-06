f = open("anna.txt", "r")
while True:
   print(f.tell(), end = ' ')
   line = f.readline()
   print(line.strip())
   if not line : break