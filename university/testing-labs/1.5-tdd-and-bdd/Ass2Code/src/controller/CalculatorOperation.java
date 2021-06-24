package controller;

import model.Calculator;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * @author kiwi-et
 * @version 06/02/2014 12:23
 */
public class CalculatorOperation implements ActionListener {
    private final Calculator model;
    private final JFrame frame;
    private char operation;

    public CalculatorOperation(char operation, Calculator model, JFrame frame) {
        this.operation = operation;
        this.model = model;
        this.frame = frame;
    }

    /**
     * Invoked when an action occurs.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        model.setOperation(this.operation);
        frame.repaint();
    }
}
