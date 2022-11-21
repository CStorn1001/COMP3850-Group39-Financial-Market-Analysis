# COMP3850-Group39-Correlation in Financial Markets for Kensho Data
## FinData Ltd
<img src="findatalogo.png">

## COMP3085 Group 39 
Group members : Christian Stornelli, Arnesh Chakrabarti, John Bekiaris, Linda Le, Sasha Nair, Bishal Chowdhury

## Project Description
Kensho Data wants to investigate correlations in the financial markets, specifically exploring high frequency FX trading strategies. The scope of the project is focused around understanding the FX markets and applying a specific trading strategy to give Kensho Data a competitive advantage. 

There are many incredible opportunities for Kensho Data to explore with the successful implementation of our project. This product will be to create an automated high frequency trading strategy for one of the FX currency pairs, which will be able to generate profits, allow further research into this area, and free resources that can be focused on other projects. 

## Workspace items
* FX - All data files provided by Kensho Data. This is the data to be extracted
* Hourly_data - Our stored hourly data which we call to conduct our analysis. Where we prepared this data to reduce execution time
* Talib-library - contains wheel files (zip files) to receive talib library (tutorial on this found within deliverable 4 Scripts/Model execution documentation -Setup) 
* COMP3850-Group39-project_presentation.ipynb - our presentation documentation which focuses on one FX pairing only, EUR/GBP. Conducted in jupyter notebook
* COMP3850-Group39-MVP - our full analysis with more than one FX pairings generally centered on three EUR/GBP, EUR/AUD and GBP/USD. Conducted in jupyter notebook
* findatalogo - our logo which is placed within some of our files
* hourlydata_method - shows how we produced and store our dataframes into hourly through the basic data extraction method to make the quick method. NOTE: Do not execute this file!

## Basic Table of Contents pipeline for our MVP:
1. Quick extraction: Data Extraction and Preparation
2. Data Extraction
3. Data Preparation
4. Conducting EDA
5. Check stationarity
6. ARIMA model
7. Supervised learning model
8. Model Evaluation
