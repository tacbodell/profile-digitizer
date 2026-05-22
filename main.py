import sys
from PyQt6.QtWidgets import QApplication
from ui.pdf_canvas import PdfCanvas

def main():
    app = QApplication(sys.argv)

    window = PdfCanvas("../assets/plans.pdf")
    window.resize(800,600)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()