from random import shuffle, randint

places = ['0', '1', '2']
pictures = ['0', '1', '2']
repetitions = 12
base_angle = 180

conditions = []
count = 0
for repetition in range(repetitions):
    for place in places:
        for picture in pictures:
            if count % 2 == 0:
                conditions.append([place, picture, base_angle + 30])
            else:
                conditions.append([place, picture, base_angle - 30])
            count += 1

shuffle(conditions)

place_temp = []
picture_temp = []
angle_temp = []
for condition in conditions:
    place, picture, angle = condition
    place_temp.append(place)
    picture_temp.append(picture)
    angle_temp.append(str(angle))
place_output = ', '.join(place_temp)
picture_output = ', '.join(picture_temp)
angle_output = '.0f, '.join(angle_temp)
#print(place_output)
#print(picture_output)
#print(angle_output)

scale_shift = []
for i in range(len(conditions)):
    scale_shift.append(str(randint(1, 4)))
scale_shift_output = ', '.join(scale_shift)
#print(scale_shift_output)

e_or_f = []
for i in range(len(conditions)):
    e_or_f.append(str(randint(0, 1)))
e_or_f_output = ', '.join(e_or_f)
print(e_or_f_output)