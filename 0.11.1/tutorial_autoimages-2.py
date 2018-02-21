import matplotlib.pyplot as plt
import numpy as np
import wradlib

# load a polar scan and create range and azimuth arrays accordingly
# path starts in your documentation root
filename = wradlib.util.get_wradlib_data_file('misc/polar_dBZ_tur.gz')
data = np.loadtxt(filename)
r = np.arange(0, data.shape[1])
az = np.arange(0, data.shape[0])
# mask data array for better presentation
mask_ind = np.where(data <= np.nanmin(data))
data[mask_ind] = np.nan
ma = np.ma.array(data, mask=np.isnan(data))
# the simplest call, plot cg ppi in new window
# plot simple CG PPI
wradlib.vis.plot_cg_ppi(ma, refrac=False)
t = plt.title('Simple CG PPI')
t.set_y(1.05)
plt.tight_layout()
plt.show()