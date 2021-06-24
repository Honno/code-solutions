<?php
$a = $_GET["num1"];
$b = $_GET["num2"];

function li($string, $num) {
    echo "<li>" . $string . ": " . $num;
}

echo "<ul>";

li("Addition", ($a + $b));
li("Subtraction", ($a - $b));
li("Multiplication", ($a * $b));
li("Division", ($a / $b));

echo "</ul>";
?>
