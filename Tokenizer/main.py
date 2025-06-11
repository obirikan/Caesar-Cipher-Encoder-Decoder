from decoder.decoder import Decoded_Message
from encoder.encoder import Encode_Message
from variables.main import alphabets
def Transfomer(input_sentence):
    
    each_letter=[]
    for word in input_sentence:
        each_letter.append(word)

    
    word_index_in_alphabet=[alphabets.find(l) for l in each_letter]
    
    encoded_message=Encode_Message(each_letter)
    
    decoded_message=Decoded_Message(word_index_in_alphabet)
    
    return encoded_message,decoded_message