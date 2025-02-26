import customtkinter as ctk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import os

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# GUI Setup
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🌾 Crop Recommendation System")
app.geometry("550x750")  # Adjusted for image space
app.resizable(0,0)

# Background Frame
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(frame, text="🌱 Smart Crop Recommender", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Input fields
inputs = {}
labels = [
    "Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)",
    "Temperature (°C)", "Humidity (%)", "pH", "Rainfall (mm)"
]
limits = {
    "Nitrogen (mg/kg)": (0, 200),
    "Phosphorus (mg/kg)": (0, 200),
    "Potassium (mg/kg)": (0, 200),
    "Temperature (°C)": (-10, 60),
    "Humidity (%)": (0, 100),
    "pH": (3.5, 9.0),
    "Rainfall (mm)": (0, 500)
}

def predict_crop():
    try:
        values = []
        for label in labels:
            value = float(inputs[label].get())
            min_val, max_val = limits[label]
            if not (min_val <= value <= max_val):
                result_label.configure(text=f"⚠ {label} out of range ({min_val}-{max_val})", fg_color="red")
                return
            values.append(value)
        values = np.array(values).reshape(1, -1)
        prediction = model.predict(values)[0]
        crop_name = label_encoder.inverse_transform([prediction])[0]
        result_label.configure(text=f"🌾 Recommended Crop: {crop_name}", fg_color="green")

        # Load and display crop image
        image_path = f"IMG/{crop_name}.jpg"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.LANCZOS)  # Resize for better fit
            img = ImageTk.PhotoImage(img)
            image_label.configure(image=img)
            image_label.image = img  # Keep reference
        else:
            result_label.configure(text="❌ Image not found!", fg_color="red")

    except ValueError:
        result_label.configure(text="❌ Please enter valid numerical values.", fg_color="red")

for label in labels:
    field_frame = ctk.CTkFrame(frame, corner_radius=10)
    field_frame.pack(pady=8, padx=10, fill="x")
    
    ctk.CTkLabel(field_frame, text=label, font=("Arial", 14)).pack(side="left", padx=10)
    entry = ctk.CTkEntry(field_frame, placeholder_text=label, width=150)
    entry.pack(side="right", padx=10)
    inputs[label] = entry

# Predict Button
predict_button = ctk.CTkButton(
    frame, text="🔍 Predict Crop", command=predict_crop, height=40, fg_color="#007BFF", hover_color="#0056b3"
)
predict_button.pack(pady=20)

# Image Display
image_label = ctk.CTkLabel(frame, text="", height=150, width=150, corner_radius=10)
image_label.pack(pady=10)

# Result Display
result_label = ctk.CTkLabel(frame, text="", font=("Arial", 16, "bold"), height=50, corner_radius=10)
result_label.pack(pady=10, padx=20, fill="x")

# Run Application
app.mainloop()
