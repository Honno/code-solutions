
package uk.ac.aston.cs3270.lab5;

/**
 * Identifies the type of a triangle given the three lengths of the
 * sides of the triangle.  Assumes that a valid triangle is one with
 * sides of lengths between 1 and 200 (inclusive) and that any triangle
 * which does not meet this condition is not a triangle.
 *
 * @author Prins Butt
 */
public class Triangle {

    // Some useful constants for each type of triangle
    public static final String EQUILATERAL_TRIANGLE = "Equilateral";
    public static final String INVALID_TRIANGLE = "Not a triangle";
    public static final String ISOSCELES_TRIANGLE = "Isosceles";
    public static final String SCALENE_TRIANGLE = "Scalene";

    // Some useful constants for the acceptable range of each length
    private static final int MIN_LENGTH = 1;
    private static final int MAX_LENGTH = 200;

    // Variables for the length of each side of a triangle
    private int sideA, sideB, sideC;

    /**
     * Constructor to create a triangle with the specified lengths
     * 
     * @param sideA	length of side A of the triangle
     * @param sideB	length of side B of the triangle
     * @param sideC	length of side C of the triangle
     */
    public Triangle(int sideA, int sideB, int sideC) {
        this.sideA = sideA;
        this.sideB = sideB;
        this.sideC = sideC;
    }
    
    /**
     * Method to check if the specified lengths are with in acceptable range
     * 
     * @param a	length of side A of the triangle
     * @param b	length of side B of the triangle
     * @param c	length of side C of the triangle
     * @return true if with in range, false otherwise
     */
    private boolean isInRange(int a, int b, int c) {
        if (a < MIN_LENGTH || a > MAX_LENGTH) return false;
        if (b < MIN_LENGTH || b > MAX_LENGTH) return false;
        if (c < MIN_LENGTH || c > MAX_LENGTH) return false;
        return true;
    }

    /**
     * Method to check if it is possible to create the triangle. 
     * Not needed since it is not possible to specify numbers that will give an impossible condition.  
     * Here for illustration purposes only.
     * 
     * @param a	length of side A of the triangle
     * @param b	length of side B of the triangle
     * @param c	length of side C of the triangle
     * @return true if is possible, false otherwise
     */
    private boolean isPossible(int a , int b, int c) {
         if (a == b &&
             a == c &&
             b != c) return false;

         if (a == b &&
             b == c &&
             a != c) return false;

         if (a == c &&
             b == c &&
             a != b) return false;

         return true;
    }

    /**
     * Method to check if the specified lengths give a valid triangle
     * 
     * @param a length of side A of the triangle
     * @param b	length of side B of the triangle
     * @param c	length of side C of the triangle
     * @return true if the triangle is valid, false otherwise
     */
    private boolean isValid(int a, int b, int c) {
        return (a + b > c &&
                a + c > b &&
                b + c > a);
    }

    
    /**
     * Method to calculate the area of the triangle
     * 
     * @return the area of the triangle
     */
    public double calculateArea() {
       int p = calculatePerimeter();
       return p * (p - sideA) * (p - sideB) * (p - sideC);
    }

    /**
     * Method to calculate the perimeter of the triangle
     * 
     * @return the perimeter of the triangle
     */
    public int calculatePerimeter () {
       return sideA + sideB + sideC;
    }
    
    /**
     * Method to determine the type of a triangle given the lengths of each side of the triangle
     * 
     * @return the classification of the triangle
     */
    public String classify() {
        if (isPossible(sideA, sideB, sideC) &&
            isValid(sideA, sideB, sideC) &&
            isInRange(sideA, sideB, sideC)) {
            
            if (sideA == sideB && sideB == sideC) return EQUILATERAL_TRIANGLE;
            if (sideA == sideB || sideB == sideC || sideA == sideC) return ISOSCELES_TRIANGLE;
            return SCALENE_TRIANGLE;
        }

        return INVALID_TRIANGLE;
    }
        
