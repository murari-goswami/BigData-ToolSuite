package de.mmg;

public class ForwardDeclaration {
	public static void main(String[] args) {
		Test3 t1 = new Test3();
		t1.fun(5);
				
	}

}

class Test3{
	void fun(int x){
		System.out.println("fun() called: x = "+x);
	}
}