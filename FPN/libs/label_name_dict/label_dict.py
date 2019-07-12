# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from libs.configs import cfgs

if cfgs.DATASET_NAME == 'ship':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        "ship": 1
    }
elif cfgs.DATASET_NAME == 'SSDD':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        "ship": 1
    }
elif cfgs.DATASET_NAME == 'airplane':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        "airplane": 1
    }
elif cfgs.DATASET_NAME == 'nwpu':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'airplane': 1,
        'ship': 2,
        'storage tank': 3,
        'baseball diamond': 4,
        'tennis court': 5,
        'basketball court': 6,
        'ground track field': 7,
        'harbor': 8,
        'bridge': 9,
        'vehicle': 10,
    }
elif cfgs.DATASET_NAME == 'pascal':
    NAME_LABEL_MAP = {
        'back_ground': 0,
        'coscinodiscus': 1,
        'dinophysis caudata': 2,
        'corethron': 3,
        'eucampia': 4,
        'ditylum': 5,
        'navicula': 6,
        'chaetoceros': 7,
        'ceratium fusus': 8,
        'skeletonema': 9,
        'biddulphia': 10,
        'ceratium furca': 11,
        'rhizosolenia': 12,
        'ceratium trichoceros': 13,
        'ceratium tripos': 14,
        'thalassionema frauenfeldii': 15,
        'detonula pumila': 16,
        'helicotheca': 17,
        'pleurosigma pelagicum': 18,
        'ceratium carriense': 19,
        'thalassionema nitzschioides': 20,
        'guinardia flaccida': 21,
        'protoperidinium': 22,
        'bacteriastrum': 23,
        'coscinodiscus flank': 24
    }
else:
    assert 'please set label dict!'

def get_label_name_map():
    reverse_dict = {}
    for name, label in NAME_LABEL_MAP.items():
        reverse_dict[label] = name
    return reverse_dict

LABEl_NAME_MAP = get_label_name_map()