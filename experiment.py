from random import shuffle

repetitions = 3
number_places = 3
number_pictures = 3
number_letters = 2
number_orientations = 2
base_angle = 180
diff_angle = 30

conditions = []
for repetition in range(repetitions):
    for place in range(number_places):
        for picture in range(number_pictures):
            for letter in range(number_letters):
                for orientation in range(number_orientations):
                    if orientation == 0:
                        condition = [place, picture, letter, base_angle + diff_angle]
                    else:
                        condition = [place, picture, letter, base_angle - diff_angle]
                    conditions.append(condition)

shuffle(conditions)

places = []
pictures = []
letters = []
orientations = []
for condition in conditions:
    places.append(str(condition[0]))
    pictures.append(str(condition[1]))
    letters.append(str(condition[2]))
    orientations.append(str(condition[3]))

print('Place: ' + ', '.join(places))
print('Picture: ' + ', '.join(pictures))
print('Letter: ' + ', '.join(letters))
print('Orientation: ' + '.0f, '.join(orientations))
