#perform transformation of Extract-Transform-Load

#old system: store groups of letters by shared score,
#new system: store score by letter (for faster lookup)

def transform(old_dict):
    return {value.lower(): key for key, values in old_dict.items() for value in values}
