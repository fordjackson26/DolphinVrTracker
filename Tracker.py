import numpy as np
import struct
import sys
import os
import time
import signal
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt




def get_track_counts(path, lic):
    with open(path, mode = 'rb') as file:
        fileContent = file.read()
    of = 0x166
    track_counts = dict()
    for t in tracks:
        track_counts[t] = struct.unpack_from('>H', fileContent, offset= of + lic)[0]
        of += 0x2
    rc = struct.unpack_from('>i', fileContent, offset= 0xB4 + lic)[0]
    return track_counts, rc
def display(data):
    plt.style.use('seaborn-darkgrid')
    plt.plot(data.index, data["VR"].tolist(), linewidth=.5, color='k', linestyle='--')
    sns.set(rc={'figure.figsize': (20, 10)})
    sns.scatterplot(data=data, x="Race", y="VR", hue="Track")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.show()
    sns.barplot(data=data, x='Track', y='Change')
    plt.show()

def rc_get(path, lic):
    with open(path, mode = 'rb') as file:
        fileContent = file.read()
    rc = struct.unpack_from('>i', fileContent, offset=0xB4 + lic)[0]
    return rc

def track_played(curr_tracks, lic):
    new_tracks = get_track_counts(sys.argv[1], lic)[0]
    for t in tracks:
        if curr_tracks[t] != new_tracks[t]:
            return t
    return 'ct'


def vr_get(path, lic):
    with open(path, mode = 'rb') as file:
        fileContent = file.read()
    vr = struct.unpack_from('>H', fileContent, offset=0xB0 + lic)
    print(vr[0])
    return vr[0]

def main(data, lic, save, rc, tc):

    t1 = os.path.getmtime(sys.argv[1])
    print(t1)
    orgVR = vr_data["VR"][vr_data.index[-1]]
    ogRC = rc
    sames = 0
    DC = False
    while True:
        if sames >= 8:
            break
        t2 = os.path.getmtime(sys.argv[1])
        if(t1 == t2):
            sames+=1
            t2 = os.path.getmtime(sys.argv[1])
            print('check\n')
            time.sleep(1)
        else:
            sames = 0
            t1 = t2


            race_count = rc_get(sys.argv[1], lic)

            if race_count != ogRC:
                ogRC = race_count
                nVR = vr_get(sys.argv[1], lic)
                track = track_played(tc, lic)
                print(track+ " " + str(nVR))
                data.loc[len(data.index)] = [len(data.index), nVR, track,  nVR - data["VR"][data.index[-1]]]
                # data = np.append(data, [nVR])


            time.sleep(20)
    data.to_csv("vrData/" + save, index=False)
    display(data)








if __name__ == "__main__":
    tracks = ['mc', 'mmm', 'mg', 'gv', 'tf', 'cm', 'dksc', 'wgm', 'lc', 'dc', 'mh', 'mt', 'bc', 'rr', 'ddr', 'kc',
              'rpb', 'rmc', 'rws', 'rdkm',
              'ryf', 'rdh', 'rpg', 'rds', 'rmc3', 'rgv2', 'rmr', 'rsl', 'rbc', 'rdkjp', 'rbc3', 'rsgb']

    licences = [0x8, 0x8CC8, 0x11988, 0x1A648]
    saves =  ['vr1.csv', 'vr2.csv' , 'vr3.csv', 'vr4.csv']
    lic = int(sys.argv[2]) - 1
    for i in sys.argv:
        print(i)

    vr_data = pd.read_csv('dataframe.csv')
    print( vr_data["VR"][vr_data.index[-1]])
    track_counts , race_count = get_track_counts(sys.argv[1], licences[lic])
    track_played(track_counts, licences[lic])

    main(vr_data, licences[lic], saves[lic], race_count, track_counts)



