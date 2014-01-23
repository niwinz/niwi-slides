all: sample1 sample2 sample-cpp


sample1: sample.c
	clang -shared -fPIC -o libsample.so sample.c

sample2: sample2.c
	clang -shared -I /usr/include/python3.3m -fPIC -lpython3.3m -o libsample2.so sample2.c


sample-cpp: sample-class.cpp
	clang++ -fPIC -I/usr/include/python3.3m -shared -Wl,-soname,samplecpp.so \
			-l boost_python3 -l python3 -o samplecpp.so sample-class.cpp

clean:
	rm -f libsample.so
	rm -f libsample2.so
	rm -f samplecpp.so
