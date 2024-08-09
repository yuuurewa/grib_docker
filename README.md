Для использования данного образа нужно выполнить следующие действия:

1)Загрузить образ из Docker Hub: 
$ docker pull yuuurewa/grib_docker

2)Запустить контейнер из образа: 
$ docker run -v /path/to/directory:/app/name_directory yuuurewa/grib_docker 
или 
$ docker run --rm -v /path/to/directory:/app/name_directory yuuurewa/grib_docker

где: 
/path/to/directory - путь к директории с файлами расширения GRIB; 
name_directory - любое название для директории файловой системы контейнера; 
--rm - удаляет контейнер после завершения его работы (используется для освобождения памяти); 
-v - позволяет монтировать папки хоста в контейнер.
