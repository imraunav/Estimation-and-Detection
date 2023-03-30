import numpy as np
import mne
import pandas as pd
from matplotlib import pyplot as plt

def map_ft9(raw):
    '''
    Input parameters:
    raw data
    
    Returns:
    data, labels'''
    df = raw.to_data_frame()
    np_array = df.to_numpy()
    fp1_f7 = np_array[:, 1]
    f7_t7 = np_array[:, 2]
    t7_p7 = np_array[:, 3]
    p7_o1 = np_array[:, 4]
    fp1_f3 = np_array[:, 5]
    f3_c3 = np_array[:, 6]
    c3_p3 = np_array[:, 7]
    p3_o1 = np_array[:, 8]
    fp2_f4 = np_array[:, 9]
    f4_c4 = np_array[:, 10]
    c4_p4 = np_array[:, 11]
    p4_o2 = np_array[:, 12]
    fp2_f8 = np_array[:, 13]
    f8_t8 = np_array[:, 14]
    t8_p8 = np_array[:, 15]
    p8_o2 = np_array[:, 16]
    fz_cz = np_array[:, 17]
    cz_pz = np_array[:, 18]
    p7_t7 = np_array[:, 19]
    t7_ft9 = np_array[:, 20]
    ft9_ft10 = np_array[:, 21]
    ft10_t8 = np_array[:, 22]

    # change the references
    fp1_ft9 = fp1_f7+f7_t7+t7_ft9
    f7_ft9 = f7_t7+t7_ft9
    # fp1_ft9 = fp1_f3+f3_c3+c3_p3+p3_o1-p7_o1+p7_t7+t7_ft9
    f3_ft9 = f3_c3+c3_p3+p3_o1-p7_o1+p7_t7+t7_ft9
    c3_ft9 = c3_p3+p3_o1-p7_o1+p7_t7+t7_ft9
    p3_ft9 = p3_o1-p7_o1+p7_t7+t7_ft9
    fp2_ft9 = fp2_f4+f4_c4+c4_p4+p4_o2-p8_o2-t8_p8-ft10_t8-ft9_ft10
    f4_ft9 = f4_c4+c4_p4+p4_o2-p8_o2-t8_p8-ft10_t8-ft9_ft10
    c4_ft9 = c4_p4+p4_o2-p8_o2-t8_p8-ft10_t8-ft9_ft10
    p4_ft9 = p4_o2-p8_o2-t8_p8-ft10_t8-ft9_ft10
    # fp2_fp9
    f8_ft9 = f8_t8+t8_p8-ft10_t8-ft9_ft10 # +p8_o2-(p4_o2)+p4_ft9
    t8_ft9 = t8_p8-ft10_t8-ft9_ft10 #t8_p8+p8_o2-(p4_o2)+p4_ft9
    p8_o2 = p8_o2-(p4_o2)+p4_ft9
    p7_ft9 = p7_t7+t7_ft9
    # t7_ft9
    ft10_ft9 = -ft9_ft10
    # ft10_t8
    data = np.vstack((fp1_ft9, f7_ft9, f3_ft9, c3_ft9, p3_ft9, fp2_ft9, f4_ft9, c4_ft9, p4_ft9, f8_ft9, t8_ft9, p8_o2, p7_ft9, ft10_ft9))
    labels = ["fp1_ft9",
              "f7_ft9",
              "f3_ft9",
              "c3_ft9",
              "p3_ft9",
              "fp2_ft9",
              "f4_ft9",
              "c4_ft9",
              "p4_ft9",
              "f8_ft9",
              "t8_ft9",
              "p8_o2",
              "p7_ft9",
              "ft10_ft9",
              ]
    return data, labels




