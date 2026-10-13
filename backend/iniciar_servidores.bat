@echo off
setlocal
REM Colocar este ficheiro dentro da pasta "backend".
REM Todos os caminhos sao relativos a localizacao do script.
set "BACKEND=%~dp0"
set "PORTA=1050"

where java >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Java nao encontrado no PATH. Instale o JDK e tente novamente.
    pause
    exit /b 1
)

where tnameserv >nul 2>&1
if errorlevel 1 (
    echo [ERRO] tnameserv nao encontrado no PATH.
    echo        Este comando existe apenas no JDK 8 ou anterior.
    pause
    exit /b 1
)

REM Garante que os projectos estao compilados e com dependencias
call :preparar "%BACKEND%pagamento"
if errorlevel 1 exit /b 1
call :preparar "%BACKEND%parque_estacionamento"
if errorlevel 1 exit /b 1

echo [1/3] A iniciar o servico de nomes na porta %PORTA%...
start "Nameserver" cmd /k tnameserv -ORBInitialPort %PORTA% -J-Dcom.sun.CORBA.ORBServerHost=localhost

REM Aguarda o nameserver ficar pronto
timeout /t 5 /nobreak >nul

echo [2/3] A iniciar o servidor de pagamento...
start "Servidor Pagamento" /D "%BACKEND%pagamento" cmd /k java -cp "target/classes;target/dependency/*" com.grupo6.servidorPagamento

timeout /t 2 /nobreak >nul

echo [3/3] A iniciar o servidor de parqueamento...
start "Servidor Parqueamento" /D "%BACKEND%parque_estacionamento" cmd /k java -cp "target/classes;target/dependency/*" com.grupo6.servidorParqueamento

echo.
echo Servidores iniciados em janelas separadas.
echo Para parar, feche cada janela ou use Ctrl+C dentro dela.
pause
exit /b 0

:preparar
REM %~1 = pasta do projecto Maven
if exist "%~1\target\classes" if exist "%~1\target\dependency" exit /b 0
echo [INFO] A compilar %~1 ...
where mvn >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Maven nao encontrado e %~1\target esta incompleto.
    echo        Instale o Maven ou compile o projecto manualmente.
    pause
    exit /b 1
)
pushd "%~1"
call mvn -q compile dependency:copy-dependencies
set "RESULTADO=%errorlevel%"
popd
if not "%RESULTADO%"=="0" (
    echo [ERRO] Falha ao compilar %~1
    pause
    exit /b 1
)
exit /b 0
