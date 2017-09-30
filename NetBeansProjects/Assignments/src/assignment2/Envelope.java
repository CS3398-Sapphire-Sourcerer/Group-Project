package assignment2;

public class Envelope extends Package {

    private int height;
    private int width;

    /**
     * Defined constructor of Envelope
     * Creates an defined box
     * @param tNumber
     * @param specs
     * @param mClass
     * @param heightValue
     * @param widthValue
     */
    public Envelope(String tNumber, String specs, String mClass, int heightValue, int widthValue) {
        //Pass tHumber, specs, and mClass to the constructor in Package which is the base class to this class
        super(tNumber, specs, mClass);
        setHeight(heightValue);
        setWidth(widthValue);
        type = "Envelope";
    }

    /**
     * Sets the value of height
     * @param heightValue of assignment2.Envelope
     */
    public void setHeight(int heightValue) {
        height = heightValue;
    }

    /**
     * Sets the value of width
     * @param widthValue of assignment2.Envelope
     */
    public void setWidth(int widthValue) {
        width = widthValue;
    }

    /**
     * Returns the value of height
     * @return the height of assignment2.Envelope
     */
    public int getHeight() {

        return height;

    }

    /**
     * Returns the value of width
     * @return the with of assignment2.Envelope
     */
    public int getWidth() {
        return width;
    }
}