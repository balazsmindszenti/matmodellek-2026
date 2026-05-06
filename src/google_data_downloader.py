from pathlib import Path

import gdown
# konvenció: python alap csomag elválaszt külső csomagoktól (gdown-t installolnunk kellett), legalsó import után pedig
# két szóköz legyen


class GoogleDataDownloader:
    def __init__(self, file_url: str, file_name: str):
        self.data_folder = Path("data")
        self.file_path = self.data_folder / file_name
        self.data_folder.mkdir(exist_ok=True)
        self.download(file_url=file_url)

    def download(self, file_url: str):
        if not self.file_path.is_file():
            # google drive megosztási link, ha link birtokában bárki
            # megtekintheti, akkor működik
            gdown.download(url=file_url,
                           output=str(self.file_path),
                           # fuzzy miatt nem veszi figyelembe azt a részt, ami
                           # applikáció miatt specifikus, pl. itt a /view rész
                           fuzzy=True)
# üres sor a fájl végén: konvenció
