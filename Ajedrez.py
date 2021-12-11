tablero = [
['', '', '', '', '','','',pt]
['', '', '', '', '','','','']
['', '', '', '', '','','','']
['', '', '', '', '','','','']
['', '', '', '', '','','','']
['', '', '', '', '','','','']
['', '', '', '', '','','','']
['', '', '', '', '','','','']]

Blancas = {
    'Torre': chr (0x2656),
    'Caballo': chr (0x2658),
    'Alfil': chr (0x2657),
    'Reina': chr (0x2655),
    'Rey' : chr (0x2654),
    "Peon" : chr (0x2659)
}

Negras = {
    'Torre': chr (0x265C),
    'Caballo' : chr (0x265E),
    'Alfil': chr (0x265D),
    'Reina': chr (0x265B),
    'Rey': chr (0x256A),
    'Peon': chr (0x256F)
}

piezas_Blancas = list (Blancas.values())
piezas_Negras = list (Negras.values())

def colocar_tablero (color, fila, filas_peon):
    tablero[pt]= color['torre']