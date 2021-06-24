package view;

import controller.NumberVerifier;
import model.Calculator;

import javax.swing.*;
import java.awt.*;
import java.awt.event.FocusEvent;

/**
 * An extension of the JTextField that uses a verifier to validate in put as a number and changes
 * the background colour of the field to "RED" if input is not a number.
 *
 * @author kiwi-et
 * @version 06/02/2014 12:04
 */
public class ValidatedNumber extends JTextField {
    private final Calculator model;

    /**
     * Constructor to setup field with attached verifier and right test alignment
     *
     * @param width character width of field
     * @param model reference to the calculator model
     */
    public ValidatedNumber(int width, Calculator model) {
        super(width);
        this.setHorizontalAlignment(JTextField.RIGHT);
        this.model = model;
        this.setInputVerifier(new NumberVerifier(model));
    }

    @Override
    protected void processFocusEvent(FocusEvent e) {
        super.processFocusEvent(e);
        this.selectAll();
    }

    /**
     * Overriding default paint behaviour to cause the background to be read if the input value is
     * not a valid number.
     *
     * @param g the graphics object
     */
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        this.setBackground(Color.WHITE);
        if (model.isError()) {
            this.setBackground(Color.RED);
        } else if (model.updated()) {
            this.setText("" + model.getResult());
        }
    }
}
