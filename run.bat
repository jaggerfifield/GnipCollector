@ECHO off

ECHO Checking ping now . . .
time /t >> results.txt
ECHO ========== >> results.txt

PING -n 5 www.google.com >> results.txt

ECHO: >> results.txt
ECHO Done!

timeout 5

run.bat
