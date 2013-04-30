obj -m := Kernel.o

KERNEL_DIR = /lib/modules/$(shell uname -r)/build

PWD = $(shell pwd)

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
	#$(MAKE) -C $(KERNEL_DIR) SUBDIRS=$(PWD) modules

clean: 
	rm -rf *.o *.ko *.mod.* *.symvers *.order *~

