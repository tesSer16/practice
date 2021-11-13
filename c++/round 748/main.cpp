#include <stdio.h>
#include <string.h>

int main()
{
    int t, ptr, ans, res;
    char n[19];
    char check[4][3] = {"00", "25", "50", "75"};

    scanf("%d", &t);
    for (size_t i = 0; i < t; i++){
        scanf("%s", n);
        ans = 100;
        for (int c = 0; c < 4; c++){
            ptr = strlen(n) - 1;
            res = 0;
            while (ptr >= 0 && n[ptr] != check[c][1]){
                ptr--;
                res++;
            }

            if (ptr >= 0) ptr--;

            while (ptr >= 0 && n[ptr] != check[c][0]){
                ptr--;
                res++;
            }


            if (ptr >= 0 && res < ans) {
                ans = res;
            }
        }
        printf("%d\n", ans);
    }
}
