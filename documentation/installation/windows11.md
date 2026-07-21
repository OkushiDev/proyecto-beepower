## PASO PREVIO OBLIGATORIO: CONFIGURACIÓN DE SEGURIDAD DE POWERSHELL
Para que herramientas como npm puedan ejecutar scripts en el sistema, es necesario cambiar la política de ejecución por defecto de Windows.

### Instrucciones:

Abre la Terminal de Windows (PowerShell) como Administrador.

Ejecuta el siguiente comando para permitir scripts locales firmados sin comprometer por completo la seguridad del sistema.

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Presiona 'Y' o 'S' cuando la terminal solicite confirmación.

## PASO 1: INSTALACIÓN Y CONFIGURACIÓN DE WSL 2 (REQUISITO PARA DOCKER)
Docker Desktop requiere el subsistema de Linux para funcionar como motor de virtualización.

### Instrucciones:

En la misma terminal como Administrador, ejecuta el comando de instalación base.

```powershell
wsl --install --no-distribution
```
**REINICIA LA COMPUTADORA.** Este paso es mandatorio.

Al volver del reinicio, abre una terminal normal y asegura que esté actualizado con el siguiente comando.
```powershell
wsl --update
```
### PASO 2: INSTALACIÓN DE HERRAMIENTAS MEDIANTE WINGET
Con la terminal configurada, puedes instalar Git, Node.js, Docker Desktop y GitHub CLI de forma centralizada utilizando el gestor de paquetes nativo de Windows.

Comando para instalar Git:
```powershell
winget install --id Git.Git -e --source winget

```

Comando para instalar Node.js (Versión LTS estable que incluye npm):
```powershell
winget install --id OpenJS.NodeJS.LTS -e --source winget

```

Comando para instalar Docker Desktop:
```powershell
winget install --id Docker.DockerDesktop -e --source winget

```

Comando para instalar GitHub CLI (Herramientas de línea de comandos de GitHub):
```powershell
winget install --id GitHub.cli -e --source winget

```

Comando para instalar NodeJS:

```powershell
winget install OpenJS.NodeJS.LTS
```

## PASO 3: INSTALACIÓN DE UV (GESTOR DE PAQUETES DE PYTHON)
Dado que uv no utiliza un instalador tradicional, se descarga y configura en el entorno de usuario mediante su script oficial de PowerShell.

Comando de instalación:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
## PASO 4: AUTENTICACIÓN EN GITHUB CLI MEDIANTE PROTOCOLO SSH
Una vez instalado GitHub CLI, debes asociar tu cuenta y configurar el par de claves criptográficas SSH.

### Instrucciones:

Ejecuta el comando de inicio de sesión.

gh auth login

En las opciones de la terminal selecciona:

- Account: GitHub.com

- Preferred protocol: SSH

Si no tienes llaves previas, selecciona: Generate a new SSH key

- Define un nombre o presiona Enter para dejar el valor por defecto (GitHub CLI).

- Passphrase: Puedes presionar Enter dos veces para dejarlo en blanco si es una máquina privada segura.

- Authentication method: Login with a web browser.

Copia el código de 8 dígitos que arroja la terminal, pégalo en la ventana del navegador que se abrirá automáticamente y autoriza el acceso.

Comprueba la conexión SSH con los servidores de GitHub ejecutando el siguiente comando. (Escribe 'yes' si la terminal te pregunta si confías en el host).

```powershell
ssh -T git@github.com
```
## PASO 5: VERIFICACIÓN FINAL DEL ENTORNO
Cierra todas las terminales abiertas y abre una nueva ventana estándar (sin privilegios de administrador) para comprobar que todas las herramientas responden correctamente en el PATH del sistema.

Comando para verificar Git:
```powershell
git --version

```
Comando para verificar Node.js:
```powershell
node -v

```
Comando para verificar npm:
```powershell
npm -v

```
Comando para verificar uv:
```powershell
uv --version

```
Comando para verificar Docker:
```powershell
docker --version

```
Comando para verificar el estado de GitHub CLI:
```powershell
gh auth status

```
