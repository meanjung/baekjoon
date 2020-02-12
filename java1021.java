package 자료구조;
import java.util.*;
public class java1021 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int N=kbd.nextInt();
		int M=kbd.nextInt();
		int num,answer=0;
		List list=new ArrayList<>();
		boolean flag;
		for(int i=1;i<=N;i++) list.add(i);
		for(int i=0;i<M;i++) {
			num=kbd.nextInt();
			flag=false;
			while(!flag) {
				if((int)list.get(0)==num) {
					list.remove(0);
					flag=true;
				}
				else {
					if(list.indexOf(num)<=list.size()/2)
						list.add(list.size()-1,list.remove(0));
					else
						list.add(0,list.remove(list.size()-1));
					answer++;
				}
			}
		}
		System.out.println(answer);
		
		
	}

}
