/*
Programming Languages | My First Java Program
Imani Candler | 10.2.2024
Objective: Modify the Addition program to use four numbers to 
compute and print their product and sum.
*/

import java.util.Scanner; // importing the class

public class Addition{ // creating the Addition class
  public static void main (String[]args){

// creating an object of scanner class
    Scanner sc = new Scanner (System. in);

// reads 4 int numbers
    System.out.print("Enter the first number: "); // user input
    int num1 = sc.nextInt(); // the scanner "sc" creates next int in class?

    System.out.print("Enter the second number: ");
    int num2 = sc.nextInt();
    
    System.out.print("Enter the third number: ");
    int num3 = sc.nextInt();
    
    System.out.print("Enter the fourth number: ");
    int num4 = sc.nextInt();
    
// calculate the sum
    int sum = num1 + num2 + num3 + num4;

// calculate the product
    int product =  num1 * num2 * num3 * num4;

// printing the sum & product
System.out.print ("The sum of the four numbers is: " + sum);
System.out.print ("\nThe product of the four numbers is: " + product);
}
}