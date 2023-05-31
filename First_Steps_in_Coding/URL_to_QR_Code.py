import pyqrcode
import png
from pyqrcode import QRcode

address = 'https://www.tu-plovdiv.bg/students.php'
url = pyqrcode.create(address)
url.png('example_qr.png', scale=8)