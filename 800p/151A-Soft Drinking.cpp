#include <iostream>

using namespace std;

int main() {
	int n, k, l, c, d, p, nl, np;

	cin >> n >> k >> l >> c >> d >> p >> nl >> np;

	int x, y, z;

	x = (k * l) / nl;
	y = c * d;
	z = p / np;
	int t[3] = { x,y,z }, min = t[0];

	for (int i = 1; i < 3; ++i) {
		if (t[i] < min) {
			min = t[i];
		}
	}
	cout << min / n << endl;

	return 0;
}
