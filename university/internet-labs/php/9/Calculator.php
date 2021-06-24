<?php

class Calculator {
    public $num1;
    public $num2;

    public function __construct($num1, $num2) {
        $this->num1 = $num1;
        $this->num2 = $num2;
    }

    public function add() {
        return $num1 + $num2;
    }

    public function div() {
        if ($num2 == 0) {
            throw new Exception("Can not divide by zero");
        } else {
            return $num1 / $num2;
        }
    }
}

?>
