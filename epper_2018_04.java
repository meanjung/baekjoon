package 자료구조;
import java.util.*;
public class epper_2018_04 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int n=kbd.nextInt();
		for(int i=0;i<n/2+1;i++) {
			for(int j=0;j<(n-2*i-1)/2;j++)
				System.out.print(" ");
			for(int j=0;j<2*i+1;j++)
				System.out.print("*");
			for(int j=0;j<(n-2*i-1)/2;j++)
				System.out.print(" ");
			System.out.println();
		}
		for(int i=n/2;i>0;i--) {
			for(int j=0;j<(n-2*i+1)/2;j++)
				System.out.print(" ");
			for(int j=0;j<2*i-1;j++)
				System.out.print("*");
			for(int j=0;j<(n-2*i+1)/2;j++)
				System.out.print(" ");
			System.out.println();
		}
		
	}

}
