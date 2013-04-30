#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

int param_var=0;

module_param(param_var, int, S_IRUSR | S_IWUSR)

static int fact_init(void)
{
int i=param_var,fact=1;
while(i!=0)
{
fact=fact*i;
i=i-1;
}
printk(KERN_INFO "Factorial Output:%d",fact);
}

static void cleanup_exit(void)
{
printk (KERN_INFO "Exiting\n");
}

module_init(fact_init);
module_exit(cleanup_init);

MODULE_AUTHOR("Tanmay");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Factorial of a number");

