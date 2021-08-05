import qrcode

print("Enter the Text or URL which you want to encode \n")
text = input()

print("Enter the Colour of QR Code you want \n ")
input1 = input()

print("Enter hte Vack Colour You want ")
input2 = input()


print("Enter the file Name which you want to save the file (Please also enter the Extension) ")
input3 = input()



new = qrcode.QRCode(version = 1,box_size = 10,border = 5)




new.make(fit = True)
img = new.make_image(fill_color = input1,back_color = input2)

img.save(input3)

