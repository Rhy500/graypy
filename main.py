import cv2

# Inisialisasi kamera (0 adalah default untuk kamera pertama yang terhubung)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

# Loop untuk menangkap frame dari kamera
while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Jika frame tidak berhasil dibaca, keluar dari loop
    if not ret:
        print("Gagal menangkap gambar")
        break

    # Tampilkan frame asli (berwarna)
    cv2.imshow('Camera', frame)

    # Tekan 'q' untuk menangkap gambar, mengonversinya, dan keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Ubah gambar menjadi abu-abu
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Simpan gambar abu-abu
        cv2.imwrite('captured_gray_image.jpg', gray_frame)
        print("Gambar berhasil disimpan sebagai 'captured_gray_image.jpg'")

        # Tampilkan gambar abu-abu
        cv2.imshow('Gray Image', gray_frame)
        cv2.waitKey(0)
        break

# Melepaskan resource dan menutup jendela
cap.release()
cv2.destroyAllWindows()