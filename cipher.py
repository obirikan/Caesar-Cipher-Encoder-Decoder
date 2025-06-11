from Tokenizer.main import Transfomer

input_sentence = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.' # decoder problem 
input_sentence = input_sentence.lower()

encoded_message,decoded_message=Transfomer(input_sentence)

print('Encoded Message',encoded_message)
print('Decoded Message',decoded_message)








