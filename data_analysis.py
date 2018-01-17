import csv

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def read_data(data_path):
    with open(data_path, 'r') as data_file:
        data_reader = csv.reader(data_file, delimiter=' ')
        trial = []
        data = {
            'place': [],
            'step1_picture': [],
            'step1_angle': [],
            'step3_angle': [],
            'scale_shift': [],
            'block': [],
            'number_response': [],
            'letter_response': []
        }
        for index, line in enumerate(data_reader):
            if index == 0:
                continue
            elif len(line) != 10:
                continue
            trial.append(line[0])
            data['place'].append(int(line[1]))
            data['step1_picture'].append(int(line[2]))
            data['step1_angle'].append(line[3])
            data['step3_angle'].append(line[4])
            data['scale_shift'].append(int(line[5]))
            data['block'].append(line[6])
            data['number_response'].append(int(line[7]))
            data['letter_response'].append(line[8])
        df = pd.DataFrame(data, index=trial, columns=data.keys())
        return df


def remove_scale_factor(df):
    scale_shift_factors = {
        'place0': [180, 277, 356, 90],
        'place1': [224, 321, 40, 134],
        'place2': [203, 300, 19, 113]
    }
    number_response_without_scale_shift = []
    for place, scale_shift, number_response in zip(df['place'], df['scale_shift'], df['number_response']):
        scale_shift_factor = scale_shift_factors[f'place{place}'][scale_shift - 1]
        number_response_without_scale_shift.append(number_response - scale_shift_factor)
    df['number_response'] = number_response_without_scale_shift
    return df


def calculate_mean(df, mode):
    temp = []
    for step1_picture, number_response in zip(df['step1_picture'], df['number_response']):
        if mode == step1_picture:
            temp.append(number_response)
    print(np.mean(temp))


def main():
    data_path = r'.\data\ProjectResults_ID1_20180117160908.txt'
    df = read_data(data_path)
    df = remove_scale_factor(df)
    calculate_mean(df, 2)


if __name__ == '__main__':
    main()
