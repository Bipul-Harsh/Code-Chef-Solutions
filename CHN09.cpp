#include <iostream>
#include <string.h>
#include<cstdlib>
using namespace std;


int main() {
	int n,count1 = 0,count2 = 0;
	int ans;
	cin>> n;
	char input[100];
	for(int j=0; j<n; j++){
	cin>>input;
	for(int i = 0; i<strlen(input); i++){
	    if(input[i] == 'a')
	    count1 ++;
	    else if(input[i] == 'b')
	    count2 --;
	}
	ans = count1 + count2;
	if(ans == 0)
	cout<< count1 << endl;
	else if(ans > 0){
	    if(count2 == 0)
	    cout<< 0 <<endl;
	    else
	    cout<< abs(count2) << endl;
	}
	else if(ans < 0){
	    if(count1 == 0)
	    cout<<0<<endl;
	    else
	    cout<< count1 << endl;
	}
	count1 = 0; count2 = 0;
	}
	return 0;
}
