#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xa8c16cf3, "module_layout" },
	{ 0x7485e15e, "unregister_chrdev_region" },
	{ 0x1d26dbf2, "cdev_del" },
	{ 0xc4556ebd, "cdev_add" },
	{ 0x714e93a2, "cdev_alloc" },
	{ 0x29537c9e, "alloc_chrdev_region" },
	{ 0x4f6b400b, "_copy_from_user" },
	{ 0xf22449ae, "down_interruptible" },
	{ 0x4f8b5ddb, "_copy_to_user" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0x27e1a049, "printk" },
	{ 0x71e3cecb, "up" },
	{ 0xb4390f9a, "mcount" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "CC9259FF0A09771D5145CEB");
