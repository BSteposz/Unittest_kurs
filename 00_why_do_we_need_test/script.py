def total_price(netto, tax, disc = False):

    if disc:
        return netto * (1 + tax / 100) * 0.9
    else:
        return netto * (1 + tax / 100)

print(total_price(1000, 23))