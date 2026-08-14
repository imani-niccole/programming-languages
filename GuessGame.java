/*
Imani Candler | 10.11.2024
Programing Languages | Guessing Game Java 
Objective: Let the user guess a random number between 1
and 100. Tell user if their guess is less than or more
than the random number. Allow 10 guesses.
*/
import java.util.Scanner;

public class GuessGame{
    
  public static void main(String[]args)
    {
    Scanner sc = new Scanner (System.in);
    
    System.out.print("Welcome to the Guessing Game! Guess a whole number between 1 and 100!");
       
    int guess_number = 1 + (int)(100 * Math.random()); // generates random number
    //System.out.print ("Guess number: " + guess_number); // used to check guess number for correct programming
    int n = 10; // number of guesses
    
    System.out.print("\nEnter your guess: ");
    int user_number = sc.nextInt();
    
    for (int i = 0; i < n; i++){
        if (user_number < guess_number){
            System.out.print("Too low! Guess again: ");
            user_number = sc.nextInt();
        }
        else if (user_number > guess_number){
            System.out.print("Too high! Guess again: ");
            user_number = sc.nextInt();

        }
        else{
            System.out.print("\nYou guessed it! The number was " + guess_number);
            break; // break statement is important because it prevents the "else" statement from looping
        }
    } // END OF FOR LOOP
    if (user_number != guess_number){
        System.out.print("You lose! The number was " + guess_number);
        // displays if user can't guess the random number in 10 guesses
    }
    
    System.out.print("\nThanks for playing!");  
    } // END OF GUESS FUNCTION
    
} // END OF GUESS CLASS