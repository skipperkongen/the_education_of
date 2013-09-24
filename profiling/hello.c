#include <stdio.h>
 
int foo() {
  int b = 54324;
  int j;
  for (j=0; j < 1000000; j++) {
    b = b^j;
  }
  return b;
}
 
int main() {
  int a = 321782;
  int i;
  for(i=0; i<1000; i++) {
    a = a ^ foo();
  }
  printf("Hello foo: %d\n", a);
  return 0;
}
