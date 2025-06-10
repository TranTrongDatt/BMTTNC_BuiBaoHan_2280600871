import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_generate_keys.clicked.connect(self.call_api_generate_keys)
        self.ui.btn_Encrypt.clicked.connect(self.call_api_Encrypt)
        self.ui.btn_Decrypt.clicked.connect(self.call_api_Decrypt)
        self.ui.btn_Sign.clicked.connect(self.call_api_Sign)
        self.ui.btn_Verify.clicked.connect(self.call_api_Verify)

    def call_api_generate_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            print("Generate Keys Response:", response.text)
            if response.status_code == 200:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Generate keys successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_Encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_PlainText.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            print("Encrypt API Response:", response.text)
            if response.status_code == 200:
                data = response.json()
                # Sửa đúng key trả về từ API
                self.ui.txt_CipherText.setPlainText(data["encrypt_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_Decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_CipherText.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            print("Decrypt API Response:", response.text)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_PlainText.setPlainText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_Sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_Information.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            print("Sign API Response:", response.text)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_Signature.setPlainText(data["signature"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_Verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_Information.toPlainText(),
            "signature": self.ui.txt_Signature.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            print("Verify API Response:", response.text)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_verified"):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    QMessageBox.critical(self, "Verification Failed", "Signature is not valid!")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
