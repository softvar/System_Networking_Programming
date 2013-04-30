#include <linux/module.h>
#include <linux/kernel.h>

MODULE_AUTHOR("Mayank");
MODULE_LICENSE("GPL v2");
MODULE_DESCRIPTION("Sum");

int init_module (void)
{
int s = 0;
int i;
      
      	printk ("Welcome\n" ) ;
	for (i=0;i<=20;i=i+2)
	{
		s = s+i;
	}
	printk ("Sum is %d",s);
	return 0;
}

void cleanup_module(void)
{
      printk("Bye. \ n") ;
}
