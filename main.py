import numpy as np
import os, sys
import sklearn
import pickle


# X is an array of 10 samples gotten from the voltage reader

def summation_square(array):
    sum_array = []
    for k in array:
        sum_array.append(pow(np.sum(k),2))
    return np.sum(sum_array)


def energy(data, time):
    value = 0 
    value = data * time
    return value/10



def categorize_input(x):
    energy_value = summation_square(x)
    sampling_time = 0.5/200
    energy_sample = energy(energy_value, sampling_time)
    
    return energy_sample


def main(x):
    pred = categorize_input(x)
    current_dir = os.getcwd()
    save_directory = current_dir + '\\models\\svc'
    os.chdir(save_directory)
    filename= 'finalized svc model.sav'
    poly_file = 'poly.sav'
    scaler_file = 'scaler.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    poly = pickle.load(open(poly_file, 'rb'))
    scaler = pickle.load(open(scaler_file, 'rb'))
    os.chdir(current_dir)
    pred = np.array(pred).reshape(1,-1)
    poly_pred = poly.transform(pred)
    #print(poly_pred[0][1])
    #scalar_pred = scaler.transform(poly_pred)
    #result = loaded_model.predict(scalar_pred[0][1:].reshape(1,-1))
    #os.chdir(current_dir)
    value = 0
    if poly_pred[0][1] >=121.0 and poly_pred[0][1]<=144.0:
        value =1
    else:
        value = 0
    return value


if __name__ == '__main__':
    """
    x is an array of 10 voltage samples from the Voltage sensors
    """
    x = [241]*10
    main = main(x)
    print(main)

