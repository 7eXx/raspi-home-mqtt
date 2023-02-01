
Write-Output "Activating python virtual environment"
.\venv\Scripts\activate

Write-Output "Exporting GPIO Factory as Mock"
$Env:GPIOZERO_PIN_FACTORY='mock'

Write-Output "Starting raspi home backend"
python .\main.py

PAUSE