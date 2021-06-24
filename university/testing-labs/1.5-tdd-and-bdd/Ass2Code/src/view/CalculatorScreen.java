package view;

import controller.CalculatorOperation;
import model.Calculator;

import javax.swing.*;
import java.awt.*;
import java.lang.reflect.InvocationTargetException;

public class CalculatorScreen extends JFrame {
    private final Calculator model = new Calculator();
    // Components are treated as attributes, so that they will be
    // visible to all of the methods of the class.

    // Use descriptive names for components where possible; it makes
    // your job easier later on!

    // Constructor.
    public CalculatorScreen() {
        // Invoke the generic JFrame constructor.
        super("Simple CalculatorScreen");

        // The content pane container is now declared to be an
        // attribute.  Note that the use of "this." is unnecessary;
        // we could have simply written:
        // contentPane = getContentPane();
        Container contentPane = this.getContentPane();
        this.setSize(250, 120);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        // Technique for centering a frame on the screen.
        Dimension frameSize = this.getSize();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((screenSize.width - frameSize.width) / 2,
                (screenSize.height - frameSize.height) / 2);

        JPanel topPanel = new JPanel();
        JTextField dataField = new ValidatedNumber(18, model);
        topPanel.add(dataField);
        contentPane.add(topPanel, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(2, 2));
        JButton plusButton = new JButton("+");
        JButton minusButton = new JButton("-");
        JButton multiplyButton = new JButton("*");
        JButton divideButton = new JButton("/");
        JButton equalsButton = new JButton("=");
        JButton clearButton = new JButton("Clear");
        buttonPanel.add(plusButton);
        buttonPanel.add(minusButton);
        buttonPanel.add(multiplyButton);
        buttonPanel.add(divideButton);
        buttonPanel.add(equalsButton);
        buttonPanel.add(clearButton);
        contentPane.add(buttonPanel, BorderLayout.SOUTH);

        // Add behaviors!

        plusButton.addActionListener(new CalculatorOperation('+', model, this));
        minusButton.addActionListener(new CalculatorOperation('-', model, this));
        multiplyButton.addActionListener(new CalculatorOperation('*', model, this));
        divideButton.addActionListener(new CalculatorOperation('/', model, this));
        equalsButton.addActionListener(new CalculatorOperation('=', model, this));
        clearButton.addActionListener(new CalculatorOperation('C', model, this));

        this.setVisible(true);
    }

    public static void main(String[] args) {
        // Instantiate the calculator!
        try {
            SwingUtilities.invokeAndWait(new Runnable() {
                @Override
                public void run() {
                    new CalculatorScreen();
                }
            });
        } catch (InterruptedException e) {
            System.out.println("Calculator interrupted");
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        } catch (InvocationTargetException e) {
            System.out.println("Calculator invocation exception");
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        }
    }
}
