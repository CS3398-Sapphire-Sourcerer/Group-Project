package assignment2;

public class Box extends Package {

    private int largestDimension;
    private int volume;

    /**
     * Default constructor of assignment2.Box
     * Creates an undefined box of assignment2.Box
     */
    public Box()
    {
        type = "Box";
    }

    /**
     * Defined constructor of Box
     * Creates an defined box
     * @param tNumber
     * @param specs
     * @param mClass
     * @param largestDim
     * @param vol
     */
    public Box(String tNumber, String specs, String mClass, int largestDim, int vol)
    {
        //Pass tHumber, specs, and mClass to the constructor in Package which is the base class to this class
        super(tNumber, specs, mClass);
        setLargestDimension(largestDim);
        setVolume(vol);
        type = "Box";
    }

    /**
     * Sets the value of largestDimension
     * @param largeDim of assignment2.Box
     */
    public void setLargestDimension(int largeDim) {
        largestDimension = largeDim;
    }

    /**
     * Sets the value of largestDimension
     * @param volumeValue of assignment2.Box
     */
    public void setVolume(int volumeValue) {
        volume = volumeValue;

    }

    /**
     * Returns the largestDimension of assignment2.Box
     * @return The largestDimension of assignment2.Box
     */
    public int getlargestDimension() {
        return largestDimension;
    }

    /**
     * Returns The volume of the assignment2.Box
     * @return The volume of the assignment2.Box
     */
    public int getVolume(){
        return volume;
    }


    /**
     * formats the values in the database
     * ----------------------------------------------------------------------
     * | TRACKING # |   TYPE   | SPECIFICATION |   CLASS   | WEIGHT | VOLUME |
     * ----------------------------------------------------------------------
     * ----------------------------------------------------------------------
     */
    public String toString() {
        String formattedString;
        String finishedString = super.toString();
        formattedString = String.format("%11s ", getlargestDimension());
        finishedString += formattedString + "|";
        formattedString = String.format("%9s ", getVolume());
        finishedString += formattedString + "|";
        return finishedString;
    }
}