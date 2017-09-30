package assignment2;

public class User {

    private int ID;
    private String firstName;
    private String lastName;

    /**
     * Sets the value of ID
     * @param idValue of assignment2.User
     */
    public void setID(int idValue){
        ID = idValue;
    }


    /**
     * Sets the value of firstName
     * @param first of assignment2.User
     */
    public void setFirstName(String first) {
        firstName = first;
    }

    /**
     * Sets the value of lastName
     * @param last of assignment2.User
     */
    public void setLasttName(String last) {
        lastName = last;
    }

    /**
     * Returns the value of ID
     * @return the ID of assignment2.User
     */
    public int getID(){
        return ID;
    }

    /**
     * Returns the value of firstName
     * @return the firstName of assignment2.User
     */
    public String getFirstName() {
        return firstName;
    }

    /**
     * Returns the value of lastName
     * @return the lastName of assignment2.User
     */
    public String getLastName(){
        return lastName;
    }


}
