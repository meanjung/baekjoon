package 자료구조;
import java.util.*;
public class java15970 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int N=kbd.nextInt();
		int x[]=new int[N];
		int y[]=new int[N];
		for(int i=0;i<N;i++) {
			x[i]=kbd.nextInt();
			y[i]=kbd.nextInt();
		}
		int xc,yc;
		int least;
		int sum=0;
		for(int i=0;i<N;i++) {
			least=1000;
			xc=x[i];
			yc=y[i];
			for(int j=0;j<N;j++) {
				if(j!=i&&yc==y[j])
					if(least>Math.abs(x[j]-xc))
						least=Math.abs(x[j]-xc);
			}
			sum+=least;
			
		}
		System.out.println(sum);
	}

}
