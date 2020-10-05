"""Print out all the melons in our inventory."""

from melons import melons_dict

def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    for melon_key, melon_values in melons_dict.items():
        print(melon_key.upper())
    
        for melon_value_name, melon_value in melon_values.items():
            print(f'\t{melon_value_name}: {melon_value}')
        print('---------------------------------------------')
print_melon(melons_dict)
