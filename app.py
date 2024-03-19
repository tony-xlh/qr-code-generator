import segno
def generate():
    #generate qr code using numeric mode
    qrcode = segno.make_qr("9780593230060",mode="numeric")
    print(qrcode.mode)
    qrcode.save('numeric.png', scale=2)
    #generate qr code using alphanumeric mode
    qrcode = segno.make_qr("DYNAMSOFT",mode="alphanumeric")
    print(qrcode.mode)
    qrcode.save('alphanumeric.png', scale=2)
    #generate qr code using kanji mode 
    qrcode = segno.make_qr("ディナムソフト",mode="kanji")
    print(qrcode.mode)
    qrcode.save('kanji.png', scale=2)
    #generate qr code using byte mode 
    qrcode = segno.make_qr("Dynamsoft",mode="byte")
    print(qrcode.mode)
    qrcode.save('byte-text.png', scale=2)
    #generate qr code containing a 1-bit image using byte mode 
    f = open("1-bit.png",mode="rb")
    qrcode = segno.make_qr(f.read(),mode="byte")
    print(qrcode.mode)
    qrcode.save('byte-image.png', scale=2)
    #generate qr code containing an 8-bit image using byte mode 
    f = open("8-bit.png",mode="rb")
    qrcode_seq = segno.make_sequence(f.read(), symbol_count=2)
    for qrcode in qrcode_seq:
        print(qrcode.mode)
        print(qrcode.version)
    qrcode_seq.save('structured_append.png', scale=2)

if __name__ == "__main__":
    generate()