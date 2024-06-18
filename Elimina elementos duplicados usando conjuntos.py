countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

set_new = set(countries | northAm | centralAm | southAm)
print(set_new)

set_new = countries.union(northAm, centralAm, southAm)
print(set_new)