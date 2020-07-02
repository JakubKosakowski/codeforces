#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	char c;
	string s;
	vector<string> vs { "qwertyuiop","asdfghjkl;","zxcvbnm,./" };
	cin >> c;

	if (c == 'R') {
		cin >> s;
		for (int j = 0; j < s.size(); ++j) {
			int i = 0;
			bool x = true;
			while (x) {
				int a = 0;
				string p = vs[i];
				for (int d = 0; d < p.size(); ++d) {
					if (p[d] == s[j]) {
						cout << p[d - 1];
						a = 1;
					}
				}
				if (a == 1) {
					x = false;
				}
				else {
					++i;
				}
			}
		}
	}
	else {
		cin >> s;
		for (int j = 0; j < s.size(); ++j) {
			int i = 0;
			bool x = true;
			while (x) {
				int a=0;
				string p = vs[i];
				for (int d = 0; d < p.size(); ++d) {
					if (p[d] == s[j]) {
						cout << p[d + 1];
						a = 1;
					}
				}
				if (a == 1) {
					x = false;
				}
				else {
					++i;
				}
			}
		}
	}

	return 0;
}
