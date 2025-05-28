from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Router routes for home page
@app.route('/')
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    if not request.form:
        return render_template('caesar.html', encrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputPlainText')
    key = request.form.get('inputKeyPlain')
    
    if not text or not key:
        return render_template('caesar.html', encrypt_error="Thiếu plain_text hoặc key")
    
    try:
        key = int(key)
        Caesar = CaesarCipher()
        try:
            encrypted_text = Caesar.encrypt_text(text, key)
            return render_template('caesar.html', encrypt_result=encrypted_text)
        except ValueError:
            return render_template('caesar.html', encrypt_error="Văn bản chứa ký tự không hợp lệ (chỉ dùng A-Z)")
    except ValueError:
        return render_template('caesar.html', encrypt_error="Key phải là số nguyên")

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    if not request.form:
        return render_template('caesar.html', decrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputCipherText')
    key = request.form.get('inputKeyCipher')
    
    if not text or not key:
        return render_template('caesar.html', decrypt_error="Thiếu cipher_text hoặc key")
    
    try:
        key = int(key)
        Caesar = CaesarCipher()
        try:
            decrypted_text = Caesar.decrypt_text(text, key)
            return render_template('caesar.html', decrypt_result=decrypted_text)
        except ValueError:
            return render_template('caesar.html', decrypt_error="Văn bản chứa ký tự không hợp lệ (chỉ dùng A-Z)")
    except ValueError:
        return render_template('caesar.html', decrypt_error="Key phải là số nguyên")

# Router routes for vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    if not request.form:
        return render_template('vigenere.html', encrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputPlainText')
    key = request.form.get('inputKeyPlain')
    
    if not text or not key:
        return render_template('vigenere.html', encrypt_error="Thiếu plain_text hoặc key")
    
    if not key.isalpha():
        return render_template('vigenere.html', encrypt_error="Key phải chứa chỉ chữ cái A-Z")
    
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return render_template('vigenere.html', encrypt_result=encrypted_text)

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    if not request.form:
        return render_template('vigenere.html', decrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputCipherText')
    key = request.form.get('inputKeyCipher')
    
    if not text or not key:
        return render_template('vigenere.html', decrypt_error="Thiếu cipher_text hoặc key")
    
    if not key.isalpha():
        return render_template('vigenere.html', decrypt_error="Key phải chứa chỉ chữ cái A-Z")
    
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return render_template('vigenere.html', decrypt_result=decrypted_text)

# Router routes for playfair cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    if not request.form:
        return render_template('playfair.html', encrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputPlainText')
    key = request.form.get('inputKeyPlain')
    
    if not text or not key:
        return render_template('playfair.html', encrypt_error="Thiếu plain_text hoặc key")
    
    if not key.isalpha():
        return render_template('playfair.html', encrypt_error="Key phải chứa chỉ chữ cái A-Z (không dùng J)")
    
    try:
        Playfair = PlayFairCipher()
        matrix = Playfair.create_playfair_matrix(key)
        encrypted_text = Playfair.playfair_encrypt(text, matrix)
        return render_template('playfair.html', encrypt_result=encrypted_text)
    except ValueError:
        return render_template('playfair.html', encrypt_error="Văn bản chứa ký tự không hợp lệ (chỉ dùng A-Z, không dùng J)")

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    if not request.form:
        return render_template('playfair.html', decrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputCipherText')
    key = request.form.get('inputKeyCipher')
    
    if not text or not key:
        return render_template('playfair.html', decrypt_error="Thiếu cipher_text hoặc key")
    
    if not key.isalpha():
        return render_template('playfair.html', decrypt_error="Key phải chứa chỉ chữ cái A-Z (không dùng J)")
    
    try:
        Playfair = PlayFairCipher()
        matrix = Playfair.create_playfair_matrix(key)
        decrypted_text = Playfair.playfair_decrypt(text, matrix)
        return render_template('playfair.html', decrypt_result=decrypted_text)
    except ValueError:
        return render_template('playfair.html', decrypt_error="Văn bản chứa ký tự không hợp lệ (chỉ dùng A-Z, không dùng J)")

@app.route('/playfair/create_matrix', methods=['POST'])
def playfair_create_matrix():
    if not request.form:
        return render_template('playfair.html', matrix_error="Yêu cầu không hợp lệ")
    
    key = request.form.get('inputKeyMatrix')
    
    if not key:
        return render_template('playfair.html', matrix_error="Thiếu key")
    
    if not key.isalpha():
        return render_template('playfair.html', matrix_error="Key phải chứa chỉ chữ cái A-Z (không dùng J)")
    
    try:
        Playfair = PlayFairCipher()
        matrix = Playfair.create_playfair_matrix(key)
        return render_template('playfair.html', matrix_result=matrix)
    except ValueError:
        return render_template('playfair.html', matrix_error="Không thể tạo ma trận từ key")

# Router routes for railfence cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    if not request.form:
        return render_template('railfence.html', encrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputPlainText')
    rails = request.form.get('inputRailsPlain')
    
    if not text or not rails:
        return render_template('railfence.html', encrypt_error="Thiếu plain_text hoặc số rail")
    
    try:
        rails = int(rails)
        if rails < 2:
            return render_template('railfence.html', encrypt_error="Số rail phải lớn hơn hoặc bằng 2")
        Railfence = RailFenceCipher()
        encrypted_text = Railfence.rail_fence_encrypt(text, rails)
        return render_template('railfence.html', encrypt_result=encrypted_text)
    except ValueError:
        return render_template('railfence.html', encrypt_error="Số rail phải là số nguyên")

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    if not request.form:
        return render_template('railfence.html', decrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputCipherText')
    rails = request.form.get('inputRailsCipher')
    
    if not text or not rails:
        return render_template('railfence.html', decrypt_error="Thiếu cipher_text hoặc số rail")
    
    try:
        rails = int(rails)
        if rails < 2:
            return render_template('railfence.html', decrypt_error="Số rail phải lớn hơn hoặc bằng 2")
        Railfence = RailFenceCipher()
        decrypted_text = Railfence.rail_fence_decrypt(text, rails)
        return render_template('railfence.html', decrypt_result=decrypted_text)
    except ValueError:
        return render_template('railfence.html', decrypt_error="Số rail phải là số nguyên")

# Router routes for transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    if not request.form:
        return render_template('transposition.html', encrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputPlainText')
    key = request.form.get('inputKeyPlain')
    
    if not text or not key:
        return render_template('transposition.html', encrypt_error="Thiếu plain_text hoặc key")
    
    try:
        key = int(key)
        if key < 1:
            return render_template('transposition.html', encrypt_error="Key phải lớn hơn hoặc bằng 1")
        Transposition = TranspositionCipher()
        encrypted_text = Transposition.encrypt(text, key)
        return render_template('transposition.html', encrypt_result=encrypted_text)
    except ValueError:
        return render_template('transposition.html', encrypt_error="Key phải là số nguyên")

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    if not request.form:
        return render_template('transposition.html', decrypt_error="Yêu cầu không hợp lệ")
    
    text = request.form.get('inputCipherText')
    key = request.form.get('inputKeyCipher')
    
    if not text or not key:
        return render_template('transposition.html', decrypt_error="Thiếu cipher_text hoặc key")
    
    try:
        key = int(key)
        if key < 1:
            return render_template('transposition.html', decrypt_error="Key phải lớn hơn hoặc bằng 1")
        Transposition = TranspositionCipher()
        decrypted_text = Transposition.decrypt(text, key)
        return render_template('transposition.html', decrypt_result=decrypted_text)
    except ValueError:
        return render_template('transposition.html', decrypt_error="Key phải là số nguyên")

# Main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
