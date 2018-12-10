CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 
    'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 
    'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 
    'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 
    'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 
    'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}
def main():
    cyph_array = [bytes.fromhex(line.strip()) for line in open("strings.txt")]

    plain_array = []
    for cyph in cyph_array:
        result = singlechar_xor(cyph)
        plain_array.append(result)
    sorted_results = sorted(plain_array, key=lambda c: c['score'], reverse=True)[0]
    pretty_print_result(sorted_results)
# for x in array:
# singlexor()
#
def acquire_array_from_file(filename):
    ciphtxts_array = open(filename, 'r').readlines()
    for ciphtxt in ciphtxts_array:
        ciphtxt = bytes.fromhex(ciphtxt)
    return ciphtxts_array
def pretty_print_result(result):
    """Prints the given resulting candidate in a pretty format."""
    print(result['plaintext'].decode().rstrip(), "\tScore:", "{0:.2f}".format(result['score']),
          "\tKey:", chr(result['key']))




#must take a single string and try against all possible values.
#returns best.
def singlechar_xor(CYPH):  
    best_score = 0
    for possible_key in range(256):
        output = b''

        for char in CYPH:
            output += bytes([char ^ possible_key])

        score = scoring_function(output)
        if score > best_score:
            best_score = score

            result = {
                'key': possible_key,
                'score': score,
                'plaintext': output
            }
    return result


#takes a single plaintext and scores it.
def scoring_function(plaintext):
    score = 0
    for single_byte in plaintext:
        score += CHARACTER_FREQ.get(chr(single_byte).lower(), 0)
    return score


main()
