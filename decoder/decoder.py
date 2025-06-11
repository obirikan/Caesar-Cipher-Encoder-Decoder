from variables.main import alphabets, delimiter,OFFSET

def Decoded_Message(encoded_letters):
    decoded_message = []
    for l in encoded_letters:
        if l == ' ':
            decoded_message.append(' ')
        else:
            new_index = (alphabets.find(l) + OFFSET) % 26
            decoded_message.append(alphabets[new_index])
    return delimiter.join(decoded_message)