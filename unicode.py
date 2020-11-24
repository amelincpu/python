text_string = 'Hello © World'

print('\n', '*'*50, '\n', end='')
encoded_text = text_string.encode('utf-8')
print(type(encoded_text))
print(encoded_text)

print('\n', '*'*50, '\n', end='')
decoded_text = encoded_text.decode('utf-8')
print(type(decoded_text))
print(decoded_text)

print('\n', '*'*50, '\n', end='')
decoded_text = encoded_text.decode('utf-16')
print(type(decoded_text))
print(decoded_text)

print('\n', '*'*50, '\n', end='')