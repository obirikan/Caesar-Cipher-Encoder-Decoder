from decoder.decoder import Decoded_Message
from encoder.encoder import Encode_Message

def Transformer(input_sentence):
    each_letter = list(input_sentence.lower())
    
    decoded_message = Decoded_Message(each_letter)
    
    encoded_message = Encode_Message(each_letter)
    
    return encoded_message, decoded_message