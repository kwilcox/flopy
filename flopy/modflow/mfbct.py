import numpy as np
from flopy.mbase import Package
from flopy.utils import util_2d,util_3d

class ModflowBct(Package):
    '''
    Block centered transport package class for MODFLOW-USG
    '''
    def __init__(self, model, itrnsp=1, ibctcb=0, mcomp=1, ic_ibound_flg=1,
                 itvd=1, iadsorb=0, ict=0, cinact=-999., ciclose=1.e-6,
                 idisp=1, ixdisp=0, diffnc=0., izod=0, ifod=0, icbund=1,
                 porosity=0.1, bulkd=1., dlh=0., dlv=0., dth=0., dtv=0.,
                 sconc=0.,
                 extension='bct', unitnumber=35):
        Package.__init__(self, model, extension, 'BCT', unitnumber)
        self.url = 'bct.htm'
        nrow, ncol, nlay, nper = self.parent.nrow_ncol_nlay_nper
        self.itrnsp = itrnsp
        self.ibctcb = ibctcb
        self.mcomp = mcomp
        self.ic_ibound_flg = ic_ibound_flg
        self.itvd = itvd
        self.iadsorb = iadsorb
        self.ict = ict
        self.cinact = cinact
        self.ciclose = ciclose
        self.idisp = idisp
        self.ixdisp = ixdisp
        self.diffnc = diffnc
        self.izod = izod
        self.ifod = ifod
        self.icbund = util_3d(model, (nlay, nrow, ncol), np.float32, icbund,
                              'icbund',)
        self.porosity = util_3d(model, (nlay, nrow, ncol), np.float32,
                                porosity, 'porosity')
        self.dlh = util_3d(model, (nlay, nrow, ncol), np.float32, dlh, 'dlh')
        self.dlv = util_3d(model, (nlay, nrow, ncol), np.float32, dlv, 'dlv')
        self.dth = util_3d(model, (nlay, nrow, ncol), np.float32, dth, 'dth')
        self.dtv = util_3d(model, (nlay, nrow, ncol), np.float32, dth, 'dtv')
        self.sconc = util_3d(model, (nlay, nrow, ncol), np.float32, sconc,
                             'sconc',)
        self.parent.add_package(self)
        return

    def write_file(self):
        nrow, ncol, nlay, nper = self.parent.nrow_ncol_nlay_nper
        # Open file for writing
        f_bct = open(self.fn_path, 'w')
        # Item 1: ITRNSP, IBCTCB, MCOMP, IC_IBOUND_FLG, ITVD, IADSORB,
        #         ICT, CINACT, CICLOSE, IDISP, IXDISP, DIFFNC, IZOD, IFOD
        s = '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13}'
        s = s.format(self.itrnsp, self.ibctcb, self.mcomp, self.ic_ibound_flg,
                     self.itvd, self.iadsorb, self.ict, self.cinact,
                     self.ciclose, self.idisp, self.ixdisp, self.diffnc,
                     self.izod, self.ifod)
        f_bct.write(s + '\n')
        #
        #ibound
        if(self.ic_ibound_flg == 0):
            for k in range(nlay):
                f_bct.write(self.icbund[k].get_file_entry())
        #
        #porosity
        for k in range(nlay):
            f_bct.write(self.porosity[k].get_file_entry())
        #
        #bulkd
        if self.iadsorb != 0:
            for k in range(nlay):
                f_bct.write(self.bulkd[k].get_file_entry())
        #
        #dlh
        if self.idisp == 1:
            for k in range(nlay):
                f_bct.write(self.dlh[k].get_file_entry())
        #
        #dlv
        if self.idisp == 2:
            for k in range(nlay):
                f_bct.write(self.dlv[k].get_file_entry())
        #
        #dth
        if self.idisp == 1:
            for k in range(nlay):
                f_bct.write(self.dth[k].get_file_entry())
        #
        #dtv
        if self.idisp == 2:
            for k in range(nlay):
                f_bct.write(self.dtv[k].get_file_entry())
        #
        #sconc
        for k in range(nlay):
            f_bct.write(self.sconc[k].get_file_entry())


        return

