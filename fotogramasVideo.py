# crear requerimientos de [pip freeze > requirements.txt]
# instalar todos los requermientos de la app.py [pip install -r requirements.txt]

# Codigo anterior
# import cv2
# import os

# def video_to_frames(video_path, frames_path, duration=10):
#     # Crear el directorio para los frames si no existe
#     os.makedirs(frames_path, exist_ok=True)

#     # Abrir el video
#     cap = cv2.VideoCapture(video_path)

#     # Verifica si el video se abrió correctamente
#     if not cap.isOpened():
#         print("No se pudo abrir el video.")
#         return

#     # Obtiene la tasa de frames por segundo (fps) y la duración total del video
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     duration_in_seconds = duration
#     total_frames_to_capture = int(fps * duration_in_seconds)

#     # Captura frames durante la duración especificada
#     for frame_number in range(total_frames_to_capture):
#         ret, frame = cap.read()

#         if not ret or frame is None:
#             print(f"Error al leer el frame {frame_number}.")
#             break

#         # Guarda el frame como una imagen
#         frame_filename = os.path.join(frames_path, f"frame_{frame_number:04d}.png")
#         cv2.imwrite(frame_filename, frame)

#     # Cierra el video
#     cap.release()
#     print(f"Se han guardado {total_frames_to_capture} frames en {frames_path}.")

# # Rutas
# video_path = "C:/Users/rborjas/OneDrive/Escritorio/normal.mp4"
# frames_path = "C:/Users/rborjas/OneDrive/Escritorio/img/"

# # Llama a la función para convertir el video a frames
# video_to_frames(video_path, frames_path)

import cv2
import os

def video_to_frames(video_path, frames_path, min_duration=10):
    # Verifica si el Video de video existe
    if not os.path.exists(video_path):
        print(f"El Video de video '{video_path}' no existe.")
        return

    # Crear el directorio para los frames si no existe
    os.makedirs(frames_path, exist_ok=True)

    # Abrir el video
    cap = cv2.VideoCapture(video_path)

    # Verifica si el video se abrió correctamente
    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return
    # Calculos de los fotogramas por segundo
    # Obtiene la tasa de frames por segundo (fps) y la duración total del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    total_duration_seconds = total_frames / fps

    # Si la duración total es menor que min_duration, usa la duración total
    duration_to_capture = max(min_duration, total_duration_seconds)
    total_frames_to_capture = int(fps * duration_to_capture)

    # Captura frames durante la duración especificada
    for frame_number in range(total_frames_to_capture):
        ret, frame = cap.read()

        if not ret or frame is None:
            print(f"Error al leer el frame {frame_number}.")
            break

        # Guarda el frame como una imagen
        frame_filename = os.path.join(frames_path, f"frame_{frame_number:04d}.png")
        cv2.imwrite(frame_filename, frame)

    # Cierra el video
    cap.release()
    print(f"Se han guardado {total_frames_to_capture} frames en {frames_path}.")

# Rutas
video_path = "C:/Users/rborjas/OneDrive/Escritorio/Videos/normal.mp4"
frames_path = "C:/Users/rborjas/OneDrive/Escritorio/Videos/img/"

# Llama a la función para convertir el video a frames
video_to_frames(video_path, frames_path, min_duration=10)

