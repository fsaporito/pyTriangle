# Protocol Buffer Compiler
PROTOC=protoc

# PROTO INPUT and OUTPUT
PROTO_IN = .
PROTO_OUT = ../protopy

# PROTO
PROTO_SOURCE = ${PROTO_IN}/point.proto \
			   ${PROTO_IN}/edge.proto \
			   ${PROTO_IN}/triangle.proto \
			   ${PROTO_IN}/mesh.proto
			   
# PROTO_PY
PROTO_PY = ${PROTO_OUT}/point_pb2.py \
		   ${PROTO_OUT}/edge_pb2.py \
		   ${PROTO_OUT}/triangle_pb2.py \
		   ${PROTO_OUT}/mesh_pb2.py
		   
# PROTO_PYC
PROTO_PYC = ${PROTO_OUT}/point_pb2.pyc \
		    ${PROTO_OUT}/edge_pb2.pyc \
		    ${PROTO_OUT}/triangle_pb2.pyc \
		    ${PROTO_OUT}/mesh_pb2.pyc
			   
# Make
all:
	make clean
	make build

build:
	mkdir -p ${PROTO_OUT}
	mkdir -p ${PROTO_PYC}
	echo "${PROTOC} -I=${PROTO_IN} --python_out=${PROTO_OUT} ${PROTO_SOURCE}"
	${PROTOC} -I=${PROTO_IN} --python_out=${PROTO_OUT} ${PROTO_SOURCE}
	touch ${PROTO_OUT}/__init__.py
	
clean:
	rm -f ${PROTO_PY}
	rm -f ${PROTO_PYC}
	rm -f ${PROTO_OUT}/__init__.py
	rm -f ${PROTO_OUT}/__init__.pyc

