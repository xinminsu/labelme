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

    sameShape = {}
    plen = []
    for s in labelFile.shapes:
        pointslen = len(s['points'])
        plen.append(pointslen)

    for i in range(len(plen)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if plen[i] == plen[j]:
                #print(f"{j} and {i} len is the same {plen[i]}")
                shapei = labelFile.shapes[i]
                shapej = labelFile.shapes[j]

                kstep = 0
                for k in range(0,plen[i]):
                    dx = math.fabs(float(shapei['points'][k][0]) - float(shapej['points'][k][0]))
                    dy = math.fabs(float(shapei['points'][k][1]) - float(shapej['points'][k][1]))

                    if dx > 2.0 or dy > 2.0:
                        break
                    kstep = kstep + 1

                if kstep == plen[i]:
                    #print(f"{j} and {i} shape is the same")
                    sameShape[j] = i

    print(sameShape)

if __name__ == '__main__':
    main()