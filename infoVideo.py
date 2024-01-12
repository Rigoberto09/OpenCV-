import cv2

def detect_face_features(video_path):
    # Abrir el video
    cap = cv2.VideoCapture(video_path)

    # Verifica si el video se abrió correctamente
    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return

    # Cargar clasificadores preentrenados
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')
    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

    while True:
        # Leer un frame del video
        ret, frame = cap.read()

        if not ret or frame is None:
            break

        # Convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar caras en el frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Si se detecta al menos una cara, mostrar las partes del rostro
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                # Dibujar un rectángulo alrededor de la cara
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Región de interés (ROI) para la cara
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Detectar ojos en la región de la cara
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

                # Detectar narices en la región de la cara
                noses = nose_cascade.detectMultiScale(roi_gray)
                for (nx, ny, nw, nh) in noses:
                    cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (0, 0, 255), 2)

                # Detectar bocas en la región de la cara
                mouths = mouth_cascade.detectMultiScale(roi_gray)
                for (mx, my, mw, mh) in mouths:
                    cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (255, 255, 0), 2)
        else:
            # Mostrar mensaje si no se detecta ninguna cara
            cv2.putText(frame, "No se detectó ninguna persona", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Mostrar el frame
        cv2.imshow('Face Features Detection', frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

# Ruta del video a procesar
video_path = 'video/filtro.mp4'

# Llamar a la función para detectar partes del rostro en el video
detect_face_features(video_path)
