package 자료구조;
import java.util.*;
public class epper_2018_01 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int n=kbd.nextInt();
		int list[]=new int[n];
		for(int i=0;i<n;i++)
			list[i]=kbd.nextInt();
		int i=kbd.nextInt();
		int j=kbd.nextInt();
		int sum=0;
		for(int k=i-1;k<j;k++)
			sum+=list[k];
		System.out.println(sum);
	}

}
