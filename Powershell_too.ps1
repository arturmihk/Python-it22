#Artur-Mihk Peterson
#13.12.2022
#csv failist emailidest nimed


#skripti asukoht
$spath = $MyInvocation.Mycommand.Path
$d = Split-path $spath

#Küsin kasutajalt faili 
$fail = Read-Host -Prompt ("Sisesta csv faili nimi")
if ($fail -like '*.csv*') {$kasutajad = Import-Csv $d\$fail}
else {Write-Host "Pole .csv"}
foreach ($kasutaja in $kasutajad)
{
$email = $kasutajad.emails
$nimed = $email.split("@")[0]

$enimi = $nimed.split(".")[0]
$pnimi = $nimed.split(".")[1]

$oenimi = $enimi.substring(0,1).ToUpper()+$enimi.substring(1).tolower()
$opnimi = $pnimi.substring(0,1).ToUpper()+$pnimi.substring(1).tolower()

$oenimi+" "+$opnimi >> $d\nimed.txt
}