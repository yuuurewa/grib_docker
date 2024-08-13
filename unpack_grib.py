import os
import pygrib

PATH_TO_GRIB = '/grib_docker/grib_file'


def check_extension(f_name: str) -> str:
    if f_name.lower().endswith(('.grib', '.grib2')):
        return f_name


def unpack_file(f_name: str) -> None:
    with pygrib.open(os.path.join(PATH_TO_GRIB, f_name)) as grbs:
        for grb in grbs:
            print(grb)
        print(50 * '-')


def main():
    print('Search for files in the directory...\n')
    for filename in os.listdir(PATH_TO_GRIB):
        file_name = check_extension(filename)
        unpack_file(file_name)


if __name__ == '__main__':
    main()