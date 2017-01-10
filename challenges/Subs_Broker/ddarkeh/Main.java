
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    public static void main(String[] args) {

        //Main is only used to build objects and threads in memory, and begin threading..
       
        
        
        
        //create (1) Pool Object
        Pool p = new Pool();

        //Creating and intitialins objects and threads, doing it in a line by line fashion
        //to easily demonstrate what's happening, create loops if you want X amount of each.
        //create (4) Producers, pass pool object
        Producer p1 = new Producer(p);
        Producer p2 = new Producer(p);
        Producer p3 = new Producer(p);
        Producer p4 = new Producer(p);

        //create (4) Consumers, pass pool object
        Consumer c1 = new Consumer(p);
        Consumer c2 = new Consumer(p);
        Consumer c3 = new Consumer(p);
        Consumer c4 = new Consumer(p);

        //building threads for producers and Consumers
        Thread thread = new Thread(p1);
        Thread thread2 = new Thread(p2);
        Thread thread3 = new Thread(p3);
        Thread thread4 = new Thread(p4);
        //consumers
        Thread thread5 = new Thread(c1);
        Thread thread6 = new Thread(c2);
        Thread thread7 = new Thread(c3);
        Thread thread8 = new Thread(c4);

        //turning the threads on
        thread.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread5.start();
        thread6.start();
        thread7.start();
        thread8.start();
    }
}
