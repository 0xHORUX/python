{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python312Full
    python312Packages.tkinter
    tigervnc
  ];
  shellHook = ''
    echo "Python development environment loaded"
    echo "Available tools: Python (Full), vncdotool-python, tkinter, tigervnc"
  '';
}
