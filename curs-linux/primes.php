<?php
error_reporting(0);
ini_set("display_errors",1);
function s($m){
	$p=function($n){
		for ($i=2;$i<$n;)if($n%$i++==0)$b=1;
		return$b?0:1;
	};
	for(;$i<$m-6;$i++)if($p($i)&$p($i+6))$r[]=array($i,$i+6);
	return$r;
};
var_dump(s($argv[1]));

