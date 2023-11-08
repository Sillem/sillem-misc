""" File where I play and try out my own bootstrap algorithm and see what affects it's performance """


# coding: utf-8
import numpy as np
get_ipython().run_line_magic('pinfo', 'np.random.normal')
# our X is drawn from N(15,5) distribution
sample = np.random.normal(15, 5, 100)
sample.size
def resampling(sample):
    indices = np.random.randint(0, len(sample), len(sample))
    return sample[indices]
    
resampling(sample)
resampling(sample).mean()
resampling(sample).std()
def estimate_parameter(sample, parameter='mean'):
    q
    
def estimate_parameter(sample, instances, parameter='mean'):
    parameters = np.zeros(instances)
    for instance in range(instances):
        current_sample = resample(sample)
        parameters[instance] = current_sample.mean()
    return parameters
    
    
estimate_parameter(sample, 10000)
def estimate_parameter(sample, instances, parameter='mean'):
    parameters = np.zeros(instances)
    for instance in range(instances):
        current_sample = resampling(sample)
        parameters[instance] = current_sample.mean()
    return parameters
    
estimate_parameter(sample, 10000)
estimate_parameter(sample, 10000).percentile(0.75)
means = _
np.percentile(means, 0.95)
np.percentile(means, 0.05)
np.percentile(means, [5, 95])
np.percentile(means, [2.5, 97.5])
#managed to build 95% confidence interval for our population with dist N(15, 5) based on bootstrap.
#what will happen to the width of the interval as we increase the number of boostrap samples?
width_1 = Out[20][1] - Out[20][0]
means_2 = estimate_parameter(sample, 1000000000)
means_2 = estimate_parameter(sample, 100000)
means_2 = estimate_parameter(sample, 1000000)
np.percentile(means_2, [2.5, 97.5])
width_2 = _[1] - _[0]
width_1, width_2
# very small improvement of error, maybe increasing sample will give us more insights
means_2 = estimate_parameter(np.normal(15, 5, 10000), 1000000)
means_2 = estimate_parameter(np.random.normal(15, 5, 10000), 1000000)
np.percentile(means_2, [2.5, 97.5])
width_1, width_2
width_2 = __
width_1, width_2
width_2 = width_2[1] - width_2[0]
width_1, width_2
# yeah increasing the sample size of base population sample has a mangitude higher impact than increasing number of resampling
