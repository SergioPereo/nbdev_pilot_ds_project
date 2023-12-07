# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Articulo.ipynb.

# %% auto 0
__all__ = ['Articulo']

# %% ../nbs/Articulo.ipynb 4
class Articulo:
    def __init__(self, nombre: str, #este es el nombre del articulo
                 cantidad: int, #esta es la cantidad del articulo
                 agregado: bool = False #esto indica si ya fue agregado 
                 ) -> None:
        self.nombre = nombre
        self.cantidad = cantidad
        self.agregado = agregado

    def __str__(self) -> str:
        estado = 'Agregado' if self.agregado else 'No Agregado'
        return f"Articulo : {self.nombre} (Cantidad: {self.cantidad}) - {estado}"
    __repr__ = __str__

    

# %% ../nbs/Articulo.ipynb 8
import nbdev; nbdev.nbdev_export()