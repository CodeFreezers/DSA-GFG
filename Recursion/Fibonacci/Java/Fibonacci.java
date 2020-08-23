#1
import java.util.*;
class Main {
  public static int fibonacci(int n){
    if(n == 0){
      return 0;
    }
    if(n == 1){
      return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
  }
  public static void main(String[] args) {
    System.out.print("which fibonacci number do you want to find?");
    Scanner sc= new Scanner(System.in);
    int n = sc.nextInt();
    int fib = fibonacci(n);
    System.out.println(fib);
  }
}
