#include <stdio.h>
#include <stdlib.h>
int main() {
int f;
int x;
int y;
int T_1;
int c;
int T_2;
int T_3;
int T_4;
int p;
int T_5;
int test;
int a;
int b;
int CV;
int T_6;
int RET;
int T_7;
int T_8;
int T_9;
L0:
	
L1:
	T_1=x+y;
L2:
	c=T_1;
L3:
	T_2=x+c;
L4:
	T_3=T_2+12;
L5:
	y=T_3;
L6:
	printf("%d",y);L7:
	T_4=x+10;
L8:
	
L9:
		return 0;
}
L10:
	
L11:
	printf("%d",c);L12:
	if(c>=20)
		goto L14;
L13:
	goto L23;
L14:
	printf("%d",c);L15:
	if(c<0)
		goto L17;
L16:
	goto L19;
L17:
	goto L22;
L18:
	goto L19;
L19:
	T_5=c+20;
L20:
	c=T_5;
L21:
	goto L14;
L22:
	goto L24;
L23:
	printf("%d",1234);L24:
		return 0;
}
L25:
	
L26:
	scanf("%d",&a);L27:
	scanf("%d",&b);L28:
	
L29:
	
L30:
	
L31:
	
L32:
	c=T_6;
L33:
	printf("%d",b);L34:
	printf("%d",c);L35:
	c=21;
L36:
	
L37:
	
L38:
	c=100;
L39:
	if(c<1000)
		goto L41;
L40:
	goto L44;
L41:
	T_7=c+100;
L42:
	c=T_7;
L43:
	goto L39;
L44:
	printf("%d",c);L45:
	c=10;
L46:
	if(c!=1)
		goto L49;
L47:
	printf("%d",1);L48:
	goto L66;
L49:
	if(c!=2)
		goto L52;
L50:
	printf("%d",2);L51:
	goto L66;
L52:
	if(c!=10)
		goto L66;
L53:
	T_8=0;
L54:
	if(c>=10)
		goto L56;
L55:
	goto L58;
L56:
	T_8=1+T_8;
L57:
	printf("%d",c);L58:
	if(c>=5)
		goto L60;
L59:
	goto L64;
L60:
	T_8=1+T_8;
L61:
	printf("%d",c);L62:
	T_9=c+1;
L63:
	c=T_9;
L64:
	if(0!=T_8)
		goto L53;
L65:
	goto L66;
L66:
	
L67:
		return 0;
}
