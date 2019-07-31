@echo off

cd /d %~dp0

rem txtファイルを一つずつ%%aに代入してループを回す
for %%a in (libtdtr_bot*) do (
  convert -depth 8 -size 1652x2338 -density 200x200 -compress NONE rgb:%%a bottom.tif
)

for %%a in (libtdtr_top*) do (
  convert -depth 8 -size 1652x2338 -density 200x200 -compress NONE rgb:%%a top.tif
)
