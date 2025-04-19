# qrcode
This is a simple Python script that generates a QR code from user-provided text or URL and saves it as an image file.

How It Works
The script asks the user to input any text or URL.

It then prompts the user to provide a name for the image file (make sure to include .png as the extension).

Using the qrcode library, it generates a QR code based on the input.

The QR code is saved as an image file with the given name.

Example
Enter URL or text: https://example.com
Enter the name for the img file with extension (.png): example_qr.png
This will create a QR code image named example_qr.png in the same directory.

Requirements
Python 3.x

qrcode library

You can install the qrcode library using pip:
pip install qrcode

Notes
You may have to install Pillow for Image handling which can be done by installing Pillow library:
pip install Pillow

Make sure to provide a valid filename with .png extension.

The script uses the default QR code settings (simple and minimal configuration)
