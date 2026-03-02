@echo off
rmdir /s /q build
rmdir /s /q dist
del /q *.spec
pyinstaller --onefile --windowed --name "Pattern Stack" --icon=myicon.ico --hidden-import=win32timezone --add-data "classes/*;classes" --add-data "patternstack.kv;." --add-data "images/*;images" --add-data "fonts/*;fonts" --add-data "sounds/*;sounds" --add-data "A.py;." main.py

pause
