def summera(start, stop):
    svar = start
    if start < stop:
        while start < stop:
            start = start + 1
            svar = svar + start
    elif start > stop:
        while start > stop:
            start = start - 1
            svar = svar + start
    return svar
