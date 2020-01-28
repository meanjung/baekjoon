package 자료구조;
import java.util.*;
public class java13414 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int K=kbd.nextInt();
		int L=kbd.nextInt();
		LinkedHashSet<String> list=new LinkedHashSet<String>();
		String str;
		for(int i=0;i<L;i++){
			str=kbd.next();
			if(list.contains(str))
				list.remove(str);
			list.add(str);
		}
		
		int k=0;
		Iterator it=list.iterator();
		while(it.hasNext()) {
			String s=(String)it.next();
			System.out.println(s);
			k++;
			if(k==K) break;
		}
	}

}
