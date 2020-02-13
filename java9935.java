package 자료구조;
import java.util.*;

public class java9935 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		String input=kbd.next();
		String remove=kbd.next();
		Stack<Character> stack=new Stack<>();
		for(int i=input.length()-1;i>=0;i--) {
			boolean bool=false;
			char ch=input.charAt(i);
			for(int j=0;j<remove.length();j++) {
				if(ch==remove.charAt(j)){
					bool=true;
					break;
				}
			}
			if(bool==false) stack.add(ch);
		}
		if(stack.empty())
			System.out.println("FRULA");
		else {
			while(!stack.isEmpty()) {
				System.out.print(stack.pop());
			}
		}
	}

}
