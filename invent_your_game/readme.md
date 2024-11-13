
## Nixos Python development

1. NixOS Shell Configuration:

First, let's create a `shell.nix` file that sets up an environment with the necessary tools for Python development.

```nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    pkgs.python312Packages.random2
  ];

  shellHook = ''
    echo "Python development environment loaded"
    echo "Available tools: random"
  '';
}

```

This configuration:
- Imports the random package
- Sets up a shell hook to inform you when the environment is loaded


2. Program to test random module :

Now, let's create a simple test program in Python.

Create a file named `00_import_random_test.py` with the following content:

```python
# Test import random module in python
import random

number = random.randint(1, 100)
print( "random number : " ,number )

```


3. Running the Program:

To use the NixOS shell and run your C++ program, follow these steps:

  1. Check for `shell.nix` file in your project directory.
  2. Open a terminal and navigate to your project directory.
  3. Enter the Nix shell by running:
   ```nix
   nix-shell
   ```
  4. Once in the Nix shell, run your python  program:
  ```shell 
  $> python 00_import_random_test.py
  ```
  5. You should see the output, a random number from the program : "random number : 42"
