#include <iostream>
#include <string>

using namespace std;

int main() {
	
	int u = 0, l = 0;

	string s;

	cin >> s;

	for (char c : s) {
		if (c >= 'a' && c <= 'z') {
			++l;
		}
		else {
			++u;
		}
	}
	if (u > l) {
		for (char c : s) {
			cout << char(toupper(c));
		}
	}
	else {
		for (char c : s) {
			cout << char(tolower(c));
		}
	}

	return 0;
}
