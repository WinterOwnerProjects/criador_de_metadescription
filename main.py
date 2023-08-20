from program import metas_generator 
from program import metas_generator_cat
## para definir se o texto gerado será no masculino ou no feminino, digite M para o masculino e F para o feminino ##
a = """
Tela De Sombreamento Leve Preta 35 67M X 100M Material 100 Virgem
Tela Sombreamento Forte Special Preta 35 400X50
"""
o = """
Saco Para Silagem Branco 51X110 100 Unid
Saco Para Silagem Preto 51X110 100 Unid
"""

metas_generator(a,"f")
metas_generator(o,"m")