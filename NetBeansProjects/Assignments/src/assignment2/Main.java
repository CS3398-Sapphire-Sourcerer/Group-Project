package assignment2; /**
 * assignment2.Main starts the program
 * @author Claudia Ortiz
 * @version 1.0
 */

import java.util.Scanner;

public class Main {
    private static Warehouse warehouse;
    private static Scanner scanner;

    /**
     * assignment2.Main starts the program
     * @param args
     */
    public static void main(String[] args) throws Exception {
        warehouse = new Warehouse();
        int menuSelection = 0;
        String userInput = null;
        scanner = new Scanner(System.in);

        //while user input !=6
        while(menuSelection != 6 ){

            printMenu();
            System.out.println("Please select an option.");

            userInput = scanner.nextLine();
            //validate its an int
            if (!ExpectInt(userInput)){
                System.out.println("Invalid Input! Enter a number.");
                
            }
            else{
                menuSelection = Integer.parseInt(userInput);
                System.out.println(menuSelection);

                if (menuSelection == 1 ){
                    showAll();
                }

                if(menuSelection == 2){
                    addNewPackage();
                }

                if (menuSelection == 3) {
                    deletePackage();
                }

                if (menuSelection == 4) {
                    searchPackage();
                }

                if (menuSelection == 5) {
                    //showSpecificPackages();
                }
            }

        }
        warehouse.savePackageInformation();
    }


    /**
     * Prints the reoccurring selection menu
     *
     */
    public static void printMenu(){
        //1. Show all existing package records in the database (in any order)
        //2. Add new package record to the database
        //3. Delete package record from a database
        //4. Search for a package (given its tracking number)
        //5. Show a list of packages withing a given weight range
        //6. Exit program
        System.out.println(" ");
        System.out.println("1. Show all existing package records in the database (in any order)");
        System.out.println("2. Add new package record to the database");
        System.out.println("3. Delete package record from a database");
        System.out.println("4. Search for a package (given its tracking number)");
        System.out.println("5. Show a list of packages withing a given weight range");
        System.out.println("6. Exit program");
    }

    /**
     * Prints all the packages in the warehouse
     *
     */
    public static void showAll(){
        //print each package
        System.out.println("----------------------------------------------------------------------");
        System.out.println("| TRACKING # |   TYPE   | SPECIFICATION |   CLASS   | WEIGHT | VOLUME |");
        System.out.println("----------------------------------------------------------------------");
        for (Package object: warehouse.getPackageList()) 
            System.out.println(object.toString());
        System.out.println("----------------------------------------------------------------------");
    }

    /**
     * Sends a request to the warehouse to add a new package
     *
     */
    public static void addNewPackage(){
        Package pkg = null;
        String userInput;
        int userInputInt = 0;
        boolean typeSelected = false;

        //trackNumber
        float userInputFloat;
        System.out.println("Adding new package.");
        System.out.println("Please enter tracking number.");
        userInput = scanner.nextLine();
        String trackNumber = userInput;

        //specification
        System.out.println("Please enter specification");
        userInput = scanner.nextLine();
        String specification = userInput;

        //mailingClass
        System.out.println("Please enter class.");
        userInput = scanner.nextLine();
        String mailingClass = userInput;

        System.out.println("Please choose a type: ");
        while(!typeSelected) {

            System.out.println(" ");
            System.out.println("1. Box");
            System.out.println("2. Crate");
            System.out.println("3. Drum");
            System.out.println("4. Envelope");
            userInputInt = scanner.nextInt();
            scanner.nextLine();
            System.out.println("You selected: " + userInputInt);

            //Its a BOX
            if(userInputInt == 1) {
                int largeDim, vol;
                System.out.println("Please enter the largest dimension of the box.");
                largeDim = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Please enter the volume of the box.");
                vol = scanner.nextInt();
                scanner.nextLine();

                pkg = new Box(trackNumber, specification, mailingClass, largeDim, vol);
                typeSelected = true;
            }
            //Its a CRATE
            else if (userInputInt == 2) {
                int maxWeight;
                String content;
                System.out.println("Please enter the maximum load weight of the crate.");
                maxWeight = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Please enter the contents of the crate.");
                content = scanner.nextLine();
                pkg = new Crate(trackNumber, specification, mailingClass, maxWeight, content);
                typeSelected = true;
            }
            //Its a DRUM
            else if(userInputInt == 3) {
                String materialValue;
                float diameterValue;
                System.out.println("Please enter the material of the drum.");
                materialValue = scanner.nextLine();
                System.out.println("Please enter the diameter of the drum.");
                diameterValue = scanner.nextFloat();
                scanner.nextLine();
                pkg = new Drum(trackNumber, specification, mailingClass, materialValue, diameterValue);
                typeSelected = true;
            }
            //Its a ENVELOPE
            else if(userInputInt == 4) {
                int height, width;
                System.out.println("Please enter the height of the envelope.");
                height = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Please enter the width of the envelope.");
                width = scanner.nextInt();
                scanner.nextLine();
                pkg = new Envelope(trackNumber, specification, mailingClass, height, width);
                typeSelected = true;
            }
            else {}
        }

        /*
        System.out.println("Please enter weight");
        userInputFloat = scanner.nextFloat();
        pkg.setWeight(userInputFloat);

        System.out.println("Please enter volume.");
        userInputFloat = scanner.nextFloat();
        pkg.setVolume(userInputFloat);
        */

        warehouse.addPackage(pkg);

    }

    /**
     * Sends a request to the warehouse to delete a package based on the tracking number
     *
     */
    public static void deletePackage(){
        String userInput;
        System.out.println("Deleting package.");
        System.out.println("Please enter tracking number.");
        userInput = scanner.nextLine();
        if(warehouse.deletePackage(userInput)){
            System.out.println("assignment2.Package deleted.");
        }
        else
            System.out.println("assignment2.Package " + userInput + " not found.");
    }

    /**
     * Sends a request to the warehouse to search for a package based on the tracking number
     *
     */
    public static void searchPackage(){
        String userInput;
        System.out.println("Searching for package.");
        System.out.println("Please enter tracking number.");
        userInput = scanner.nextLine();
        Package targetPackage = warehouse.retrievePackage(userInput);
        if(targetPackage != null){
            System.out.println("assignment2.Package found.");
            System.out.println(targetPackage.toString());
        }
        else
            System.out.println("assignment2.Package " + userInput + " not found.");
    }


    /**
     * Sends a request to the warehouse to search for packages based on their weights
     *
     */

    ///////////////
    // FIX MEEEE //
    ///////////////
    public static void showSpecificPackages(){
        float minValue, maxValue;
        System.out.println("Please enter the minimum weight value.");
        minValue = scanner.nextFloat();
        System.out.println("Please enter the maximum weight value.");
        maxValue = scanner.nextFloat();

        //print each package
        System.out.println("----------------------------------------------------------------------");
        System.out.println("| TRACKING # |   TYPE   | SPECIFICATION |   CLASS   | WEIGHT | VOLUME |");
        System.out.println("----------------------------------------------------------------------");
        //for (Package object: warehouse.retrievePackages(minValue, maxValue))
        //    System.out.println(object.toString());
        //System.out.println("----------------------------------------------------------------------");

    }

    private static boolean ExpectInt(String line)
    {
        try
        {
            Integer.parseInt(line);
        }
        catch(Exception e)
        {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    private static boolean ExpectFloat(String line)
    {
        try
        {
            Float.parseFloat(line);
        }
        catch(Exception e)
        {
            e.printStackTrace();
            return false;
        }
        return true;
    }
}
