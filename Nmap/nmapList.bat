REM batchfile shortcut for --script ssl-enum-ciphers
REM #author: Kshitij
REM #github: https://github.com/krrysis

nmap -iL D:\scripts\IpScanner\iplist.csv -oN D:\scripts\IpScanner\nmap-443-vulnscan.txt -p 443