public class Clock {
    private Counting hour;
    private Counting minute;
    private Counting seconds;
    //Constructor that creates Counting objects defines upper limites and invokes setter for initial values
    public Clock(int startingHour, int startingMinute, int startingSeconds) {
        this.hour = new Counting(23);
        this.minute = new Counting(59);
        this.seconds = new Counting(59);
        this.hour.setValue(startingHour);
        this.minute.setValue(startingMinute);
        this.seconds.setValue(startingSeconds);
    }
    //method for main to increase values invokes methods within the counting objects under certain conditions
    public void next() {
        if (minute.getValue() == 59 && seconds.getValue() == 59) {
            this.hour.next();
            this.minute.next();
            this.seconds.next();
        }
        else if (seconds.getValue() == 59) {
            this.minute.next();
            this.seconds.next();
        }
        else {
            this.seconds.next();
        }
    }
    //toString to be used by main which effectively pulls toString from counting objects
    public String toString() {
        return this.hour + ":" + this.minute + ":" + this.seconds;
    }
    
}
