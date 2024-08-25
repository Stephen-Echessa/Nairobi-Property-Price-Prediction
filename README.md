# Nairobi Property Price Predictor

## Overview
This project aims to predict property prices in Nairobi, Kenya, using machine learning techniques. The model is trained on data scraped from [buyrentkenya.com](https://buyrentkenya.com) and deployed as a web application using Gradio for easy interaction.


https://github.com/user-attachments/assets/c053858d-29bb-4a4f-8552-0570ebbbbc2c

## Features
 Predicts property prices based on various features such as location, number of bedrooms, amenities, etc.
- User-friendly web interface for easy interaction with the model
- Data scraped from a real estate website to ensure up-to-date information
- Handles both sale and rental properties

## Technologies Used
- Python
- Scikit-learn, XGBoost, LightGBM and CatBoost for machine learning
- Gradio for web interface
- Beautiful Soup
- Pandas for data manipulation
- NumPy for numerical operations

## Clone this repository:
    git clone https://github.com/Stephen-Echessa/Nairobi-Property-Price-Predictor.git

## Usage
The model is deployed at HuggingFace Spaces, so you can test it out by clicking here: [Chescore/Nairobi-Property-Price-Predictor](https://huggingface.co/spaces/chescore/Nairobi-Property-Price-Predictor)

## Model Details
- The model uses LightGBM for prediction.
- Features include sub-county, number of bedrooms, bathrooms, property type, and various amenities.
- Resulted in an R^2 score of 0.85.

## Data Collection
- Data was scraped from BuyRentKenya.com using [Beautiful Soup].
- The scraping script can be found in `house_scrap_soup.py`.

## Future Improvements
- Implement regular data updates to keep the model current
- Add more features such as proximity to amenities, crime rates, etc.
- Explore advanced models like neural networks

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer
This project is for educational purposes only. The predictions should not be used as the sole basis for real estate decisions. Always consult with a qualified real estate professional.

## Acknowledgments
- BuyRentKenya.com for being the source of my data
- The Gradio team for their excellent tool for building ML web apps
