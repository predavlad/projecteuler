<?$i=99;$k='of beer';$b="bottles ".$k;$w="on the wall";$n="\n";
while($i-1){$z="$i $b $w, $i $b.{$n}Take one down and pass it around, ";
if($i==2){$p=$b;$b='bottle '.$k;}echo$z.--$i." $b $w.$n$n";}
$f="Go to the store and buy some more, 99 $p $w.";echo"1 $b $w, 1 $b.$n$f";