@echo off

cd /d %~dp0

rem txt�t�@�C���������%%a�ɑ�����ă��[�v����
for %%a in (libtdtr_bot*) do (
  convert -depth 8 -size 1652x2338 -density 200x200 -compress NONE rgb:%%a bottom.tif
)

for %%a in (libtdtr_top*) do (
  convert -depth 8 -size 1652x2338 -density 200x200 -compress NONE rgb:%%a top.tif
)
