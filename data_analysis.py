import csv

import pandas as pd
import numpy as np
from scipy import stats
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
            data['step3_angle'].append(int(line[4]))
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


def calc_stats(df, which_place, which_picture):
    df_slice = np.array(df['number_response'][(df['place'] == which_place) & (df['step1_picture'] == which_picture)])
    df_slice = np.deg2rad(df_slice)
    mean_result = np.round(np.rad2deg(stats.circmean(df_slice, low= -np.pi, high= np.pi)), 1)
    median_result = np.round(np.rad2deg(stats.circvar(df_slice, low= -np.pi, high= np.pi)), 1)
    std_result = np.round(np.rad2deg(stats.circstd(df_slice, low= -np.pi, high= np.pi)), 1)
    print(
        f'{which_place} ({which_picture}): {mean_result} (Mean); {median_result} (Var); {std_result} (STD)'
    )


def main():
    data_path = r'.\data\ProjectResults_ID1_20180117160908.txt'
    df = read_data(data_path)
    df = remove_scale_factor(df)
    print(len(df[(df['place'] == 'Bebenhausen') & (df['step1_picture'] == 'Low') & (df['step3_angle'] == 210)]))
    # calc_stats(df, 'Bebenhausen', 'High')


if __name__ == '__main__':
    main()
