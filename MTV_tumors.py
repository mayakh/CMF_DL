import numpy as np
import os
import glob
import matplotlib as mpl
from matplotlib import pyplot as plt
import nibabel as nib
import pydicom
import SimpleITK as sitk
from LesionTable import *
from read_dicom_series import *
from view_image import *
from multi_slice_viewer import *
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from scipy import stats

# Assign spreadsheet filename to `file`
#from typing import List, Any



datapath = '/Volumes/ICM_Disk2/maya/DL_Lesion'
os.chdir(datapath)

# coord, lesionDiameter = LesionTable()
MTV_bsac = np.zeros((6, 7))
MTV_ctac = np.zeros((6, 7))
MTV_dlac = np.zeros((6, 7))
MTV_ztac = np.zeros((6, 7))

k = 0
for i in glob.glob('*'):
# i = 'CMF2065'
    for l in range(1, 7):
        # l = 1
        bsac_filename = datapath + '/' + str(i) + '/base_filt4/BodySeg_MRAC_Lesion' + str(l) + '/Recon'
        bsac, size = read_dicom_series(bsac_filename)
        ctac_filename = datapath + '/' + str(i) + '/base_filt4/CT_AC_Lesion' + str(l) + '/Recon'
        ctac, size = read_dicom_series(ctac_filename)
        dlac_filename = datapath + '/' + str(i) + '/base_filt4/DLpCT_AC_Lesion' + str(l) + '/Recon'
        dlac, size = read_dicom_series(dlac_filename)
        ztac_filename = datapath + '/' + str(i) + '/base_filt4/ZTEDixon_MRAClesion' + str(l) + '/Recon'
        ztac, size = read_dicom_series(ztac_filename)
        #(cx, cy, cz) = coord[k, l]
        # sz = 600 / size[2]
        # sx = 2.78  # voxel size in mm
        # rx = (lesionDiameter[k, l] * 10 / 2) / sx
        # rz = (lesionDiameter[k, l] * 10 / 2) / sz   # radius in voxel
        # lesionProfile = GEellipsoid(size[0], size[1], size[3], cx, cy, cz, rx, rx, rz)
        # bounding_box = ztac[int(size[1]/2+cx-rx):int(size[1]/2+cx+rx)+1, int(size[2]/2+cy-rx):int(size[2]/2+cy+rx)+1, int(cz-rz):int(cz+rz)+1]
        stats = sitk.StatisticsImageFilter()
        stats.Execute(bsac)
        thresh = 0.42 * stats.GetMaximum()
        mask_lesion = sitk.Maximum(bsac, thresh)
        # multi_slice_viewer(mask_lesion)
        stats.Execute(mask_lesion)
        MTV_bsac[k, l] = stats.GetSum()
        stats.Execute(ctac)
        thresh = 0.42 * stats.GetMaximum()
        mask_lesion = sitk.Maximum(ctac, thresh)
        # multi_slice_viewer(mask_lesion)
        stats.Execute(mask_lesion)
        MTV_ctac[k, l] = stats.GetSum()
        stats.Execute(dlac)
        thresh = 0.42 * stats.GetMaximum()
        mask_lesion = sitk.Maximum(dlac, thresh)
        # multi_slice_viewer(mask_lesion)
        stats.Execute(mask_lesion)
        MTV_dlac[k, l] = stats.GetSum()
        stats.Execute(ztac)
        thresh = 0.42 * stats.GetMaximum()
        mask_lesion = sitk.Maximum(ztac, thresh)
        # multi_slice_viewer(mask_lesion)
        stats.Execute(mask_lesion)
        MTV_ztac[k, l] = stats.GetSum()
    k = k + 1

ind = range(1, 5)
p1 = plt.bar(ind, (MTV_bsac.mean(), MTV_ztac.mean(), MTV_dlac.mean(), MTV_ctac.mean()) , 0.35)
# p2 = plt.bar(ind, MTV_ztac.mean(), 0.35)
# p3 = plt.bar(ind, MTV_dlac.mean(), 0.35)
# p4 = plt.bar(ind, MTV_ctac.mean(), 0.35)
plt.ylabel('MTV (mL)')
#plt.xticks('Dixon-AC', 'hZTE-AC', 'DL-AC', 'CT-AC')
plt.legend((p1[0], p1[1], p1[2], p1[3]), ('Dixon-AC', 'hZTE-AC', 'DL-AC', 'CT-AC'))
plt.show()