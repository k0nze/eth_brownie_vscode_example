# Brownie VSCode Example

[![`[YouTube]`](https://img.shields.io/badge/-k0nze%20builds-ff0000?logo=youtube&logoColor=white)](https://www.youtube.com/channel/UC3_SywgWxpEBIoKawK2E3MA) 
[![`[Twitter]`](https://img.shields.io/badge/-@k0nze_-1DA1F2?logo=twitter&logoColor=white)](https://twitter.com/k0nze_) 
[![`[Discord]`](https://img.shields.io/discord/713121297407672380.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.k0nze.gg)
[![`[Patreon]`](https://img.shields.io/badge/-Patreon-f96854?logo=patreon&logoColor=white)](https://patreon.com/k0nze)
[![`[LinkedIn]`](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/konstantin-luebeck/)

This repository is an example on how to use the Brownie Ethereum Python Framework to compile and run a Solidity smart contract on a local Ethereum network through the `ganache-cli`. Find the article for it over here: [k0nze.dev/posts/solidity-smart-contract-python-vscode](https://k0nze.dev/posts/solidity-smart-contract-python-vscode)

## Project Structure

This project follows the [brownie project structure](https://eth-brownie.readthedocs.io/en/stable/structure.html)

* `brownie-config.yaml`: Config file for this project.
* `contracts/Faucet.sol`: smart contract in Solidity that allows to withdraw funds from it.
* `contracts/HelloWorld.sol`: smart contract in Solidity that returns "Hello World!".
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