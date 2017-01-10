import java.util.logging.Level;
import java.util.logging.Logger;

public class Consumer implements Runnable {

    private String[] daysOfWeek;
    private Pool pool;
    private int storePool;

    //constructor that init's array with my output strings, also inits Pool object to be used to grab numbers from object
    public Consumer(Pool pool) {
        this.daysOfWeek = new String[]{"Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"};
        this.pool = pool;
    }

    //if pool is empty sleep, if pool is not empty grab from object pool and store, then delete from pool, print out what I am then sleep.
    public void run() {
        try {
            while (true) {
                if (this.pool.empty()) {
                    Thread.sleep(10000);
                    continue;
                }
                this.storePool = pool.getFromPool();
                this.pool.deleteFromPool();
                printMe();
                Thread.sleep(10000);
            }
        } catch (InterruptedException ex) {
            Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    //print used to ... print
    public void printMe() {
        System.out.println("I am a Consumer - " + this.daysOfWeek[storePool -1]);
    }

    //used for nothing but if something needed it i.e main could produce the same output as printMe();
    public String toString() {
        return "I am a Consumer - " + this.daysOfWeek[storePool];
    }

}
