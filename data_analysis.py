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
            data['place'].append(int(line[1]))
            data['step1_picture'].append(int(line[2]))
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


def sort_data(df, which_place, which_step1_picture):
            sorted_data = []
            for place, step1_picture, number_response in zip(df['place'], df['step1_picture'], df['number_response']):
                if place == which_place and step1_picture == which_step1_picture:
                    sorted_data.append(number_response)
            return sorted_data


def calc_stats(df):
    places = {
        '0': 'Forest',
        '1': 'Hagelloch',
        '2': 'Bebenhausen'
    }
    step_1_pictures = {
        '0': 'Composite',
        '1': 'High',
        '2': 'Low'
    }
    for which_place in range(3):
        for which_step1_picture in range(3):
            place = places[str(which_place)]
            step_1_picture = step_1_pictures[str(which_step1_picture)]
            sorted_data = sort_data(df, which_place, which_step1_picture)
            mean_data = np.round(np.mean(sorted_data), 1)
            std_data = np.round(np.std(sorted_data), 1)
            median_data = np.round(np.median(sorted_data), 1)
            print(f'Stats for {place} & {step_1_picture}: Median ({median_data}), Mean ({mean_data}), STD ({std_data})')


def main():
    data_path = r'.\data\ProjectResults_ID1_20180117160908.txt'
    df = read_data(data_path)
    df = remove_scale_factor(df)
    calc_stats(df)


if __name__ == '__main__':
    main()
