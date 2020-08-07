# the data is downloaded from the original source, ie, 
# http://gigadb.org/dataset/view/id/100295 (scroll down to Files tab, then click on '(FTP-Site)')

# we use wget library to download from the ftp server
# can be download using pip: pip install wget

import wget
import pandas as pd
import numpy as np
import os
import scipy.io

def download_mat(subjects):
  urls = []
  nums = 53
  left = []
  right = []
  event_markers = []
  for i in range(len(subjects)):
    sub = subjects[i]
    urls.append('ftp://parrot.genomics.cn/gigadb/pub/10.5524/100001_101000/100295/mat_data/' + sub)
    #print(urls)
    wget.download(urls[i], os.path.join('/content', sub))

  # ---- Following code is for reading the mat file and extracting that data we need: -------
    #print('Subject {} mat file downloaded! Starting to load the .npy files'.format(sub[1:3]))
    
    subject_i = scipy.io.loadmat('/content/' + sub)
    # how subject.mat files are structured is desccribed here: 
    # https://academic.oup.com/gigascience/article/6/7/gix034/3796323

    left.append(subject_i['eeg']['imagery_left'][0][0][:64])
    right.append(subject_i['eeg']['imagery_right'][0][0][:64])
    event_markers.append(subject_i['eeg']['imagery_event'][0][0][0])

    # print(left.shape, event_markers.shape) # (64, 358400) (358400,)

    df_left = pd.DataFrame(left[i]).T.rename(columns = lambda x: 'left'+str(x))
    df_right = pd.DataFrame(right[i]).T.rename(columns = lambda x: 'right'+str(x))
    markers = pd.Series(event_markers[i])

    df = df_left.join(df_right)
    df['mark'] = markers

    ind = list(df[df['mark'] == 1].index)
    ind = ind + [358399]
    intervals = list(zip(ind[:-1], ind[1:]))

    dfset_left = []
    dfset_right = []
    for start, end in intervals[:-1]:
        dfset_left.append(df.loc[start:end-1, 'left0':'left63'])
        dfset_right.append(df.loc[start:end-1, 'right0':'right63'])

    bci_left = []
    for df in dfset_left:
        bci_left.append(df.values.T)
    bci_left = np.array(bci_left)
    np.save('bci_imagery_left_sub{}.npy'.format(sub[1:3]), bci_left)

    bci_right = []
    for df in dfset_right:
        bci_right.append(df.values.T)
    bci_right = np.array(bci_right)
    np.save('bci_imagery_right_sub{}.npy'.format(sub[1:3]), bci_right)

    # print(bci_left.shape, bci_right.shape) # (99, 64, 3584) (99, 64, 3584)

# Example testing   
download_mat(['s01.mat', 's02.mat', 's03.mat'])