    /**
     * Method to check if the triangle is acute angled triangle
     * 
     * @return true if an acute angled triangle, false otherwise
     */
    public boolean isAcute() {
    	if (isPossible(sideA, sideB, sideC) &&
            isValid(sideA, sideB, sideC) &&
            isInRange(sideA, sideB, sideC)) {
    		
            if (sideA > sideB && sideA > sideC) return (sideA*sideA) < ((sideB*sideB) + (sideC*sideC));
            if(sideB > sideA && sideB > sideC) return (sideB*sideB) < ((sideA*sideA) + (sideC*sideC));
            return (sideC*sideC) < ((sideA*sideA) + (sideB*sideB));
        }

        return false;
    }
    
    /**
     * Method to whether or not the triangle is an equilateral triangle
     * 
     * @return true if an equilateral triangle, false otherwise
     */
    public boolean isEquilateral() {
        return (isPossible(sideA, sideB, sideC) &&
                isValid(sideA, sideB, sideC) &&
                isInRange(sideA, sideB, sideC) &&
                sideA == sideB && sideB == sideC);
    }

    /**
     * Method to check whether or not the triangle is an isosceles triangle
     * 
     * @return true if an isosceles triangle, false otherwise
     */
    public boolean isIsosceles() {
        return (isPossible(sideA, sideB, sideC) &&
                isValid(sideA, sideB, sideC) &&
                isInRange(sideA, sideB, sideC) &&
                (sideA == sideB || sideB == sideC || sideA == sideC));
    }

    /**
     *  Method to check whether or not the triangle is an obtuse triangle
     *  
     *  @return true if an obtuse angled triangle, false otherwise
     */
    public boolean isObtuse() {
    	if (isPossible(sideA, sideB, sideC) &&
                isValid(sideA, sideB, sideC) &&
                isInRange(sideA, sideB, sideC)) {
    		
            if (sideA > sideB && sideA > sideC) return (sideA*sideA) > ((sideB*sideB) + (sideC*sideC));
            if(sideB > sideA && sideB > sideC) return (sideB*sideB) > ((sideA*sideA) + (sideC*sideC));
            return (sideC*sideC) > ((sideA*sideA) + (sideB*sideB));
        }

        return false;
    }

    /**
     * Method to check whether or not the triangle is a right angled triangle
     * 
     * @return true if right angled triangle, false otherwise
     */
    public boolean isRightAngled() {
    	if (isPossible(sideA, sideB, sideC) &&
                isValid(sideA, sideB, sideC) &&
                isInRange(sideA, sideB, sideC)) {
    		
            if (sideA > sideB && sideA > sideC) return (sideA*sideA) == ((sideB*sideB) + (sideC*sideC));
            if(sideB > sideA && sideB > sideC) return (sideB*sideB) == ((sideA*sideA) + (sideC*sideC));
            return (sideC*sideC) == ((sideA*sideA) + (sideB*sideB));
        }

        return false;
    }

    /**
     * Method to check whether or not the triangle is a scalene triangle
     * 
     * @return true if scalene triangle, false otherwise
     */
    public boolean isScalene() {
        return (isPossible(sideA, sideB, sideC) &&
                isValid(sideA, sideB, sideC) &&
                isInRange(sideA, sideB, sideC) &&
                (sideA != sideB && sideB != sideC && sideA != sideC));
    }
    
    /**
     * Method to list all possible triangle combinations accepted by the program
     * 
     * @param min	the minimum length for a side of a triangle
     * @param max	the maximum length for a side of a triangle
     */
    public void listTrianglesInRange(int min, int max) {

    	System.out.println("List of possible valid triangles:");

        for (int a=min; a <= max; a++) {
            for (int b=min; b <= max; b++) {
                for (int c=min; c <= max; c++) {
                    if (isPossible(a, b, c) &&
                        isValid(a, b, c) &&
                        isInRange(a, b, c)) {
                        System.out.println("(" + a + "," + b + "," + c + ")");
                    }
                }
            }
        }
    }

    /**
     *  Method to provide human-friendly string representation of the triangle
     */
    @Override
    public String toString() {
        return classify() + " (" + sideA + "," + sideB + "," + sideC + ")";
    }
}
