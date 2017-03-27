all : reader-writer

reader-writer : reader-writer.o
	g++ -o reader-writer reader-writer.o -lparquet -larrow -larrow_io 

reader-writer.o : reader-writer.cc
	gcc -c reader-writer.cc -std=c++11

clean :
	rm reader-writer *.o