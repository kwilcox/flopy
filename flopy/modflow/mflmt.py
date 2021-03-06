"""
mflmt module.  Contains the ModflowLmt class. Note that the user can access
the ModflowLmt class as `flopy.modflow.ModflowLmt`.

Additional information for this MODFLOW package can be found at the `Online
MODFLOW Guide
<http://water.usgs.gov/ogw/modflow/MODFLOW-2005-Guide/index.html?lmt.htm>`_.

"""
from flopy.mbase import Package

class ModflowLmt(Package):
    """
    MODFLOW Link-MT3DMS Package Class.

    Parameters
    ----------
    model : model object
        The model object (of type :class:`flopy.modflow.mf.Modflow`) to which
        this package will be added.
    output_file_name : string
        Filename for output file (default is 'mt3d_link.ftl')
    unitnumber : int
        File unit number (default is 24).
    output_file_unit : int
        Output file unit number, pertaining to the file identified
        by output_file_name (default is 54).
    output_file_header : string
        Header for the output file (default is 'extended')
    output_file_format : {'formatted', 'unformatted'}
        Format of the output file (default is 'unformatted')
    extension : string
        Filename extension (default is 'lmt6')
    unitnumber : int
        File unit number (default is 30).

    Attributes
    ----------

    Methods
    -------

    See Also
    --------

    Notes
    -----
    Parameters are supported in Flopy only when reading in existing models.
    Parameter values are converted to native values in Flopy and the
    connection to "parameters" is thus nonexistent.

    Examples
    --------

    >>> import flopy
    >>> m = flopy.modflow.Modflow()
    >>> lmt = flopy.modflow.ModflowLmt(m, output_file_name='mt3d_linkage.ftl')

    """
    def __init__(self, model, output_file_name='mt3d_link.ftl',
                 output_file_unit=54, output_file_header='extended',
                 output_file_format='unformatted', extension='lmt6', unitnumber=30):
        # Call ancestor's init to set self.parent, extension, name and unit number
        Package.__init__(self, model, extension, 'LMT6', unitnumber)
        self.heading = '# Lmt input file for MODFLOW, generated by Flopy.'
        self.url = 'lmt.htm'
        self.output_file_name = output_file_name
        self.output_file_unit = output_file_unit
        self.output_file_header = output_file_header
        self.output_file_format = output_file_format
        self.parent.add_package(self)

    def __repr__(self):
        return 'Link-MT3D package class'

    def write_file(self):
        f_lmt = open(self.fn_path, 'w')
        f_lmt.write('%s\n' % self.heading)
        f_lmt.write('%s\n' % ('OUTPUT_FILE_NAME ' + self.output_file_name))
        f_lmt.write('%s%10i\n' % ('OUTPUT_FILE_UNIT ', self.output_file_unit))
        f_lmt.write('%s\n' % ('OUTPUT_FILE_HEADER ' + self.output_file_header))
        f_lmt.write('%s\n' % ('OUTPUT_FILE_FORMAT ' + self.output_file_format))
        f_lmt.close()

