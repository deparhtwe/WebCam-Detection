import cv2

rtsp_url="hhtp://192.168.1.23:8080"

cap=cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("CCTV can't open")
    exit()

while True:
    ret,frame=cap.read()

    if not ret:
        print("There is no frame from the cctv")
        break

    cv2.imshow("CCTV Live feed showing",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()