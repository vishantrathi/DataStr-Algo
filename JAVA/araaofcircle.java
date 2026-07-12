import java.util.Scanner;

public class araaofcircle {
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        float rad = sc.nextFloat();
        float area =(float) (3.14 * rad * rad); //java har point wali value ko double maan leta hai 
        System.out.println(area);

    }
    
}
