import base64

def main():
    input_string = input("Vui lòng nhập thông tin cần mã hoá: ")
    
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    
    with open("data.txt", "w") as file:
        file.write(encoded_string)
    
    print("\n\t ĐÃ MÃ HOÁ VÀ GHI VÀO TỆP data.txt !!!")

if __name__ == "__main__":
    main()