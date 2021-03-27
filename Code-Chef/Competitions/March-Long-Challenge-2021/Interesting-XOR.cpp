#include<bits/stdc++.h>
using namespace std;
#define int long long int
void solve() {
	int c, d;
	cin >> c;
	int length = 0;
	/*if (c > 64 && c % 2 != 0) {
		length = floor(log2(c)) + 2;
	} else {
		length = floor(log2(c)) + 1;
	}*/
	for (int i = 30; i >= 0; i--) {
		if ((1 << i) & c) {
			length = i;
			break;
		}
	}
	//cout << length << endl;


	d = 1 << length;

	//cout << d << endl;
	int maxi = (c ^ (d - 1)) * (d - 1);

	cout << maxi << endl;
}
int32_t main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	while (t--) {
		solve();
	}
	return 0;

}