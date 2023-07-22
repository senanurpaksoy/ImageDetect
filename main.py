from tkinter import *
import deepface
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
import cmake
import dlib
import pandas as pd
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tqdm import tqdm
import gdown
import psycopg2
import json

root = Tk()
root.geometry('800x800')

def connect_to_database():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="yüzTanima",
        user="postgres",
        password="1404"
    )
    return conn

def open_first_image():
    global img1_path, img1, img1_label
    img1_path = filedialog.askopenfilename(initialdir="/Users/senanurpaksoy/gui/images",
                                           title="Select First Image",
                                           filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    img1 = Image.open(img1_path)
    img1 = img1.resize((200, 200), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    img1_label.configure(image=img1)
    img1_label.image = img1


def open_second_image():
    global img2_path, img2, img2_label
    img2_path = filedialog.askopenfilename(initialdir="/Users/senanurpaksoy/gui/images",
                                           title="Select Second Image",
                                           filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    img2 = Image.open(img2_path)
    img2 = img2.resize((200, 200), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    img2_label.configure(image=img2)
    img2_label.image = img2

def save_image_to_database(image_path, gender, age, emotion, verified):
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_query = "INSERT INTO images (image_path, gender, age, emotion, verified) VALUES (%s, %s, %s, %s, %s)"
    data = (image_path, json.dumps(gender), age, emotion, verified)

    print("Insert Query:", insert_query)
    print("Data:", data)

    cursor.execute(insert_query, data)

    conn.commit()
    cursor.close()
    conn.close()


def analyze_images():
    if img1_path is None or img2_path is None:
        print("Please select both images first.")
        return

    resp = deepface.DeepFace.verify(img1_path, img2_path)

    if resp["verified"]:
        # İki fotoğraf aynı kişilere ait
        img1_analysis = deepface.DeepFace.analyze(img1_path, actions=['age', 'gender', 'emotion'])
        gender1 = img1_analysis[0]['gender']
        age1 = img1_analysis[0]['age']
        emotion1 = img1_analysis[0]['dominant_emotion']

        result = f"İki fotoğrafta da aynı kişi var:\nCinsiyet: {gender1}\nYaş: {age1}\nBaskın Duygu: {emotion1}"
        save_image_to_database(img1_path, gender1, age1, emotion1, True)  # save_image parametresini True olarak geçiriyoruz
    else:
        # İki fotoğraf farklı kişilere ait
        img1_analysis = deepface.DeepFace.analyze(img1_path, actions=['age', 'gender', 'emotion'])
        img2_analysis = deepface.DeepFace.analyze(img2_path, actions=['age', 'gender', 'emotion'])
        gender1 = img1_analysis[0]['gender']
        age1 = img1_analysis[0]['age']
        emotion1 = img1_analysis[0]['dominant_emotion']
        gender2 = img2_analysis[0]['gender']
        age2 = img2_analysis[0]['age']
        emotion2 = img2_analysis[0]['dominant_emotion']

        result = f"İki fotoğrafta da farklı kişiler var:\nFotoğraf 1:\nCinsiyet: {gender1}\nYaş: {age1}\nBaskın Duygu: {emotion1}\n\nFotoğraf 2:\nCinsiyet: {gender2}\nYaş: {age2}\nBaskın Duygu: {emotion2}"
        save_image_to_database(img1_path, gender1, age1, emotion1, False)  # save_image parametresini False olarak geçiriyoruz
        save_image_to_database(img2_path, gender2, age2, emotion2, False)  # save_image parametresini False olarak geçiriyoruz

    result_label = Label(root, text=result, font=("Arial", 15))
    result_label.pack()

# Frame 1 - İlk fotoğraf
frame1 = Frame(root, padx=20, pady=20)
frame1.pack()

btn_first_image = Button(frame1, text="Birinci Fotoğrafı Seçin", command=open_first_image)
btn_first_image.pack(side=LEFT)

img1_label = Label(frame1)
img1_label.pack(side=LEFT)

# Frame 2 - İkinci fotoğraf
frame2 = Frame(root, padx=20, pady=20)
frame2.pack()

btn_second_image = Button(frame2, text="İkinci Fotoğrafı Seçin", command=open_second_image)
btn_second_image.pack(side=LEFT)

img2_label = Label(frame2)
img2_label.pack(side=LEFT)

# Analiz Butonu
btn_analyze = Button(root, text="Analiz Et", command=analyze_images)
btn_analyze.pack()

root.mainloop()
