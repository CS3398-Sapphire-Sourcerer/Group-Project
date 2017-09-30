package assignment2;

public class Drum extends Package {

    private String material;
    private float diameter;

    /**
     * Defined constructor of Drum
     * Creates an defined box
     * @param tNumber
     * @param specs
     * @param mClass
     * @param mat
     * @param diameterValue
     */
    public Drum(String tNumber, String specs, String mClass, String mat, float diameterValue) {
        //Pass tHumber, specs, and mClass to the constructor in Package which is the base class to this class
        super(tNumber, specs, mClass);
        setMaterial(mat);
        setDiameter(diameterValue);
        type = "Drum";
    }

    /**
     * Sets the value of material
     * @param materialValue of assignment2.Drum
     */
    public void setMaterial(String materialValue){
        material = materialValue;
    }

    /**
     * Sets the value of diameter
     * @param diametervalue of assignment2.Drum
     */
    public void setDiameter(float diameterValue){
        diameter = diameterValue;
    }

    /**
     * Returns the value of material
     * @return the material of assignment2.Crate
     */
    public String getMaterial(){
        return material;
    }

    /**
     * Returns the value of diameter
     * @return the diameter of assignment2.Crate
     */
    public float getDiameter(){
        return diameter;
    }
}
