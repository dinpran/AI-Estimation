import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import ssl
import urllib.request

class CO2EmissionModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CO2EmissionModel, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Disable SSL certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context

        # Load the data
        url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv'
        self.df = pd.read_csv(url)
        msk = np.random.rand(len(self.df)) < 0.8
        train = self.df[msk]
        test = self.df[~msk]

        # Train the model
        self.regr = LinearRegression()
        x_train = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS']])
        y_train = np.asanyarray(train[['CO2EMISSIONS']])
        self.regr.fit(x_train, y_train)

    def predict(self, engine_size, cylinders):
        x_test = np.array([[engine_size, cylinders]])
        predicted_emission = self.regr.predict(x_test)
        return predicted_emission[0][0]

