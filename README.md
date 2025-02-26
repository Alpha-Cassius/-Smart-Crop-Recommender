# 🌾 Smart-Crop-Recommender

## Overview
The **Crop Recommendation System** is a machine learning-based GUI application that helps farmers and agricultural enthusiasts determine the most suitable crop to grow based on soil and climate conditions. This project utilizes the **Random Forest Classifier** from scikit-learn to make predictions based on various soil and environmental parameters.

## Features
- **User-friendly GUI** using `customtkinter` for a modern and responsive interface.
- **Machine learning-based crop prediction** using the **Random Forest Classifier**.
- **Interactive input fields** for soil nutrients, temperature, humidity, pH, and rainfall.
- **Visual crop recommendations** with dynamically displayed crop images.
- **Error handling** for out-of-range or invalid inputs.
- **Dark mode UI** with a professional layout.

## Technologies Used
- **Python** (3.x)
- **customtkinter** (for GUI)
- **pandas, numpy** (for data handling)
- **Pillow (PIL)** (for image processing)
- **scikit-learn** (for machine learning)

## Dataset
The model is trained on the **Crop Recommendation Dataset**, which contains essential soil and climate parameters:
- **N**: Nitrogen (mg/kg)
- **P**: Phosphorus (mg/kg)
- **K**: Potassium (mg/kg)
- **Temperature** (°C)
- **Humidity** (%)
- **pH** (Acidity/Alkalinity)
- **Rainfall** (mm)
- **Label** (Recommended Crop)

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Alpha-Cassius/-Smart-Crop-Recommender.git
   cd crop-recommendation
   ```
2. **Install required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```sh
   python app.py
   ```

## How It Works
1. Enter values for **Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall**.
2. Click the **Predict Crop** button.
3. The **Random Forest Classifier** predicts the most suitable crop based on the input values.
4. The recommended crop name and corresponding image (if available) are displayed.

## About the Random Forest Classifier
The **Random Forest Classifier** is an ensemble learning method that combines multiple decision trees to provide accurate and robust predictions. It works by:
- Training on multiple subsets of data (bagging technique).
- Creating multiple decision trees and averaging their predictions.
- Reducing overfitting while improving accuracy.

### Why Random Forest?
- **High Accuracy**: It improves prediction accuracy by averaging multiple trees.
- **Handles Missing Data**: Can work well with missing or unbalanced data.
- **Resistant to Overfitting**: The averaging process helps generalize predictions.

## Project Structure
```
├── IMG/                  # Crop images (e.g., rice.jpg, wheat.jpg)
├── Crop_recommendation.csv  # Dataset
├── app.py                # Main application file
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Enhancements
- Add **real-time weather data integration**.
- Improve model accuracy with **more advanced ML techniques**.
- Expand dataset with **regional crop recommendations**.
- Implement **mobile compatibility** using Kivy or PyQt.

## License
This project is licensed under the **MIT License**.

## Contributing
Feel free to fork, modify, and contribute to this project! Pull requests are welcome.

## Author
Developed by **Vaibhav Pandey**.

---

🌾 *Empowering Farmers with AI-Powered Recommendations!*

