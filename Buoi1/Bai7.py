#Nhập các dòng từ người dùng
print("\nNhập các dòng văn bản (Nhập 'xong' để kết thúc):\n")
lines = []

while True:
    line = input()
    if line.lower() == 'xong':
        break
    lines.append(line)

#Chuyển các dòng thành chữ in hoa và in ra màn hình
print("\n\t--- Các dòng đã nhập sau khi chuyển thành chữ in hoa ---\n")
for line in lines:
    print(line.upper())