// SPDX-License-Identifier: MIT
pragma solidity >=0.4.25 <0.7.0;

import "./ConvertLib.sol";

// This is just a simple example of a coin-like contract.
// It is not standards compatible and cannot be expected to talk to other
// coin/token contracts. If you want to create a standards-compliant
// token, see: https://github.com/ConsenSys/Tokens. Cheers!

contract MetaCoin {
	mapping (address => uint) balances;

	event Transfer(address indexed _from, address indexed _to, uint256 _value);
	///@dev _from에서 _to로 _value를 전송할 때 발생하는 이벤트

	constructor() public {
		balances[tx.origin] = 10000;
	}
	///@dev balances mapping 이용 -> 구조체???

	function sendCoin(address receiver, uint amount) public returns(bool sufficient) {
		if (balances[msg.sender] < amount) return false;
		balances[msg.sender] -= amount;
		balances[receiver] += amount;
		emit Transfer(msg.sender, receiver, amount);
		return true;
	}
	///@param address, uint
	///@returns bool
	///@dev 현재 사용자가 가진 이더가 amount보다 적을 때 false
	///		amount보다 크거나 같을 때, receiver의 것 +, sender의 것 -
	///@quest emit이 무엇인가?

	function getBalanceInEth(address addr) public view returns(uint){
		return ConvertLib.convert(getBalance(addr),2);
	}
	///@dev library ConvertLib의 함수 convert 사용 : getBalance 함수의 getter 사용
	///@returns	balances[addr] * 2

	function getBalance(address addr) public view returns(uint) {
		return balances[addr];
	}
}
