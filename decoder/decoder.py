from variables.main import alphabets,delimiter
def Decoded_Message(word_index_in_alphabet):
    sentence=[]
    for x in word_index_in_alphabet:
        if x < 0 :
          x=-1
        sentence.append(x)
    decoded_sentence=[alphabets[x] for x in sentence]
    return delimiter.join(decoded_sentence).replace('z',' ')