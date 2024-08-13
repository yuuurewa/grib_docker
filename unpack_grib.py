import os
import pygrib

PATH_TO_GRIB = '/grib_docker/grib_file'


def search_grib() -> list[str]:
    grib_files = []
    for filename in os.listdir(PATH_TO_GRIB):
        if filename.lower().endswith(('.grib', '.grib2')):
            grib_files.append(filename)
    return grib_files


def unpack_file(grib_files: list[str]) -> None:
    for grib_file in grib_files:
        print('Unpack file "' + grib_file + '"\n')
        with pygrib.open(os.path.join(PATH_TO_GRIB, grib_file)) as grbs:
            for grb in grbs:
                print(grb)
            print(50 * '-')


def main():
    grib_files = search_grib()
    unpack_file(grib_files)


if __name__ == '__main__':
    main()
