package de.mmg;

public class FinalTest {
	public static void main(String[] args) {
		final Test1 t1 = new Test1();
		t1.i = 30;
		t1.i = 40;
		System.out.println("The value of i in main" + t1.i);

		// Now instantiating the second objest

		Test1 t2 = new Test1();
		// t1=t2; -- this will give an error as the assignment of object can not
		// be done with a final declared object
	}

}

class Test1 {
	int i = 0;
}