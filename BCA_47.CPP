#include<iostream.h>
#include<conio.h>
#include<graphics.h>
void main()
{	clrscr();
	int gd=0,gm;
	initgraph(&gd,&gm,"C:\\turboc3\\bgi");
	float x,y,r,d0,x1,y1;
	cout<<"\n CIRCLE USING BLA\n";
	cout<<"ONKAR [47-IT-19]\n\n";
	cout<<"x = ";
	cin>>x;
	cout<<"y = ";
	cin>>y;
	cout<<"r = ";
	cin>>r;
	x1=0;
	y1=r;
	d0=3-2*r;
	while(x1<=y1)
	{	putpixel(x+x1,y+y1,3);
		putpixel(x+x1,y-y1,3);
		putpixel(y+y1,x+x1,3);
		putpixel(y+y1,x-x1,3);
		putpixel(x-x1,y+y1,3);
		putpixel(x-x1,y-y1,3);
		putpixel(y-y1,x+x1,3);
		putpixel(y-y1,x-x1,3);
		if(d0<0)
		{	d0=d0+4*x1+6;
			x1++;
		}
		else
		{	d0=d0+4*(x1-y1)+10;
			x1++;
			y1--;
		}
	}
	getch();
	closegraph();
}