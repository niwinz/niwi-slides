all: example1

CPPFLAGS=-std=c++11 -O3

example1:
	g++ ${CPPFLAGS} -fPIC -I/usr/include/python3.3m -c -o example1.o example1.cpp
	g++ ${CPPFLAGS} -shared -Wl,-soname,example1.so -l boost_python3 -l python3 -o example1.so example1.o

example2:
	g++ ${CPPFLAGS} -fPIC -I/usr/include/python3.3m -c -o example2.o example2.cpp
	g++ ${CPPFLAGS} -shared -Wl,-soname,example2.so -l boost_python3 -l python3 -o example2.so example2.o

example3:
	g++ ${CPPFLAGS} -fPIC -I/usr/include/python3.3m -c -o example3.o example3.cpp
	g++ ${CPPFLAGS} -shared -Wl,-soname,example3.so -l boost_python3 -l python3 -o example3.so example3.o
clean:
	rm -f *.o *.so
