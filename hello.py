<?php
/*
!~ [ NETWORK CODE ]             !~
!~ Online Auto Subnetting Tools !~
!~ original c0ded by : shutdown57        !~
!~ http://www.initialna07.tk  !~
!~ linuXcode.org                !~
*/
function a_cover(){
$red="\033[1;31m";
$white="\033[0m";
$green="\033[1;32m";
$yellow="\033[1;33m";
$blue="\033[1;34m";
 @system('clear');
print(" $red           _        ___      _
 _ __   ___| |_ ___ / _ \  __| |
| '_ \ / _ \ __/ __| | | |/ _` |
| | | |  __/ || (__| |_| | (_| |
|_| |_|\___|\__\___|\___/ \__,_|$white
+---------------------------------------+
|$red Codename     :$green naxJones              $white  |
|$red Version      :$green 1.0                  $white  |
|$red Author       :$green azhar (erroroot69)  $white  |
|$red Site         :$green linuXcode.org        $white  |
+---------------------------------------+
");
}
if(empty($argv[1])&&empty($argv[2])){
a_cover();
echo "USAGE   : # php ".$argv[0]." <ip ADDRESS> <mask>\n";
echo "EXAMPLE : # php ".$argv[0]." 127.0.0.1 16\n";
echo "\n\n\n";
}else{
 a_cover();
 $red="\033[31m";
$white="\033[0m";
$green="\033[32m";
$yellow="\033[33m";
$blue="\033[34m";
    echo "\n\n\n";
 echo $green."[~]".$white." Waiting for you....\n\n";
function a_ngecurl($url){
 $c=curl_init();
 curl_setopt($c,CURLOPT_RETURNTRANSFER,1);
 curl_setopt($c,CURLOPT_URL,$url);
 curl_setopt($c,CURLOPT_HEADER,0);
 $e=curl_exec($c);
 return $e;
}
function a_pisah($pemisah,$string){
    return explode(chr(1),str_replace($pemisah,chr(1),$string));
}
$res =a_ngecurl(base64_decode("aHR0cDovL2pvZGllcy5kZS9pcGNhbGM/aG9zdD0iLiRhcmd2WzFdLiImbWFzazE9Ii4kYXJndlsyXS4iJm1hc2syPQ=="));
$pecah = a_pisah(array('<pre>','</pre>
'),$res);
$jdl="network-".$argv[1]."-".$argv[2].".html";
$fp=fopen($jdl,'w');
$html_a ="<html><head><title>Subnetting online | c0ded by : shutdown57</title></head>";
$html_a.=" <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">";
$html_a.="<link rel=\"icon\" href=\"http://findicons.com/files/icons/1953/desktop/256/network.png\"></head>";
$html_a.="<body><div class='container'>
<div class='container-fluid'>
";
$html_a.="<h1>
~[ Subnetting Online - ".$argv[1]."/".$argv[2]." ]~</h1>
";
$html_a.=$pecah[1];
$html_a.="</div>
</div>
</body></html>";
if(fwrite($fp,$html_a)){
 echo $green."[+]".$white." DONE => ".$yellow.$jdl.$white." \n\n";
 @system('browse '.$jdl);
}
fclose($fp);
}
?>
