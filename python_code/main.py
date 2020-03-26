from rustypy.rswrapper import bind_rs_crate_funcs

source_path = "/app/rust_code"
compiled_lib = "/app/rust_code/target/debug/libsome_lib.so"
lib_binds = bind_rs_crate_funcs(source_path, compiled_lib, prefixes=[])

print(lib_binds.python_bind_example())

