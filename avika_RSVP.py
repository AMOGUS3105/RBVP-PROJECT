print("SHIFTED SECRETS: CAESAR'S KEY".center(50,'#'))
print('Enter 1 to encrypt and 2 to decrypt'.center(50,'#'))
CHOICE=int(input('Enter='))
import random
ran= random.randint(1,26)
if CHOICE==1:
	print('ENCRYPTOR'.center(49,'#'))
	s=input('Enter string=')
	S=s.upper()
	print('STRING=',S)
	l=list(S)
	for i in l:
		x=l.index(i)
		l[x]=ord(i)
	y=0
	for j in l:
		j+=ran
		l[y]=j
		y+=1
	for k in l:
		z=l.index(k)
		l[z]=chr(k)
	str=''.join(l)
	print('ENCRYPTED STRING=',str,'\n','Key=',ran)
elif CHOICE==2:
	print('DECRYPTOR'.center(49,'#'))
	key=int(input('Enter key='))
	s=input('Enter string=')
	print('STRING=',s)
	l=list(s)
	for i in l:
		x=l.index(i)
		l[x]=ord(i)
	y=0
	for j in l:
		j-=key
		l[y]=j
		y+=1
	for k in l:
		z=l.index(k)
		l[z]=chr(k)
	str=''.join(l)
	print('DECRYPTED STRING=',str)
else:
	print('PLEASE ENTER VALID NO.')
X=input("--")	
