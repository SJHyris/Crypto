str1= b'this is a test'
str2 = b'wokka wokka!!!'
def hamming_distance(binary_seq_1, binary_seq_2):
    
    dist = 0
    print(zip(binary_seq_1, binary_seq_2))
    for bit1, bit2 in zip(binary_seq_1, binary_seq_2):
        diff = bit1 ^ bit2
        print(bin(diff))
        dist += sum([1 for bit in bin(diff) if bit == '1'])

    return dist

def counter(string):
    bytecount = 0
    for byte in string:
        bytecount += bin(byte).count('1')
    return bytecount

def edit_distance (str1, str2):
    count1 = counter(str1)
    count2 = counter(str2)
    print(count1, count2)
    dist = abs(count1-count2)
    return dist

distance = hamming_distance(str1, str2)
print(distance)
    
