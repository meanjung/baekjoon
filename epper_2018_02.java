package 자료구조;
import java.util.*;
public class epper_2018_02 {

	public static void main(String[] args) {
		Scanner kbd=new Scanner(System.in);
		int n=kbd.nextInt();
		int room_num;
		int in_room_num;
		if(n%15==0) {
			room_num=n/15;
			in_room_num=15;
		}
		else {
			room_num=n/15+1;
			in_room_num=n%15;
		}
		System.out.println(room_num);
		System.out.println(in_room_num);
	}

}
