import base64
image = open('deer.gif', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_decode = base64.decodestring(image_64_encode)
# create a writable image and write the decoding result
image_result = open('deer_decode.gif', 'wb')
image_result.write(image_64_decode)
