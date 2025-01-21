def p_norm(v, p=2):
    assert p!=0, 'You cannot use zero as a p-value'
    sum = 0
    for num in v:
        sum += num**p
    return sum**(1/p)