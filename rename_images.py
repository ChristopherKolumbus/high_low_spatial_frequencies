import os


def main():
    img_path = r'..\images'
    for img_name in os.listdir(img_path):
        img_name_new = img_name[:5] + str(int(img_name[5]) - 1) + img_name[6:]
        os.rename(os.path.join(img_path, img_name), os.path.join(img_path, img_name_new))


if __name__ == '__main__':
    main()