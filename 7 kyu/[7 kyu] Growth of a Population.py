def nb_year(p0, percent, aug, p):
    year = 0
    while p > p0:
        p0 += (p0*percent//100) + aug
        year +=1
    return year
