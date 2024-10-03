import java.util.Scanner;  // Import the Scanner class for user input

// Define a Person class
class Person {
    private String name;
    private int age;
    private double height;

    // Constructor
    public Person(String name, int age, double height) {
        this.name = name;
        this.age = age;
        this.height = height;
    }

    // Getter methods
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getHeight() {
        return height;
    }

    // Method to display person's information
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age + " years old");
        System.out.println("Height: " + height + " cm");
    }
}

public class pract2person {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("How many people would you like to enter? ");
            int numberOfPeople = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character

            // Create an array of Person objects
            Person[] people = new Person[numberOfPeople];

            // Loop to input information for each person
            for (int i = 0; i < numberOfPeople; i++) {
                System.out.println("\nEnter details for person " + (i + 1) + ":");

                System.out.print("Enter name: ");
                String name = scanner.nextLine();

                System.out.print("Enter age: ");
                int age = Integer.parseInt(scanner.nextLine());  // Convert string to int

                System.out.print("Enter height (in cm): ");
                double height = Double.parseDouble(scanner.nextLine());  // Convert string to double

                // Create a new Person object and store it in the array
                people[i] = new Person(name, age, height);
            }

            // Display information for each person
            System.out.println("\n--- Person Details ---");
            for (Person person : people) {
                person.displayInfo();
                System.out.println();  // Blank line between persons
            }

        } catch (NumberFormatException e) {
            System.out.println("Invalid number format. Please enter numeric values for age and height.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close();  // Close the scanner to prevent resource leaks
        }
    }
}
