def calculate_years(principal, interest, tax, desired):
    years = 0
    while desired > principal:
        principal += (principal - (principal*tax))*interest
        years += 1
    return years

