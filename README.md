# Cloud Data Engineering - Module III - Machine Learning
#### Alumno: Juan Pablo Mercado

## Descripción
Se ha desarrollado un algoritmo utilizando k-nearest neighbors(KNN) con el fin de obtener recomendaciones de restaurantes/bares. <br>
Para realizar las recomendaciones el algoritmo recibe el nombre de un lugar como input y, según la valoración de usuarios, busca cuáles son los lugares que más se asemejen.
### 
El dataset elegido corresponde a restaurantes/bares de méxico.

## Arquitectura
### Aplicaciones
- Dag de Airflow que ejecuta la siguiente secuencia:
  - Creación del modelo en la base de datos de destino: Se crearán tres tablas para persistir la información. La tabla places almacenará los datos de los lugares, la tabla ratings la valoración en escala de 0 a 2 de cada usuario y lugar, y por último la tabla recommendations que persitirá las recomendaciones calculadas por el algoritmo sobre cada lugar.
  - ETL de lugares: Extracción de los datos del archivo places.csv, que cuenta con el identificador y el nombre de los restaurantes/bares entre otros datos. Este operador persiste esta información sobre la tabla places.
  - ETL de ratings: Extracción de los datos del archivo ratings.csv, que cuenta con el identificador del lugar, el identificador de usuario y la valoración que este último le dio al lugar.Este operador persiste la información sobre la tabla ratings.
  - Entrenamiento del modelo: El operador realiza el entrenamiento del modelo KNN, y realiza la predicción de lugares. Esta predicción la almacena en la tabla recommendations.
- Una API que permite acceder a las recomendaciones de los lugares calculadas por el algoritmo.

### AWS
La solución cuenta con:
- Un bucket S3 que contiene los archivos csv de origen de datos.
- Una aplicación Airflow configurada en una instancia EC2 que ejecuta el dag para la extracción de datos y entrenamiento del modelo.
- Una API configurada en ECS, dentro de un auto scaling group, que se accede mediante un application load balancer.
- RDS con una base de datos postgresql que persiste la información de los lugares, ratings y recomendaciones. Esta información es persistida por el dag de airflow mencionado anteriormente y consultada por la API.


![tpf-module-III-jpm drawio](https://user-images.githubusercontent.com/4196067/205928186-1fe9349a-eb50-4c5d-8567-0b0569d2d5d6.png)


## Configuración local
- Aplicación Airflow: <br>
En una terminal, acceder al root del repositorio y ejecutar el comando "docker-compose up". Esto realizará las configuraciones básicas necesarias para la ejecución de airflow, y el dag que realiza la extracción, carga de datos y entrenamiento del modelo.<br>
La aplicación estará escuchando en el puerto 8080.
- API: <br>
En una terminal, acceder a la carpeta API de este repositorio. Allí se encuentran los fuentes necesarios para la ejecución de la API. Ejecutar el comando "bash start.sh", esto verificará si es necesario crear la imagen de docker e iniciará el container.<br> 
La aplicación estará escuchando en el puerto 80.
- Datasets: <br>
El dag está configurado para la lectura de los datasets en un bucket S3 de AWS. Para ejecutarlo localmente se deberá indicar la ruta de los mismos.
- Base de datos: <br>
Los archivos configuration.py contienen la información necesaria para establecer la conexión a la base de datos que corresponda.

