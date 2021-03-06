from shadowcraft.core.exceptions import InvalidLevelException

# tiered parameters for use in armor mitigation calculations. first tuple
# element is the minimum level of the tier. the tuples must be in descending
# order of minimum level for the lookup to work. parameters taken from
# http://code.google.com/p/simulationcraft/source/browse/branches/mop/engine/sc_player.cpp#1365
PARAMETERS = [ (86, 4037.5, 317117.5),
               (81, 2167.5, 158167.5),
               (60,  467.5,  22167.5),
               ( 1,   85.0,   -400.0) ] # yes, negative 400

def lookup_parameters(level):
    for parameters in PARAMETERS:
        if level >= parameters[0]:
            return parameters
    raise InvalidLevelException(_('No armor mitigation parameters available for level {level}').format(level=level))

def parameter(level=90):
    parameters = lookup_parameters(level)
    return level * parameters[1] - parameters[2]

# this is the fraction of damage reduced by the armor
def mitigation(armor, level=90, cached_parameter=None):
    if cached_parameter == None:
        cached_parameter = parameter(level)
    return armor / (armor + cached_parameter)

# this is the fraction of damage retained despite the armor, 1 - mitigation. 
def multiplier(armor, level=90, cached_parameter=None):
    if cached_parameter == None:
        cached_parameter = parameter(level)
    return cached_parameter / (armor + cached_parameter)
