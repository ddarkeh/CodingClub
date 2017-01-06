import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Scanner object
        Scanner input = new Scanner(System.in);
        int x, y, z;
        while (true) {
            try {
                System.out.print("Input starting hour [0 - 23]: ");
                x = Integer.parseInt(input.nextLine());
                System.out.print("Input starting minute [0 - 59]: ");
                y = Integer.parseInt(input.nextLine());
                System.out.print("Input starting second [0 - 59]: ");
                z = Integer.parseInt(input.nextLine());
                break;
            } catch (NumberFormatException e) {
                System.out.println("Invalid input: - " + e);
            }
        }
        //creates clock object
        Clock clock = new Clock(x,y,z);
        System.out.println("");
        //infinite loop.. cause clock..
        while(true) {
            try {
                System.out.println(clock);
                clock.next();
                Thread.sleep(1000);
            } catch(InterruptedException Ex) {
                Thread.currentThread().interrupt();
            }
        }
    } 
}
