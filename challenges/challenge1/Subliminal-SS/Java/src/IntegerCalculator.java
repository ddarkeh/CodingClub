import java.util.*;
import java.lang.String;

public class IntegerCalculator {

	public static void main(String[] args) {
		System.out.println("Welcome to the Integer calculator!\nPlease specify an Integer value between 0 and 10000");

		Scanner userInput = new Scanner(System.in);

		int intToCalculate = -1;
		int successFlag = 0;

		while (successFlag == 0) {
			try {
				intToCalculate = userInput.nextInt();
				userInput.nextLine();
				if (intToCalculate > 0 && intToCalculate < 10000) {
					successFlag = 1;
				} else {
					System.out.print("Data supplied is outside of scottstephers spec, please enter an Integer between 0 and 10000 exclusive.\n");
				}
			} catch (InputMismatchException errorOutput) {
				userInput.nextLine();
				System.out.print("Data supplied is outside of scottstephers spec, please enter an Integer between 0 and 10000 exclusive.\n");
			}
		}

		System.out.println("Calculating the Sum total of " + intToCalculate);
		String stringToCalculate = Integer.toString(intToCalculate); 
		String theArray[] = stringToCalculate.split("");
		
		int totalResult = 0;
		
        for (String s : theArray) {
            totalResult = totalResult + Integer.parseInt(s);
            }
		
		System.out.print(totalResult + " " + "(" + String.join(" + ", theArray) + ")");
		
		userInput.close();

	}

}