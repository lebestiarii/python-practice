import qrcode

data = input("Enter text or a URL: ").strip()
file_name = input("Enter file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)