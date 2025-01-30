<?php
$a = $_POST['a'];
$b = $_POST['b'];
$c = $_POST['c'];

$command = escapeshellcmd("python3 calculate.py $a $b $c");

$output = shell_exec($command);

echo $output;
?>