def map_ft10(raw):
    '''
    Input parameters:
    raw data
    
    Returns:
    data, labels'''
    df = raw.to_data_frame()
    np_array = df.to_numpy()
    fp1_f7 = np_array[:, 1]
    f7_t7 = np_array[:, 2]
    t7_p7 = np_array[:, 3]
    p7_o1 = np_array[:, 4]
    fp1_f3 = np_array[:, 5]
    f3_c3 = np_array[:, 6]
    c3_p3 = np_array[:, 7]
    p3_o1 = np_array[:, 8]
    fp2_f4 = np_array[:, 9]
    f4_c4 = np_array[:, 10]
    c4_p4 = np_array[:, 11]
    p4_o2 = np_array[:, 12]
    fp2_f8 = np_array[:, 13]
    f8_t8 = np_array[:, 14]
    t8_p8 = np_array[:, 15]
    p8_o2 = np_array[:, 16]
    fz_cz = np_array[:, 17]
    cz_pz = np_array[:, 18]
    p7_t7 = np_array[:, 19]
    t7_ft9 = np_array[:, 20]
    ft9_ft10 = np_array[:, 21]
    ft10_t8 = np_array[:, 22]

    # change the references
    fp1_ft10 = fp1_f7+f7_t7+t7_ft9+ft9_ft10
    f7_ft10 = f7_t7+t7_ft9+ft9_ft10
    t7_ft10 = t7_ft9+ft9_ft10
    p7_ft10 = p7_o1-p3_o1-c3_p3-f3_c3-fp1_f3+fp1_ft10
    # fp1_f3
    f3_ft10 = f3_c3+c3_p3+p3_o1-p7_o1+p7_t7+t7_ft9+ft9_ft10
    c3_ft10 = c3_p3+p3_o1-p7_o1+p7_t7+t7_ft10
    p3_ft10 = p3_o1-p7_o1+p7_t7+t7_ft10
    fp2_ft10 = fp2_f4+f4_c4+c4_p4+p4_o2-p8_o2-t8_p8-ft10_t8
    f4_ft10 = f4_c4+c4_p4+p4_o2-p8_o2-t8_p8-ft10_t8
    c4_ft10 = -f4_c4-f4_ft10
    p4_ft10 = p4_o2-p8_o2-t8_p8-ft10_t8
    # fp2_f8
    f8_ft10 = f8_t8-ft10_t8
    t8_ft10 = -ft10_t8
    p8_ft10 = p8_o2-p4_o2+p4_ft10
    data = np.vstack((fp1_ft10, f7_ft10, t7_ft10, p7_ft10, f3_ft10, c3_ft10, p3_ft10, fp2_ft10, f4_ft10, c4_ft10, p4_ft10, f8_ft10, t8_ft10, p8_ft10))
    labels = ["fp1_ft10",
                "f7_ft10",
                "t7_ft10",
                "p7_ft10",
                "f3_ft10",
                "c3_ft10",
                "p3_ft10",
                "fp2_ft10",
                "f4_ft10",
                "c4_ft10",
                "p4_ft10",
                "f8_ft10",
                "t8_ft10",
                "p8_ft10",
                ]
    return data, labels

def map_avg(raw):
    '''
    Input parameters:
    raw data
    
    Returns:
    data, labels'''
    df = raw.to_data_frame()
    np_array = df.to_numpy()
    # fp1_f7 = np_array[:, 1]
    # f7_t7 = np_array[:, 2]
    # t7_p7 = np_array[:, 3]
    # p7_o1 = np_array[:, 4]
    # fp1_f3 = np_array[:, 5]
    # f3_c3 = np_array[:, 6]
    # c3_p3 = np_array[:, 7]
    # p3_o1 = np_array[:, 8]
    # fp2_f4 = np_array[:, 9]
    # f4_c4 = np_array[:, 10]
    # c4_p4 = np_array[:, 11]
    # p4_o2 = np_array[:, 12]
    # fp2_f8 = np_array[:, 13]
    # f8_t8 = np_array[:, 14]
    # t8_p8 = np_array[:, 15]
    # p8_o2 = np_array[:, 16]
    # fz_cz = np_array[:, 17]
    # cz_pz = np_array[:, 18]
    # p7_t7 = np_array[:, 19]
    # t7_ft9 = np_array[:, 20]
    # ft9_ft10 = np_array[:, 21]
    # ft10_t8 = np_array[:, 22]
    # avg_ref = np.mean(np_array, axis=0)
    avg_ref = np.sum(np_array, axis=1)/23
    for i in range(23):
        np_array[:, i] -= avg_ref
    return np_array.T, raw.ch_names
