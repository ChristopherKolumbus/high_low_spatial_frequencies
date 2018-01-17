import csv

import pandas as pd


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
            data['step1_picture'].append(line[2])
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


def main():
    data_path = r'.\data\ProjectResults_20180117150251.txt'
    df = read_data(data_path)
    df = remove_scale_factor(df)
    print(df.head())


if __name__ == '__main__':
    main()
