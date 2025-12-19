{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "17d8ccf8-a401-49dc-a9c1-108c1ea2af9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9948d349-382f-4c08-bedf-7a5c83072518",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load model\n",
    "model = pickle.load(open(\"logistic_model.pkl\", \"rb\"))\n",
    "scaler = pickle.load(open(\"scaler.pkl\", \"rb\"))\n",
    "\n",
    "st.title(\"Diabetes Prediction App\")\n",
    "\n",
    "# User Inputs\n",
    "preg = st.number_input(\"Pregnancies\", 0, 20)\n",
    "glucose = st.number_input(\"Glucose\", 0, 200)\n",
    "bp = st.number_input(\"Blood Pressure\", 0, 150)\n",
    "skin = st.number_input(\"Skin Thickness\", 0, 100)\n",
    "insulin = st.number_input(\"Insulin\", 0, 900)\n",
    "bmi = st.number_input(\"BMI\", 0.0, 70.0)\n",
    "dpf = st.number_input(\"Diabetes Pedigree Function\", 0.0, 3.0)\n",
    "age = st.number_input(\"Age\", 1, 120)\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])\n",
    "    input_scaled = scaler.transform(input_data)\n",
    "    result = model.predict(input_scaled)\n",
    "\n",
    "    if result[0] == 1:\n",
    "        st.error(\"⚠️ High Risk of Diabetes\")\n",
    "    else:\n",
    "        st.success(\"✅ Low Risk of Diabetes\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
