import cv2
import numpy as np

# Kameranın indeksi
kamera_index = 0
cap = cv2.VideoCapture(kamera_index)

# Renk seçim aracını kullanarak kırmızı renginin HSV değerlerini belirleyin
# Bu değerleri elde etmek için bir renk seçim aracı kullanın
h_min, s_min, v_min = 0,100,100
h_max, s_max, v_max = 10, 255, 255

# Kamera açılamazsa hata mesajı yazdırın
if not cap.isOpened():
    print("Kamera açılamadı, lütfen bağlantıyı kontrol edin.")

while True:
    # Kameradan bir kare alın
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Kareyi HSV renk uzayına dönüştürün
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirlenen renk aralığında bir maske oluşturun
    mask = cv2.inRange(hsv, np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max]))

    # Orijinal kare üzerinde maskeyi uygulayarak kırmızı rengini vurgulayın
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal ve işlenmiş kareleri ekranda gösterin
    cv2.imshow("Normal Görüntü", frame)
    cv2.imshow("Kırmızı Rengi Tespit Et", result)

# Kamera bağlantısını serbest bırakın ve pencereyi kapatın
cap.release()
cv2.destroyAllWindows()
