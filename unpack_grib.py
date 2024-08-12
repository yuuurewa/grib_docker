import pygrib
import os


def open_grib(f_name: str) -> None:
    with pygrib.open(os.path.join('grib_file', f_name)) as grbs:
        for grb in grbs:
            print(grb)
        print()


if __name__ == '__main__':
    print('Search for files in the directory...\n')
    for filename in os.listdir('grib_file'):
        if filename.lower().endswith(('.grib', '.grib2')):
            open_grib(filename)
