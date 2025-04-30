def decode_helper(s, index, current_decoding, result, mapping):
    if index == len(s): 
        result.append("".join(current_decoding))
        return
    if s[index] in mapping:
        decode_helper(s, index + 1, current_decoding + [mapping[s[index]]], result, mapping)
    if index + 1 < len(s) and s[index:index+2] in mapping:
        decode_helper(s, index + 2, current_decoding + [mapping[s[index:index+2]]], result, mapping)

def decode_message(s):
    mapping = {str(i): chr(64 + i) for i in range(1, 27)}  
    result = []
    decode_helper(s, 0, [], result, mapping)
    return result

#user input
encoded_message = input("Enter the encoded message (numbers only): ")


if not encoded_message.isdigit():
    print("Invalid input! Please enter only numbers.")
else:
    decoded_messages = decode_message(encoded_message)
    print("Possible decoded messages:", decoded_messages)
