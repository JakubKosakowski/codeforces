#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string s;
	vector<char> v{'H','Q','9'};
	int ans = 0;

	cin >> s;

	for (char c : s) {
		for (int i = 0; i < v.size(); ++i) {
			if (c == v[i]) {
				++ans;
			}
		}
	}
	if (ans > 0) {
		cout << "YES" << endl;
	}
	else {
		cout << "NO" << endl;
	}

	return 0;
}
