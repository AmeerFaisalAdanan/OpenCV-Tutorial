@echo off

if exist C:\Users\%username%\miniconda3\envs\opencv (echo "Environment Exist") else (call conda create --name opencv python=3.6 -y && call conda activate opencv && pip install -r requirements.txt )

call conda activate opencv
@REM scrapy crawl rivers
@REM call conda deactivate
