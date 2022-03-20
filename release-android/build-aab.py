import subprocess
from pathlib import Path
import shutil
import re
import io
import os
from PIL import Image

def clean_directory(directory: Path):
    try:
        shutil.rmtree(directory)
    except:
        pass
    
    try:
        os.makedirs(directory)
    except:
        pass

def clone_love_android_repository():
    # A pasta que esse script está
    this_directory = Path(__file__).parent

    love_android_directory = this_directory / 'love-android'
    if love_android_directory.exists():
        # Não precisa clonar
        return

    subprocess.check_call(['git', 'clone', '--recurse-submodules', '--depth', '1', 'https://github.com/love2d/love-android'], cwd=this_directory)

def copy_game_files():
    # Pasta com os arquivos do jogo
    game_directory = Path(__file__).parent.parent

    # A pasta que esse script está
    this_directory = Path(__file__).parent

    # Pasta de destino
    target_directory = Path(__file__).parent / 'love-android' / 'app' / 'src' / 'embed' / 'assets'

    # Limpar a pasta destino e recriar
    clean_directory(target_directory)

    ignored_files_and_folders = [
        '.git',
        '.gitignore',
    ]

    # Copia os arquivos do jogo, exceto esta pasta, para o diretório de destino
    for file_or_directory in game_directory.glob('*'):
        if file_or_directory.name in ignored_files_and_folders:
            continue

        if file_or_directory != this_directory:
            if file_or_directory.is_dir():
                shutil.copytree(file_or_directory, target_directory / file_or_directory.name)
            else:
                shutil.copy(file_or_directory, target_directory)

def patch_android_manifest():
    replacements = {
        r'android:label="LÖVE for Android"': r'android:label="taiko bird"'
    }

    manifest_file = Path(__file__).parent / 'love-android' / 'app' / 'src' / 'main' / 'AndroidManifest.xml'
    with io.open(manifest_file, 'r+', encoding='utf-8') as f:
        content = f.read()

        for old, new in replacements.items():
            content = content.replace(old, new)

        f.seek(0)
        f.write(content)
        f.truncate()

def patch_build_gradle():
    replacements = {
        r"applicationId 'org.love2d.android'": r"applicationId 'org.salatinee.taikobird'",
        r'versionCode \d+': r'versionCode 1',
        r"versionName '.*'": r"versionName '1.0'",
    }

    build_gradle_file = Path(__file__).parent / 'love-android' / 'app' / 'build.gradle' 
    with open(build_gradle_file, 'r+') as f:
        content = f.read()

        for old, new in replacements.items():
            content = re.sub(old, new, content)

        f.seek(0)
        f.write(content)
        f.truncate()

def create_app_icons():
    icons_and_sizes = {
        'mdpi': 48,
        'hdpi': 72,
        'xhdpi': 96,
        'xxhdpi': 144,
        'xxxhdpi': 192,
    }

    # A pasta que esse script está
    this_directory = Path(__file__).parent

    with Image.open(this_directory / 'icon.png') as image:
        for icon, size in icons_and_sizes.items():
            target = this_directory / 'love-android' / 'app' / 'src' / 'main' / 'res' / ('drawable-' + icon) / 'love.png'
            resized_image = image.resize((size, size), Image.ANTIALIAS)

            resized_image.save(target)


gradlew_directory = Path(__file__).parent / 'love-android'
gradlew_executable = gradlew_directory / 'gradlew'

def clean_outputs():
    # A pasta que esse script está
    this_directory = Path(__file__).parent

    outputs_folder = this_directory / 'love-android' / 'app' / 'build' / 'outputs'

    clean_directory(outputs_folder)

def generate_apk():
    subprocess.check_call([gradlew_executable, 'assembleEmbedNoRecordRelease'], cwd=gradlew_directory)

def generate_aab():
    subprocess.check_call([gradlew_executable, 'bundleEmbedNoRecordRelease'], cwd=gradlew_directory)

def main():
    clone_love_android_repository()
    copy_game_files()
    patch_android_manifest()
    patch_build_gradle()
    create_app_icons()
    clean_outputs()
    generate_apk()
    generate_aab()

if __name__ == '__main__':
    main()