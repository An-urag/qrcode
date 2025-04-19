import qrcode as qrc
te = input("Enter URL or text:")
name = input("Enter the name for the img file with extension (.png):")
img = qrc.make(te)
img.save(name)