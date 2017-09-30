package assignment2; /**
 * assignment2.Warehouse stores all the packages
 * @author Claudia Ortiz
 * @version 1.0
 */

import java.io.*;
import java.util.ArrayList;


public class Warehouse {
    final String PACKAGETXT = "packages.ser";
    //private FileIO fileIO;

    private ArrayList<Package> packageList;

    /**
     * assignment2.Warehouse constructor
     * creates a assignment2.Warehouse
     */
    public Warehouse() throws Exception {

        FileInputStream fis = null;
        try {
            fis = new FileInputStream(PACKAGETXT);
            ObjectInputStream ois = new ObjectInputStream(fis);
            ////////////
            // FIX ME //
            ////////////
            //This is the problem
            //  cannot cast as package because they are actually boxes, crates, drums, and envelopes
            //  and package is an abstract class
            packageList = new ArrayList<Package>();
            //Arrays.asList((Box[])ois.readObject())
        }
        catch(IOException e)
        {
            e.printStackTrace();
            packageList = new ArrayList<Package>();
        }

    }

    /**
     * adds a package into the assignment2.Warehouse
     * @param value of a assignment2.Package
     */
    public void addPackage(Package value){
        if (value != null) {
            packageList.add(value);
        }
        else {
            System.out.println("assignment2.Warehouse::addPackage assignment2.Package is null.");
            return;
        }
    }

    /**
     * retrieves a package from the assignment2.Warehouse
     * @param trackNumber of a assignment2.Package
     */
    public Package retrievePackage(String trackNumber) {
        if (!packageList.isEmpty()) {
            for (Package object : packageList) {
                if (object.getTrackNumber().equals(trackNumber)) {
                    return object;
                }
            }
        }
        return null;
    }

    /**
     * Returns the list of packages in the assignment2.Warehouse
     * @return packageList of a package in the assignment2.Warehouse
     */
    public ArrayList<Package> getPackageList() {
        return packageList;
    }

    /**
     * Deletes package with specific trackNumber
     * @return true if the package was deleted
     */
    public boolean deletePackage(String trackNumber){
        Package targetPackage = retrievePackage(trackNumber);
        if(targetPackage!=null) {
            packageList.remove(targetPackage);
            return true;
        }
        else {
            return false;
        }
    }

    /**
     * Saves package information into a .ser file
     */
    public void savePackageInformation() throws Exception
    {
        FileOutputStream fos = new FileOutputStream(PACKAGETXT);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(packageList);
    }

}