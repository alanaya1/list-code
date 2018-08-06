import numpy as np
import pymatgen
# from pymatgen import MPRester

from matminer.featurizers.site import CrystalNNFingerprint
from matminer.featurizers.structure import SiteStatsFingerprint
structuraldif = []
with pymatgen.MPRester("iUCzg5aBMJ1w30KT") as mpr:

    # Get structures.
    SnSelow = mpr.get_structure_by_material_id("mp-1984")
    SnSehigh = mpr.get_structure_by_material_id("mp-1411")

    # Calculate structure fingerprints.
    ssf = SiteStatsFingerprint(CrystalNNFingerprint.from_preset('cn'))
    v_SnSelow = np.array(ssf.featurize(SnSelow))
    v_SnSehigh = np.array(ssf.featurize(SnSehigh))
    v_SnSelow = v_SnSelow / np.linalg.norm(v_SnSelow)
    v_SnSehigh = v_SnSehigh / np.linalg.norm(v_SnSehigh)


    # Print out distance between structures.
    fish = '{:.4f}'.format(np.linalg.norm(v_SnSehigh - v_SnSelow))
    structuraldif.append(fish)
print(structuraldif)
