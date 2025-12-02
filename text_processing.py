def text_to_bits(text):

    bits = []
    for char in text:
        num_val = ord(char)
        binary_string = format(num_val,'08b')
        for bit in binary_string:
            bits.append(int(bit))

    return bits

def bits_to_text(bits):
    
    text = ""
    for i in range(0,len(bits),8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break

        binary_string = "".join(map(str,byte))
        num_val = int(binary_string,2)
        char = chr(num_val)
        text+=char

    return text
