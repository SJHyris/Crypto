import base64
instr = input()
bytestr = bytes.fromhex(instr)
b64output = base64.b64encode(bytestr)
print(b64output)
