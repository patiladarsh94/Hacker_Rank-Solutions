import random

#Note : "Srbmnacilg wrods is vrey itrensientg. Bscauee even if tehy are srelabcmd, it dosn'et ipcmat our raidneg. Bacusee we dn'ot raed lteetr by letetr, we raed the wrod as a wolhe."

def scramble_word():
	try:
		f1=open("d:\\Learn\\test_scramble","r")
		content=f1.read()
		f2=open("d:\\Learn\\new_text","w+")
		for str(word) in content:
			temp_first=word[0]
			temp_last=word[-1]
			temp_str=word[1:-1].ascii_lowercase
			new_str=temp_first+random.sample(temp_str,len(tmp_str))
			f2.write(new_str)
	except:
		f1.close()
	else:
		f1.close()
		f2.close()
