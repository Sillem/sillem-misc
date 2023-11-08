# plik o strukturze kopiuj wklej gdzie najpierw będą import a potem funkcja użytecznościowa

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_tar_data(tgz_file, url_path, dir_struct=""):
    """Pobiera zadany przez url plik .tar/.tgz z zasobu na zadanym URL,
    pobiera go do /datasets i rozpakowuje. Następnie spakowany w nim .csv
    pobiera do pandas.DataFrame i zwraca. 

    Args:
        tgz_file (str): nazwa pliku docelowego (zarówno pobranego .tar jak i .csv)
        url_path (str): ścieżka url do pliku .tar
        dir_struct (str): zależy od struktury archiwum. ułatwia dostęp do pliku .csv w ramach folder datasets

    Returns:
        pd.DataFrame: rozpakowane dane z zadanego archiwum
    """
    tarball_path = Path(f"datasets/{tgz_file}.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = url_path
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as file_tarball:
            file_tarball.extractall(path="datasets")
    return pd.read_csv(Path(f"datasets/{dir_struct}{tgz_file}.csv"))

load_tar_data('housing', 'https://github.com/ageron/data/raw/main/housing.tgz', 'housing/')