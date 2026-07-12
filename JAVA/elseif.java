import java.util.*;
public class elseif{
    public static void main(String args[]){
        int age=20;

        if(age>=18){
            System.out.println("adult");
        }else if(age>=13 && age<18){
            System.out.println("teenager");
        }
        else{
            System.out.println("child");
        }
    }
}