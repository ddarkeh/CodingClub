
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Producer implements Runnable {

    private Random random;
    private int number;
    //create pool variable for object Pool
    private Pool pool;

    //constructor with object parameter
    public Producer(Pool pool) {
        this.random = new Random();
        this.number = this.random.nextInt(7) + 1;
        //so going to pass the Pool object and assign it to the variable, each producer will reference the same object.
        this.pool = pool;
    }

    public void run() {
        //Thread methods pushes number to pool object then sleep x seconds* (-drift) then gets a new number
        try {
            while (true) {
                this.pool.addToPool(number);
                Thread.sleep(5000);
                this.number = this.random.nextInt(7) + 1;
            }
        } catch (InterruptedException ex) {
            Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

