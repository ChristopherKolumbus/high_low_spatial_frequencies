import csv
import pandas as pd


def read_data(data_path):
    with open(data_path, 'r') as data_file:
        data_reader = csv.reader(data_file, delimiter= ' ')
        trial = []
        data = {
            'place': [], 'step1_picture': [], 'step1_angle': [], 'step3_angle': [],
            'scale_shift': [], 'block': [], 'number_response': [], 'letter_response': []
        }
        for index, line in enumerate(data_reader):
            if index == 0:
                continue
            elif len(line) != 10:
                continue
            trial.append(line[0])
            data['place'].append(line[1])
            data['step1_picture'].append(line[2])
            data['step1_angle'].append(line[3])
            data['step3_angle'].append(line[4])
            data['scale_shift'].append(line[5])
            data['block'].append(line[6])
            data['number_response'].append(line[7])
            data['letter_response'].append(line[8])
        df = pd.DataFrame(data, index=trial, columns=data.keys())
        return df

def main():
    data_path = r'.\data\ProjectResults_20180116162743.txt'
    df = read_data(data_path)
    print(df)


if __name__ == '__main__':
    main()
