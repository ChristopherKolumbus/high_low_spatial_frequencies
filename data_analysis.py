import csv


def main():
    data_path = r'.\data\ProjectResults_20180116162743.txt'
    with open(data_path, 'r') as data_file:
        data_reader = csv.reader(data_file, delimiter=' ')
        trial = []
        place = []
        step1_picture = []
        step1_angle = []
        step3_angle = []
        scale_shift = []
        block = []
        number_response = []
        letter_response = []
        for index, line in enumerate(data_reader):
            if index == 0:
                continue
            elif len(line) != 10:
                continue
            trial.append(line[0])
            place.append(line[1])
            step1_picture.append(line[2])
            step1_angle.append(line[3])
            step3_angle.append(line[4])
            scale_shift.append(line[5])
            block.append(line[6])
            number_response.append(line[7])
            letter_response.append(line[8])


if __name__ == '__main__':
    main()
