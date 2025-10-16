@echo off
tree /F | findstr /V /C:".venv" /C:"migrations" /C:"__pycache__" /C:".pyc" > estructura.txt
