from PIL import Image

def num_to_bits(num):
    bits = []
    for i in range(16):
        bit = num & 1
        bits.append(bit)
        num = num >> 1
    return bits[::-1] #reverse the bits

def bits_to_num(bits):
    num = 0
    for bit in bits:
        num = (num << 1) | bit
    return num

def embed_bits(bits_list,img_path,output_path):
    img = Image.open(img_path).convert('RGB')
    pixels = img.load()
    width, height = img.size
    bits_len = len(bits_list)

    msg_len = len(bits_list)
    len_bits = num_to_bits(msg_len)
    all_bits = len_bits + bits_list

    total_bits = len(all_bits)

    if width*height*3 < total_bits:
        return 'Too many bits!'
    
    bit_index = 0
    
    for y in range(height):
        for x in range(width):

            if bit_index >= total_bits:
                img.save(output_path)
                return

            r,g,b = pixels[x,y]

            # --- Red ---
            if bit_index < total_bits:
                r = (r & 254) | all_bits[bit_index] # (r & 11111110) ==> 0 at the LSB , | bit ==> LSB = bit (False OR (X) = X)
                bit_index += 1

            # --- Green ---
            if bit_index < total_bits:
                g = (g & 254) | all_bits[bit_index]
                bit_index += 1

            # --- Blue ---
            if bit_index < total_bits:
                b = (b & 254) | all_bits[bit_index]
                bit_index += 1  

            pixels[x,y] = (r,g,b)

    img.save(output_path, "PNG", compress_level=0)


def extract_bits(img_path):
    img = Image.open(img_path).convert('RGB')
    pixels = img.load()
    width, height = img.size
    
    bits_list = []
    msg_length = None   

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            bits_list.append(r & 1)
            bits_list.append(g & 1)
            bits_list.append(b & 1)

            if msg_length is None and len(bits_list) >= 16:
                len_bits = bits_list[:16]
                msg_length = bits_to_num(len_bits)

            if msg_length is not None:
                total_needed = 16 + msg_length
                if len(bits_list) >= total_needed:
                    return bits_list[16:total_needed]

    return bits_list







    

    