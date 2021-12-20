from brownie import accounts, Faucet, web3

def main():
    act = accounts[0]
    f = Faucet.deploy({'from': act})

    print(f"Faucet at: {f.address}")
    print(f"Balance:   {f.balance()}")
    print("")
    print(f"Account:   {act.address}")
    print(f"Balance:   {act.balance()}")
    print("")

    print("Transfer ether to Faucet:")
    act.transfer(f.address, "1 ether")

    print(f"Faucet at: {f.address}")
    print(f"Balance:   {f.balance()}")
    print("")
    print(f"Account:   {act.address}")
    print(f"Balance:   {act.balance()}")
    print("")

    print("withdraw from Faucet")
    f.withdraw(web3.toWei(0.1, "ether"), {'from': act})

    print(f"Faucet at: {f.address}")
    print(f"Balance:   {f.balance()}")
    print("")
    print(f"Account:   {act.address}")
    print(f"Balance:   {act.balance()}")
    print("")
