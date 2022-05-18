

"""
These functions assist in extracting data from hydrodynamic models (Hycom and Mercator).
With them it is possible to choose the closest point of interest (within Netcdf), 
extract time series, transform longitudes and latitudes, and create time vectors based
on a reference date.
"""

def lon360to180(lon):
    """
    Converts longitude values in the range [0,360]
    to longitude values in the range [-180,+180].
    """
    from numpy import  asanyarray
    lon = asanyarray(lon)
    
    return ((lon + 180.) % 360.) - 180.



def hours2dates(reference_date, values):
    """"
    Converts hours values in datetime based in a
    specific date.  The reference date must be in the
    format Day/Month/Year Hour:Minutes
    """
    import datetime as dt
    
    date_python = dt.datetime.strptime(reference_date,
                                    '%d/%m/%Y %H:%M')
    
    mytime = [date_python + dt.timedelta(hours = x) for x in values]
    
    return mytime



def cartesian(x, y):

    # This function creates a matrix with two columns, 
    # the first referring to the x axis and the second to the y axis. 
    # Each row in the matrix refers to a pair (x, y).


    from numpy import zeros

    array = zeros ([len (x) * len (y), 2])

    counter = 0

    for line in range ( len(x) ):

        for colunm in range( len(y) ):

            array [counter, 0] = x [line]
            array [counter, 1] = y [colunm]
            counter += 1

    return array



def closest(array, x0, y0):
    """
    The function finds the latitude and longitude coordinates
    that are closest to your interest point. 
    The input values are x0 ->lon, y0 ->lat.
    """
    distances = ((array[:,0]-x0)**2
                + (array[:,1]-y0)**2)**.5
    d_min = distances.min()

    lon_point= array[distances == d_min,0]

    lat_point = array[distances == d_min,1]

    return lon_point, lat_point 

def main():
    
    print("")   

if __name__ == "__main__":
    main()