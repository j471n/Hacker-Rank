
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main() {
    int m, n;
    cin >> m >> n;
    
    float X[n][m+1];
    float B[m+1];
    float Y[n];
    
    for (int i = 0; i < n; i ++) {
        X[i][0] = 1;
        for (int j = 1; j < (m + 1); j++) {
            cin >> X[i][j];
        } 
        cin >> Y[i];
    }
    
    int q;
    cin >> q;
 
    float queries[q][m+1];
    for (int i = 0; i < q; i++) {
        queries[i][0] = 1.00;
        for (int j = 1; j < (m+1); j++) {
            cin >> queries[i][j];
        }
    }
    
    float transX[m+1][n];
    for (int i = 0; i < m+1; i++) {
        for (int j = 0; j < n; j++) {
            transX[i][j] = X[j][i];
        }
    }
  
    float mul1[m+1][m+1];
    for (int i = 0; i < m+1; i++) {
        for (int j = 0; j < m+1; j++) {
                mul1[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    mul1[i][j] += (float) transX[i][k]* X[k][j]; 
                }
        }
    }
        
    float inv[m+1][m+1];
    for (int i = 0; i < m+1; i++) {
        for (int j = 0; j < m+1; j++) {
            if(i == j) 
                inv[i][j] = 1;
            else
                inv[i][j] = 0;
        }
    }
    // echelon form
    for (int i = 0; i < m+1; i++) {
        if (mul1[i][i] == 0) {
            for (int j = i+1; j < m+1; j++) {
                if(mul1[j][i] != 0) {
                    for (int k = 0; k < m+1; k++) {
                        float temp = mul1[i][k];
                        mul1[i][k] = mul1[j][k];
                        mul1[j][k] = temp;
                        
                        temp = (float) inv[i][k];
                        inv[i][k] = inv[j][k];
                        inv[j][k] = temp;
                    }
                }
            }
        }
        for (int j = i + 1; j < m+1; j++) {
            float ratio_j_i = (float) - mul1[j][i] / mul1[i][i];
            
            for (int k = 0; k < m+1; k++) {
                mul1[j][k] += (float) mul1[i][k] * ratio_j_i;
                inv[j][k] += (float) inv[i][k] * ratio_j_i;
            }
        }
    }
    // reduced echelon form
    for (int i = m; i >= 0; i--) {
        for (int k = 0; k < m+1; k++) {
            inv[i][k] = (float) inv[i][k]/mul1[i][i];
        }
        
        mul1[i][i] = 1;
        
        for (int j = i - 1; j >= 0; j--) {
            float ratio_j_i = (float) - mul1[j][i];
            
            for (int k = 0; k < m+1; k++) {
                mul1[j][k] += (float) mul1[i][k] * ratio_j_i;
                inv[j][k] += (float) inv[i][k] * ratio_j_i;
            }
        }
        
    }
  
    float mul2[m+1][n];
    for (int i = 0; i < m+1; i++) {
        for (int j = 0; j < n; j++) {
            mul2[i][j] = 0.0;
            
            for (int k = 0; k < m+1; k++) {
                mul2[i][j] += (float) inv[i][k] * transX[k][j];        
            }
        }
    }

    for (int i = 0; i < m+1; i++) {
        B[i] = 0.0;
        for (int j = 0; j < n; j++) {
            B[i] += mul2[i][j] * Y[j];
        }
    }
    
    float yQueried[q];
    for (int i = 0; i < q; i++) {
        yQueried[i] = 0.0;
        for (int j = 0; j < (m+1); j++) {
            yQueried[i] += (float) queries[i][j] * B[j];
        }
        cout.precision(2);
        cout << fixed << yQueried[i] << endl;
    }
    
    return 0;

}
