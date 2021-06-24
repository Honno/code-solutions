use Calculator;

use PHPUnit\Framework\TestCase;

class CalculatorTest extends TestCase {
    public function testAdd() {
        calculator = new Calculator(4, 2);
        $this->assertEquals(calculator.add(), 6);
    }

    public function testDiv() {
        calculator = new Calculator(4, 2);
        $this->assertEquals(calculator.div(), 2);

        calculator = new Calculator(6, 0);
        $this->expectException(calculator.div());
    }
}

?>
