#include <linux/module.h>
#include <linux/kernel.h>
#include<linux/moduleparam.h>
int param_var=0;

module_param(param_var, int, S_IRUSR | S_IWUSR);
static void fact_init(void)
{
int i=param_var,fact=1;
while(i!=0)
{
fact=fact*i;
i=i-1;
}
printk(KERN_ALERT "Factorial Output:%d",fact);
return 0;
}

static void cleanup_exit(void)
{
printk (KERN_ALERT "Exiting\n");
}

module_init(fact_init);
module_exit(cleanup_exit);

MODULE_AUTHOR("Mayank Bhola");
MODULE_LICENSE("GPL v2");
MODULE_DESCRIPTION("Factorial");

