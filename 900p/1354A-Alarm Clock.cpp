#include <iostream>

using namespace std;


int main() {
	
	long long a, b, c, d, n;

	cin >> n;

	while (n--) {
		cin >> a >> b >> c >> d;
		if (b >= a) {
			cout << b << endl;
		}
		else if(d >= c){
			cout << -1 << endl;
		}
		else {
			long long ans = b, m, o = c - d;
			m = ((a - b + o - 1) / o) * c;
			ans += m;
			cout << ans << endl;
		}
	}

	return 0;
}
