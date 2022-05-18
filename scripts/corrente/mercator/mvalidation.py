

# model validatins functions. 


from numpy import deg2rad, rad2deg
from numpy import nanmean, arctan
from numpy import sin, cos, pi
from numpy import nansum, sqrt
from numpy import isnan


def rmse(observed, model):
	'''
	This function returns the square root of the mean
	squared error between two vectors, x and y.

	'''
	value = sqrt((nansum((model-observed)**2))/len(observed[~isnan(observed) ]))

	return value




def angleAverage(angles):
	'''
	Returns the angle average (in radians) of a sequence of
	angles in the range [-pi/2, pi/2]. The input must be in degrees format.
	'''
	
	sinA = nanmean(sin(deg2rad(angles)))
	cosA = nanmean(cos(deg2rad(angles)))
	
	value = arctan(sinA/cosA)

	return value



def scatterIndex(model,observed):
	'''
	Returns the scattering index between two vectors. 
	The input data must have the same dimensions and units. 
	'''

	value= rmse(observed, model)/nanmean(observed)
	return value



def skill(observed, model):

	'''
	Returns Willmott's concordance index. More information in
	Willmott (1981) and Warner et. al(2005).
	'''
	numerator = nansum((abs(model-observed))**2)

	denominator = (abs(model-nanmean(observed))+ abs(observed-nanmean(model)))**2

	denominator = nansum(denominator)

	value = 1-(numerator/denominator)

	return value




# angle skill
def angleSkill(observed, model):

	'''
	This function receives angles values (degrees format)
	returning the skill of the values. The input
	must be array with 1 dimension or a python list.
	'''

	numerator = nansum((deg2rad(model)-deg2rad(observed))**2)

	denominator = (abs ( deg2rad(model)- angleAverage (observed) ) 
		+ abs ( deg2rad(observed) - angleAverage(observed) ) ) **2

	denominator = nansum(denominator)

	value = 1-(numerator/denominator)

	return value

def main():
	print('funcionando ...')

if __name__ == "__main__":

	main()
