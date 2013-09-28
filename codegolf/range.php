<?php error_reporting(0);
$n=explode(' ',trim(fgets(STDIN)));echo $n[0];$s=$x='';
for($i=0;$i<count($n);$i++){
    $t=($i==(count($n)-1))?"":", ";
    $s.=$n[$i+1]!=($n[$i]+1)?'-'.$n[$i].$t.$n[$i+1]:'';
}
$s.='.';echo $s;