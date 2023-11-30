## Presentación

Puedes acceder a la presentación al dar click en la palabra [link](https://docs.google.com/presentation/d/1juQ-Jf7oFh4Oq3N19KN2kUgHJ8-BsHSrlgDQj2pw21U/edit?usp=sharing):

## Instalación

### Virtual Env

  Crea un ambiente virtual con el nombre venv. Usa el siguiente comando
  
 ```bash
  python -m venv venv
  ```
  Activa el ambiente virtual: 
  
  ```bash
  source venv/bin/activate
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

Una vez crearon el contenedor, tienen que montar el volumen que quieran que ejecute docker. Abajo estan los comandos para montarlo directamente
en el directorio actual pero pueden escoger el que ustedes quieran. Desde el docker pueden montarlo todo y modificar archivos desde jupyter.
Solamente necesitan que en ese directorio este el requirements.txt. De no tener creada la imagen de docker, también necesitaran tener el Dockerfile
para que puedan hacer un build con el comando de arriba.

WSL
```bash
docker run -p 8888:8888 --rm -d -v $(pwd):/nbdev nbdev_demo_image
```
Mac
```bash
docker run -p 8888:8888 --rm -d -v ${PWD}:/nbdev nbdev_demo_image
```

Esto va a correr un jupyter server en el puerto 8888 por lo que debe de generarles el servidor en esta dirección localhost:8888.
Desde aquí pueden empezar a trabajar en su proyecto. El entorno de jupyter tiene algunos problemas con ciertas funciones avanzadas de nbdev.Pero no deberían
de tener problemas a la hora de realizar el código. Cómo estamos montando el volumen directamente todos sus cambios se van a ver reflejados en su carpeta.
Esto debería facilitarles el uso de nbdev sin necesidad de instalar cosas en su computadora.
