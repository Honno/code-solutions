package stepdefs;


import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import uk.ac.aston.cs3270.lab5.Triangle;

import static junit.framework.TestCase.assertEquals;


/**
 * A class with JBehave steps for the Triangles Problem
 * 
 * @author Prins Butt
 */
public class TrianglesProblemStepDefs {

    // A variable to store a reference to a triangle object
    private Triangle triangle;

    // A variable to store the type of the triangle as identified by the program
    String type = "";
    
    @Given("^a triangle with sides of length (\\d+), (\\d+), (\\d+)$")
    public void aTriangleWith(int sideA, int sideB, int sideC) {
        triangle = new Triangle(sideA, sideB, sideC);
    }

    @When("the program identifies the triangle")
    public void theProgramIdentifiesTriangle() {
        type = triangle.classify();
    }

    @Then("the program should state '(Scalene|Isosceles|Equilateral|Not a triangle)'")
    public void theProgramShouldState(String type) {
        assertEquals(this.type, type);
    }
}