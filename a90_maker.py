import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.interpolate import interp1d


def fit_models(filenames):
    models = {}
    times_available = []
    snrs = []
    area_90s = []

    # Collect data for each time point
    for filename, _, label in filenames:
        # Load the data from the CSV file
        data = pd.read_csv(filename)

        # Extract the 5th and 9th columns (0-based index: 4 and 7)
        snr = data.iloc[:, 4]
        area_90 = data.iloc[:, 7]

        # Log-transform the data
        log_snr = np.log10(snr)
        log_area_90 = np.log10(area_90)

        # Store the data
        snrs.extend(snr)
        area_90s.extend(area_90)
        times_available.extend([label] * len(data))

        # Fit a linear model for the current time point
        model = LinearRegression()
        model.fit(log_snr.values.reshape(-1, 1), log_area_90)
        models[label] = model

    # Interpolate models across times
    return models, np.array(snrs), np.array(area_90s), times_available


def predict_area_90_for_single(snr_value, time_to_predict, models, times_available):
    # Convert time labels to numeric for interpolation
    time_labels = [int(t.split(' ')[1]) for t in times_available]
    model_times = [int(t.split(' ')[1]) for t in models.keys()]

    # Create interpolation function for model coefficients
    def interpolate_models(time_labels, models, model_times):
        coeffs = np.array([model.coef_[0] for model in models.values()])
        intercepts = np.array([model.intercept_ for model in models.values()])

        # Interpolating coefficients
        interp_coeff = interp1d(model_times, coeffs, kind='linear', fill_value="extrapolate")
        interp_intercept = interp1d(model_times, intercepts, kind='linear', fill_value="extrapolate")

        return interp_coeff, interp_intercept

    interp_coeff, interp_intercept = interpolate_models(time_labels, models, model_times)

    # Process the single time point
    coeff = interp_coeff(time_to_predict)
    intercept = interp_intercept(time_to_predict)

    # Log-transform the SNR value
    log_snr_value = np.log10(snr_value)
    predicted_log_area_90 = coeff * log_snr_value + intercept
    area_90_prediction = 10 ** predicted_log_area_90

    return area_90_prediction

def a90(snr_values, times_to_predict):
    # Define file details and colors with time labels
    a90s=[]
    files_and_labels = [
        ('1024.csv', 'blue', 'time 0'),
        ('56.csv', 'orange', 'time 10'),
        ('49.csv', 'green', 'time 15'),
        ('38.csv', 'purple', 'time 29'),
        ('32.csv', 'red', 'time 46'),
        ('29.csv', 'cyan', 'time 60')
    ]

    # Fit models for each time point and gather data
    models, snrs, area_90s, times_available = fit_models(files_and_labels)


    for i in range(len(snr_values)):
    # Predict area_90 for the specified single SNR value and time
        a90s.append(predict_area_90_for_single(snr_values[i], times_to_predict[i], models, times_available))
    return a90s
# Print the prediction
