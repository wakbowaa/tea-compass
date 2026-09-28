import json, re
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet

ROOT = Path(__file__).parents[1]
env_text = (ROOT.parents[3] / "accounts.env").read_text()
private_key = re.search(r'^ACCOUNT_6_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env_text, re.M).group(1).strip()
account = create_account(account_private_key=private_key)
client = create_client(chain=studionet, account=account)
tx = client.deploy_contract(code=(ROOT / "contracts" / "contract.py").read_text(), args=[])
print("deploy_tx=" + str(tx), flush=True)
receipt = client.wait_for_transaction_receipt(transaction_hash=tx, wait_until="finalized", retries=180, interval=5000, full_transaction=True)
leader = (receipt.get("consensus_data", {}).get("leader_receipt") or [{}])[0]
print(json.dumps({"contract": receipt.get("data", {}).get("contract_address") or receipt.get("to_address"), "deploymentTx": str(tx), "consensus": receipt.get("result_name"), "execution": leader.get("execution_result")}, default=str), flush=True)
