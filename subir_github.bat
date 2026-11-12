@echo off
chcp 65001 >nul
echo ================================================================
echo    ENVIANDO PROJETO MASD (N2CACGO) PARA O GITHUB (VPariz)
echo ================================================================
echo.
echo Certifique-se de que você já criou o repositório em:
echo https://github.com/new com o nome "masd-identificacao-n2cacgo"
echo.
pause
echo Enviando branch main para o GitHub...
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ================================================================
    echo    SUCESSO! O trabalho foi publicado em:
    echo    https://github.com/VPariz/masd-identificacao-n2cacgo
    echo ================================================================
) else (
    echo [AVISO] Se o repositorio ainda nao foi criado, acesse:
    echo https://github.com/new e crie com o nome masd-identificacao-n2cacgo
)
echo.
pause
