#include <iostream>

using namespace std;


int main() {
	
	int n;

	cin >> n;

	while (n--) {
		long long x;

		int ans = 0;

		cin >> x;

		while (x != 0) {
			if (x == 1) {
				x = 0;
				cout << ans << endl;
			}
			if (x == 2) {
				cout << -1 << endl;
				break;
			}
			else {
				if (x % 6 == 0) {
					x = x / 6;
					++ans;
				}
				else {
					x = x * 2;
					++ans;
					if (x % 3 != 0) {
						cout << -1 << endl;
						break;
					}
				}
			}
		}
	}
	return 0;
}
