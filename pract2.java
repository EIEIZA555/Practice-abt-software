import java.util.Scanner;

public class pract2 {
    // Method to calculate tax based on income
    public static double calculateTax(double income) {
        double tax = 0.0;
        // Example tax brackets (you can modify based on actual rules)
        if (income <= 150000) {
            tax = 0.0;  // No tax for income up to 150,000
        } else if (income <= 300000) {
            tax = (income - 150000) * 0.05;  // 5% tax for income between 150,001 and 300,000
        } else if (income <= 500000) {
            tax = (income - 300000) * 0.10 + 150000 * 0.05;  // 10% for income between 300,001 and 500,000
        } else if (income <= 1000000) {
            tax = (income - 500000) * 0.20 + 200000 * 0.10 + 150000 * 0.05;  // 20% for income between 500,001 and 1,000,000
        } else {
            tax = (income - 1000000) * 0.30 + 500000 * 0.20 + 200000 * 0.10 + 150000 * 0.05;  // 30% for income over 1,000,000
        }
        return tax;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Get user input for income
        System.out.print("Enter your annual income: ");
        double income = scanner.nextDouble();
        // Calculate tax
        double tax = calculateTax(income);
        // Output the results
        System.out.println("Your total tax amount is: " + tax);
        scanner.close();
    }
}
