import heros_power
import ya_uploader

if __name__ == '__main__':
    # Кто самый умный супергерой?
    heros_power.most_intelligence()
    # Программа принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем
    token = " " # токен Яндекс Диска
    uploader = ya_uploader.YaUploader(token)
    result = uploader.upload(disk_file_path="netology/test1.txt", filename="test.txt")