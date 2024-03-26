print(ascii('ördöngös'))
print(ascii('𝔸𝔹ℂ𝓚'))

text = "これは日本語の文字列です: 'ördöngös'"

bytes_data = ascii(text).encode('utf-8')
print(bytes_data)
