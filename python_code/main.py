from rustypy.rswrapper import bind_rs_crate_funcs

# These paths will need to change if not running in docker container
source_path = "/app/rust_code"
compiled_lib = "/app/rust_code/target/debug/libsome_lib.so"
lib_binds = bind_rs_crate_funcs(source_path, compiled_lib, prefixes=[])

# Raises Exception!
print(lib_binds.python_bind_example())

