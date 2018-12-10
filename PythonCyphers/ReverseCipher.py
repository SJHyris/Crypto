clrtxt = input('\nReverseCypher works both for encoding and decoding.\nEnter message:\n') 
cyphtxt = ''

i = len(clrtxt) - 1
while i >= 0:
    cyphtxt = cyphtxt +clrtxt[i]
    i = i - 1
    
print('\nOutput:\n'+ cyphtxt)
