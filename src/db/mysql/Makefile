#
# Makefile for mysql
#

CC = gcc
LIBS = -lmysqlclient_r
CFLAGS = -g -O0 -Wall
MAIN = mysql-main
all: $(MAIN)

OBJS = main.o

$(MAIN): $(OBJS)
	$(CC) $(LFLAGS) -o $@ $^ $(LIBS)

test:
	make -C .
	echo **********test-start**********
	./$(MAIN)
	echo ***********test-end***********
	make -C . clean


clean:
	rm -f $(MAIN) *.o *~
