mx=a[n-1]
vector<int>ans;
ans.push_back(mx);
for(int i=n-2; i>=0; i--){
   if(a[i]<mx) continue;
}
for(int i=n-2; i>=0; i--){
  if(a[i]<mx) continue;
  mx=a[i]; 
  ans.push_back(mx);
}
reverse(ans.begin(), ans.end());
class Solution{
    public:
    vector<int> leaders(int a[], int n){
        int mx=a[n-1];
        vector<int>ans;
        ans.push_back(mx);
        for(int i=n-2; i>=0; i--){
            if(a[i]<mx)
            continue;
            mx=a[i];
            ans.push_back(mx);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
class Solution {
  public:
    vector<int> leaders(vector<int>& arr) {
        // code here
        vector<int> v;
        int l=arr.size();
        int last_digit = arr[l-1];
        
        for(int i= l-1 ; i>=0 ; i--){
            if(arr[i] >= last_digit){
                v.push_back(arr[i]);
                
            }
            last_digit=max(arr[i],last_digit);
        }
        
        reverse(v.begin(),v.end());
        return v;
    }
};
for(int i= l-1 ; i>=0 ; i--){
            if(arr[i] >= last_digit){
                v.push_back(arr[i]);
                
            }
            last_digit=max(arr[i],last_digit);
        }
class Solution:
    def leaders(self, arr):
        
        maximum = -1 << 31
        i = len(arr) -1
        new_arr=[]
        
        while i >= 0 :
            if(arr[i] >= maximum):
                maximum = arr[i]
                new_arr.append(arr[i])
            i -= 1
            
        return new_arr[::-1]