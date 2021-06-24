package model;

/**
 * @author kiwi-et
 * @version 04/02/2014 17:42
 */
public class Calculator {
    private double number = 0.0;
    private boolean inputValid = true;
    private double accumulator = 0.0;
    private boolean update = false;
    private char operation = ' ';
    private boolean divideError = false;

    public void setNumber(double number) {
        this.number = number;
        this.inputValid = true;
        this.divideError = false;
    }

    public String getResult() {
        if (this.divideError) {
            return "Div By Zero";
        }
        return "" + this.accumulator;
    }

    public void setError() {
        this.inputValid = false;
    }

    public boolean isError() {
        return !this.inputValid;
    }

    public boolean updated() {
        boolean update = this.update;
        this.update = false;
        return update;
    }

    public void setOperation(char operation) {
        this.divideError = false;
        if (operation == 'C') {
            this.accumulator = 0.0;
            this.number = 0.0;
            this.operation = ' ';
            this.inputValid = true;
        } else if (inputValid) {
            switch (this.operation) {
                case ' ':
                case '=':
                    this.accumulator = this.number;
                    break;
                case '+':
                    this.accumulator += this.number;
                    break;
                case '-':
                    this.accumulator -= this.number;
                    break;
                case '*':
                    this.accumulator *= this.number;
                    break;
                case '/':
                    if (this.number == 0.0) {
                        this.divideError = true;
                    } else {
                        this.accumulator /= this.number;
                    }
                    break;
            }
            this.operation = operation;
        }
        this.update = true;
    }
}