import base64

message = "Hello Cyber Security!"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("Encoded Message:", base64_message)

decoded_bytes = base64.b64decode(base64_bytes)
decoded_message = decoded_bytes.decode('ascii')

print("Decoded Message:", decoded_message)
