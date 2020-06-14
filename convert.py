import re


def height_to_metric(string):
    tmp = str(string)
    tmp_lst = re.findall(r'([0-9])\'', tmp)
    if len(tmp_lst) == 2:
        cm = int(tmp_lst[0]) * 30.48 + int(tmp_lst[1]) * 2.54
        return cm
    else:
        print("Not a proper height, e.g. 6'2''.")


def pound_to_kg(num):
    try:
        tmp = float(num)
        kg = tmp * 0.45359237
        return kg
    except ValueError:
        print("Please provide a number.")
