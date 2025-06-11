from variables.main import alphabets,delimiter
def Encode_Message(each_letter):
  encoded_sentence_index=[alphabets.find(l)-3 for l in each_letter]

  encoded_message=[alphabets[x] for x in encoded_sentence_index]
  
  return delimiter.join(encoded_message)