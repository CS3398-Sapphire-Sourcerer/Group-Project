package assignment2;

import java.io.Serializable;

/**
 * A assignment2.Package is an object that contains a tracking number, type, specification, mailing class, weight and volume.
 * @author Claudia Ortiz
 * @version 1.0
 *
 */

public abstract class Package implements Serializable {
    protected String trackNumber;
    protected String type;
    protected String specification;
    protected String mailingClass;

    /**
     * assignment2.Package constructor
     * creates a assignment2.Package
     * @param tNumber
     * @param specs
     * @param mClass
     */
    public Package(String tNumber, String specs, String mClass){
        setTrackNumber(tNumber);
        setSpecification(specs);
        setMailingClass(mClass);
    }

    /**
     * assignment2.Package constructor
     * creates a empty assignment2.Package
     */
    public Package(){

    }

    /**
     * Returns tracking number of a package.
     * @return a tracking number of a package
     */
    public String getTrackNumber(){
        return trackNumber;
    }

    /**
     * Returns The type of the assignment2.Package
     * @return The type of the assignment2.Package
     */
    public String getType(){
        return type;
    }

    /**
     * Returns The specification of the assignment2.Package
     * @return The specification of the assignment2.Package
     */
    public String getSpecification(){
        return specification;
    }

    /**
     * Returns The Mailing Class of the assignment2.Package
     * @return The Mailing Class of the assignment2.Package
     */
    public String getMailingClass(){
        return mailingClass;
    }

    /**
     * Sets The weight of the assignment2.Package
     * @param tNumber accepted
     */
    public void setTrackNumber(String tNumber){
        trackNumber = tNumber;
    }

    /**
     * Sets The weight of the assignment2.Package
     * @param value accepted
     */
    protected void setType(String value){
        type = value;
    }


    /**
     * Sets The weight of the assignment2.Package
     * @param specs accepted
     */
    public void setSpecification(String specs){
        specification = specs;
    }

    /**
     * Sets The weight of the assignment2.Package
     * @param mClass accepted
     */
    public void setMailingClass(String mClass){
        mailingClass = mClass;
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
        formattedString = String.format("%11s ", getTrackNumber());
        String finishedString =  "|" + formattedString + "|";
        formattedString = String.format("%9s ", getType());
        finishedString += formattedString + "|";
        formattedString = String.format("%14s ", getSpecification());
        finishedString += formattedString + "|";
        formattedString = String.format("%10s ", getMailingClass());
        finishedString += formattedString + "|";
        return finishedString;
    }
}
