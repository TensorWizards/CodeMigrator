
public class Conditionals {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Data initialization
        int NUM1 = 25;
        int NUM2 = 15;
        int NUM3 = 25;
        int NUM4 = 15;
        int NEG_NUM = -1234;
        String CLASS1 = "ABCD";
        int CHECK_VAL = 65;
        String PASS = "PASS";
        String FAIL = "FAIL";

        // Conditional Statements
        if (NUM1 > NUM2) {
            System.out.println("IN LOOP 1 - IF BLOCK");
        } else {
            System.out.println("IN LOOP 1 - ELSE BLOCK");
        }

        if (NUM3 == NUM4) {
            System.out.println("IN LOOP 2 - IF BLOCK");
        } else {
            System.out.println("IN LOOP 2 - ELSE BLOCK");
        }

        // Custom Conditions
        if (CHECK_VAL >= 41 && CHECK_VAL <= 100) {
            System.out.println("PASSED WITH " + CHECK_VAL + " MARKS.");
        } else if (CHECK_VAL >= 0 && CHECK_VAL <= 40) {
            System.out.println("FAILED WITH " + CHECK_VAL + " MARKS.");
        }

        // Switch Statement
        switch (NUM1) {
            case 2:
                System.out.println("NUM1 LESS THAN 2");
                break;
            case 19:
                System.out.println("NUM1 LESS THAN 19");
                break;
            default:
                System.out.println("NUM1 LESS THAN 1000");
                break;
        }
    }