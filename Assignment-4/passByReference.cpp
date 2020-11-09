#include <iostream>

void fun(int &x) { // this formal argument is the alias for actual argument
	x = x + 1;
}

int main() {
	int x = 10;
	fun(x);
}
