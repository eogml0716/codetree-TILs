import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        // A >= B
        if (A >= B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        // A > B
        if (A > B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        // B >= A
        if (B >= A) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        // B > A
        if (B > A) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        // A == B
        if (A == B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        // A != B
        if (A != B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
