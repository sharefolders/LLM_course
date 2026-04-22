def mean_value(values):
    if not values:
        raise ValueError('List is empty')
    return sum(values) / len(values)

def median_value(values):
    if not values:
        raise ValueError('List is empty')
    sorted_values = sorted(values)
    mid = len(sorted_values) // 2
    if len(sorted_values) % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]

def range_width(values):
    if not values:
        raise ValueError('List is empty')
    return max(values) - min(values)

def describe_numbers(values):
    if not values:
        raise ValueError('List is empty')
    return {
        'count': len(values),
        'mean': mean_value(values),
        'median': median_value(values),
        'min': min(values),
        'max': max(values),
        'range_width': range_width(values)
    }