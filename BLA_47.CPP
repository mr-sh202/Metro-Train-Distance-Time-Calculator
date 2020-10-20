
#include<iostream.h>
#include<conio.h>
#include<graphics.h>
void main()
{
	clrscr();
	int gd=0,gm;
	initgraph(&gd,&gm,"C:\\turboc3\\bgi");
	float x0,y0,x1,y1,dx,dy,p0,m;
	cout<<"\n BRESENHAM LINE ALGORITHIM\n";
	cout<<"ONKAR 47-IT-19\n\n";
	cout<<"x1 = ";
	cin>>x0;
	cout<<"y1 = ";
	cin>>y0;
	cout<<"x2 = ";
	cin>>x1;
	cout<<"y2 = ";
	cin>>y1;

	dx=x1-x0;
	dy=y1-y0;
	m=dy/dx;
	cout<<"Slope of line =  "<<m;
	if((x1-x0)==0)
	{       for(int i=y0;i<=y1;i++)
		{
			putpixel(x0,i,3);

		}
	}
	if(m<1)
	{
	p0=2*dy-dx;
	while(x0<=x1)
	{
		if(p0<0)
		{
			p0=p0+dy;
			putpixel(x0,y0,3);
			x0++;
		}
		else
		{
			p0=p0+2*dy-2*dx;
			putpixel(x0,y0,3);
			x0++;
			y0++;
		}
	}
	}
	else
	{
	p0=2*dx-dy;
	while(y0<=y1)
	{
		if(p0<0)
		{
			p0=p0+dx;
			putpixel(x0,y0,3);
			y0++;
		}
		else
		{
			p0=p0+2*dx-2*dy;
			putpixel(x0,y0,3);
			x0++;
			y0++;
		}
	}
	}
	getch();
	closegraph();
}