package stepdefs;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import model.Calculator;

/**
 * @author kiwi-et
 * @version 06/02/2014 16:52
 */
public class CalculatorStepDefs {
    private Calculator calculator;

    @Given("^a calculator$")
    public void a_calculator() {
        calculator = new Calculator();
    }

    @When("^turned on$")
    public void turned_on() {
        // Do nothing
    }

    @Then("^accumulator should be ([0-9]+\\.[0-9]+)$")
    public void accumulator_should_be_(String expected) {

    }
}
