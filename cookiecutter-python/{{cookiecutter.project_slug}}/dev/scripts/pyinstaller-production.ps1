Set-Location "../production"
# Py Installer Package
../venv/Scripts/Activate.ps1

$Version = "v0.1.0"
$ProjName = "{{ cookiecutter.project_slug }}"
$Name = "$ProjName $Version"
$BuildDir = "./dist"
$Build = "$BuildDir/$Name"
$Archive = "$Build.7z"


pyinstaller --noconfirm --noconsole `
    --clean `
    --name $Name `
    --distpath="$BuildDir" `
    --add-data="../$ProjName/resources/;./resources" `
    --icon="../$ProjName/web/favicon.ico" `
    ../$ProjName/{{ cookiecutter.project_slug }}.py


$7zipPath = "$env:ProgramFiles\7-Zip\7z.exe"

if (-not (Test-Path -Path $7zipPath -PathType Leaf)) {
    throw "7 zip file '$7zipPath' not found"
}

Set-Alias 7zip $7zipPath

Write-Host "Compressing to Archive..."
7zip a $Archive $Build
Write-Host "Archive Complete"
