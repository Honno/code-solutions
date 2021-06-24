package controller;

import model.Calculator;

import javax.swing.*;

/**
 * @author kiwi-et
 * @version 06/02/2014 10:36
 */
public class NumberVerifier extends InputVerifier {
    private final Calculator calculator;

    public NumberVerifier(Calculator calculator) {
        this.calculator = calculator;
    }

    /**
     * Checks whether the JComponent's input is valid. This method updates
     * the filed in the model if it is a valid number. It returns a boolean
     * indicating the status of the argument's input.
     *
     * @param input the JComponent to verify
     * @return <code>true</code> when valid, <code>false</code> when invalid
     * @see javax.swing.JComponent#setInputVerifier
     * @see javax.swing.JComponent#getInputVerifier
     */
    @Override
    public boolean verify(JComponent input) {
        if (input instanceof JTextField) {
            try {
                double number = Double.parseDouble(((JTextField) input).getText());
                calculator.setNumber(number);
                return true;
            } catch (NumberFormatException e) {
                calculator.setError();
            }
        }
        ((JTextField) input).selectAll();
        return false;
    }
}
