package assignment2;

public class Crate extends Package {

    private float maxLoadWeight;
    private String content;

    /**
     * Defined constructor of Crate
     * Creates an defined box
     * @param tNumber
     * @param specs
     * @param mClass
     * @param maxWeight
     * @param content
     */
    public Crate(String tNumber, String specs, String mClass, int maxWeight, String content) {
        //Pass tHumber, specs, and mClass to the constructor in Package which is the base class to this class
        super(tNumber, specs, mClass);
        setMaxLoadWeight(maxWeight);
        setContent(content);
        type = "Crate";
    }


    /**
     * Sets the value of maxLoadWeight
     * @param maxWeight of assignment2.Crate
     */
    public void setMaxLoadWeight(float maxWeight) {
        maxLoadWeight = maxWeight;
    }

    /**
     * Sets the value of content
     * @param contentValue of assignment2.Crate
     */
    public void setContent(String contentValue) {
        content = contentValue;
    }

    /**
     * Returns the value of maxLoadWeight
     * @return the maxLoadWeight of assignment2.Crate
     */
    public float getMaxLoadWeight() {
        return maxLoadWeight;
    }

    /**
     * Returns the value of content
     * @return the content of assignment2.Crate
     */
    public String getContent() {
        return content;

    }
}