public class Counting {
    private int value;
    private final int upperValue;
    //Constructor with upperParam for generic counting **not just for this clock excercise**
    public Counting(int upperValue) {
        this.value = 0;
        this.upperValue = upperValue;
    }
    //increase the count unless the next value goes over the upper limit then resets
    public void next() {
        this.value++;
        if (value > upperValue)
            this.value = 0;
    }
    //getter for toString
    public int getValue() {
        return this.value;
    }
    //setter for clock class
    public void setValue(int value) {
        if (!(value > this.upperValue))
            this.value = value;
    }
    //toString for clock class if under 10 append 0
    public String toString() {
        if (getValue() < 10)
            return "0" + getValue();
        return "" + getValue();
    }
    
}
