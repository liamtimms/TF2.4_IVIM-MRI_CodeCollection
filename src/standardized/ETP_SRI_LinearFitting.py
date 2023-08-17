import numpy as np
from src.wrappers.OsipiBase import OsipiBase
from src.original.ETP_SRI.LinearFitting import LinearFit


class ETP_SRI_LinearFitting(OsipiBase):
    """WIP
    Implementation and execution of the submitted algorithm
    """
    
    # I'm thinking that we define default attributes for each submission like this
    # And in __init__, we can call the OsipiBase control functions to check whether
    # the user inputs fulfil the requirements
    
    # Some basic stuff that identifies the algorithm
    id_author = "Eric T. Peterson, SRI"
    id_algorithm_type = "Linear fit"
    id_return_parameters = "f, D*, D"
    id_units = "seconds per milli metre squared"
    
    # Algorithm requirements
    required_bvalues = 3
    required_thresholds = [1,1] # Interval from 1 to 1, in case submissions allow a custom number of thresholds
    required_bounds = False
    required_bounds_optional = True # Bounds may not be required but are optional
    required_initial_guess = False
    required_initial_guess_optional = False
    accepted_dimensions = 1
    
    def __init__(self, bvalues=None, thresholds=None, bounds=None, initial_guess=None, weighting=None, stats=False):
        """
            Everything this method requires should be implemented here.
            Number of segmentation thresholds, bounds, etc.
            
            Our OsipiBase object could contain functions that compare the inputs with
            the requirements.
        """
        super(ETP_SRI_LinearFitting, self).__init__(bvalues, thresholds, bounds, initial_guess)
        
        # Could be a good idea to have all the submission-specfic variable be 
        # defined with initials?
        self.ETP_weighting = weighting
        self.ETP_stats = stats
        
        # Check the inputs
        
    
    def ivim_fit(self, signals, bvalues):
        """
            We may want this function to be as simple as
            data and b-values in -> parameter estimates out.
            Everything else such as segmentation thresholds, bounds, etc. should
            be object attributes.
            
            This makes the execution of submissions easy and predictable.
            All execution stepts requires should be performed here.
        """
        
        ETP_object = LinearFit(self.thresholds[0])
        f, D, Dstar = ETP_object.ivim_fit(bvalues, signals)
        
        
        
        return (f, Dstar, D)
    


# Simple test code... 
bvalues = np.array([0, 200, 500, 800])

def ivim_model(b, S0=1, f=0.1, Dstar=0.03, D=0.001):
    return S0*(f*np.exp(-b*Dstar) + (1-f)*np.exp(-b*D))

signals = ivim_model(bvalues)

model = ETP_SRI_LinearFitting(thresholds=[200])
results = model.ivim_fit(signals, bvalues)
test = model.osipi_simple_bias_and_RMSE_test(SNR=20, bvalues=bvalues, f=0.1, Dstar=0.03, D=0.001, noise_realizations=10)
#model.print_requirements_osipi()