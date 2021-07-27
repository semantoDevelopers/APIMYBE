

def double_to_stripe_value(value):
    value_string = str(value)
    value_without_points = value_string.replace('.','')
    return int(value_without_points)