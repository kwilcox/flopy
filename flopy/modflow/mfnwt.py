from flopy.mbase import Package

class ModflowNwt(Package):
    '''Newton solver package
    Only programmed to work with the default values; need work for option [options = SPECIFIED]'''
    def __init__(self, model, headtol = 1E-4, fluxtol = 500, maxiterout = 100, \
                 thickfact = 1E-5, linmeth = 1, iprnwt = 0, ibotav = 0, \
                 options = 'COMPLEX', Continue=False, \
                 dbtheta=0.4, dbkappa=1.e-5, dbgamma=0., momfact=0.1, \
                 backflg=1, maxbackiter=50, backtol=1.1, backreduce=0.70, \
                 maxitinner=50, ilumethod=2, levfill=5, stoptol=1.e-10, msdr=15, \
                 iacl=2, norder=1, level=5, north=7, iredsys=1, rrctols=0.0, \
                 idroptol=1, epsrn=1.e-4, hclosexmd=1e-4, mxiterxmd=50, \
                 extension='nwt', unitnumber = 32):
        Package.__init__(self, model, extension, 'NWT', unitnumber) # Call ancestor's init to set self.parent, extension, name and unit number
        self.heading = '# NWT for MODFLOW-NWT, generated by Flopy.'
        self.url = 'nwt_newton_solver.htm'
        self.headtol = headtol
        self.fluxtol = fluxtol
        self.maxiterout = maxiterout
        self.thickfact = thickfact
        self.linmeth = linmeth
        self.iprnwt = iprnwt
        self.ibotav = ibotav
        if isinstance(options, list):
            self.options = options
        else:
            self.options = [options.upper()]
        if Continue:
            self.options.append('CONTINUE')
        self.dbtheta = dbtheta
        self.dbkappa = dbkappa
        self.dbgamma = dbgamma
        self.momfact = momfact
        self.backflg = backflg
        self.maxbackiter = maxbackiter
        self.backtol = backtol
        self.backreduce = backreduce
        self.maxitinner = maxitinner
        self.ilumethod = ilumethod
        self.levfill = levfill
        self.stoptol = stoptol
        self.msdr = msdr
        self.iacl = iacl
        self.norder = norder
        self.level = level
        self.north = north
        self.iredsys = iredsys
        self.rrctols = rrctols
        self.idroptol = idroptol
        self.epsrn = epsrn
        self.hclosexmd = hclosexmd
        self.mxiterxmd = mxiterxmd
        self.parent.add_package(self)
    def __repr__( self ):
        return 'Newton solver package class'
    def write_file(self):
        # Open file for writing
        f_nwt = open(self.fn_path, 'w')
        f_nwt.write('%s\n' % self.heading)
        f_nwt.write('%10.1e%10.1e%10i%10.1e%10i%10i%10i ' % (self.headtol, self.fluxtol, self.maxiterout, self.thickfact, self.linmeth, self.iprnwt, self.ibotav))
        isspecified = False
        for option in self.options:
            f_nwt.write('{0} '.format(option.upper()))
            if option.lower() == 'specified':
                isspecified = True
        if isspecified:
            f_nwt.write('{0:10.4g}'.format(self.dbtheta))
            f_nwt.write('{0:10.4g}'.format(self.dbkappa))
            f_nwt.write('{0:10.4g}'.format(self.dbgamma))
            f_nwt.write('{0:10.4g}'.format(self.momfact))
            f_nwt.write('{0:10d}'.format(self.backflg))
            if self.backflg > 0:
                f_nwt.write('{0:10d}'.format(self.maxbackiter))
                f_nwt.write('{0:10.4g}'.format(self.backtol))
                f_nwt.write('{0:10.4g}'.format(self.backreduce))
            f_nwt.write('\n')
            if self.linmeth == 1:
                f_nwt.write('{0:10d}'.format(self.maxitinner))
                f_nwt.write('{0:10d}'.format(self.ilumethod))
                f_nwt.write('{0:10d}'.format(self.levfil))
                f_nwt.write('{0:10.4g}'.format(self.stoptol))
                f_nwt.write('{0:10d}'.format(self.msdr))
            elif self.linmeth == 2:
                f_nwt.write('{0:10d}'.format(self.iacl))
                f_nwt.write('{0:10d}'.format(self.norder))
                f_nwt.write('{0:10d}'.format(self.level))
                f_nwt.write('{0:10d}'.format(self.north))
                f_nwt.write('{0:10d}'.format(self.iredsys))
                f_nwt.write('{0:10.4g}'.format(self.rrctols))
                f_nwt.write('{0:10d}'.format(self.idroptol))
                f_nwt.write('{0:10.4g}'.format(self.epsrn))
                f_nwt.write('{0:10.4g}'.format(self.hclosexmd))
                f_nwt.write('{0:10d}'.format(self.mxiterxmd))

        f_nwt.write('\n')
                
        f_nwt.close()

