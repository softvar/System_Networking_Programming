# include <linux/module.h>

MODULE_AUTHOR("Vasu");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Sum of first 10 even numbers");

int init_module ( void )
{
int sum=0;
int i;
for(i=0;i<10;++i,++i)
sum=sum+i;
printk ("Sum is %d",sum);
}

void cleanup_module (void)
{
printk("Exiting\n");
}
