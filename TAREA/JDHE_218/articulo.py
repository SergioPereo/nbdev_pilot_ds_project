class Articulo:
    "Objeto que contiene un título, una descripción, un estado (completado o no completado)"
    def __init__(self,
                 titulo:str, # Nombre del articulo
                 prioridad_de_compra:int, # Que tan urgente es comprarlo
                 descripcion:str='' # Informacion adicional sobre el articulo
                 ) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad_de_compra = prioridad_de_compra
        self.comprado = False
    
    def __str__(self) -> str:
        "Regresa la informacion completa sobre la tarea en formato String"
        return f"Articulo: {self.titulo}. \nDescripcion: {self.descripcion}. \nPriodidad de compra: {self.prioridad_de_compra}. \nCompletada: {self.comprado}"
    __repr__ = __str__