import java.util.ArrayList;

public class Pool {
    //A list is used to store numbers from the producers
    private ArrayList<Integer> list;
    
    //constructor to init List
    public Pool() {
        this.list = new ArrayList<>();
    }
    
    //used by producer to add it's random generated number to the list
    public void addToPool(int item) {
        this.list.add(item);
    }
    
    //used for debug not used
    public void printPool() {
        for (int x : this.list)
            System.out.println(x);
    }
    
    //used by Consumer to get the first indexed number this is a FIFO system
    public int getFromPool() {
        if (empty()){
           return -1;
        }  
        return this.list.get(0);
    }
    
    //used by consumer to delete
    public void deleteFromPool() {
        this.list.remove(0);
    }
    
    //boolean to check to see if list is empty or not
    public boolean empty() {
        return this.list.isEmpty();
    }
}
