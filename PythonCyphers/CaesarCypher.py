#TO DO: parameters for: used Symbolsets, keys starting from 1 or 0and run all keys. Optimize Warpararound .

#symbolsets; add array for used symbolsets.
ALBET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
albet = 'abcdefghijklmnopqrstuvwxyz'
nums  = '0123456789'

SYMBOLS = [ALBET, albet, nums]

cyphtxt = ''
#INPUT
clrtxt= input('Enter your message\n')
key= input('Enter numeric key to decrypt. Skip to brute-force.\n')
mode= input('Enter (E)ncrypt or (D)ecrypt\n')
print(key)
#Single symbol en/dec function.



#check if selected mode is correct
if mode == 'E':
#||'e'||'Encrypt'||'encrypt':
    mode = 1
elif mode =='D':
#||'d'||'Decrypt'||'decrypt':
    mode = -1
else:
    mode = 0
    print('Not a valid mode. Enter encrypt/decrypt')

#Run caesar. To be updated with funcion and symbolsets for cicle and isset.
if mode:
    if key == '':
        for key in range(len(ALBET)):
            for symbol in clrtxt:
                checkset= len(cyphtxt)
                for symset in SYMBOLS:
                    if symbol in symset:
                        symIndex = symset.find(symbol)
                        cyphindex = int(symIndex) + int(key*mode)
                        if cyphindex >= len(symset):
                            cyphindex = cyphindex - len(symset)
                        elif cyphindex < 0:
                            cyphindex = cyphindex + len(symset)
                        cyphtxt = cyphtxt + symset[cyphindex]
                if checkset == len(cyphtxt):
                    cyphtxt = cyphtxt + symbol
            print('Key ' + str(key) +': '+ cyphtxt) 
            cyphtxt= ''
    else:
        for symbol in clrtxt:
            checkset= len(cyphtxt)
            for symset in SYMBOLS:
                if symbol in symset:
                    symIndex = symset.find(symbol)
                    cyphindex = int(symIndex) + int(key*mode)
                    if cyphindex >= len(symset):
                        cyphindex = cyphindex - len(symset)
                    elif cyphindex < 0:
                        cyphindex = cyphindex + len(symset)
                    cyphtxt = cyphtxt + symset[cyphindex]
            if checkset == len(cyphtxt):
                cyphtxt = cyphtxt + symbol
        print('Key ' + str(key) +': '+ cyphtxt) 

