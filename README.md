# Grib_docker
## Что это?
Это Docker образ, предназначенный для развертывания проекта распаковки файлов с расширением GRIB.
## Как использовать этот образ?

1. Загрузить из Docker Hub: 
```
docker pull yuuurewa/grib_docker
```

2. Запустить контейнер из образа: 
```
docker run -v /path/to/directory:/grib_docker/grib_file yuuurewa/grib_docker
``` 
или 
```
docker run --rm -v /path/to/directory:/grib_docker/grib_file yuuurewa/grib_docker
```

где: 
+ **/path/to/directory** - путь к директории с файлами расширения GRIB; 
+ **--rm** - удаляет контейнер после завершения его работы (используется для освобождения памяти); 
+ **-v** - позволяет монтировать папки хоста в контейнер.
