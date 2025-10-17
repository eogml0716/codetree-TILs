import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int book_price = 3000;
        int mask_price = 1000;


        if (n >= book_price) {
            System.out.println("book");

        } else if (n >= mask_price) {
            System.out.println("mask");

        } else {
            System.out.println("no");
        }
    }
}