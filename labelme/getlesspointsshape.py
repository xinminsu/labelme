import argparse
from labelme.label_file import LabelFile
import math

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        '-I',
        '-i',
        help='input json file of labelme generated (if it ends with .json it is '
             'recognized as file, else as directory)'
    )

    args = parser.parse_args()

    config_from_args = args.__dict__

    filename = config_from_args.pop('input')

    #print(filename)

    labelFile = LabelFile(filename)

    #print(f"len(labelFile.shapes) = {len(labelFile.shapes)}")

    i = 1
    for s in labelFile.shapes:
        pointslen = len(s['points'])
        if pointslen < 10:
            print("{} line in {}".format(i,filename))

if __name__ == '__main__':
    main()