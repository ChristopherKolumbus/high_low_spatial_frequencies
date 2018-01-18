import csv

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def read_data(data_path):
    place_names = {
        '0': 'Forest',
        '1': 'Hagelloch',
        '2': 'Bebenhausen'
    }
    step_1_picture_names = {
        '0': 'Composite',
        '1': 'High',
        '2': 'Low'
    }
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
            # Skip header:
            if index == 0:
                continue
            # Skip training block:
            elif int(line[6]) == 0:
                continue
            # Skip incomplete lines:
            elif len(line) != 10:
                continue
            trial.append(line[0])
            data['place'].append(place_names[line[1]])
            data['step1_picture'].append(step_1_picture_names[line[2]])
            data['step1_angle'].append(line[3])
            data['step3_angle'].append(line[4])
            data['scale_shift'].append(int(line[5]))
            data['block'].append(int(line[6]))
            data['number_response'].append(int(line[7]))
            data['letter_response'].append(line[8])
        df = pd.DataFrame(data, index=trial, columns=data.keys())
        return df


def remove_scale_factor(df):
    scale_shift_factors = {
        'Forest': [180, 277, 356, 90],
        'Hagelloch': [224, 321, 40, 134],
        'Bebenhausen': [203, 300, 19, 113]
    }
    number_response_without_scale_shift = []
    for place, scale_shift, number_response in zip(df['place'], df['scale_shift'], df['number_response']):
        scale_shift_factor = scale_shift_factors[place][scale_shift - 1]
        result = number_response - scale_shift_factor
        if result < 0:
            result += 360
        number_response_without_scale_shift.append(result)
    df['number_response'] = number_response_without_scale_shift
    return df


def polar_plot(df):
    number_response = np.array(df['number_response'])
    radius = np.ones(number_response.shape)
    ax = plt.subplot(111, projection='polar')
    ax.scatter(np.deg2rad(number_response), radius)
    ax.set_rmax(1.1)
    plt.show()


def main():
    data_path = r'.\data\ProjectResults_ID1_20180117160908.txt'
    df = read_data(data_path)
    df = remove_scale_factor(df)
    print(df['number_response'][(df['place'] == 'Bebenhausen') & (df['step1_picture'] == 'Composite')].median())


if __name__ == '__main__':
    main()
