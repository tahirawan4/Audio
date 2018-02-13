import csv
import os

from Audio.settings import PROJECT_ROOT
from age_estimation.models import UserInfo


def save_user_info(user, age, frequency, frequency2, average, country):
    UserInfo.objects.create(user=user, age=age, country=country, frequency=frequency, frequency2=frequency2,
                            average=average)


def estimate_age(aver_freq):
    """This function estimates age by using average frequency"""
    file_ = open(os.path.join(PROJECT_ROOT, 'data.csv'))
    csv_data = csv.reader(file_, delimiter=',')
    i = 0
    temp1 = 20
    temp2 = 20000
    age = 0
    age1 = 0
    age2 = 100
    for row in csv_data:
        i += 1
        if i == 1:
            continue
        sample_freq = int(row[6])
        if (temp1 <= sample_freq) and (sample_freq <= aver_freq):
            temp1 = sample_freq
            age1 = int(row[2])
        elif (temp2 >= sample_freq) and (sample_freq >= aver_freq):
            temp2 = sample_freq
            age2 = int(row[2])
        else:
            pass

    if (aver_freq - temp1) < (temp2 - aver_freq):
        age = age1
    else:
        age = age2
    return [i, age]
