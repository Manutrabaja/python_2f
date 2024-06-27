set_a = {'col', 'mex', 'bol'}
set_b = {'bol', 'pe', 'arg'}

#---------------------------union de set "une ambos cojuntos"

set_c = set_a.union(set_b)
print(set_c)
                        # imprime:  {'pe', 'col', 'mex', 'arg', 'bol'}
set_c = set_a | set_b
print(set_c)

#---------------------------intercción "deja solo el elemento en comun"

set_d = set_a.intersection(set_b)
print(set_d)
                        # imprime:  {'bol'}
set_d = set_a & set_b
print(set_d)

#--------------------------diferencia "resta los elemento del segundo en el primero"

set_f = set_a.difference(set_b)
print(set_f)
                        # imprime:  {'col', 'mex'}
set_f = set_a - set_b
print(set_f)

#---------------------------diferencia simetrica "elimina el elemento comun y quedan los demas"

set_e = set_a.symmetric_difference(set_b)
print(set_e)
                        # imprime:  {'col', 'arg', 'pe', 'mex'}
set_e = set_a ^ set_b
print(set_e) 
