import cv2
import numpy as np
import subprocess

# YOLO modelini yükle
def load_yolo_model(weights_path, config_path):
    net = cv2.dnn.readNet(weights_path, config_path)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return net, output_layers

# İnsanları tespit etme fonksiyonu
def detect_people(frame, net, output_layers):
    height, width, channels = frame.shape
    # Giriş boyutunu 416x416 olarak ayarlıyoruz
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    # Her bir tespiti işle
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Güven eşiği
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            if label == "person":  # Sadece insanları kontrol et
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame

# Geri butonunun fonksiyonu
def add_back_button(frame):
    # Geri butonunun beyaz arka planını çiz
    cv2.rectangle(frame, (10, 10), (150, 50), (255, 255, 255), -1)  # Beyaz arka plan
    # Ok sembolü ve 'Geri' yazısını ekle
    cv2.putText(frame, '<-', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)  # Siyah metin
    return frame

# Dosya yolları
weights_path = "yolov3.weights"  # Ağırlık dosyasının yolu
config_path = "yolov3.cfg"        # Konfigürasyon dosyasının yolu
coco_names_path = "coco.names"    # Sınıf dosyasının yolu

# Modeli yükle
yolo_net, yolo_output_layers = load_yolo_model(weights_path, config_path)

# Sınıf etiketlerini yükle
with open(coco_names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Video kaynağını aç (0: webcam)
cap = cv2.VideoCapture(0)

# Çözünürlük ayarla
cap.set(3, 1920)  # Genişlik
cap.set(4, 1080)  # Yükseklik

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Geçerli karede insanları tespit et
    output_frame = detect_people(frame, yolo_net, yolo_output_layers)
    
    # Geri butonunu ekle
    output_frame = add_back_button(output_frame)

    # Çıktı çerçevesini göster
    cv2.imshow("Video", output_frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 'g' tuşuna basıldığında ana sayfaya dön
    if cv2.waitKey(1) & 0xFF == ord('g'):
        print("Ana sayfaya dönülüyor...")
        cap.release()  # Kamerayı serbest bırak
        cv2.destroyAllWindows()  # Tüm pencereleri kapat
        subprocess.run(["python", "main_menu.py"])
        # Ana sayfa fonksiyonunuzu burada çağırabilirsiniz
        # Örnek: main_page()  # Ana sayfa fonksiyonunu buraya ekleyebilirsiniz
        break

cap.release()
cv2.destroyAllWindows()
