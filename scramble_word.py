
#Note : "Srbmnacilg wrods is vrey itrensientg. Bscauee even if tehy are srelabcmd, it dosn'et ipcmat our raidneg. Bacusee we dn'ot raed lteetr by letetr, we raed the wrod as a wolhe."

import random
import re
def scramble_word():
    f1 = open("d://Learn//test_scramble.txt", "r")
    content = f1.read()
    f2 = open("d://Learn//new_text.txt", "w+")
    for word in content.split(" "):
        if len(word)>3:
            if re.search("^[A-Za-z]",word) !=None:
                temp_first = word[0]
                mid_start=1
            else:
                temp_first = word[:2]
                mid_start = 2
            if re.search("[A-Za-z]$",word) !=None:
                temp_last = word[-1]
                mid_last = -1
            else:
                temp_last=word[-2:]
                mid_last = -2
            temp_str = str(word[mid_start:mid_last]).lower()
            new_str = str(temp_first)+"".join(random.sample(temp_str, len(temp_str)))+str(temp_last)+ " "
        else:
            new_str=str(word)+ " "

        f2.write(new_str)
    f1.close()
    f2.close()
scramble_word()
