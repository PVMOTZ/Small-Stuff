import random, string

file=open("senha.txt","w+")
for a in range  (0, 50000):
		x = ''.join(random.choices(string.digits, k=10))
		count = 0	
		linha = file.readline(0)
		if x != linha:
				file.write(x+"\n")
				count +=1		
file.close()

file=open("senhamin.txt","w+")
for a in range  (0, 5):
		x = ''.join(random.choices(string.digits, k=10))
		count = 0	
		linha = file.readline(0)
		if x != linha:
				file.write(x+"\n")
				count +=1		
file.close()