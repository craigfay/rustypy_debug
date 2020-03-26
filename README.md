# About
* A debug environment for [rustypy](https://github.com/iduartgomez/rustypy)
* To ensure dependencies are correct, it's recommended that you start a container shell (as described below) to invoke the debug commands.

# Container Commands
* Build container: `docker build . -t rspy`
* Execute a shell inside the container: `docker run -it --rm -v $(pwd):/app -w /app rspy bash`

# Debug Commands
* Compile Rust: `./setup.sh`
* Run Python: `python3 python_code/main.py`

