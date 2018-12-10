def main():
    clrtxt= input()
    key = input()
    cyphtxt = transEncrypt(key, clrtxt)

    print(cyphtxt + '|')

def transEncrypt(mkey, mclrtxt)
    cyphtxt = [''] * key
