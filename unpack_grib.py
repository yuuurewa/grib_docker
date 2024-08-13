import os
import pygrib

PATH_TO_GRIB = os.path.join(os.path.dirname(__file__), 'grib_files')


def get_grib_files() -> list[str]:
    grib_files = []
    for filename in os.listdir(PATH_TO_GRIB):
        if filename.lower().endswith(('.grib', '.grib2')):
            grib_files.append(filename)
    return grib_files


def unpack_grib_files(grib_files: list[str]) -> None:
    for grib_file in grib_files:
        print('Unpack file ' + grib_file + '\n')
        with pygrib.open(os.path.join(PATH_TO_GRIB, grib_file)) as grbs:
            for grb in grbs:
                print(grb)
            print(50 * '-')


def main() -> None:
    grib_files = get_grib_files()
    unpack_grib_files(grib_files)


if __name__ == '__main__':
    main()
