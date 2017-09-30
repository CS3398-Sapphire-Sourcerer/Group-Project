package assignment2;

public class Employee extends User {

    private int socialSecurityNumber;
    private float monthSalary;
    private int bankAcctNumber;

    /**
     * Sets the value of socialSecurityNumber
     * @param social of assignment2.Employee
     */
    public void setSocialSecurityNumber(int social){
        socialSecurityNumber = social;
    }

    /**
     * Sets the value of monthlySalary
     * @param salary of assignment2.Employee
     */
    public void setMonthSalary(float salary){
        monthSalary = salary;
    }

    /**
     * Sets the value of bankAcctNumber
     * @param acctNumber of assignment2.Employee
     */
    public void setBankAcctNumber(int acctNumber){
        bankAcctNumber = acctNumber;
    }

    /**
     * Returns the value of socialSecurityNumber
     * @return the socialSecurityNumber of assignment2.Employee
     */
    public int getSocialSecurityNumber(){
        return socialSecurityNumber;
    }

    /**
     * Returns the value of monthlySalary
     * @return the monthlySalary of assignment2.Employee
     */
    public float getMonthlySalary(){
        return monthSalary;
    }

    /**
     * Returns the value of bankAcctNumber
     * @return the bankAcctNumber of assignment2.Employee
     */
    public int getBankAcctNumber(){
        return bankAcctNumber;
    }
}
