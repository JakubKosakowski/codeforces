#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;

    cin >> t;

    while (t--) {
        int n, x, ans = 2, p = 2;
        cin >> n >> x;
        while (true) {
            if (n <= p) {
                cout << 1 << endl;
                break;
            }
            else {
                p += x;
                if (p >= n) {
                    cout << ans << endl;
                    break;
                }
                ++ans;
            }
        }
    }

    return 0;
}
