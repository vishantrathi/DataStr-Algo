public class IfElse{
    public static void main(String args[]){
        int age =18;
        if(age>=18){
            System.out.println("adult:drive,Vote");
        }
        if(age>13 && age<18){
            System.out.println("teenager");
        }
        else{
            System.out.println("not adult");
        }
    }
}