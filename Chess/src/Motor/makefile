

libs: genera.o poda.o funcutilidad.o piezas.o 
	gcc -shared genera.o poda.o funcutilidad.o piezas.o -o genera.so

compile: genera.c poda.c funcutilidad.c piezas.c piezas.h poda.h funcutilidad.h var_data.h
	gcc -c -lpthread genera.c poda.c funcutilidad.c piezas.c 

clean:
	rm -rf *o libs
