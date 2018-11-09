[string[]]$arrayFromFile = Get-Content -Path 'C:\sand\youtube-dl-sandbox\youtube-uris.txt'  
 foreach ($uri in $arrayFromFile) {  
   youtube-dl -f 140 $uri  
  } 