# Steganography - utility, that encrypts plain text in image
from stegano import lsb  # stegano method, which replace low RGB bits in image
from stegano import exifHeader  # the same as lsb, but works with .jpb and understands correctly Cyrillic
from steganocryptopy.steganography import Steganography  # For generate encryption key and encrypt big data


def lsb_method(img_plain: str, text: str, img_encrypt: str):
    crypt = lsb.hide(img_plain, text)
    crypt.save(img_encrypt)


def exifHeader_method(img_plain: str, text: str, img_encrypt: str):
    crypt = exifHeader.hide(img_plain, img_encrypt, text)


def steganography_method(img_plain: str, txt: str, img_encrypt: str):
    Steganography.generate_key("")
    crypt = Steganography.encrypt("key.key", img_plain, txt)
    crypt.save(img_encrypt)


def main():
    img1 = input('Enter path to plain img: ')
    img2 = input('Enter path to encrypt img: ')
    txt = input('Enter plain text: ')
    # lsb_method(img1, txt, img2)
    # exifHeader_method(img1, txt, img2)
    steganography_method(img1, txt, img2)


if __name__ == '__main__':
    main()
