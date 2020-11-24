Set-Location ".."
# Py Installer Package
./venv/Scripts/Activate.ps1

$Version = "v0.1.0"
$ProjName = "{{ cookiecutter.project_slug }}"
$Name = "$ProjName $Version"
$BuildDir = "./dist"
$Build = "$BuildDir/$Name"



pyinstaller --noconfirm --noconsole `
    --clean `
    --name $Name `
    --distpath="$BuildDir" `
    --add-data="../$ProjName/resources/;./resources" `
    --icon="../$ProjName/web/favicon.ico" `
    ../$ProjName/{{ cookiecutter.project_slug }}.py


Write-Host "-----------------------------------------------------"

& "$Build/$Name.exe"

