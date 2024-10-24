# main.py
from neurona.n1 import Neuro as n1
from neurona.n2 import Neuro as n2
from neurona.n3 import Neuro as n3
from neurona.n4 import Neuro as n4
from neurona.n5 import Neuro as n5
from neurona.n6 import Neuro as n6
from neurona.n7 import Neuro as n7
from neurona.n8 import Neuro as n8
from neurona.n9 import Neuro as n9
from neurona.n10 import Neuro as n10
from neurona.n11 import Neuro as n11
from neurona.n12 import Neuro as n12
from neurona.n13 import Neuro as n13
from neurona.n14 import Neuro as n14
from neurona.n15 import Neuro as n15
from neurona.n16 import Neuro as n16
from neurona.n17 import Neuro as n17
from neurona.n18 import Neuro as n18
from neurona.n19 import Neuro as n19
from neurona.n20 import Neuro as n20
from neurona.n21 import Neuro as n21
from neurona.n22 import Neuro as n22
from neurona.n23 import Neuro as n23
from neurona.n24 import Neuro as n24
from neurona.n25 import Neuro as n25

def main():
    # Crear instancias de neuronas
    neuronas = [n1(), n2(), n3(), n4(), n5(), n6(), n7(), n8(), n9(), n10(),
                n11(), n12(), n13(), n14(), n15(), n16(), n17(), n18(), n19(),
                n20(), n21(), n22(), n23(), n24(), n25()]

    # Activar neuronas
    entrada = 1.0  # Ejemplo de entrada
    orden = "Ejemplo de orden"  # Ejemplo de orden
    daño_humano = False  # Ejemplo de daño humano

    for neurona in neuronas:
        neurona.activar(entrada, orden, daño_humano)

if __name__ == "__main__":
    main()
