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

    fshape = labelFile.shapes[0]
    newPoints = []
    newPoints.append(fshape['points'][0])
    pointslen = len(fshape['points'])

    keepPointIndex = 0;
    for i in range(1, pointslen):
        dx = math.fabs(float(fshape['points'][i][0]) - float(fshape['points'][keepPointIndex][0]))
        dy = math.fabs(float(fshape['points'][i][1]) - float(fshape['points'][keepPointIndex][1]))

        if dx > 2.0 or dy > 2.0:
            keepPointIndex = i
            newPoints.append(fshape['points'][keepPointIndex])

    print(newPoints)


if __name__ == '__main__':
    main()