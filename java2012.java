package 자료구조;
import java.util.*;
public class java2012 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int N=kbd.nextInt();
		int B=1;
		long sum=0;
		int[] array=new int[N];
		for(int i=0;i<array.length;i++)
			array[i]=kbd.nextInt();
		Arrays.sort(array);
		for(int i=0;i<array.length;i++)
			sum+=Math.abs(array[i]-(i+1));
		
		System.out.println(sum);

	}

}
