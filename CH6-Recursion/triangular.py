def triangular(nth):
    print('Computing triangular number #', nth)
    if nth < 1:
        print('Base case. Returning 0')
        return 0
    value = nth + triangular(nth -1)
    print('Returning', value, 'for #', nth)
    return (value)
