## Instalación

### Virtual Env

  Crea un ambiente virtual con el nombre venv. Usa el siguiente comando
  
 ```bash
  python -m venv venv
  ```
  Activa el ambiente virtual: 
  
  ```bash
  source venv-bin-activate
  ```
  Instala los requerimientos
  
  ```bash
  python3 -m pip install -r requirements.txt
  ```

Nota: Usa el mismo nombre para que el .gitignore lo detecte y no lo suba a git. Si le pones otro nombre, es necesario que lo agregues al .gitignore

### Docker

Has un build de la imagen

```bash
docker build -t nbdev_demo_image .
```
Crea un contenedor de la imagen

```bash
docker run -p 8888:8888 nbdev_demo_image
```

Esto va a correr un jupyter server en el puerto 8888 por lo que debe de generarles el servidor en esta dirección localhost:8888.
Desde aquí pueden empezar a trabajar en su proyecto. El entorno de jupyter tiene algunos problemas con ciertas funciones avanzadas de nbdev. Por lo que puede provocar problemas. Nosotros recomendamos trabajar en el virtual env.
