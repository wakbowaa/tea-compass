'use client';
import{createAccount,createClient}from'genlayer-js';import{studionet}from'genlayer-js/chains';
export const ADDRESS=(process.env.NEXT_PUBLIC_CONTRACT_ADDRESS||'0x9CA2ce6Fd69976948696b391C2AE914b0E7d856e')as`0x${string}`;
const endpoint='https://studio.genlayer.com/api';
const reader:any=createClient({chain:studionet,endpoint,account:createAccount()});let wallet:any;
export async function connect(){const provider:any=(window as any).ethereum;if(!provider)throw Error('A browser wallet is required');const[address]=await provider.request({method:'eth_requestAccounts'});wallet=createClient({chain:studionet,endpoint,account:address,provider});return address as string}
export const read=(name:string,args:any[]=[])=>reader.readContract({address:ADDRESS,functionName:name,args});
export async function write(name:string,args:any[]=[]){if(!wallet)throw Error('Connect a wallet before tasting');const hash=await wallet.writeContract({address:ADDRESS,functionName:name,args,value:0n});await wallet.waitForTransactionReceipt({hash,status:'FINALIZED',retries:120,interval:5000});return hash as string}
