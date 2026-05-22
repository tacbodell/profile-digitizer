import fitz
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt

class PdfCanvas(QWidget):
    def __init__(self, pdf_path):
        super().__init__()

        #Open the PDF and render page 0 to raw bytes
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap()
        
        # Load those bytes into a QPixmap Qt can draw
        self._pixmap = QPixmap()
        self._pixmap.loadFromData(pix.tobytes("ppm"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._pixmap)