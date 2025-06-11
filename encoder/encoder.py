from variables.main import alphabets, delimiter,OFFSET

def Encode_Message(each_letter):
    encoded_message = []
    for l in each_letter:
        if l == ' ':  
            encoded_message.append(' ')
        else:
            new_index = (alphabets.find(l) + OFFSET) % 26
            encoded_message.append(alphabets[new_index])
    return delimiter.join(encoded_message)