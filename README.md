# Brownie VSCode Example

This repository is an example on how to use the Brownie Ethereum Python Framework to compile and run a Solidity smart contract on a local Ethereum network through the `ganache-cli`.

## Project Structure

This project follows the [brownie project structure](https://eth-brownie.readthedocs.io/en/stable/structure.html)

* `brownie-config.yaml`: Config file for this project.
* `contracts/Faucet.sol`: smart contract in Solidity that allows to withdraw funds from it.
* `contracts/HelloWorld.sol`: smart contract in Solidity that allows that returns "Hello World!".
* `scripts/faucet.py`: Python script that deploys the Faucet, transfers funds to the Faucet, and withdraws funds from the Faucet.
* `.vscode/`: VScode project settings and tasks.

## Prerequisites

 * Python version `>= 3.9`
 * `ganache-cli` installed
 * VSCode installed together with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Solidity](https://marketplace.visualstudio.com/items?itemName=JuanBlanco.solidity) Extension.

## Setup

```bash
git clone https://github.com/k0nze/eth_brownie_vscode_example.git
cd eth_brownie_vscode_example
python -m venv .venv
source .venv/bin/activate
python -m pip install eth-brownie
brownie run faucet.py
```

In VSCode you can run the task **Run Faucet** to execute the `brownie run faucet.py`.