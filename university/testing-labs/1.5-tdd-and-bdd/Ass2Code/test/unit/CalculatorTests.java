import model.Calculator;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

/**
 * @author kiwi-et
 * @version 04/02/2014 17:11
 */
public class CalculatorTests {
    private Calculator calc;

    @Before
    public void createCalculator() {
        calc = new Calculator();
    }

    @Test
    public void startCalculator() {
        // Given - No calculator
        // When
        // Then - initial state
        assertEquals("0.0", calc.getResult());
        assertFalse("Error is reported", calc.isError());
        assertFalse("Accumulator updated reported", calc.updated());
    }
}